import numpy

class State: #per instructions making the class with x and y
    x = 0
    y = 0
    def __init__(self, positionX, positionY):
        self.x = positionX
        self.y = positionY

#make the state objects leaving out the obstacle
S = [State(0,0), State(0,1), State(0,2), State(0,3), State(1,0), State(1,2), State(1,3), State(2,0), State(2,1), State(2,2), State(2,3)]

#action arrays in order
Action = ['u', 'r', 'd', 'l']

#hard coded discounts and awards
discount = 0.99
reward = -0.04

#location
terminalLocation = [6,10]

#numpy array of the rewards states
reward_states = numpy.array([reward, reward, reward, reward, reward, reward, -1, reward, reward, reward, 1])

#gets the expected utility for each state
def expectedUtility(P, U, index, S, stateAction):
    #makes and array to store the values, put 0 in to start so the less than below works
    utilityList = [0.0]
    #goes through the actions list
    for list, stateAction in enumerate(stateAction):
        value = 0.0
        action1 = list
        #goes through the states
        for list2,s in enumerate(S):
            #stores the state
            state1 = list2
            #the equation from the book for finding the best utility
            value += P[action1][index][state1] * U[state1]
        #checks to see if the utility is better then the previous then stores the highest
        if (value > utilityList[0]):
            utilityList.insert(0, value)
    #returns the best utility
    return utilityList[0]


def valueIteration(S, Action, P, reward_states, discount, terminalindexlocation):
    eps = 0.000001
    gam = discount
    
    #the U array per instructions
    U = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 1.0]) #the current utlities to use

    #u prime array per instructions
    U_prime = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 1.0]) #the current utlities to use

    #delta for the psuodo code in instructions and textbook
    delta = 1

    #per psuodo code as long as this is true it iterates through
    while(delta > eps):
        #updates U, little confused about instructions compared to psuodo code though
        U = U_prime.copy()
        delta = 0.0

        #iterates through state list
        for position, s in enumerate(S):
            #if its not a terminal location goes through
            if(position != terminalindexlocation[0] and position != terminalindexlocation[1]):
                U_prime[position] = reward_states[position] + (gam * expectedUtility(P, U, position, S, Action)) #bellmans equation
            if(abs(U_prime[position] - U[position]) > delta):
                #updates delta
                delta = abs(U_prime[position] - U[position])

    return U

#function to return the location
def locationState(S, x, y):
    for indexofstate,s in enumerate(S):
        if s.x == x and s.y == y:
            return indexofstate
    #if its terminal return 66, gota have a star wars reference since kenobi is over
    return -66
#, terminalstateindex
def policy(S, U, Action, P):
    #create an array for the policy
    policyArray = []

    #iterates through the states
    for iterateS, s in enumerate(S):
        #intermediate array
        iArray = []

        #get the indexs
        upIndex = locationState(S, s.x, s.y+1)
        downIndex = locationState(S, s.x, s.y-1)
        rightIndex = locationState(S, s.x+1, s.y)
        leftIndex = locationState(S, s.x-1, s.y)

        #check if the index is a block
        if upIndex != -66:
            iArray.append(upIndex)

        if downIndex != -66:
            iArray.append(downIndex)

        if rightIndex != -66:
            iArray.append(rightIndex)

        if leftIndex != -66:
            iArray.append(leftIndex)

        #update the intermediate array
        iArray.append(iterateS)

        #create some local variables for the calculations. actionset is set to T because it wont iterate if its terminal. also calcmax is set to
        #-1 so it will run on first
        iterationMaxUtilities = 0
        calcMaxUtilities = -1
        actionset = 'T'

        for iterateAction,action in enumerate(Action):
            expectedUtilityVar = 0

            #following book instructions
            for neighbor in iArray:
                prime = U[neighbor]
                probability = P[iterateAction, iterateS, neighbor]
                expectedUtilityVar += (probability * prime)

            if (expectedUtilityVar > calcMaxUtilities):
                calcMaxUtilities = expectedUtilityVar
                iterationMaxUtilities = iterateAction

        #update the action to the actual action
        actionset = Action[iterationMaxUtilities]
    #update the policy
        policyArray.append(actionset)

    return policyArray

#function to print out the actual policy
def printPolicy(policyfinal, tl):
    width = 4
    height = 3

    #if its the obsicle, put in the O
    for whereObsticle in tl:
        policyfinal.insert(whereObsticle, '0')

    #go through starting at top left and print out the action
    for rowindexs in range(height-1, -1, -1):
        #print("in the for loop")
        #print(policyfinal)
        #print("indexs to follow")
        #print(rowindexs)
        row = [policyfinal[((width * rowindexs) + i)] for i in range(0,width)]
        print(row)


# P is the transition model matrix for the 4x3 grid world problem
# P gets converted to a numpy array after it is hard-coded here
# actions are in order: up, right, down, left
# rows -> s
# cols -> s'
# [action, state, outcome], [a, s, s']
P = [[[0.1, 0.1, 0.,  0.,  0.8, 0.,  0.,  0.,  0.,  0.,  0.],
  [0.1, 0.8, 0.1, 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0. ],
  [0.,  0.1, 0.,  0.1, 0.,  0.8, 0.,  0.,  0.,  0.,  0. ],
  [0.,  0.,  0.1, 0.1, 0.,  0.,  0.8, 0.,  0.,  0.,  0. ],
  [0.,  0.,  0.,  0.,  0.2, 0.,  0.,  0.8, 0.,  0.,  0. ],
  [0.,  0.,  0.,  0.,  0.,  0.1, 0.1, 0.,  0.,  0.8, 0. ],
  [0.,  0.,  0.,  0.,  0.,  0.1, 0.1, 0.,  0.,  0.,  0.8],
  [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.9, 0.1, 0.,  0. ],
  [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.1, 0.8, 0.1, 0. ],
  [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.1, 0.8, 0.1],
  [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.1, 0.9]],
 [[0.1, 0.8, 0.,  0.,  0.1, 0.,  0.,  0.,  0.,  0.,  0. ],
  [0.,  0.2, 0.8, 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0. ],
  [0.,  0.,  0.1, 0.8, 0.,  0.1, 0.,  0.,  0.,  0.,  0. ],
  [0.,  0.,  0.,  0.9, 0.,  0.,  0.1, 0.,  0.,  0.,  0. ],
  [0.1, 0.,  0.,  0.,  0.8, 0.,  0.,  0.1, 0.,  0.,  0. ],
  [0.,  0.,  0.1, 0.,  0.,  0.,  0.8, 0.,  0.,  0.1, 0. ],
  [0.,  0.,  0.,  0.1, 0.,  0.,  0.8, 0.,  0.,  0.,  0.1],
  [0.,  0.,  0.,  0.,  0.1, 0.,  0.,  0.1, 0.8, 0.,  0. ],
  [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.2, 0.8, 0. ],
  [0.,  0.,  0.,  0.,  0.,  0.1, 0.,  0.,  0.,  0.1, 0.8],
  [0.,  0.,  0.,  0.,  0.,  0.,  0.1, 0.,  0.,  0.,  0.9]],
 [[0.9, 0.1, 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0. ],
  [0.1, 0.8, 0.1, 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0. ],
  [0.,  0.1, 0.8, 0.1, 0.,  0.,  0.,  0.,  0.,  0.,  0. ],
  [0.,  0.,  0.1, 0.9, 0.,  0.,  0.,  0.,  0.,  0.,  0. ],
  [0.8, 0.,  0.,  0.,  0.2, 0.,  0.,  0.,  0.,  0.,  0. ],
  [0.,  0.,  0.8, 0.,  0.,  0.1, 0.1, 0.,  0.,  0.,  0. ],
  [0.,  0.,  0.,  0.8, 0.,  0.1, 0.1, 0.,  0.,  0.,  0. ],
  [0.,  0.,  0.,  0.,  0.8, 0.,  0.,  0.1, 0.1, 0.,  0. ],
  [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.1, 0.8, 0.1, 0. ],
  [0.,  0.,  0.,  0.,  0.,  0.8, 0.,  0.,  0.1, 0.,  0.1],
  [0.,  0.,  0.,  0.,  0.,  0.,  0.8, 0.,  0.,  0.1, 0.1]],
 [[0.9, 0.,  0.,  0.,  0.1, 0.,  0.,  0.,  0.,  0.,  0. ],
  [0.8, 0.2, 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0. ],
  [0.,  0.8, 0.1, 0.,  0.,  0.1, 0.,  0.,  0.,  0.,  0. ],
  [0.,  0.,  0.8, 0.1, 0.,  0.,  0.1, 0.,  0.,  0.,  0. ],
  [0.1, 0.,  0.,  0.,  0.8, 0.,  0.,  0.1, 0.,  0.,  0. ],
  [0.,  0.,  0.1, 0.,  0.,  0.8, 0.,  0.,  0.,  0.1, 0. ],
  [0.,  0.,  0.,  0.1, 0.,  0.8, 0.,  0.,  0.,  0.,  0.1],
  [0.,  0.,  0.,  0.,  0.1, 0.,  0.,  0.9, 0.,  0.,  0. ],
  [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.8, 0.2, 0.,  0. ],
  [0.,  0.,  0.,  0.,  0.,  0.1, 0.,  0.,  0.8, 0.1, 0. ],
  [0.,  0.,  0.,  0.,  0.,  0.,  0.1, 0.,  0.,  0.8, 0.1]]]
P = numpy.array(P)



Utest = (valueIteration(S, Action, P, reward_states, discount, terminalLocation))

print('discount = ')
print(discount)

print("reward = ")
print(reward)

print("utilities: ")
print(Utest)

#, terminalLocation
finalTestPolicy = policy(S, Utest, Action, P)
#print(finalTestPolicy)

print("policy: ")

printPolicy(finalTestPolicy, [5])

