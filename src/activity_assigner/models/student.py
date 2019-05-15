# Class to model a student with choices
class Student:
    def __init__(self, name=None):
        self.name = name
        self.choices = {}
        self.assigned = {}

    def add_choice(self, choice=None, rank=0):
        self.choices[rank] = choice
    
    def set_choices(self, choices=[]):
        for i in range(len(choices)):
            self.choices[i] = choices[i]

    def get_choices(self):
        choices_array = []

        for i in range(len(self.choices)):
            choices_array.append(self.choices[i])
        
        return choices_array
    
    def add_assigned(self, choice=None, rank=0):
        self.assigned[rank] = choice

    def get_assigned(self):
        assigned_array = []

        for i in range(len(self.assigned)):
            assigned_array.append(self.assigned[i])
        
        return assigned_array