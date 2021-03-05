from CampPopulation import CampPopulation
from Camper import Camper 
from Activity import Activity
from Counselor import Counselor
from Rotation import Rotation
# give access to all the funcitons in the rotation class

chloe = Camper("Chloe", 15, "Los Angeles", "sailing")
alec = Counselor("Alec", 19, "Bay Area", "Running")
isabel = Camper("Isabel", 9, "Seattle", "swimming")
annie = Counselor("Annie", 21, "Portland", "Musical Theater")

# instantiated rotation class
rotation = Rotation()
# the dot is the instance and calling a s
# pecific method within that instance. (left side instance and right side is part of hte class)
rotation.populate_activities()

# call random rotation function and pass info to the camper
random = rotation.get_activities()
chloe.add_activity(random)


# print(chloe.greeting())
# print(alec.greeting())
# print(chloe.gets_cabin())
# print(chloe.gets_trip())

# act = Activity("2pm", "camp") 
# print(chloe.add_activity(act))

# print(alec.responsible_for_cabin())
# print(alec.leads_evening_activities(act))

# pickleball = Activity("3pm" "pickleball courts")
# chloe.add_activity("twizzly bob")
# chloe.add_activity("pickleball")
# chloe.add_activity("arts and crafts")
# print(chloe.activities)

# print(annie.responsible_for_cabin())
# print(chloe.greeting())
# print(chloe.gets_trip())