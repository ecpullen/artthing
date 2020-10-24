import turtle
import math



if __name__ == "__main__":
    pos1 = (10,200)
    pos2 = (20,190)
    r1 = 5
    r2 = 3
    r3 = 2
    l1 = 9
    l2 = 14
    l = 30
    degree = math.pi/180
    angle_table = 0
    angle1 = math.pi/2
    angle2 = math.pi/3
    angle3 = 0
    omega_table = .1*degree
    omega1 = -4*degree
    omega2 = 3*degree
    omega3 = -5*degree

    
    turtle.penup()
    turtle.ht()
    turtle.tracer(0,0)

    for i in range(0,10000):
        angle1 += omega1 + omega_table
        angle2 += omega2 + omega_table
        angle3 += omega3 + omega1 + omega_table
        angle_table += omega_table

        disc1 = math.atan(pos1[1]/pos1[0])
        dis1 = math.sqrt(pos1[0]*pos1[0]+pos1[1]*pos1[1])
        disc2 = math.atan(pos2[1]/pos2[0])
        dis2 = math.sqrt(pos2[0]*pos2[0]+pos2[1]*pos2[1])
        p1 = (dis1*math.cos(disc1+angle_table),dis1*math.sin(disc1+angle_table))
        p2 = (dis2*math.cos(disc2+angle_table),dis2*math.sin(disc2+angle_table))

        pivotsub1 = (p1[0] + r1*math.cos(angle1),p1[1] + r1*math.sin(angle1))
        pivot1 = (pivotsub1[0] + r3*math.cos(angle3),pivotsub1[1] + r3*math.sin(angle3))
        pivot2 = (p2[0] + r2*math.cos(angle2),p2[1] + r2*math.sin(angle2))

        c = math.sqrt((pivot2[1] - pivot1[1])*(pivot2[1] - pivot1[1]) + (pivot2[0] - pivot1[0])*(pivot2[0] - pivot1[0]))
        cosa = (c*c - l1*l1 - l2*l2)/(2*l1*l2)
        sina = math.sqrt(1-cosa*cosa)
        d = sina/c
        gamma = -math.atan((pivot2[1]-pivot1[1])/(pivot2[0]-pivot1[0]))*(pivot2[0]-pivot1[0])/math.fabs(pivot2[0]-pivot1[0])
        b = math.asin(d*l2)

        mult = 1
        if pivot2[0] > pivot1[0]:
            mult = -1

        # print("iteration:", i)
        # print("gamma:", gamma*180/3.1415)
        # print("beta:", b*180/3.1415)
        pen = (pivot1[0] + mult*l*math.cos(mult*b+gamma+math.pi),pivot1[1] + l*math.sin(mult*b+gamma+math.pi))
        # print("pen x", pen[0])
        # turtle.goto(pivot1)
        # turtle.dot(3,'green')
        # turtle.pendown()
        # turtle.goto(pivot1[0]+mult*c*math.cos(gamma+math.pi),pivot1[1]+c*math.sin(gamma+math.pi))
        # turtle.penup()
        # turtle.goto(pivot2)
        # turtle.dot(3,'red')
        # turtle.goto(p1)
        # turtle.dot(3,'blue')
        # turtle.goto(p2)
        # turtle.dot(3,'yellow')
        # turtle.goto(pen)
        # turtle.dot(3,'black')
        turtle.goto(pen)
        # turtle.dot(3,'black')
        turtle.pendown()

    turtle.update()
    turtle.Screen().exitonclick()