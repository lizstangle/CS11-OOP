from CampPopulation import CampPopulation
from Camper import Camper 
from Activity import Activity
from Counselor import Counselor

chloe = Camper("Chloe", 15, "Los Angeles", "sailing")
alec = Counselor("Alec", 19, "Bay Area", "Running")
isabel = Camper("Isabel", 9, "Seattle", "swimming")
annie = Counselor("Annie", 21, "Portland", "Musical Theater")

# print(chloe.greeting())
# print(alec.greeting())
# print(chloe.gets_cabin())
# print(chloe.gets_trip())

# act = Activity("2pm", "camp") 
# print(chloe.add_activity(act))

# print(alec.responsible_for_cabin())
# act = Activity("4pm", "greeny hill")
# print(alec.leads_evening_activities(act))

pickleball = Activity("3pm" "pickleball courts")
chloe.add_activity("twizzly bob")
chloe.add_activity("pickleball")
chloe.add_activity("arts and crafts")
print(chloe.activities)

print(annie.responsible_for_cabin())
print(chloe.greeting())
print(chloe.gets_trip())