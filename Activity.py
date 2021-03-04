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
      assign_random_activity = choice(activities_arr)
      assigned_activity = assign_random_activity     
      activity = assigned_activity
      return f'{self.name}\'s activity today is {activity}'

    def set_night_play(self):
      night_play_arr = ["evening_fires", "skits", "singing", "capture_the_chicken"]
      assign_random_night_play = choice(night_play_arr)
      assigned_night_play = assign_random_night_play     
      night_play = assigned_night_play
      return f"Nights are magical on {camp_location}. {Night_play} by the stars, in crisp ocean air leads to the sweetest sleep."
      
    def set_trip_themes(self):
      trip_themes_arr = ["canoeing", "kayaking", "hiking"]
      assign_random_trip_theme = choice(trip_theme_arr)
      trip_theme = assigned_trip_theme
      return f"Campers go on overnight {trip_themes} trips where they learn valuable wilderness skills and have a blast."