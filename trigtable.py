import numpy as np

def trigtable2():
    print("angle\t\tsin\t\tcos\t\ttan")
    for ang in range(0,4):
        a = ang*np.pi/6
        s,c,t = np.sin(a),np.cos(a),np.tan(a)
        deg = np.round(np.degrees(a))
        if (deg<90):
            print("{0:2.0f}\t\t{1:7.6f}\t{2:7.6f}\t{3:7.6f}".format(deg,s,c,t))
        else:
            print("{0:2.0f}\t\t{1:7.6f}\t{2:7.6f}\t{3}".format(deg,s,c,"undefined"))

trigtable2()

