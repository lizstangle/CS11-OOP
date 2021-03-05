from CampPopulation import CampPopulation
from Activity import Activity
from random import choice
from Rotation import Rotation

class Camper(CampPopulation, Activity):
    def __init__(self, name, age, hometown, interest):
      super().__init__(name, age, hometown, interest)
      self.cabin = None
      self.activities = []
    
    def gets_cabin(self):
      # Here I create the array that assigns a cabin
      cabin_arr = ["Romany Winds", "Wandervogel", "Juniper", "Top Gallant", "Moonraker", "Top Sail"]
      # Random cabin assignment by using "choice"
      cabin = choice(cabin_arr)
      
      return f"{self.name} is in the {cabin} cabin."

# must use self.tripduration because it is an instance variable
    def gets_trip(self, trip_duration=0):
      if self.age <= 12:
        self.trip_duration = 3
      else: 
        self.trip_duration = 7 


    # def set_trip_themes(self):
      trip_themes_arr = ["canoeing", "kayaking", "hiking"]
      trip_theme = choice(trip_themes_arr)  

      return f"Going on a {trip_theme} trip for {self.trip_duration} days is an adventure of a lifetime."

    # composition: campers are composed of activities which is composition from the Actities class. 
    def add_activity(self, activity):
    #   play = activity.get_activities()
      self.activities.append(activity)
      print(f'{self.name}\'s activity today is {activity.get_title()}')


    # demonstrates override 
    def greeting(self): 
      return(f"I'm {self.name} and I'm a camper. I'm {self.age}, from {self.hometown} and love {self.interest}.")

   