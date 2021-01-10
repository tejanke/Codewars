def street_fighter_selection(fighters, initial_position, moves):
    if len(moves) == 0:
        return []
    result = []
    cur_pos = list(initial_position)
    fighter_row = 0
    for move in moves:
        print("Current Pos {}".format(cur_pos))
        if move == "left":
            if cur_pos[0] > 0:
                cur_pos[0] = cur_pos[0] - 1
                result.append(fighters[fighter_row][cur_pos[0]])
                print("Appending {}".format(fighters[fighter_row][cur_pos[0]]))            
                continue
            if cur_pos[0] == 0:
                cur_pos[0] = len(fighters[0]) - 1
                result.append(fighters[fighter_row][cur_pos[0]])
                print("Appending {}".format(fighters[fighter_row][cur_pos[0]]))
                continue
        if move == "right":
            if cur_pos[0] < len(fighters[fighter_row]) - 1:
                cur_pos[0] = cur_pos[0] + 1
                result.append(fighters[fighter_row][cur_pos[0]])
                print("Appending {}".format(fighters[fighter_row][cur_pos[0]]))            
                continue
            if cur_pos[0] == len(fighters[fighter_row]) - 1:
                cur_pos[0] = 0
                result.append(fighters[fighter_row][cur_pos[0]])
                print("Appending {}".format(fighters[fighter_row][cur_pos[0]]))
                continue                
        if move == "up":
            if fighter_row == 0:
                result.append(fighters[fighter_row][cur_pos[0]])
                print("Appending {}".format(fighters[fighter_row][cur_pos[0]]))            
                continue
            else:
                fighter_row = fighter_row - 1
                result.append(fighters[fighter_row][cur_pos[0]])
                print("Appending {}".format(fighters[fighter_row][cur_pos[0]]))
                continue                   
        if move == "down":
            if fighter_row == 1:
                result.append(fighters[fighter_row][cur_pos[0]])
                print("Appending {}".format(fighters[fighter_row][cur_pos[0]]))            
                continue
            else:
                fighter_row = fighter_row + 1
                result.append(fighters[fighter_row][cur_pos[0]])
                print("Appending {}".format(fighters[fighter_row][cur_pos[0]]))
                continue                
    print(result)
    return result