final = [1, 2, 3, 4, 5, 6, 7, 8, 0]
stack = []
ind = int()
chk = 0
flag=0

class eightpuzzle:
    a = {}
    id=-1
    a[0] = int()
    a[1] = int()
    a[2] = int()
    a[3] = int()
    a[4] = int()
    a[5] = int()
    a[6] = int()
    a[7] = int()
    a[8] = int()
    a[9]= None

    #defining a function for the empty tile to move up

def move_up(obb=eightpuzzle()):
    lst=[]
    print("move up")
    size = len(eightpuzzle.a)
    for i in range(9):
        if obj[eightpuzzle.id].a[i] == 0:
            temp = i
            break
    if temp < 3:
        print("cannot move up")
    else:
        obj[eightpuzzle.id].a[temp], obj[eightpuzzle.id].a[temp - 3] = obj[eightpuzzle.id].a[temp - 3], \
                                                                       obj[eightpuzzle.id].a[temp]
        print(obj[eightpuzzle.id].a[0], obj[eightpuzzle.id].a[1], obj[eightpuzzle.id].a[2], obj[eightpuzzle.id].a[3],
              obj[eightpuzzle.id].a[4], obj[eightpuzzle.id].a[5], obj[eightpuzzle.id].a[6], obj[eightpuzzle.id].a[7],
              obj[eightpuzzle.id].a[8])
        for i in range(size):
            lst.append(obj[eightpuzzle.id].a[i])
        stack.append(lst)
        print("stack")
        print(stack)
        check()

#defining a function for the empty tile to move down

def move_down(obb=eightpuzzle()):
    lst=[]
    print("move down")
    size = len(eightpuzzle.a)
    for i in range(9):
        if obj[eightpuzzle.id].a[i] == 0:
            temp = i
            break
    if temp > 5:
        print("cannot move down")
    else:
        obj[eightpuzzle.id].a[temp], obj[eightpuzzle.id].a[temp + 3] = obj[eightpuzzle.id].a[temp + 3], \
                                                                       obj[eightpuzzle.id].a[temp]
        print(obj[eightpuzzle.id].a[0], obj[eightpuzzle.id].a[1], obj[eightpuzzle.id].a[2], obj[eightpuzzle.id].a[3],
              obj[eightpuzzle.id].a[4], obj[eightpuzzle.id].a[5], obj[eightpuzzle.id].a[6], obj[eightpuzzle.id].a[7],
              obj[eightpuzzle.id].a[8])
        for i in range(size):
            lst.append(obj[eightpuzzle.id].a[i])
        stack.append(lst)
        print("stack")
        print(stack)
        check()


#defining a function for the empty tile to move right

def move_right(obb=eightpuzzle()):
    lst=[]
    print("move right")
    size = len(eightpuzzle.a)
    for i in range(9):
        if obj[eightpuzzle.id].a[i] == 0:
            temp = i
            break
    if temp == 2 or temp == 5 or temp == 8:
        print("cannot move right")
    else:
        obj[eightpuzzle.id].a[temp], obj[eightpuzzle.id].a[temp + 1] = obj[eightpuzzle.id].a[temp + 1], \
                                                                       obj[eightpuzzle.id].a[temp]
        print(obj[eightpuzzle.id].a[0], obj[eightpuzzle.id].a[1], obj[eightpuzzle.id].a[2], obj[eightpuzzle.id].a[3],
              obj[eightpuzzle.id].a[4], obj[eightpuzzle.id].a[5], obj[eightpuzzle.id].a[6], obj[eightpuzzle.id].a[7],
              obj[eightpuzzle.id].a[8])
        for i in range(size):
            lst.append(obj[eightpuzzle.id].a[i])
        stack.append(lst)
        print("stack")
        print(stack)
        check()


#defining a function for the empty tile to move left

def move_left(obb=eightpuzzle()):
    lst=[]
    print("move left")
    size = len(eightpuzzle.a)
    for i in range(9):
        if obj[eightpuzzle.id].a[i] == 0:
            temp = i
            break
    if temp == 0 or temp == 3 or temp == 6:
        print("cannot move left")
    else:
        obj[eightpuzzle.id].a[temp], obj[eightpuzzle.id].a[temp - 1] = obj[eightpuzzle.id].a[temp - 1], \
                                                                       obj[eightpuzzle.id].a[temp]
        print(obj[eightpuzzle.id].a[0], obj[eightpuzzle.id].a[1], obj[eightpuzzle.id].a[2], obj[eightpuzzle.id].a[3],
              obj[eightpuzzle.id].a[4], obj[eightpuzzle.id].a[5], obj[eightpuzzle.id].a[6], obj[eightpuzzle.id].a[7],
              obj[eightpuzzle.id].a[8])
        for i in range(size):
            lst.append(obj[eightpuzzle.id].a[i])
        stack.append(lst)
        print("stack")
        print(stack)
        check()

#difing a function for finding minmum distance -

def min_dist(obb=eightpuzzle()):
    one = int()
    two = int()
    thr = int()
    fou = int()
    fiv = int()
    six = int()
    sev = int()
    eig = int()
    nin = int()
    temp = int()
    temp = 100
    sum = int()
    l = len(stack)
    for i in range(l):
       sum = 0
       c1 = 0
       c2 = 0
       c3 = 0
       c4 = 0
       c5 = 0
       c6 = 0
       c7 = 0
       c8 = 0
       c9 = 0
       for j in range(9):
           if c1==0:
               for k in range(9):
                   if stack[i][k]==1:
                       if k==0:
                           one =0
                           c1=1
                           break
                       if k==1 or k==3:
                           one =1
                           c1=1
                           break
                       if k==2 or k==4 or k==6:
                           one =2
                           c1=1
                           break
                       if k == 5 or k==7:
                           one = 3
                           c1 = 1
                           break
                       if k == 8:
                           one = 4
                           c1 = 1
                           break
               print("for one value of one- ")
               print(one)
               print("for one value of k- ")
               print(k)

           if c2==0:
               for k in range(9):
                   if stack[i][k]== 2:
                       if k==0 or k==2 or k==4:
                           two=1
                           c2 = 1
                           break
                       if k==1:
                           two=0
                           c2 = 1
                           break
                       if k == 3 or k== 5 or k==7:
                           two = 2
                           c2 = 1
                           break
                       if k== 6 or k==8:
                           two=3
                           c2 = 1
                           break
               print("for 2 value of 2- ")
               print(two)
               print("for 2 value of k- ")
               print(k)

           if c3 == 0:
               for k in range(9):
                   if stack[i][k] == 3:
                       if k == 2:
                           thr = 0
                           c3 = 1
                           break
                       if k == 1 or k == 5:
                           thr = 1
                           c3 = 1
                           break
                       if k == 0 or k == 4 or k == 8:
                           thr = 2
                           c3 = 1
                           break
                       if k == 3 or k == 7:
                           thr = 3
                           c3 = 1
                           break
                       if k == 6:
                           thr = 4
                           c3 = 1
                           break
               print("for 3 value of 3- ")
               print(thr)
               print("for 3 value of k- ")
               print(k)

           if c4 == 0:
               for k in range(9):
                   if stack[i][k] == 4:
                       if k == 3:
                           fou = 0
                           c4 = 1
                           break
                       if k == 0 or k == 4 or k==6:
                           fou = 1
                           c4 = 1
                           break
                       if k == 1 or k == 5 or k == 7:
                           fou = 2
                           c4 = 1
                           break
                       if k == 2 or k == 8:
                           fou = 3
                           c4 = 1
                           break
               print("for 4 value of 4- ")
               print(fou)
               print("for 4 value of k- ")
               print(k)

           if c5 == 0:
               for k in range(9):
                   if stack[i][k] == 5:
                       if k == 4:
                           fiv = 0
                           c5 = 1
                           break
                       if k == 1 or k == 3 or k == 5 or k == 7:
                           fiv = 1
                           c5 = 1
                           break
                       if k == 0 or k == 2 or k == 6 or k == 8:
                           fiv = 2
                           c5 = 1
                           break
               print("for 5 value of 5- ")
               print(fiv)
               print("for 5 value of k- ")
               print(k)

           if c6 == 0:
               for k in range(9):
                   if stack[i][k] == 6:
                       if k == 5:
                           six = 0
                           c6 = 1
                           break
                       if k == 2 or k == 4 or k == 8:
                           six = 1
                           c6 = 1
                           break
                       if k == 1 or k == 3 or k == 7:
                           six = 2
                           c6 = 1
                           break
                       if k == 0 or k == 6:
                           six = 3
                           c6 = 1
                           break
               print("for 6 value of 6- ")
               print(six)
               print("for 6 value of k- ")
               print(k)

           if c7 == 0:
               for k in range(9):
                   if stack[i][k] == 7:
                       if k == 6:
                           sev = 0
                           c7 = 1
                           break
                       if k == 3 or k == 7:
                           sev = 1
                           c7 = 1
                           break
                       if k == 0 or k == 4 or k == 8:
                           sev = 2
                           c7 = 1
                           break
                       if k == 1 or k == 5:
                           sev = 3
                           c7 = 1
                           break
                       if k == 2:
                           sev = 4
                           c7 = 1
                           break
               print("for 7 value of 7- ")
               print(sev)
               print("for 7 value of k- ")
               print(k)

           if c8 == 0:
               for k in range(9):
                   if stack[i][k] == 8:
                       if k == 4 or k == 6 or k == 8:
                           eig = 1
                           c8 = 1
                           break
                       if k == 7:
                           eig = 0
                           c8 = 1
                           break
                       if k == 1 or k == 3 or k == 5:
                           eig = 2
                           c8 = 1
                           break
                       if k == 0 or k == 2:
                           eig = 3
                           c8 = 1
                           break
               print("for 8 value of 8- ")
               print(eig)
               print("for 8 value of k- ")
               print(k)

           if c9 == 0:
               for k in range(9):
                   if stack[i][k] == 0:
                       if k == 8:
                           nin = 0
                           c9 = 1
                           break
                       if k == 5 or k == 7:
                           nin = 1
                           c9 = 1
                           break
                       if k == 2 or k == 4 or k == 6:
                           nin = 2
                           c9 = 1
                           break
                       if k == 1 or k == 3:
                           nin = 3
                           c9 = 1
                           break
                       if k == 0:
                           nin = 4
                           c9 = 1
                           break
               print("for 9 value of 9- ")
               print(nin)
               print("for 9 value of k- ")
               print(k)

       sum=one+two+thr+fou+fiv+six+sev+eig+nin
       print("Sum-")
       print(sum)
       if sum<=temp:
           temp=sum
           ind=i
           chk=1
    print("ind")
    print(ind)

#defifng a function for checking -

def check(obb=eightpuzzle()):
        if stack[0]==obj[eightpuzzle.id].a[0] and stack[1]==obj[eightpuzzle.id].a[1] and stack[2]==obj[eightpuzzle.id].a[2] and stack[3]==obj[eightpuzzle.id].a[3] and stack[4]==obj[eightpuzzle.id].a[4] and stack[5]==obj[eightpuzzle.id].a[5] and stack[6]==obj[eightpuzzle.id].a[6] and stack[7]==obj[eightpuzzle.id].a[7] and stack[8]==obj[eightpuzzle.id].a[8]:
            flag=1
            print("SUCESS")


obj={}
eightpuzzle.id=eightpuzzle.id+1
obj[eightpuzzle.id]= eightpuzzle()
for i in range(1):
    if chk ==0:
        obj[eightpuzzle.id].a[0] = 1
        obj[eightpuzzle.id].a[1] = 6
        obj[eightpuzzle.id].a[2] = 5
        obj[eightpuzzle.id].a[3] = 4
        obj[eightpuzzle.id].a[4] = 8
        obj[eightpuzzle.id].a[5] = 7
        obj[eightpuzzle.id].a[6] = 2
        obj[eightpuzzle.id].a[7] = 3
        obj[eightpuzzle.id].a[8] = 0
    else:
        obj[eightpuzzle.id].a[0] = stack[ind][0]
        obj[eightpuzzle.id].a[1] = stack[ind][1]
        obj[eightpuzzle.id].a[2] = stack[ind][2]
        obj[eightpuzzle.id].a[3] = stack[ind][3]
        obj[eightpuzzle.id].a[4] = stack[ind][4]
        obj[eightpuzzle.id].a[5] = stack[ind][5]
        obj[eightpuzzle.id].a[6] = stack[ind][6]
        obj[eightpuzzle.id].a[7] = stack[ind][7]
        obj[eightpuzzle.id].a[8] = stack[ind][8]
    #print(obj[eightpuzzle.id].a[0])
    move_up()
    move_down()
    move_right()
    move_left()
    min_dist()



