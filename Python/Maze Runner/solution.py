def maze_runner(maze, directions):
    print("You have {} ({}) directions: {}".format(len(directions), len(directions) -1, directions))
    print("*" * 35)
    section_num = 0
    section_length = 0
    maze_length = len(maze)
    print("Your maze is {} x {}".format(maze_length,len(maze[0])))
    print("*" * 35)
    start = []
    end = []
    for section in maze:
        print(section_num, section)
        section_length = len(section)
        if 2 in section:
            start.append(section_num)
            start.append(section.index(2))

        if 3 in section:
            end.append(section_num)
            end.append(section.index(3))

        section_num +=1
        
    print("*" * 35)
    print("Start coords: {}".format(start))
    print("End coords: {}".format(end))
    print("*" * 35)
    print("Following directions...")
    pos = start.copy()
    next_pos = start.copy()
    direction_num = 0
    for direction in directions:
        if direction == "N":
            if pos[0] - 1 < 0:
                print("*" * 35)
                print("[N] here lies so-and-so who lost their way at {}, {}".format(pos[0], pos[1]))
                return "Dead"
            if pos[0] - 1 >= 0:
                next_pos[0] = next_pos[0] - 1
                if next_pos[0] < 0:
                    print("*" * 35)
                    print("[N] you've met death at {}, {}, RIP!".format(next_pos[0], next_pos[1]))
                    return "Dead"                
                next_tile = maze[next_pos[0]][next_pos[1]] 
                print(direction_num, "[N] | current", pos, pos[0], "| next", next_pos, next_pos[0], "| next_tile", next_tile, "| ML", maze_length)
                if next_tile == 1:
                    print("*" * 35)
                    print("[N] a sand giant hits YOU for 5987 points of damage!")
                    return "Dead"
                if next_tile == 3:
                    print("*" * 35)
                    print("You found the exit at coords: {}, {}".format(next_pos[0], next_pos[1]))
                    return "Finish"
                pos[0] = next_pos[0]
                pos[1] = next_pos[1]
        if direction == "E":
            if pos[1] + 1 > section_length:
                print("*" * 35)
                print("[E] here lies so-and-so who lost their way at {}, {}".format(pos[0], pos[1]))
                return "Dead"
            if pos[1] + 1 <= section_length:
                next_pos[1] = next_pos[1] + 1
                if next_pos[1] > maze_length - 1:
                    print("*" * 35)
                    print("[E] you've met death at {}, {}, RIP!".format(next_pos[0], next_pos[1]))
                    return "Dead"                
                next_tile = maze[next_pos[0]][next_pos[1]]
                print(direction_num, "[E] | current", pos, pos[1], "| next", next_pos, next_pos[1], "| next_tile", next_tile, "| ML", maze_length)
                if next_tile == 1:
                    print("*" * 35)
                    print("[E] a sand giant hits YOU for 5987 points of damage!")
                    return "Dead"
                if next_tile == 3:
                    print("*" * 35)
                    print("You found the exit at coords: {}, {}".format(next_pos[0], next_pos[1]))                    
                    return "Finish"
                pos[0] = next_pos[0]
                pos[1] = next_pos[1]                
        if direction == "S":
            if pos[0] + 1 >= maze_length:
                print("*" * 35)
                print("[S] here lies so-and-so who lost their way at {}, {}".format(pos[0], pos[1]))
                return "Dead"
            if pos[0] + 1 < maze_length:
                next_pos[0] = next_pos[0] + 1
                if next_pos[0] > maze_length - 1:
                    print("*" * 35)
                    print("[S] you've met death at {}, {}, RIP!".format(next_pos[0], next_pos[1]))
                    return "Dead"
                next_tile = maze[next_pos[0]][next_pos[1]] 
                print(direction_num, "[S] | current", pos, pos[0], "| next", next_pos, next_pos[0], "| next_tile", next_tile, "| ML", maze_length)
                if next_tile == 1:
                    print("*" * 35)
                    print("[S] a sand giant hits YOU for 5987 points of damage!")
                    return "Dead"
                if next_tile == 3:
                    print("*" * 35)
                    print("You found the exit at coords: {}, {}".format(next_pos[0], next_pos[1]))
                    return "Finish"
                pos[0] = next_pos[0]
                pos[1] = next_pos[1]                
        if direction == "W":
            if pos[1] - 1 < 0:
                print("*" * 35)
                print("[W] here lies so-and-so who lost their way at {}, {}".format(pos[0], pos[1]))
                return "Dead" 
            if pos[1] - 1 >= 0:
                next_pos[1] = next_pos[1] - 1
                if next_pos[1] < 0:
                    print("*" * 35)
                    print("[W] you've met death at {}, {}, RIP!".format(next_pos[0], next_pos[1]))
                    return "Dead"                
                next_tile = maze[next_pos[0]][next_pos[1]]
                print(direction_num, "[W] | current", pos, pos[1], "| next", next_pos, next_pos[1], "| next_tile", next_tile, "| ML", maze_length)
                if next_tile == 1:
                    print("*" * 35)
                    print("[W] a sand giant hits YOU for 5987 points of damage!")
                    return "Dead"
                if next_tile == 3:
                    print("*" * 35)
                    print("You found the exit at coords: {}, {}".format(next_pos[0], next_pos[1]))                    
                    return "Finish"
                pos[0] = next_pos[0]
                pos[1] = next_pos[1]                
        direction_num += 1
    print("*" * 35)
    print("Finished with {} directions, you must be lost!".format(direction_num))
    return "Lost"
