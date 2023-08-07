# 1. Get user input for total number of vehicles
# 2. set the maximum limit speed. Take user input
# 3. use for loop till number of vehicle ends
# 4. get speed and vehicle details
# 5. filter the vehicle based on condition
# 6. display the vehicle details those are crossed max speed limit in descending order. when manager needs to see  the vehicles

No_of_vehicles = int(input("Enter the count of vehicles:"))
max_limit_speed = float(input("Set maximum speed limit:"))

vehicle_details = {}


def getdetails(No_of_vehicles):
    for i in range(No_of_vehicles):
        vehicle_num = input("Enter vehicle no:")
        speed_vehicle = float(input("Speed of the vehicle:"))
        if speed_vehicle > max_limit_speed:
            vehicle_details[vehicle_num] = speed_vehicle


officer = input("Do you want to display the result:")
getdetails(No_of_vehicles)
if officer == 'yes':
    print("Vehicles crossing speed limit are", vehicle_details)

sorted(vehicle_details.items(), key=lambda x: x[-1], reverse=True)
sorted_vehicles = {i: j for i, j in sorted(
    vehicle_details.items(), key=lambda x: x[-1], reverse=True)}

print("Sorted vehicles on their speed limit are: ", sorted_vehicles)
