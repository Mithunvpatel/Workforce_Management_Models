import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Create the DataFrame
data = {
    'postal_code': [
        'M5A', 'M5A', 'M5B', 'M6A', 'M6C', 'M7H', 'M6L', 'M6T', 'M6R',
        'M7C', 'M6P', 'M7A', 'M6G', 'M7B', 'M6W', 'M6X', 'M6E',
        'M6K', 'M6Y', 'M6N', 'M7E', 'M6B', 'M7M', 'M6J', 'M6V'
    ],
    'loan_amount': [
        1000000, 500000, 750000, 850000, 300000, 920000, 400000, 600000,
        700000, 250000, 500000, 800000, 450000, 650000, 900000, 350000,
        500000, 750000, 1000000, 300000, 450000, 600000, 800000, 900000,
        700000
    ],
    'default_rate': [
        0.05, 0.02, 0.1, 0.03, 0.07, 0.15, 0.04, 0.08, 0.12, 0.09,
        0.06, 0.11, 0.05, 0.2, 0.01, 0.07, 0.13, 0.02, 0.1, 0.14,
        0.03, 0.05, 0.09, 0.16, 0.07
    ],
    'latitude': [
        43.6548, 43.6548, 43.6555, 43.7201, 43.7102, 43.7303, 43.7504,
        43.7605, 43.7706, 43.7807, 43.6908, 43.7009, 43.7100, 43.7201,
        43.7302, 43.7403, 43.7504, 43.7605, 43.7706, 43.7807, 43.6908,
        43.7009, 43.7100, 43.7201, 43.7302
    ],
    'longitude': [
        -79.3623, -79.3623, -79.3783, -79.3250, -79.3400, -79.3550,
        -79.3650, -79.3750, -79.3850, -79.3950, -79.3050, -79.3150,
        -79.3250, -79.3350, -79.3450, -79.3550, -79.3650, -79.3750,
        -79.3850, -79.3950, -79.3050, -79.3150, -79.3250, -79.3350,
        -79.3450
    ]
}

df = pd.DataFrame(data)

# Define a custom color scale from green to dark red
custom_color_scale = [
    [0, "green"],       # Lowest risk
    [0.5, "yellow"],    # Medium risk
    [1, "darkred"]      # Highest risk
]

# Aggregate data by postal code
df_aggregated = df.groupby('postal_code').agg({
    'loan_amount': 'sum',
    'default_rate': 'mean',
    'latitude': 'mean',
    'longitude': 'mean'
}).reset_index()

# Create the scatter mapbox with the aggregated data
fig = px.scatter_mapbox(
    df_aggregated, 
    lat="latitude", 
    lon="longitude", 
    color="default_rate", 
    size="loan_amount",
    hover_name="postal_code",
    hover_data={"default_rate":":.2%", "loan_amount":True},
    color_continuous_scale=custom_color_scale,
    size_max=15,
    zoom=10,
    mapbox_style="carto-positron"
)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the app layout
app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(html.H3("Loan Risk Analysis Dashboard"), width={"size": 6, "offset": 3})
        ),
        dbc.Row(
            dbc.Col(dcc.Graph(id='map-fig', figure=fig), width=12)
        ),
        dbc.Row(
            dbc.Col(
                html.Div(id='tooltip-data', style={'margin-top': '20px'}),
                width=12
            )
        ),
        dcc.Store(id='selected-data')
    ],
    fluid=True,
)

# Callback to update store based on selected data point
@app.callback(
    Output('selected-data', 'data'),
    Input('map-fig', 'hoverData')
)
def update_selected_data(hoverData):
    if hoverData is None:
        return {}
    postal_code = hoverData['points'][0]['hovertext']
    selected_df = df[df['postal_code'] == postal_code]
    return selected_df.to_dict('records')

# Callback to update the tooltip-data based on the store
@app.callback(
    Output('tooltip-data', 'children'),
    Input('selected-data', 'data')
)
def update_tooltip_data(data):
    if not data:
        return "Select a point on the map to see details here."
    data_df = pd.DataFrame(data)
    items = [html.P(f"{row['postal_code']}: Loan Amount = ${row['loan_amount']:,}, Default Rate = {row['default_rate']:.2%}")
             for _, row in data_df.iterrows()]
    return html.Div(items)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Start the Dash app
import app  # Make sure your Dash app is in a file named `app.py`

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the Dash app in the browser
driver.get('http://127.0.0.1:8051')

# Wait for the page to load
time.sleep(5)

# Save the page as HTML
with open('app_output.html', 'w', encoding='utf-8') as file:
    file.write(driver.page_source)

# Close the browser
driver.quit()
