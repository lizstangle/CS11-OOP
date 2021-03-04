from CampPopulation import CampPopulation
from Camper import Camper 
from Activity import Activity
from Counselor import Counselor

joi = Camper("Joi Anderson", 25, "NYC", "Swimming")
# lacrosse = Activity("afternoon", " Noon", "field")

# joi.add_activity("lacrosse")
# joi.add_activity("sailing")
# print(joi.activities)
# print(camper_bob.activities)

camper_bob = Camper('Bob', 13, 'New York', 'Guitar')
print(camper_bob.get_activities())

print(camper_bob.gets_trip())
print(camper_bob.gets_cabin())

counselor_annie = Counselor('Annie', '21', 'Portland', 'Musical Theater')
print(counselor_annie.responsible_for_cabin())
print(joi.gets_trip())
chloe = Camper('Chloe', 15, 'Los Angeles', 'Horses')
print(chloe.gets_trip())