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

    def set_title(self, title):
        self.title = title    

    def __repr__(self):
        return f"Do {self.rotation_name} at {self.time} in {self.location}"