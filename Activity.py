from random import choice
class Activity:
    def __init__(self, name, time, location):
        self.name = name
        self.time = time
        self.location = location

    def show_activities(self):
        # composition: campers are composed of activities
        pass   
 

    def get_activities(self):    
      activities_arr = ["sailing", "swimming", "gardening", "riding", "playing soccer"]
      activity = choice(activities_arr)
      
      return f'{self.name}\'s activity today is {activity}'

    def set_night_play(self):
      night_play_arr = ["evening_fires", "skits", "singing", "capture_the_chicken"]
      night_play = choice(night_play_arr)
      
      return f"Nights are magical at camp. {night_play} by the stars, in crisp ocean air leads to the sweetest sleep."
      
    def set_trip_themes(self):
      trip_themes_arr = ["canoeing", "kayaking", "hiking"]
      trip_theme = choice(trip_themes_arr)
      
      return f"Campers go on overnight {trip_theme} trips where they learn valuable wilderness skills and have a blast."
