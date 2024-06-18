class CapabilityModel:
    def __init__(self, name):
        self.name = name
        self.skills = set()
        self.competencies = set()

    def add_skill(self, skill):
        self.skills.add(skill)

    def add_competency(self, competency):
        self.competencies.add(competency)

    def remove_skill(self, skill):
        self.skills.discard(skill)

    def remove_competency(self, competency):
        self.competencies.discard(competency)

    def list_skills(self):
        return list(self.skills)

    def list_competencies(self):
        return list(self.competencies)

    def __str__(self):
        return f"Capability Model: {self.name}\nSkills: {', '.join(self.skills)}\nCompetencies: {', '.join(self.competencies)}"

class CPGDivision:
    def __init__(self):
        self.capability_models = {}

    def add_capability_model(self, name):
        if name not in self.capability_models:
            self.capability_models[name] = CapabilityModel(name)

    def get_capability_model(self, name):
        return self.capability_models.get(name, None)

    def ensure_future_demands(self):
        # Implementation to ensure future demands can be met
        pass

# Example Usage
cpg_division = CPGDivision()
cpg_division.add_capability_model("Future Ready Model")

future_ready_model = cpg_division.get_capability_model("Future Ready Model")
future_ready_model.add_skill("Data Analysis")
future_ready_model.add_competency("Leadership")

print(future_ready_model)
