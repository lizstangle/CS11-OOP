from CampPopulation import CampPopulation
from Camper import Camper 
from Activity import Activity
from Counselor import Counselor

chloe = Camper("Chloe", 15, "Argentina", "Sailing")
alec = Counselor("Alec", 19, "Bay Area", "Running")


# print(chloe.greeting())
# print(alec.greeting())
# print(chloe.gets_cabin())
# print(chloe.gets_trip())


act = Activity("2pm", "camp") 
print(chloe.add_activity(act))
print(alec.responsible_for_cabin())
act = Activity("4pm", "greeny hill")
print(alec.leads_evening_activities(act))

# lacrosse = Activity("afternoon", " Noon", "field")

# joi.add_activity("lacrosse")
# joi.add_activity("sailing")
# print(joi.activities)
# print(camper_bob.activities)

# camper_bob = Camper('Bob', 13, 'New York', 'Guitar')
# print(camper_bob.get_activities())

# print(camper_bob.gets_trip())
# print(camper_bob.gets_cabin())

# counselor_annie = Counselor('Annie', '21', 'Portland', 'Musical Theater')
# print(counselor_annie.responsible_for_cabin())
# print(joi.gets_trip())
# chloe = Camper('Chloe', 15, 'Los Angeles', 'Horses')
# print(chloe.greeting)
# print(chloe.gets_trip())