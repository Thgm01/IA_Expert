def read_time_vel():
    time = float(input('Insert the duration (h): '))
    vel = float(input('Insert the velocity (km/h): '))
    return time, vel

def calc_distance(time, velocity):
    distace = time*velocity
    return distace

def liters_of_gas(distance, autonomy=12):
    liters = distance/autonomy
    return liters

def show_results(liters):
    print(f'You will need {liters:.2f} liters of gas for this trip!')

time, vel = read_time_vel()
distance = calc_distance(time, vel)
liters = liters_of_gas(distance)
show_results(liters)