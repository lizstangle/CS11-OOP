from Camper import Camper 
from Activity import Activity

joi = Camper("Joi Anderson", 25, "NYC", "Swimming")
lacrosse = Activity("afternoon", "field")
joi.add_activity("lacrosse")
joi.add_activity("sailing")


print(joi.activities)