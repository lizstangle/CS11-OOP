from random import choice
class Activity:
    def __init__(self, rotation_name, time, location): 
        self.time = time
        self.location = location
        self.rotation_name = rotation_name
        # within the class this array will be referenced
    # This class is only going to modify data within the class
    def get_location(self):
        return self.location

    def get_time(self): 
        return self.time
    
    def set_time(self, time):
        self.time = time

    def set_location(self, location):
        self.location = location    

    def get_title(self):
        return self.rotation_name

    
    #   return f"Nights are magical at camp. {evening_play} by the stars, in crisp ocean air leads to the sweetest sleep ever."
    
    #   return f"Campers go on overnight {trip_theme} trips where they learn valuable wilderness skills and have a blast."
