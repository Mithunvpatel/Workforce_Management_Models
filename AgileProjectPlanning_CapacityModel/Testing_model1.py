#build in some KBQs, to answer complexity/scoping/velocity requirements ect


# Define the capacity of each team in story points per sprint
team1_capacity = 25
team2_capacity = 30
team3_capacity = 20

# Define the skill level and experience level of each team member
team1_members = [{'name': 'John', 'skill_level': 0.8, 'experience_level': 0.9},
                 {'name': 'Jane', 'skill_level': 0.9, 'experience_level': 0.8},
                 {'name': 'Bob', 'skill_level': 0.7, 'experience_level': 0.6}]
team2_members = [{'name': 'Alice', 'skill_level': 0.8, 'experience_level': 0.7},
                 {'name': 'Tom', 'skill_level': 0.7, 'experience_level': 0.8},
                 {'name': 'Kate', 'skill_level': 0.9, 'experience_level': 0.9}]
team3_members = [{'name': 'Mike', 'skill_level': 0.6, 'experience_level': 0.7},
                 {'name': 'Sara', 'skill_level': 0.7, 'experience_level': 0.6},
                 {'name': 'Chris', 'skill_level': 0.8, 'experience_level': 0.8}]

# Define the number of sprints required to complete each backlog item
backlog_item1_sprints = 3
backlog_item2_sprints = 4
backlog_item3_sprints = 2

# Calculate the capacity of each team member based on their skill and experience levels
for member in team1_members:
    member['capacity'] = team1_capacity * member['skill_level'] * member['experience_level']
for member in team2_members:
    member['capacity'] = team2_capacity * member['skill_level'] * member['experience_level']
for member in team3_members:
    member['capacity'] = team3_capacity * member['skill_level'] * member['experience_level']

# Calculate the total capacity required to complete each backlog item, taking into account the skill and experience levels of each team member
backlog_item1_capacity = backlog_item1_sprints * sum([member['capacity'] for member in team1_members])
backlog_item2_capacity = backlog_item2_sprints * sum([member['capacity'] for member in team2_members])
backlog_item3_capacity = backlog_item3_sprints * sum([member['capacity'] for member in team3_members])

# Calculate the total capacity required to complete the project
total_capacity = backlog_item1_capacity + backlog_item2_capacity + backlog_item3_capacity

# Calculate the total number of sprints required to complete the project
total_sprints = backlog_item1_sprints + backlog_item2_sprints + backlog_item3_sprints

# Print the total capacity and total number of sprints required to complete the project
print("The total capacity required to complete the project is:", total_capacity)
print("The total number of sprints required to complete the project is:", total_sprints)
