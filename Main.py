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


rot = Rotation()
# call random rotation function and pass info to the camper
rand = rot.get_activities()
chloe.add_activity(rand)


print(chloe.greeting())
print(alec.greeting())
print(chloe.gets_cabin())
print(chloe.gets_trip())

badminton = Activity("badminton", "10 am", "field") 

print(alec.responsible_for_cabin())
# print(alec.leads_evening_activities(badminton))

twizzly_bop = Activity("twizzly bop", "10 am", "dock")

print(chloe.activities)

print(annie.responsible_for_cabin())
print(chloe.greeting())
print(chloe.gets_trip())
rot = Rotation()
rot.print_all_activities()