from CampPopulation import CampPopulation
from Activity import Activity
from random import choice
class Counselor(CampPopulation):
  def __init__(self, name, age, hometown, interest):
    super().__init__(name, age, hometown, interest) 
    self.cabin = None
    self.activities = []
    self.camp_duration = 0

  #This greeting overrides the greeting in CampPolulation.py 
  def greeting(self):   
    return f"I'm counselor {self.name}. I'm {self.age}, from {self.hometown} and love {self.interest}."

  def responsible_for_cabin(self):
     # Here I create the array that assigns names of cabins
    cabin_arr = ["Romany Winds", "Wandervogel", "Juniper", "Top Gallant", "Moonraker", "Top Sail"]
      # Random cabin assignment by using "choice"
    cabin = choice(cabin_arr)
    return cabin
    
  def leads_evening_activities(self, activity):
    play = activity.get_evening_activities()
    self.activities.append(play)
    return f"Tonight's evening activity will be {play} with {self.name}."
    # return night_play

    