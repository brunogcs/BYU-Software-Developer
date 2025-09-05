import math
import datetime

#get user input (correct answer: 205, 60, 15 = 39.92)
width_mm            = int(input('Enter the width of the tire in mm (ex: 205): '))
aspect_ratio        = int(input('Enter the aspect ratio of the tire (ex: 60): '))
wheel_diameter_inch = int(input('Enter the diameter of the wheel in inches (ex: 15): '))

def compute_volume_liters():

    #compute volume liters
    width_mm_squared = width_mm ** 2
    avg_circumference_tire = (width_mm * aspect_ratio + 2540 * wheel_diameter_inch)
    area_base = math.pi * width_mm_squared
    profile_area =  area_base * aspect_ratio
    raw_volume_mm = profile_area * avg_circumference_tire
    volume_liters = raw_volume_mm / 10_000_000_000

    return format(volume_liters, ".2f")

def log_volume_liters(width_mm, aspect_ratio, wheel_diameter_inch, volume_liters):

    current_date= str(datetime.datetime.now().date())
    
    # Open a text file in append mode and insert the tire volume information
    with open("tire_volume.txt", "a") as tire_volume_file:
        print(current_date + ', ' + str(width_mm) + ', ' + str(aspect_ratio) + ', ' + str(wheel_diameter_inch) + ', ' + str(volume_liters), file=tire_volume_file)

if __name__ == "__main__":
    volume_liters = compute_volume_liters()
    print(f"The approximate volume is {volume_liters} liters.")
    log_volume_liters(width_mm, aspect_ratio, wheel_diameter_inch, volume_liters)