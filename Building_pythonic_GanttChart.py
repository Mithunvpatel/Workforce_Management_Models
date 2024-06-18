import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def create_gantt_chart(tasks):
    fig, ax = plt.subplots()

    yticks = []
    task_labels = []
    start_dates = []
    end_dates = []

    for i, (task, start_date, end_date) in enumerate(tasks):
        yticks.append(i)
        task_labels.append(task)
        start_dates.append(datetime.strptime(start_date, "%Y-%m-%d"))
        end_dates.append(datetime.strptime(end_date, "%Y-%m-%d"))

    ax.barh(yticks, [(end - start).days for start, end in zip(start_dates, end_dates)], left=start_dates, align='center', color='skyblue', edgecolor='none')
    
    ax.set_yticks(yticks)
    ax.set_yticklabels([])  # Remove y-axis tick labels

    ax.invert_yaxis()  # labels read top-to-bottom
    ax.xaxis_date()

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))

    ax.set_xlabel('Date')
    ax.set_ylabel('Tasks')
    ax.set_title('Gantt Chart')

    # Remove borders of x and y axes
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Put task labels inside the bars
    for i, (start, end) in enumerate(zip(start_dates, end_dates)):
        ax.text(start + (end - start) / 2, i, task_labels[i], ha='center', va='center', color='black')

    plt.tight_layout()
    plt.show()

# Example tasks with mock dates
tasks = [
    ('Task 1', '2024-01-01', '2024-01-10'),
    ('Task 2', '2024-01-05', '2024-01-15'),
    ('Task 3', '2024-01-10', '2024-01-20'),
    ('Task 4', '2024-01-15', '2024-01-25')
]

create_gantt_chart(tasks)
