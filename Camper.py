class Camper(CampPopulation):
    def __init__(self, name, age: int, hometown, interest):
        super.()__init__(name, age: int, hometown, interest) 
        self.cabin = None
        self.activities = []
        self.summers_at_camp = 0
        self.camp_duration = 0
        self.trip_duration = 0
    # composition: campers are composed of activities
    def add_activity(self, activity):
      self.activities.append(activity)

    # demonstrates override 
    def greeting(self, name, age, hometown, interest):   
        return(f"I'm {name} and I'm a camper. I'm {age}, from {hometown} and love {interest}.")  
      
