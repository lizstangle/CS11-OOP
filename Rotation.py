from Activity import Activity
from random import choice
class Rotation:
    # ininitalizing a brand new empty list
    def __init__(self): 
        self.activities_arr = []
        self.evening_activities_arr = []
        self.populate_activities()
        self.populate_evening_activities()

    def populate_activities(self):
        self.activities_arr.append(Activity("archery", "10 am", "field"))
        self.activities_arr.append(Activity("soccer", "10 am", "field"))
        self.activities_arr.append(Activity("pickleball", "10 am", "field"))
        self.activities_arr.append(Activity("kickball", "10 am", "field"))
        self.activities_arr.append(Activity("adventuretime", "10 am", "field"))
        self.activities_arr.append(Activity("paddleboarding", "2 pm", "dock"))
        self.activities_arr.append(Activity("extreme-canoe", "10 am", "dock"))
        self.activities_arr.append(Activity("kayaking", "10 am", "dock"))
        self.activities_arr.append(Activity("sailing", "2 pm", "dock"))
        self.activities_arr.append(Activity("sail-racing", "10 am", "dock"))
        self.activities_arr.append(Activity("swimming","2 pm", "dock"))
        self.activities_arr.append(Activity("pottery", "2 pm", "craft courts"))
        self.activities_arr.append(Activity("arts and crafts", "2 pm", "craft courts"))
        self.activities_arr.append(Activity("yoga", "2 pm", "field"))
        self.activities_arr.append(Activity("garden cookery", "2 pm", "garden"))
        self.activities_arr.append(Activity("Horsebackriding", "2 pm", "barn"))
        self.activities_arr.append(Activity("Horsebackriding", "10 am", "barn"))
        
        
    def get_activities(self):    
        
        activity = choice(self.activities_arr)
        # to only print activity title i would use variable activity and [] and put index position zero or call a function
        # use dot modifier. instance on left side and on right side i can call a method. activity.get_time 
        return activity

    def populate_evening_activities(self):
        self.activities_arr.append(Activity("skits", "8 pm", "Ruth Brown steps"))
        self.activities_arr.append(Activity("evening fires", "8 pm", "The Lodge"))
        self.activities_arr.append(Activity("singing", "8 pm", "Ruth Brown steps"))
        self.activities_arr.append(Activity("poetry", "8 pm", "Ruth Brown steps"))
        self.activities_arr.append(Activity("capture the chicken",  "8 pm", "Greenie Hill"))
        self.activities_arr.append(Activity("dances", "8 pm", "Boat Barn")) 


    def get_evening_activities(self):
        activity = choice(self.evening_activities_arr)

        return activity
        #   return f"Nights are magical at camp. {evening_play} by the stars, in crisp ocean air leads to the sweetest sleep ever."
        
        #   return f"Campers go on overnight {trip_theme} trips where they learn valuable wilderness skills and have a blast."

    def print_all_activities(self):
        print("Day-time Activities")
        for activity in self.activities_arr:
            print(activity)

        print("Evening-time Activities")
        for activity in self.evening_activities_arr:
            print(activity)       
