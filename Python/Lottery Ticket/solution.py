def bingo(ticket,win):
    wins = 0
    for item in ticket:
        str = item[0]
        num = item[1]
        char = chr(num)
        if char in str:
            wins += 1
    if wins >= win:
        return "Winner!"
    else:
        return "Loser!"