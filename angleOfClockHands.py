time = input("Time ( ex: 07:35 ):  ")
hour = int(time.split(":")[0])
minute = int(time.split(":")[1])

def findAngle(h, m):
    ha = h*30 + m*0.5
    angle = abs(ha - m*6)
    return angle

print(findAngle(hour, minute))
