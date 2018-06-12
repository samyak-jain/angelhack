import math

# Distance calculation and latitiude and longitude calculations
# Calculates the latitute and laongitude positions of a person form the image frame based on YOLO outputs

# Input:
# tl - top left pixel value of the box
# br - bottom left pixel value of the box

# Output:
# New longitude and latitiude positon of the person to be updated to firebase


# frame pixed size 600 X 800 pixels

l = 600
b = 800

# Maximum and minimun possible frame sizes (diagonal length)
max = math.sqrt(l**2 + b**2)
min = math.sqrt(2)
mid = [l//2, b//2]

# Drone latitude and longitude (update)
lat = 12.9939455
lon = 77.66040169999997

# Spread constant
const = 0.000002

# Sample data
data = [{ 'br': [583, 479], 'tl': [165, 205]}, { 'br': [200, 200], 'tl': [300, 350]}]

# Return:
# GPS coordinates
def get_locations(annots):
    res = vals(annots['tl'][0], annots['tl'][1], annots['br'][0], annots['br'][1])
    return calc(*res)

# Calculating new longitude and latitiude positions

# Input:
# dist: Distance
# x: row positon of centre
# y: column position of centre
# depth: distance of object from camera

# Return:
# latitude and longitude
def calc(dist, x, y, depth):

    R = 6378.1 #Radius of the Earth
    brng = math.radians(90) #Bearing is 90 degrees converted to radians.
    d = dist/1000.0 #Distance in km

    lat1 = math.radians(lat) #Current lat point converted to radians
    lon1 = math.radians(lon) #Current long point converted to radians

    if x>=mid[0] and y>mid[1]:
        print('A')
        lat2 = lat1 + 0.001 * math.asin( math.sin(lat1)*math.cos(d/R) +
             math.cos(lat1)*math.sin(d/R)*math.cos(brng))

        lon2 = math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
                     math.cos(d/R)-math.sin(lat1)*math.sin(lat2)) + const
    elif x>mid[0]:
        print('B')
        lat2 = lat1 - 0.001 * math.asin( math.sin(lat1)*math.cos(d/R) +
             math.cos(lat1)*math.sin(d/R)*math.cos(brng))

        lon2 = math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
                     math.cos(d/R)-math.sin(lat1)*math.sin(lat2)) + const
    elif y>mid[1]:
        print('C')
        lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
             math.cos(lat1)*math.sin(d/R)*math.cos(brng)) + const

        lon2 = lon1 + 0.01 * math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
                     math.cos(d/R)-math.sin(lat1)*math.sin(lat2))
    else:
        print('D')
        lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
             math.cos(lat1)*math.sin(d/R)*math.cos(brng)) + const

        lon2 = lon1 - 0.01 * math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
                     math.cos(d/R)-math.sin(lat1)*math.sin(lat2))

    lat2 = math.degrees(lat2) # Final latitude position converted to degrees
    lon2 = math.degrees(lon2) # Final longitude position converted to degrees

    return {'lat': lat2, 'lon': lon2}

# Calcualte depth and distance (diagonal)

# Input:
# x1, y1: tl point cooridinates
# x2, y2: br point coordinates

# Return:
# lenght of diagonal,
# row positon of centre
# y: column position of centre
# depth: distance form camera
def vals(x1, y1, x2, y2):

    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    x, y = abs(x1-x2//2), abs(y1-y2//2)
    depth = min/max * dist * 200
    return(dist, x, y, depth)

if __name__ == "__main__":

    result = []

    for each in data:
        x1, y1 = map(float, each['tl'])
        x2, y2 = map(float, each['br'])
        print(vals(x1, x2, y1, y1))
        lst = vals(x1, x2, y1, y2)
        result.append(calc(lst[0], lst[1], lst[2], lst[3]))

    print(result)
    print(min, max)

    for i in result:
        print(str(i['lat']) + "," + str(i['lon']) + ",a")
    print(str(lat) + "," + str(lon) + ",abc")

