class Project:
    def __init__(self, name, requirements):
        self.name = name
        self.requirements = requirements

class Employee:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

class WorkforcePlanner:
    def __init__(self, projects, employees):
        self.projects = projects
        self.employees = employees
    
    def assess_project_requirements(self, project):
        # Assess project requirements
        required_skills = project.requirements
        return required_skills
    
    def match_skills_to_projects(self):
        # Match skills to projects
        for project in self.projects:
            required_skills = self.assess_project_requirements(project)
            suitable_employees = []
            for employee in self.employees:
                if all(skill in employee.skills for skill in required_skills):
                    suitable_employees.append(employee.name)
            print(f"For project '{project.name}', suitable employees are: {suitable_employees}")

# Sample data
project1 = Project("Project A", ["Python", "Machine Learning"])
project2 = Project("Project B", ["Data Analysis", "SQL"])
employee1 = Employee("Alice", ["Python", "Machine Learning", "Data Analysis"])
employee2 = Employee("Bob", ["SQL", "Data Analysis"])
employee3 = Employee("Charlie", ["Python", "SQL"])

projects = [project1, project2]
employees = [employee1, employee2, employee3]

# Create workforce planner instance
planner = WorkforcePlanner(projects, employees)

# Match skills to projects
planner.match_skills_to_projects()
