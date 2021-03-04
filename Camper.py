from CampPopulation import CampPopulation
from random import choice

class Camper(CampPopulation):
    def __init__(self, name, age, hometown, interest):
      super().__init__(name, age, hometown, interest)
      self.cabin = None
      self.activities = []
      self.summers_at_camp = 0
      

    cabin_name_arr = ["Romany Winds", "Wandervogel", "Madrona", "Top Galent", "Moonraker", "7 Seas"]
    
    def gets_cabin(self):
      # Here I create the array that assigns names of cabins
      cabin_name_arr = ["Rominy Winds", "Wandervogel", "Jupiter", "Top Galent", "Moonraker", "Moose Tracks"]
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
    def add_activity(self, activity):
      self.activities.append(activity)

    # demonstrates override 
    def greeting(self, name, age, hometown, interest):   
        return(f"I'm {name} and I'm a camper. I'm {age}, from {hometown} and love {interest}.")  