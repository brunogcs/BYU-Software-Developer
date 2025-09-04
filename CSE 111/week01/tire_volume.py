import math

#get user input
width_mm            = float(input('Enter the width of the tire in mm (ex: 205): '))
aspect_ratio        = float(input('Enter the aspect ratio of the tire (ex: 60): '))
wheel_diameter_inch = float(input('Enter the diameter of the wheel in inches (ex: 15): '))

#compute volume liters
width_mm_squared = width_mm ** 2
avg_circumference_tire = (width_mm * aspect_ratio + 2540 * wheel_diameter_inch)
area_base = math.pi * width_mm_squared
profile_area =  area_base * aspect_ratio
raw_volume_mm = profile_area * avg_circumference_tire
volume_liters = raw_volume_mm / 10_000_000_000

print(f"The approximate volume is {volume_liters:.2f} liters.")