import math

l = 640.0
b = 480.0
max = math.sqrt(l**2 + b**2)
min = math.sqrt(2)
mid = [l//2, b//2]
lat = 12.9939455
lon = 77.66040169999997
const = 0.000002
data = [{ 'br': [583, 479], 'tl': [165, 205]}, { 'br': [200, 200], 'tl': [300, 350]}]

def calc(dist, x, y, depth):

    R = 6378.1 #Radius of the Earth
    brng = math.radians(90) #Bearing is 90 degrees converted to radians.
    d = dist/1000.0 #Distance in km

    #lat2  52.20444 - the lat result I'm hoping for
    #lon2  0.36056 - the long result I'm hoping for.

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

    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)

    return {'lat': lat2, 'lon': lon2}

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
