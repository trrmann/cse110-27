"""
    filname:  amusementParkRides.py
        Rules:
        1)  No one under 36 inches may ever ride, either by themselves or with another rider.
        2)  Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.
        3)  If there are two riders and one of them is at least 18 years old, they may ride together.
        Requirements:
        1)  Prompt the user for the age and height of the first person. Then, ask whether there is a second rider, and if so, ask for their age and height.
        2)  Handle the case of a single rider.
        3)  Finish implementing the basic rules.
    author:  Tracy Mann
    version:  1.0
    date:  10/18/2022
    class:  CSE110
    teacher:  Brother Wilson
    section:  27
        inputs:  an integer to represent the age of the first rider from the user to the question "What is the rider's age? "
                 a floating point decimal to represent the height of the first rider from the user to the question "How tall is the the rider in inches?"
                 a boolean to represent if there is a second rider from the user to the question "Is there a second rider? "
                 if there is a second rider an integer to represent the age of the second rider from the user to the question "What is the second rider's age? "
                 if there is a second rider a floating point decimal to represent the height of the second rider from the user to the question "How tall is the 
                    the second rider in inches?"
        process:  if-elif-else statements to determine if the riders may ride the ride.
        output:  "Sorry you may not ride this ride." for no or "Welcome to the ride.  Please be safe and have fun!" for yes
    version 1.1:
    date:  10/19/2022
        inputs:  if either is 12 to 17 years old a boolean to represent if they have a golden passport from the user to the question "Do you have a golden passport? "
        process:  if-elif-else statements to determine the additional cases
    Challenge:
        Requirements:
        1)  If there are two riders, but neither one is at least 18 years old, they may still ride as long as they are both at least 12 years old and at least 52
                inches tall.
        2)  If a person is age 12–17, ask if that person has a golden passport. If they do, they should be treated as if they were 18 years old for the sake of
                all rules. (Don't forget to apply this to the single rider case.)
        3)  If there are two riders, but neither one is at least 18 years old, they may still ride if one rider is at least 16 years old and the other is at least
                14. (Keep in mind that the first rider may be the younger of the two or they may be the older of the two.)
"""
from input import *

def request_rider_information(rider_identifier: str = "first"):
    rider = {}
    if rider_identifier == "first":
        rider_id = ""
    else:
        rider_id = f"{rider_identifier} "
    rider[age_key] = input_integer(f"What is the {rider_id}rider's age? ", "Invalid Age, Please Try again!", 0, 150)
    rider[height_key] = input_float(f"How tall is the the {rider_id}rider in inches? ", "Invalid Height, Please Try again!", 6.0, 100.0)
    # added in version 1.1 req. 2
    rider[golden_pass_key] = False
    # added in version 1.1 req. 2
    if (rider[age_key] >= 12) and (rider[age_key] <= 17):
        rider[golden_pass_key] = input_bool(f"Does the {rider_id}rider have a Golden Pass? ", "Invalid Reply, try (Y)es or (N)o!", ["Y", "YES"], ["N", "NO"])
    return rider

def validate_rider(**rider_information):
    rider_information["rider_information"][can_ride_key] = True
    rider_information["rider_information"][can_ride_alone_key] = False
    rider_information["rider_information"][adult_key] = False
    rider_information["rider_information"][minor_key] = True
    rider_information["rider_information"][tall_minor_pair_key] = False
    # added in version 1.1 req. 3
    rider_information["rider_information"][minor_pair_sponsor_key] = False
    # added in version 1.1 req. 3
    rider_information["rider_information"][minor_pair_sponsorable_key] = False
    # changed in version 1.1 req. 2
    #if rider_information["rider_information"][age_key] >= 18:
    if (rider_information["rider_information"][age_key] >= 18) or rider_information["rider_information"][golden_pass_key]:
        rider_information["rider_information"][adult_key] = True
    # added in version 1.1 req. 1
    elif rider_information["rider_information"][age_key] >= 12 and rider_information["rider_information"][height_key] >= 52:
        rider_information["rider_information"][tall_minor_pair_key] = True
    # added in version 1.1 req. 3
    if (not rider_information["rider_information"][adult_key]) and rider_information["rider_information"][age_key] >= 16:
        rider_information["rider_information"][minor_pair_sponsor_key] = True
    # added in version 1.1 req. 3
    if (not rider_information["rider_information"][adult_key]) and rider_information["rider_information"][age_key] >= 14:
        rider_information["rider_information"][minor_pair_sponsorable_key] = True
    if rider_information["rider_information"][height_key] < 36:
        rider_information["rider_information"][can_ride_key] = False
    elif (rider_information["rider_information"][height_key] >= 62) and rider_information["rider_information"][adult_key]:
        rider_information["rider_information"][can_ride_alone_key] = True
    return rider_information["rider_information"]

def validate_riders(**rider_collection):
    for rider_key, rider_value in rider_collection["rider_collection"].items():
        rider_collection["rider_collection"][rider_key] = validate_rider(rider_information = rider_value)
    return rider_collection["rider_collection"]

first_rider_key = "first"
second_rider_key = "second"
age_key = "age"
height_key = "height"
can_ride_key = "canRide"
adult_key = "adult"
minor_key = "minor"
# added in version 1.1 req. 1
tall_minor_pair_key = "tallMinorPair"
# added in version 1.1 req. 2
golden_pass_key = "goldenPass"
# added in version 1.1 req. 3
minor_pair_sponsor_key = "minorPairSponsor"
# added in version 1.1 req. 3
minor_pair_sponsorable_key = "minorPairSponsorable"
can_ride_alone_key = "canRideAlone"
has_second_rider = False
riders = {}
riders[first_rider_key] = request_rider_information()
has_second_rider = input_bool("Is there a second rider? ", "Invalid Reply, try (Y)es or (N)o!", ["Y", "YES"], ["N", "NO"], False)
if has_second_rider:
    riders[second_rider_key] = request_rider_information("second")
riders = validate_riders(rider_collection = riders)
if len(riders) > 1:
    if riders[first_rider_key][adult_key] or riders[second_rider_key][adult_key]:
        print("Welcome to the ride.  Please be safe and have fun!")
    # added in version 1.1 req. 1
    elif riders[first_rider_key][tall_minor_pair_key] and riders[second_rider_key][tall_minor_pair_key]:
        print("Welcome to the ride.  Please be safe and have fun!")
    # added in version 1.1 req. 3
    elif (riders[first_rider_key][minor_pair_sponsor_key] and riders[second_rider_key][minor_pair_sponsorable_key]) or (riders[second_rider_key][minor_pair_sponsor_key] and riders[first_rider_key][minor_pair_sponsorable_key]):
        print("Welcome to the ride.  Please be safe and have fun!")
    elif riders[first_rider_key][can_ride_key] and riders[first_rider_key][can_ride_key]:
        print("Sorry you may not ride this ride together, you need one rider over 18.")
    elif (not riders[first_rider_key][can_ride_key]) and (not riders[first_rider_key][can_ride_key]):
        print("Sorry neither rider may ride this ride at all.")
    elif (not riders[first_rider_key][can_ride_key]):
        print("Sorry the first rider may not ride this ride at all.")
    else:
        print("Sorry the second rider may not ride this ride at all.")
else:
    if riders[first_rider_key][can_ride_alone_key]:
        print("Welcome to the ride.  Please be safe and have fun!")
    elif riders[first_rider_key][can_ride_key]:
        print("Sorry you may not ride this ride alone.")
    else:
        print("Sorry you may not ride this ride at all.")