'''
Author: Holden Vail
KUID: 2936812
Date: 2022/09/12
Lab: lab02
Last modified: 2022/09/12
Purpose: This program helps users define the type of storm based off wind speed
'''

wind_speed = float(input("Input a wind speed (m/s)"))
    
if wind_speed < 0:
    print("Error. Please input a valid wind speed.")
elif 0 <= wind_speed < 18:
    storm_type = "tropical depression"
    print("A hurricane with a windspeed of", wind_speed, "m/s is a",storm_type)
elif 18 <= wind_speed < 33:
    storm_type = "tropical storm"
    print("A hurricane with a windspeed of", wind_speed, "m/s is a",storm_type)
elif 33 <= wind_speed < 43:
    storm_type = "Cat 1"
    print("A hurricane with a windspeed of", wind_speed, "m/s is a",storm_type)
elif 43 <= wind_speed < 50:
    storm_type = "Cat 2"
    print("A hurricane with a windspeed of", wind_speed, "m/s is a",storm_type)
elif 50 <= wind_speed < 58:
    storm_type = "Cat 3"
    print("A hurricane with a windspeed of", wind_speed, "m/s is a",storm_type)
elif 58 <= wind_speed < 70:
    storm_type = "Cat 4"
    print("A hurricane with a windspeed of", wind_speed, "m/s is a",storm_type)
else:
    storm_type = "Cat 5"
    print("A hurricane with a windspeed of", wind_speed, "m/s is a",storm_type)