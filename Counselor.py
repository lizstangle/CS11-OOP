from CampPopulation import CampPopulation
from random import choice
class Counselor(CampPopulation):
  def __init__(self, name, age, hometown, interest):
    super().__init__(name, age, hometown, interest) 
    self.cabin = None
    self.activities = []
    self.camp_duration = 0

  def greeting(self, name, age, hometown, interest):   
    return f"I'm {name}. I'm {age}, from {hometown} and love {interest}."

  def responsible_for_cabin(self):
     # Here I create the array that assigns names of cabins
    cabin_name_arr = ["Romany Winds", "Wandervogel", "Juniper", "Top Gallant", "Moonraker", "Top Sail"]
      # Random cabin assignment by using "choice"
    assign_random_cabin = choice(cabin_name_arr)
    assigned_cabin = assign_random_cabin     
    cabin = assigned_cabin
    
    return f"I am Counselor {self.name} I am in charge of {cabin}"

  def leads_activities():
    pass