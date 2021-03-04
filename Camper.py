from CampPopulation import CampPopulation
from Activity import Activity
from random import choice

class Camper(CampPopulation, Activity):
    def __init__(self, name, age, hometown, interest):
      super().__init__(name, age, hometown, interest)
      self.cabin = None
      self.activities = []
    
    def gets_cabin(self):
      # Here I create the array that assigns names of cabins
      cabin_name_arr = ["Romany Winds", "Wandervogel", "Juniper", "Top Gallant", "Moonraker", "Top Sail"]
      # Random cabin assignment by using "choice"
      assign_random_cabin = choice(cabin_name_arr)
      assigned_cabin = assign_random_cabin     
      cabin = assigned_cabin
      return f"{self.name} has been assigned to cabin: {cabin}"

    def gets_trip(self, trip_duration=0):
      if self.age <= 12:
        trip_duration = 3
      else: 
        trip_duration = 7 
      return f"Trip duration was changed to {trip_duration} days"   

    # composition: campers are composed of activities
    def add_activity(self):
      func_call = Activity.get_activities()
      return func_call

    # demonstrates override 
    def greeting(self, name, age, hometown, interest):   
      return(f"I'm {name} and I'm a camper. I'm {age}, from {hometown} and love {interest}.")  