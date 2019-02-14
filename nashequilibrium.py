
equi=[]
veryweakA=[]
strongA=[]
wdominA=[]
nodominanceA=[]
veryweakB = []
strongB = []
wdominB = []
nodominanceB = []

def dominantstrategyA():

    abc=[[0]*(int((len(payoffmatrix[0]))/2))]*len(payoffmatrix)


    for i in range(int(len(payoffmatrix[0])/2)):

        for j in range(int(len(payoffmatrix))):
            #print("j=%d"%(j))
            for x in range(int(len(payoffmatrix))):
                #print("i=%d j=%d x=%d " % (i, j, x))
                if(x!=j):

                    #print(payoffmatrix[j][i * 2])
                    #print(payoffmatrix[x][i * 2])
                    if(payoffmatrix[j][i*2]>payoffmatrix[x][i*2]):
                        abc[j][i]+=1
                    elif(payoffmatrix[j][i*2]<payoffmatrix[x][i*2]):
                        if(j not in nodominanceA):
                            nodominanceA.append(j)
                            break

                if(j in nodominanceA):
                    break
            #print(abc[j])

    for i in range(int(len(payoffmatrix))):
        if(i not in nodominanceA):
            if(sum(abc[i])==0):
                veryweakA.append(i)
            elif(sum(abc[i])==((len(payoffmatrix)-1)* len(payoffmatrix[0])/2)):
                strongA.append(i)
            elif(sum(abc[i])>=(len(payoffmatrix[0])/2)):
                wdominA.append(i)


def printstrategyA():
    print("Very Weak Strategy")
    print(veryweakA)
    print("Strong Strategy")
    print(strongA)
    print("Weak Strategy")
    print(wdominA)



def dominantstrategyB():
    abc = [[0] * (len(payoffmatrix))] * (int(len(payoffmatrix[0])/2))

    for i in range(len(payoffmatrix)):

        for j in range(int(len(payoffmatrix[0])/2)):

                for x in range(int(len(payoffmatrix[0])/2)):
                    #print("i=%d" % (i))
                    #print("j=%d x=%d" % (j, x))
                    #print(payoffmatrix[i][j * 2 + 1])
                    #print(payoffmatrix[i][x * 2 + 1])

                    if (x != j):
                        #print("heyy")
                        if (payoffmatrix[i][j*2+1] > payoffmatrix[i][x*2+1]):
                            #print("a")
                            abc[j][i] += 1
                        elif (payoffmatrix[i][j*2+1] < payoffmatrix[i][x*2+1]):
                            if (j not in nodominanceB):
                                #print(" put in nodominance")
                                nodominanceB.append(j)
                                break
                #print("j=%d"%(j))
                #print(abc[j])

    for i in range(int(len(payoffmatrix[0])/2)):
        if (i not in nodominanceB):
            if (sum(abc[i]) == 0):
                veryweakB.append(i)
            elif(sum(abc[i]) == ((len(payoffmatrix[0])/2)-1)*(len(payoffmatrix))):

                strongB.append(i)
            elif(sum(abc[i])>=(len(payoffmatrix))):
                wdominB.append(i)

def printstrategyB():
    if(len(veryweakB)):
        print("Very Weak Strategy of B")
        print(veryweakB)
    if(strongB):
        print("Strong Strategy of B")
        print(strongB)
    if(wdominB):
        print("Weak Strategy of B")
        print(wdominB)


def checkstrategyequilibrium():
    for i in strongA:
        for j in strongB:
            equi.append([i,j])
    for i in veryweakA:
        for j in veryweakB:
            equi.append([i,j])
    for i in wdominA:
        for j in wdominB:
            equi.append([i,j])

    if(len(equi)):
        return(1)
    else:
        return(0)

def checknash(i,j):
    x=len(payoffmatrix)
    y=int(len(payoffmatrix[0])/2)
    suma=0
    for a in range(x):
        if(i!=a):
            if(payoffmatrix[i][2*j]>payoffmatrix[a][2*j]):
                suma=suma+1

    for a in range(y):
        if(j!=a):
            if(payoffmatrix[i][2*j+1]>payoffmatrix[i][2*a+1]):
                suma=suma+1
    if(suma==(x+y-2)):
        return(1)
    else:
        return(0)


def nashequilibrium():
    x=len(payoffmatrix)
    y=int(len(payoffmatrix[0])/2)
    for i in range(x):
        for j in range(y):
            if(checknash(i,j)):
                equi.append([i,j])
    if(len(equi)):
        print("The nash Equilibrium is ")
        print(equi)
    else:
        print("No Nash Equilibrium")

def maxminA():
    x=len(payoffmatrix)
    y=len(payoffmatrix[0])
    small=999

    for i in range(x):
        for j in range(int(y/2)):
            if(payoffmatrix[i][j*2]<small):
                row=i
                column=j
                small=payoffmatrix[i][j*2]
    big=small

    for i in range(x):
        if(payoffmatrix[i][column*2]>big):
            bigrow=i
    print("The maxmin strategy of player 1 is ")
    print(bigrow)

payoffmatrix=[[10,10,0,5],[5,0,5,5]]

dominantstrategyA()
printstrategyA()
dominantstrategyB()
printstrategyB()
if(checkstrategyequilibrium()):
    print("The Nash Equilibrium is ")
    print(equi)
else:
    nashequilibrium()
print("")

maxminA()