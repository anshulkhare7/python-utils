#!/usr/bin/env python

polyCorners = 4
poly_1_x = [22.017965, 22.017852, 22.016992, 22.017187]
poly_1_y = [85.432761, 85.433074, 85.432577, 85.432243]

poly_2_x = [22.017187, 22.016992, 22.015849, 22.015982]
poly_2_y = [85.432243, 85.432577, 85.431865, 85.431574]

poly_3_x = [22.015850, 22.015636, 22.015874, 22.016053]
poly_3_y = [85.431406, 85.43173, 85.431889, 85.431516]

def main():
    point_M = (22.017603, 85.432641)
    point_L = (22.016598, 85.432157)
    point_O = (22.015838, 85.431621)
    print("Does the point{} lie in the polygon? {}".format(str(point_O), pointInPolygon(point_O, poly_3_x, poly_3_y)))

def pointInPolygon(point, polyX, polyY):
    i = 0
    j = polyCorners-1
    x = point[0]
    y = point[1]
    oddNodes = False
    print(polyX)
    print(polyY)
    for i in range(0, polyCorners):
        if((polyY[i]<y and polyY[j]>=y) or (polyY[j]<y and polyY[i]>=y)): 
            if (polyX[i]+(y-polyY[i])/(polyY[j]-polyY[i])*(polyX[j]-polyX[i])<x): 
                oddNodes = not oddNodes         
        j=i

    return oddNodes

if __name__=="__main__":
    main()