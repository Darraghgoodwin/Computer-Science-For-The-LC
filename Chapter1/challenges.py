def calcSpeed(d,t):
    speed = d/t
    return speed

def checkSpeedLimit(speed):
    limit = 30
    return limit

def timeTravelEstimater(d,speed):
    time = round(d/speed,1)
    return time
    
def converter(speed):
    km = round(
    


print("-----Average Speed Calculater-----")

distance = int(input("Enter a distance travelled in metres:"))
time = int(input("Enter the time to complete the journey:"))

avgSpeed = distance/time
print(avgSpeed)

avgSpeed = calcSpeed(distance, time)
print(avgSpeed)
print("The average speed is",round(avgSpeed,2))

speedLimit = checkSpeedLimit(avgSpeed)
if (avgSpeed < speedLimit):
    print("You going fast cheeky boy")
    
'''
Challenge 2: Travel Time Estimator
Create a function that uses the calculated avgSpeed to predict how long it would take to travel a much longer distance (like a marathon: 42,195 meters).
Hint: distance divided by speed
Round to 1 dp
'''
avgTime = timeTravelEstimater(distance,avgSpeed)
print("Average time:", avgTime)

'''Challenge 3: Convert to km/h
Average speed in meters per second (m/s) can be hard to visualize for cars. Create a function that converts avgSpeed into kilometers per hour (km/h).
Hint: To convert m/s to km/h, multiply the speed by 3.6.
Round to 2 dp
'''





