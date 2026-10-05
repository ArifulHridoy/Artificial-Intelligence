import math
import copy

def player(state):
    xCount=0
    oCount=0
    for row in state:
        for cell in row:
            if cell=='X':
                xCount+=1
            elif cell=='O':
                oCount+=1
    if xCount==oCount:
        return 'X'
    else:
        return 'O'

def display(state):
    for row in state:
        print(" | ".join(row))
    print("-" * 9)

def actions(state):
    moves=[]
    for i in range(3):
        for j in range(3):
            if state[i][j]==' ':
                moves.append((i,j))
    return moves

def result(state,action):
    i,j=action
    newState=copy.deepcopy(state)
    newState[i][j]=player(state)
    return newState

def terminal(state):
    lines=[]
    for row in state:
        lines.append(row)
    for j in range(3):
        col=[]
        for i in range(3):
            col.append(state[i][j])
        lines.append(col)
    lines.append([state[0][0],state[1][1],state[2][2]])
    lines.append([state[0][2],state[1][1],state[2][0]])

    for l in lines:
        if l==['X','X','X'] or l==['O','O','O']:
            return True
    for r in state:
        for c in r:
            if c==' ':
                return False
    return True

def utility(state):
    lines=[]
    for row in state:
        lines.append(row)
    for j in range(3):
        col=[]
        for i in range(3):
            col.append(state[i][j])
        lines.append(col)
    lines.append([state[0][0],state[1][1],state[2][2]])
    lines.append([state[0][2],state[1][1],state[2][0]])

    for l in lines:
        if l==['X','X','X']:
            return 1
        if l==['O','O','O']:
            return -1
    return 0

def maxValue(state):
    if terminal(state):
        return utility(state)
    
    val=-math.inf
    for act in actions(state):
        newState=result(state,act)
        evalValue=minValue(newState)
        
        if evalValue>val:
            val=evalValue
    return val

def minValue(state):
    if terminal(state):
        return utility(state)
    
    val=math.inf
    for act in actions(state):
        newState=result(state,act)
        evalValue=maxValue(newState)
        if evalValue<val:
            val=evalValue
    return val

def minimax(state):
    bestAct=None

    if player(state)=='X':
        bestValue=-math.inf
        for act in actions(state):
            newState=result(state,act)
            value=minValue(newState)

            if value>bestValue:
                bestValue=value
                bestAct=act
    else:
        bestValue=math.inf
        for act in actions(state):
            newState=result(state,act)
            value=maxValue(newState)

            if value<bestValue:
                bestValue=value
                bestAct=act
    return bestAct

def play():
    state=[
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]

    print("Welcome to Tic-Tac-Toe! You are O, AI is X.")
    display(state)

    while not terminal(state):
        if player(state)=='O':
            position = input("Enter row and col: ").split()
            row = int(position[0])
            col = int(position[1])
            action = (row, col)
            #action=minimax(state)
            if action not in actions(state):
                print("Invalid move! Try again.")
                continue

            state=result(state,action)
        else:
            action=minimax(state)
            print(f"AI plays: {action}")
            state = result(state, action)

        display(state)

    score = utility(state)
    if score == 1:
        print("X wins!")
    elif score == -1:
        print("O wins!")
    else:
        print("It's a draw!")

play()
