def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third
  
most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()
print(most_popular1)
print(most_popular2)
print(most_popular3)
print("Can't take this")



#Functions test
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)
trip_planner_welcome("Gleb")
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time
estimate = estimated_time_rounded(4.7)
def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print('Your trip starts off in ' + origin)
  print('And you are traveling to ' + destination)
  print('You will be traveling by ' + mode_of_transport)
  print('It will take approximately ' + str(estimated_time) + ' hours')
destination_setup('Summer palace', "Lama Temple", estimate)
