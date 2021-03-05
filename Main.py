from CampPopulation import CampPopulation
from Camper import Camper 
from Activity import Activity
from Counselor import Counselor
from Rotation import Rotation
# give access to all the funcitons in the rotation class

chloe = Camper("Chloe", 15, "Los Angeles", "sailing")
alec = Counselor("Alec", 19, "Bay Area", "Running")
annie = Counselor("Annie", 21, "Portland", "Musical theater")

# print(chloe.greeting())
# print(chloe.gets_cabin())
# print(chloe.gets_trip())

# print(alec.greeting()))
# print(alec.responsible_for_cabin())



# Need to call Rotation b/c it's an instance of Rotation class & 
# how we get access to the activities we want to print. 
rot = Rotation()
# call random rotation function and pass info to the camper
rand = rot.get_activities()
chloe.add_activity(rand)

print(alec.leads_evening_activities(rot))





# print(alec.responsible_for_cabin())


# twizzly_bop = Activity("twizzly bop", "10 am", "dock")

# print(chloe.activities)


# print(chloe.greeting())
# print(chloe.gets_trip())
# rot = Rotation()
# rot.print_all_activities()