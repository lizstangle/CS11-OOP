from Activity import Activity
class CampPopulation:
    #Class Attributes
    camp_name = "Four Winds"
    camp_location = "Orcas Island"

    def __init__(self, name, age, hometown, interest):
        # public attributes
        self.name = name
        self.age = age
        self.hometown = hometown
        self.interest = interest

    def greeting(self, name, age, hometown, interest):   
      return f"I'm {name}. I'm {age}, from {hometown} and love {interest}."
  
