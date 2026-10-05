import math

def actions(n):
    moves=[]
    for i in range(1,4):
        if i<=n:
            moves.append(i)
    return moves

def result(n,action):
    return n-action

def terminal(n):
    return n==0

def utility(n,turn):
    if n==0:
        if turn=='X':
            return -1
        else:
            return 1
    return 0

def maxValue(n,turn):
    if terminal(n):
        return utility(n,turn)

    val=-math.inf
    for act in actions(n):
        newState=result(n,act)
        if turn=='X':
            nextTurn='O'
        else:
            nextTurn='X'
        evalValue=minValue(newState,nextTurn)
        if evalValue>val:
            val=evalValue
    return val

def minValue(n,turn):
    if terminal(n):
        return utility(n,turn)

    val=math.inf
    for act in actions(n):
        newState=result(n,act)
        if turn=='X':
            nextTurn='O'
        else:
            nextTurn='X'
        evalValue=maxValue(newState,nextTurn)
        if evalValue<val:
            val=evalValue
    return val

def minimax(n,turn):
    bestAct=None

    if turn=='X':
        bestValue=-math.inf
        for act in actions(n):
            newState=result(n,act)
            value=minValue(newState,'O')

            if value>bestValue:
                bestValue=value
                bestAct=act
    else:
        bestValue=math.inf
        for act in actions(n):
            newState=result(n,act)
            value=maxValue(newState,'X')

            if value<bestValue:
                bestValue=value
                bestAct=act
    return bestAct

def play():

    stones = 7
    turn = 'O'

    print("Welcome to Nim Game!")
    print("You are O, AI is X.")
    print("Take 1, 2, or 3 stones.")
    print("The player who takes the last stone wins.\n")

    while not terminal(stones):
        print("Stones remaining:", stones)
        if turn == 'O':

            print("Your turn.")
            print("Available moves:", actions(stones))

            action = int(input("How many stones do you want to take? "))

            if action not in actions(stones):
                print("Invalid move! Try again.\n")
                continue

            stones = result(stones, action)

            if terminal(stones):
                print("You took the last stone!")
                print("O wins!")
                break

            turn = 'X'

        else:

            action = minimax(stones, turn)
            print("AI takes:", action)
            stones = result(stones, action)
            if terminal(stones):
                print("AI took the last stone!")
                print("X wins!")
                break

            turn = 'O'


play()
