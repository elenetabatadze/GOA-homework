def digitize(n):
    return [int(digit) for digit in str(n)[::-1]]



def to_alternating_case(s):
    return s.swapcase()

def abbrev_name(name):
    first, last = name.split()
    return f"{first[0].upper()}.{last[0].upper()}"

def rps(player1, player2):
    if player1 == player2:
        return "Draw!"
    
    wins = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    if wins[player1] == player2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"