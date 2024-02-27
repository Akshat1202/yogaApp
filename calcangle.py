import numpy as np

def calculateAngle(a,b,c):
        cc = type(a)
        #print(cc)
        x1=a[0]
        x2=b[0]
        x3=c[0]
        y1=a[1]
        y2=b[1]
        y3=c[1]
        radians = np.arctan2(y3-y2, x3-x2) - np.arctan2(y1-y2, x1-x2)
        angle = np.abs(radians*180.0/np.pi)

        if angle >180.0:
            angle = 360-angle


        return angle