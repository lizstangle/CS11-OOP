from random import choice
class Activity:
    def __init__(self, time, location): 
        self.time = time
        self.location = location

    def show_activities(self):
        # composition: campers are composed of activities
        pass   
 

    def get_activities(self):    
      activities_arr = ["sailing", "swimming", "gardening", "riding", "playing soccer"]
      activity = choice(activities_arr)
      return activity

    def set_evening_activities(self):
      evening_play_arr = ["evening_fires", "skits", "singing", "capture_the_chicken"]
      evening_play = choice(evening_play_arr)
      return evening_play
    #   return f"Nights are magical at camp. {evening_play} by the stars, in crisp ocean air leads to the sweetest sleep ever."
    
    #   return f"Campers go on overnight {trip_theme} trips where they learn valuable wilderness skills and have a blast."
