equi=[]
veryweakA=[]
strongA=[]
wdominA=[]
nodominanceA=[]
veryweakB = []
strongB = []
wdominB = []
nodominanceB = []
nodominanceC=[]
strongC=[]
wdominanceC=[]
veryweakC=[]

def dominantstrategyA():
    abc=[[0]*(int((len(payoffmatrix[0]))/3))]*len(payoffmatrix)


    for i in range(int(len(payoffmatrix[0])/3)):

        for j in range(int(len(payoffmatrix))):
            for x in range(int(len(payoffmatrix))):
                if(x!=j):
                    if(payoffmatrix[j][i*3]>payoffmatrix[x][i*3]):
                        abc[j][i]+=1
                    elif(payoffmatrix[j][i*3]<payoffmatrix[x][i*3]):
                        if(j not in nodominanceA):
                            nodominanceA.append(j)
                            break
                    if (payoffmatrixs[j][i * 3] > payoffmatrixs[x][i * 3]):
                        abc[j][i] += 1
                    elif (payoffmatrixs[j][i * 3] < payoffmatrixs[x][i * 3]):
                        if (j not in nodominanceA):
                            nodominanceA.append(j)
                            break
                if(j in nodominanceA):
                    break

    for i in range(int(len(payoffmatrix))):
        if(i not in nodominanceA):
            if(sum(abc[i])==0):
                veryweakA.append(i)
            elif(sum(abc[i])==int((2*(len(payoffmatrix)-1))* (len(payoffmatrix[0])/3))):
                strongA.append(i)
            elif(sum(abc[i])>=(len(payoffmatrix[0])/3)):
                wdominA.append(i)


def printstrategyA():
    print("Very Weak Strategy")
    print(veryweakA)
    print("Strong Strategy")
    print(strongA)
    print("Weak Strategy")
    print(wdominA)



def dominantstrategyB():
    abc = [[0] * (len(payoffmatrix))] * (int(len(payoffmatrix[0])/3))

    for i in range(len(payoffmatrix)):

        for j in range(int(len(payoffmatrix[0])/3)):

                for x in range(int(len(payoffmatrix[0])/3)):
                    #print("i=%d" % (i))
                    #print("j=%d x=%d" % (j, x))
                    #print(payoffmatrix[i][j * 2 + 1])
                    #print(payoffmatrix[i][x * 2 + 1])

                    if (x != j):
                        #print("heyy")
                        if(payoffmatrix[i][j*3+1] > payoffmatrix[i][x*3+1]):
                            #print("a")
                            abc[j][i] += 1
                        elif(payoffmatrix[i][j*3+1] < payoffmatrix[i][x*3+1]):
                            if(j not in nodominanceB):
                                #print(" put in nodominance")
                                nodominanceB.append(j)
                                break
                        if(payoffmatrixs[i][j*3+1] > payoffmatrixs[i][x*3+1]):
                            abc[j][i] += 1
                        elif(payoffmatrixs[i][j*3+1] < payoffmatrixs[i][x*3+1]):
                            if(j not in nodominanceB):
                                #print(" put in nodominance")
                                nodominanceB.append(j)
                                break
                #print("j=%d"%(j))
                #print(abc[j])

    for i in range(int(len(payoffmatrix[0])/3)):
        if (i not in nodominanceB):
            if (sum(abc[i]) == 0):
                veryweakB.append(i)
            elif(sum(abc[i]) == int((2*((len(payoffmatrix[0])/3)-1))*(len(payoffmatrix)))):

                strongB.append(i)
            elif(sum(abc[i])>=(len(payoffmatrix))):
                wdominB.append(i)

def printstrategyB():
    print("Very Weak Strategy")
    print(veryweakB)
    print("Strong Strategy")
    print(strongB)
    print("Weak Strategy")
    print(wdominB)

def dominantstrategyC():
    abc=[[0]*int(len(payoffmatrix)*(len(payoffmatrix[0])/3))]*2

    for i in range(len(payoffmatrix)):
        for j in range(int(len(payoffmatrix[0])/3)):
            if(payoffmatrix[i][j*3+2]>payoffmatrixs[i][j*3+2]):
                if(1 not in nodominanceC):
                    nodominanceC.append(1)
                abc[0][j+(i*(int(len(payoffmatrix[0])/3)))]+=1
            elif(payoffmatrix[i][j*3+2]<payoffmatrixs[i][j*3+2]):
                if(0 not in nodominanceC):
                    nodominanceC.append(0)
                abc[1][j + (i * (int(len(payoffmatrix[0]) / 3)))] += 1



    for i in range(2):
        if(i not in nodominanceC):
            if(sum(abc[i])==(len(payoffmatrix)*(len(payoffmatrix[0])/3))):
                strongC.append(i)
            elif(sum(abc[i])>=(int(len(payoffmatrix)*(len(payoffmatrix[0])/3)))):
                wdominanceC.append(i)
            else:
                veryweakC.append(i)
def printstrategyC():
    print("Very Weak Strategy")
    print(veryweakC)
    print("Strong")
    print(strongC)
    print("Weak Strategy")
    print(wdominanceC)


def checkstrategyequilibrium():
    for i in strongA:
        for j in strongB:
            for k in strongC:
                equi.append([i,j,k])
    for i in veryweakA:
        for j in veryweakB:
            for k in veryweakC:
                equi.append([i,j,k])
    for i in wdominA:
        for j in wdominB:
            for k in wdominanceC:
                equi.append([i,j,k])

    if(len(equi)):
        return(1)
    else:
        return(0)

def checknash(i,j,k):
    x=len(payoffmatrix)
    y=int(len(payoffmatrix[0])/3)
    suma=0
    if(k==0):
        for a in range(x):
            if(i!=a):
                if(payoffmatrix[i][3*j]>payoffmatrix[a][3*j]):
                    suma=suma+1


        if (payoffmatrix[i][3*j+2] > payoffmatrixs[i][3*j+2]):
            suma = suma + 1



        for a in range(y):
            if(j!=a):
                if(payoffmatrix[i][3*j+1]>payoffmatrix[i][3*a+1]):
                    suma=suma+1


    else:
        for a in range(x):
            if (i != a):
                if (payoffmatrixs[i][3 * j] > payoffmatrixs[a][3 * j]):
                    suma = suma + 1



        if (payoffmatrixs[i][3 * j + 2] > payoffmatrix[i][3 * j + 2]):
            suma = suma + 1


        for a in range(y):
            if (j != a):
                if (payoffmatrixs[i][3 * j + 1] > payoffmatrixs[i][3 * a + 1]):
                    suma = suma + 1


    if(suma==(x+y-1)):
        return(1)
    else:
        return(0)


def nashequilibrium():
    x=len(payoffmatrix)
    y=int(len(payoffmatrix[0])/3)
    z=2
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if(checknash(i,j,k)):
                    equi.append([i,j,k])
    if(len(equi)):
        print("The nash Equilibrium is ")
        print(equi)
    else:
        print("Nash Equilibrium")



payoffmatrix=[[0,0,0,1,-2,1],[-2,1,1,-1,-1,2]]
payoffmatrixs=[[1,1,-2,2,-1,-1],[-1,2,-1,0,0,0]]



dominantstrategyA()

dominantstrategyB()

dominantstrategyC()


if(checkstrategyequilibrium()):
   print("The Nash Equilibrium is ")
   print(equi)
else:
    nashequilibrium()
