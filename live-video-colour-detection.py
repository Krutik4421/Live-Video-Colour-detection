import cv2
import numpy as np
import imutils

cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
        _,frame= cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        # Range for lower
        lower_red = np.array([0,50,50])
        upper_red = np.array([10,255,255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        lower_orange = np.array([11,50,50])
        upper_orange = np.array([20,255,255])
        mask3 = cv2.inRange(hsv, lower_orange, upper_orange)

        lower_yellow = np.array([21,50,50])
        upper_yellow = np.array([30,255,255])
        mask5 = cv2.inRange(hsv, lower_yellow, upper_yellow)

        lower_green = np.array([31,50,50])
        upper_green = np.array([80,255,255])
        mask7 = cv2.inRange(hsv, lower_green, upper_green)

        lower_light_blue = np.array([81,50,50])
        upper_light_blue = np.array([110,255,255])
        mask11 = cv2.inRange(hsv, lower_light_blue, upper_light_blue)

        lower_blue = np.array([111,50,50])
        upper_blue = np.array([130,255,255])
        mask13 = cv2.inRange(hsv, lower_blue, upper_blue)

        lower_violet = np.array([131,50,50])
        upper_violet = np.array([140,255,255])
        mask15 = cv2.inRange(hsv, lower_violet, upper_violet)

        lower_purple = np.array([141,50,50])
        upper_purple = np.array([160,255,255])
        mask17 = cv2.inRange(hsv, lower_purple, upper_purple)

        lower_pink = np.array([161,50,50])
        upper_pink = np.array([170,255,255])
        mask19 = cv2.inRange(hsv, lower_pink, upper_pink)

        lower_gray = np.array([0,0,10])
        upper_gray = np.array([0,0,225])
        mask21 = cv2.inRange(hsv, lower_gray, upper_gray)

        # Range for upper range
        lower_red = np.array([170,120,70])
        upper_red = np.array([180,255,255])
        mask2 = cv2.inRange(hsv,lower_red,upper_red)

        lower_orange = np.array([181,120,70])
        upper_orange = np.array([190,255,255])
        mask4 = cv2.inRange(hsv,lower_orange,upper_orange)

        lower_yellow = np.array([191,120,70])
        upper_yellow = np.array([200,255,255])
        mask6 = cv2.inRange(hsv, lower_yellow, upper_yellow)

        lower_green = np.array([201,120,70])
        upper_green = np.array([250,255,255])
        mask8 = cv2.inRange(hsv, lower_green, upper_green)

        lower_light_blue = np.array([251,120,70])
        upper_light_blue = np.array([290,255,255])
        mask12 = cv2.inRange(hsv, lower_light_blue, upper_light_blue)

        lower_blue = np.array([291,120,70])
        upper_blue = np.array([300,255,255])
        mask14 = cv2.inRange(hsv, lower_blue, upper_blue)

        lower_violet = np.array([301,120,70])
        upper_violet = np.array([310,255,255])
        mask16 = cv2.inRange(hsv, lower_violet, upper_violet)

        lower_purple = np.array([311,120,70])
        upper_purple = np.array([330,255,255])
        mask18 = cv2.inRange(hsv, lower_purple, upper_purple)

        lower_pink = np.array([331,120,70])
        upper_pink = np.array([340,255,255])
        mask20 = cv2.inRange(hsv, lower_pink, upper_pink)

        lower_gray = np.array([361,120,70])
        upper_gray = np.array([380,255,255])
        mask22 = cv2.inRange(hsv, lower_gray, upper_gray)
        # Generating the final mask to detect red color
        mask1 = mask1+mask2
        mask3 = mask3+mask4
        mask5 = mask5+mask6
        mask7 = mask7+mask8
        mask11 = mask11+mask12
        mask13 = mask13+mask14
        mask15 = mask15+mask16
        mask17 = mask17+mask18
        mask19 = mask19+mask20
        mask21 = mask21+mask22

        borderc1=cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        borderc1=imutils.grab_contours(borderc1)

        borderc2=cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        borderc2=imutils.grab_contours(borderc2)

        borderc3=cv2.findContours(mask5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        borderc3=imutils.grab_contours(borderc3)

        borderc4=cv2.findContours(mask7, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        borderc4=imutils.grab_contours(borderc4)

        borderc6=cv2.findContours(mask11, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        borderc6=imutils.grab_contours(borderc6)

        borderc7=cv2.findContours(mask13, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        borderc7=imutils.grab_contours(borderc7)

        borderc8=cv2.findContours(mask15, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        borderc8=imutils.grab_contours(borderc8)

        borderc9=cv2.findContours(mask17, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        borderc9=imutils.grab_contours(borderc9)

        borderc10=cv2.findContours(mask19, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        borderc10=imutils.grab_contours(borderc10)

        borderc11=cv2.findContours(mask21, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        borderc11=imutils.grab_contours(borderc11)

        for a in borderc1:
                Carea = cv2.contourArea(a)
                if Carea > 1500:
                    cv2.drawContours(frame,[a],-1,(0,255,0), 1)
                    centroid = cv2.moments(a)
                    cx = int(centroid["m10"]/ centroid["m00"])
                    cy = int(centroid["m01"]/ centroid["m00"])
                    cv2.circle(frame,(cx,cy),1,(0,0,0),0)
                    cv2.putText(frame, "Red", (cx-10, cy-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255))

        for a in borderc2:
                Carea = cv2.contourArea(a)
                if Carea > 1500:
                    cv2.drawContours(frame,[a],-1,(0,255,0), 1)
                    centroid = cv2.moments(a)
                    cx = int(centroid["m10"]/ centroid["m00"])
                    cy = int(centroid["m01"]/ centroid["m00"])
                    cv2.circle(frame,(cx,cy),1,(0,0,0),0)
                    cv2.putText(frame, "Orange", (cx-20, cy-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255))


        for a in borderc3:
                Carea = cv2.contourArea(a)
                if Carea > 1500:
                    cv2.drawContours(frame,[a],-1,(0,255,0), 1)
                    centroid = cv2.moments(a)
                    cx = int(centroid["m10"]/ centroid["m00"])
                    cy = int(centroid["m01"]/ centroid["m00"])
                    cv2.circle(frame,(cx,cy),1,(0,0,0),0)
                    cv2.putText(frame, "Yellow", (cx-10, cy-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255))


        for a in borderc4:
                Carea = cv2.contourArea(a)
                if Carea > 1500:
                    cv2.drawContours(frame,[a],-1,(0,255,0), 1)
                    centroid = cv2.moments(a)
                    cx = int(centroid["m10"]/ centroid["m00"])
                    cy = int(centroid["m01"]/ centroid["m00"])
                    cv2.circle(frame,(cx,cy),1,(0,0,0),0)
                    cv2.putText(frame, "Green", (cx-10, cy-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255))


        for a in borderc6:
                Carea = cv2.contourArea(a)
                if Carea > 1500:
                    cv2.drawContours(frame,[a],-1,(0,255,0), 1)
                    centroid = cv2.moments(a)
                    cx = int(centroid["m10"]/ centroid["m00"])
                    cy = int(centroid["m01"]/ centroid["m00"])
                    cv2.circle(frame,(cx,cy),1,(0,0,0),0)
                    cv2.putText(frame, "Light Blue", (cx-10, cy-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255))


        for a in borderc7:
                Carea = cv2.contourArea(a)
                if Carea > 1500:
                    cv2.drawContours(frame,[a],-1,(0,255,0), 1)
                    centroid = cv2.moments(a)
                    cx = int(centroid["m10"]/ centroid["m00"])
                    cy = int(centroid["m01"]/ centroid["m00"])
                    cv2.circle(frame,(cx,cy),1,(0,0,0),0)
                    cv2.putText(frame, "Blue", (cx-10, cy-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255))


        for a in borderc8:
                Carea = cv2.contourArea(a)
                if Carea > 1500:
                    cv2.drawContours(frame,[a],-1,(0,255,0), 1)
                    centroid = cv2.moments(a)
                    cx = int(centroid["m10"]/ centroid["m00"])
                    cy = int(centroid["m01"]/ centroid["m00"])
                    cv2.circle(frame,(cx,cy),1,(0,0,0),0)
                    cv2.putText(frame, "Violet", (cx-10, cy-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255))


        for a in borderc9:
                Carea = cv2.contourArea(a)
                if Carea > 1500:
                    cv2.drawContours(frame,[a],-1,(0,255,0), 1)
                    centroid = cv2.moments(a)
                    cx = int(centroid["m10"]/ centroid["m00"])
                    cy = int(centroid["m01"]/ centroid["m00"])
                    cv2.circle(frame,(cx,cy),1,(0,0,0),0)
                    cv2.putText(frame, "Purple", (cx-10, cy-1), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255))


        for a in borderc10:
                Carea = cv2.contourArea(a)
                if Carea > 1500:
                    cv2.drawContours(frame,[a],-1,(0,255,0), 1)
                    centroid = cv2.moments(a)
                    cx = int(centroid["m10"]/ centroid["m00"])
                    cy = int(centroid["m01"]/ centroid["m00"])
                    cv2.circle(frame,(cx,cy),1,(0,0,0),0)
                    cv2.putText(frame, "Pink", (cx-10, cy-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255))


        for a in borderc11:
                Carea = cv2.contourArea(a)
                if Carea > 1500:
                    b=cv2.drawContours(frame,[a],-1,(0,255,0), 1)
                    centroid = cv2.moments(a)
                    cx = int(centroid["m10"]/ centroid["m00"])
                    cy = int(centroid["m01"]/ centroid["m00"])
                    cv2.circle(frame,(cx,cy),1,(0,0,0),0)
                    cv2.putText(frame, "Gray", (cx-10, cy-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255))
                        
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.imshow("result",frame)

cap.release()
cv2.destroyAllWindows()
