if __name__=="__main__":
    global l1
    global l2
    global l1points,l2points
    start=[0,0]
    rstart=[0,0]
    l1=input()
    l2=input()
    l1=l1.split(",")
    l2=l2.split(",")
    l1points=list()
    l2points=list()
    crosspoints=list()
    for i in range(0,len(l1)):
        direction=l1[i][0]
        distance=int(l1[i][1:len(l1)])
        temp=distance
        if direction == "R":
            while temp>0:
                l1points.append([rstart[0]+1,rstart[1]])
                temp=temp-1
                rstart=[rstart[0]+1,rstart[1]]
        if direction == "L":
            while temp>0:
                l1points.append([rstart[0]-1,rstart[1]])
                temp=temp-1
                rstart=[rstart[0]-1,rstart[1]]
        if direction == "U":
            while temp>0:
                l1points.append([rstart[0],1+rstart[1]])
                temp=temp-1
                rstart=[rstart[0],1+rstart[1]]
        if direction == "D":
            while temp>0:
                l1points.append([rstart[0],rstart[1]-1])
                temp=temp-1
                rstart=[rstart[0],rstart[1]-1]
    for i in range(0,len(l2)):
        direction=l2[i][0]
        distance=int(l2[i][1:len(l2[i])])
        temp=distance
        if direction == "R":
            while temp>0:
                l2points.append([start[0]+1,start[1]])
                temp-=1
                start=[start[0]+1,start[1]]
        if direction == "L":
            while temp>0:
                l2points.append([start[0]-1,start[1]])
                temp-=1
                start=[start[0]-1,start[1]]
        if direction == "U":
            while temp>0:
                l2points.append([start[0],1+start[1]])
                temp-=1
                start=[start[0],1+start[1]]
        if direction == "D":
            while temp>0:
                l2points.append([start[0],start[1]-1])
                temp-=1
                start=[start[0],start[1]-1]
    for j in range(0,len(l1points)):
        if l1points[j] in l2points:
            crosspoints.append(l1points[j])
    small=abs(crosspoints[0][0])+abs(crosspoints[0][1])
    for i in range(0,len(crosspoints)):
        if small>(abs(crosspoints[i][0])+abs(crosspoints[i][1])):
            small=(abs(crosspoints[i][0])+abs(crosspoints[i][1]))
    print(small)




