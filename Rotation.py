from Activity import Activity
from random import choice
class Rotation:
    # ininitalizing a brand new empty list
    def __init__(self): 
        self.activities_arr = []
        self.evening_activities_arr = []

    def populate_activities(self):
        activity = Activity("archery, "10 am", "field")  
        activity = Activity("soccer, "10 am", "field")
        activity = Activity("pickleball, "10 am", "field")
        activity = Activity("kickball, "10 am", "field")
        activity = Activity("adventuretime, "10 am", "field")
        activity = Activity("paddleboarding, "2 pm", "dock")
        activity = Activity("extreme-canoe, "10 pm", "dock")
        activity = Activity("kayaking, "10 am", "dock")
        activity = Activity("sailing, "2 pm", "dock")
        activity = Activity("sail-racing, "10 am", "dock")
        activity = Activity("swimming,"2 pm", "dock")
        activity = Activity("pottery, "2 pm", "craft courts")
        activity = Activity("arts and crafts", "2 pm", "craft courts")
        activity = Activity("yoga, "2 pm", "field")
        activity = Activity("garden cookery, "2 pm", "garden")
        activity = Activity("Horsebackriding, "2 pm", "barn")
        activity = Activity("Horsebackriding, "10 am", "barn")
        
        
        self.activities_arr.append(activity)
        # append function will populate the array
    #    activities_arr = ["sailing", "swimming", "gardening", "riding", "playing soccer"]
        
    def get_activities(self):    
        
        activity = choice(self.evening_activities_arr)
        # to only print activity title i would use variable activity and [] and put index position zero or call a function
        # use dot modifier. instance on left side and on right side i can call a method. activity.get_time 
        return activity

    def populate_evening_activities(self):
        activity = Activity("skits, "8 pm", "Ruth Brown steps")
        activity = Activity("evening fires, "8 pm", "The Lodge")
        activity = Activity("singing, "8 pm", "Ruth Brown steps")
        activity = Activity("poetry, "8 pm", "Ruth Brown steps")
        activity = Activity("capture the chicken  "8 pm", "Greenie Hill")
        activity = Activity("dances, "8 pm", "Boat Barn")  

        self.evening_activities_arr.append(activity)


    def get_evening_activities(self):
        activity = choice(self.activities_arr)

        return evening_activity
        #   return f"Nights are magical at camp. {evening_play} by the stars, in crisp ocean air leads to the sweetest sleep ever."
        
        #   return f"Campers go on overnight {trip_theme} trips where they learn valuable wilderness skills and have a blast."

    def print_all_activities(self):
        print("Day-time Activities")
        for activity in self.activities_arr:
            print(activity)

        print("Evening-time Activities")
        for activity in self.evening_activities_arr:
            print(activity)       
