# Redefine the graph and adjust the layout using a different approach to avoid errors

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges based on the WBS structure
edges = [
    ("Project Management", "Project Planning"),
    ("Project Management", "Risk Management"),
    ("Project Planning", "Define Project Scope"),
    ("Project Planning", "Develop Project Plan"),
    ("Project Planning", "Schedule Team Meetings"),
    ("Risk Management", "Identify Risks"),
    ("Risk Management", "Develop Risk Mitigation Plan"),
    ("Risk Management", "Implement Risk Controls"),
    ("Construction and Leasehold Improvements", "Construction Completion"),
    ("Construction and Leasehold Improvements", "Technical Improvements"),
    ("Construction Completion", "Finalize Construction Work"),
    ("Construction Completion", "Inspect Construction Quality"),
    ("Technical Improvements", "Electrical Systems Testing"),
    ("Technical Improvements", "Plumbing Systems Testing"),
    ("Technical Improvements", "Security Features Testing"),
    ("Infrastructure and Equipment", "IT Infrastructure"),
    ("Infrastructure and Equipment", "Telecommunications Equipment"),
    ("IT Infrastructure", "Purchase IT Equipment"),
    ("IT Infrastructure", "Install IT Infrastructure"),
    ("Telecommunications Equipment", "Purchase Telecommunications Equipment"),
    ("Telecommunications Equipment", "Install Telecommunications Equipment"),
    ("Coordination and Communication", "Internal Coordination"),
    ("Coordination and Communication", "External Communication"),
    ("Internal Coordination", "Coordinate with AGM Staff"),
    ("Internal Coordination", "Schedule Staff Training"),
    ("External Communication", "Notify Clients of Address Change"),
    ("External Communication", "Notify Suppliers of Address Change"),
    ("Physical Move", "Move Preparation"),
    ("Physical Move", "Execution of Move"),
    ("Move Preparation", "Secure Moving Trucks"),
    ("Move Preparation", "Pack Office Equipment"),
    ("Execution of Move", "Load Moving Trucks"),
    ("Execution of Move", "Transport Office Equipment"),
    ("Execution of Move", "Unload and Arrange Equipment"),
    ("Post-Move Activities", "Data Reinstallation"),
    ("Post-Move Activities", "Ongoing Maintenance"),
    ("Post-Move Activities", "Post-Move Support"),
    ("Data Reinstallation", "Reinstall Data on New Network"),
    ("Data Reinstallation", "Test Data Integrity"),
    ("Ongoing Maintenance", "Establish Maintenance Schedule"),
    ("Ongoing Maintenance", "Perform Initial Maintenance Checks"),
    ("Post-Move Support", "Provide Support to Staff"),
    ("Post-Move Support", "Address Any Issues Arising Post-Move")
]

# Add the edges to the graph
G.add_edges_from(edges)

# Create a layout for our nodes 
pos = nx.kamada_kawai_layout(G)

# Draw the graph
plt.figure(figsize=(20, 15))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True, arrowstyle='-|>', arrowsize=12)
plt.title("Work Breakdown Structure (WBS)")
plt.show()
x