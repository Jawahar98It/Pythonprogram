number_of_vehicles = int(input("Enter the number of vehicles: "))
speed_limit = float(input("Enter the speed limit (in km/h): "))

vehicle_details = {}

def check_speed():
    for i in range(number_of_vehicles):
        vehicle_no = input("Enter vehicle number: ")
        speed = float(input("Enter vehicle speed (in km/h): "))

        if speed > speed_limit:
            vehicle_details[vehicle_no] = speed

# Call the function
check_speed()

officer = input("Do you want to display details? (yes/no): ")
vehicle_details ={i:j for i,j in sorted(vehicle_details.items(), key=lambda x: x[1], reverse=True)}
if officer.lower() == "yes":
    print("Vehicles that crossed the speed limit:")
    for vehicle, speed in vehicle_details.items():
        print(f"Vehicle Number: {vehicle}, Speed: {speed} km/h")

