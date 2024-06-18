import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import date2num
import pandas as pd
from datetime import datetime, timedelta

# Define tasks with start and end weeks
tasks = [
    ("Initiation and Planning", "Project Kickoff", 1, 1),
    ("Initiation and Planning", "Define Scope & Plan", 1, 2),
    ("Stakeholder Engagement", "Identify & Analyze Stakeholders", 2, 3),
    ("Stakeholder Engagement", "Communication Plan", 2, 3),
    ("Stakeholder Engagement", "Stakeholder Meetings", 3, 4),
    ("Current State Analysis", "Review & Gather Data", 4, 5),
    ("Current State Analysis", "Analyze & Document", 5, 6),
    ("Future State Design", "Define Requirements", 6, 7),
    ("Future State Design", "Develop Solutions", 7, 8),
    ("Future State Design", "Validate & Finalize", 8, 9),
    ("Implementation Planning", "Roadmap & Milestones", 8, 9),
    ("Implementation Planning", "Quick Wins & Risk Plan", 8, 9),
    ("Implementation Planning", "Resource Allocation", 9, 10),
    ("Execution", "Pilot Programs & Training", 10, 11),
    ("Execution", "Monitor & Adjust", 11, 12),
    ("Execution", "Prepare for Rollout", 12, 12),
]

# Convert weeks to datetime
start_date = datetime(2024, 5, 1)
week_to_date = lambda week: start_date + timedelta(weeks=week-1)

# Create DataFrame
df = pd.DataFrame(tasks, columns=["Phase", "Task", "StartWeek", "EndWeek"])
df["StartDate"] = df["StartWeek"].apply(week_to_date)
df["EndDate"] = df["EndWeek"].apply(week_to_date)

# Reverse the order of tasks
df = df.iloc[::-1]

# Plot
fig, ax = plt.subplots(figsize=(14, 10))

for i, task in df.iterrows():
    ax.barh(task["Task"], date2num(task["EndDate"]) - date2num(task["StartDate"]),
            left=date2num(task["StartDate"]), height=0.4, align='center', color='green')

# Format the x-axis to show dates
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))

# Set labels and title
plt.xlabel('Date')
plt.ylabel('Task')
plt.title('Simplified 12-Week Gantt Chart', fontsize=22)

# Annotate Phases
for phase, group in df.groupby("Phase"):
    start = group["StartDate"].min()
    end = group["EndDate"].max()
    plt.text(date2num(start) - 5, group.index.mean(), phase, va='center', ha='right', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.gcf().autofmt_xdate()
plt.show()
