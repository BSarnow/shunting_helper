from classes import Trail, Rail_point
import random


def best_way(home_station, start, end, forbitten_names=[]):
    print(f"forbitten names = {forbitten_names}")
    
    start_trail = None
    if isinstance(start, Trail) == False:
        for trail in home_station.trails: # searching for the starting trail
            if trail.name == start:
                start_trail = trail
        if start_trail == None:
            print("No such trail or rail point exists")
    else:
        start_trail = start
    forbitten = [] # will be filled with the choises of the user in "forbitten_names"
    forbitten_repeat = [] # will be filled when a way to the end was found to try if there is a shorter way
    blocked = [] # will be filled with trails that has wagons in it
    for trail in home_station.trails: # searching for trails with wagons in it
        if len(trail.parked_wagons) != 0 and trail != start_trail:
            print(f"we add {trail.name} to blocked becouse it has wagons in it")
            blocked.append(trail)
            print(start_trail.name)
    for name in home_station.trails: # searching for trails that the user has forbitten
        if name.name in forbitten_names:
            print(f"add {name.name} to forbitten becouse its in forbiiten_names")
            forbitten.append(name)
    for name in home_station.rail_points: # searching for rail points that the user has forbitten
        if name.name in forbitten_names:
            print(f"add {name.name} to forbitten becouse its in forbiiten_names")
            forbitten.append(name)
    current_position = start_trail
    visited = [] # will be filled with already used current_positions to hinder the program to go backwarts
    way = [] # to remember the current used way
    shortest_way = [] # way if the end was found with fewer steps then the shortest_way bevor
    not_used= [] # to remember ways that was not used to take them the next way, if no end was found.
    favorit = [] # will be filled with the items of not_used when we start a new way. the code will favorit possible ways that are in favorit
    count_whiles_fails = 0 #count the fails of ways so the loop will end if the end is unreachable or the shortest way is already found
    end_while_loop = False #help-variable to end the while loop on specific conditions
    while end_while_loop == False:
        possible_ways = [] # ways that are attached to the current position and are possible to go
        print(f"current position = {current_position.name}")
        if current_position not in visited: # holdes the visited-list shorter
            print(f" add {current_position.name} to visited")
            visited.append(current_position)
        print(f" add {current_position.name} to way")
        way.append(current_position)
        if current_position.name == end: # checks if a way to the target was found
            print("current position is end")
            if len(forbitten_repeat) != 0: # pops the last forbitten_repeat and adds the next one to forbitten
                print(f"remove {forbitten_repeat[-1].name} from forbitten")
                forbitten.remove(forbitten_repeat[-1])
                forbitten_repeat.pop(-1)
            if len(way) < len(shortest_way) or len(shortest_way)==0: # set the shortest way to the current way, if the current way is shorter or there is no shortest way
                print(f"changed shortest way becouse it is None or way is shorter")
                print(f"{len(shortest_way)} {len(way)}")
                print("we make a new forbitten_repeat becouse we found a shorter way")
                forbitten_repeat = way[0:-1] # forbitten_repeat is needed later to find possible shorter ways
                shortest_way = way
                way = [] # way have to be clear so the code can start a new one
                print("way becomes [] becouse it has found the end")
                print("count fails becomes 0 becouse we found a shorter way")
                count_whiles_fails = 0 
            if len(forbitten_repeat) != 0: # adds a forbitten trail or rail_point so the loop will not always run in the same way
                print(f" add {forbitten_repeat[-1].name} to forbitten")
                forbitten.append(forbitten_repeat[-1])
        else: # no end was found so he checks possible ways to go on
            print("Searching for possible ways, becouse we found no end")
            if current_position in blocked: # blocks the search for possible ways becouse the trail is filled with wagons and the train cant drive through the current position
                print(f"we allow no possible ways becouse {current_position.name} is blocked")
            else:
                for pw in current_position.attached:
                    if pw not in visited and pw not in not_used and pw not in forbitten:
                        print(f"add {pw.name} to possible ways becouse its not in not_used and not in visited")
                        possible_ways.append(pw)
        if len(possible_ways) == 0: # checks if the way reached a dead end. if so, it starts a new way
            way = []
            count_whiles_fails += 1 # counts the found dead ends. if it reach 100 the loop will end
            print(f"way becomes [] and while fails raise to {count_whiles_fails} becouse we found no possible way")
        if len(possible_ways) != 0:
            found_favorit = None # search for the first possible favorit that can be used and takes later as the only possible way. then removes it from favorits
            print("searching for favorits...")
            for pf in possible_ways: 
                if pf in favorit:
                    found_favorit = pf
                    favorit.remove(pf)
                    possible_ways.remove(pf)
                    break
            if found_favorit != None:
                print(f" we changed current position to {found_favorit.name} becouse it was in favorits")
                current_position = found_favorit
                for pw in possible_ways:
                    print(f"add {pw.name} to not_used becouse we found a favorit")
                    not_used.append(pw)
            else: # takes the first possible way becouse no favorit was found
                print(f" we change current position to {possible_ways[0].name} becouse we found no favorit")
                current_position = possible_ways[0]
                possible_ways.pop(0)
                for pw in possible_ways:
                    print(f"add {pw.name} to not_used becouse we used a other possible way")
                    not_used.append(pw)
        if way == []: # function to start a new way with the not_useds as new favorits
            current_position = start_trail
            print(f"we changed current position to {current_position.name} becouse way was []")
            for nu in not_used:
                if nu not in favorit:
                    print(f" we added {nu.name} to favorits becouse it was in not_used")
                    favorit.append(nu)
            print("we cleared not_used and visited so we can start from the beginning")
            not_used = []
            visited = []
        if count_whiles_fails > 30: # resets the fails and removes the forbitten from forbitten_repeats. stops the loop from always running in a dead end becouse we cut the end from the rest of the station.
            if len(forbitten_repeat) != 0:
                count_whiles_fails = 0
                print(f"we removed {forbitten_repeat[-1]} from forbitten_repeat becouse we found no end with it ")
                forbitten.remove(forbitten_repeat[-1])
                forbitten_repeat.pop(-1)
                if len(forbitten_repeat) != 0:
                    forbitten.append(forbitten_repeat[-1])
                else: # ends the loop earlier if we dont cut the end form the rest of the station and the code still findes no way to the end
                    print("we break the loop becouse the last forbitten_repeat was used without finding an end")
                    end_while_loop = True
        if count_whiles_fails > 59: # ends the loop after 60 dead ends
            print("we end the loop becouse while_fails are 100")
            end_while_loop = True
        # prints every step in a readable form in the loop to help debugging
        named_way = []
        named_not_used = []
        named_visited = []
        named_favorit = []
        named_forbitten = []
        named_shortest_way = []
        named_forbitten_repeat = []
        named_blocked = []
        for position in forbitten:
            named_forbitten.append(position.name)
        for position in blocked:
            named_blocked.append(position.name)
        for position in forbitten_repeat:
            named_forbitten_repeat.append(position.name)
        for position in shortest_way:
            named_shortest_way.append(position.name)
        for position in way:
            named_way.append(position.name)
        for position in not_used:
            named_not_used.append(position.name)
        for position in visited:
            named_visited.append(position.name)
        for position in favorit:
            named_favorit.append(position.name)
        print(f"way = {named_way}")
        print(f"not_used = {named_not_used}")
        print(f"visited = {named_visited}")
        print(f"favorit = {named_favorit}")
        print(f"forbitten = {named_forbitten}")
        print(f"forbitten_repeat = {named_forbitten_repeat}")
        print(f"shortest way = {named_shortest_way}")
        print(f"blocked = {named_blocked}")
        #input("continue?") #slows down the program so we can proof it step by step
    if len(shortest_way) == 0: #needed later when the programm findes no way to the end
        return None
    else:
        return shortest_way 
                
def shunting(home_station, train):
    forbitten = []
    for trail in home_station.trails:
        if trail.name in home_station.forbitten_trails:
            forbitten.append(trail)
    ways = [] # saves all driven ways
    shunting_wagons = [] # needed to show the current driven wagons
    target = "not found yet" # the target of the working_at_wagons
    possible_end_trails = [] # possible targets for the working_at_wagons
    came_from = train.came_from # needed for the right order of the arriving train
    to_do_wagons = [] # all wagons of the arriving train
    for trail in home_station.trails: # shows the user all possible trails at let him decied on wich the train arrives
        if trail.left_end == came_from:
            print(f"{trail.name} left")
        if trail.right_end == came_from:
            print(f"{trail.name} right")
    start_trail = input("On wich trail should the train arraive: ")
    for trail in home_station.trails: # looking for the starting trail
        if trail.name == start_trail:
            start_trail = trail
    for wagon in train.wagons: # add the wagons of the train to the to_do_list
        start_trail.park_wagon(wagon)
        to_do_wagons.append(wagon)
    #test_stop = 0
    start = start_trail
    #while test_stop < 2:
        #test_stop += 1
        #print("================================================")
    while len(to_do_wagons) != 0: # while until all wagons have reached their target position
        working_at = [] # the wagons the code is looking for the right target
        for x in range(0, len(start.parked_wagons)): #looking for groups
            if working_at == [] and start.parked_wagons[x] in to_do_wagons:
                working_at.append(start.parked_wagons[x])
            else:
                if start.parked_wagons[x] in to_do_wagons:
                    if working_at[0].target_stop == start.parked_wagons[x].target_stop:
                        working_at.append(start.parked_wagons[x])
                    else:
                        if len(working_at) == 1:
                            working_at = []
                            working_at.append(start.parked_wagons[x])

        for x in range(0, len(start.parked_wagons)): # put all wagons befor the working_at to the shunting wagons.
            if start.parked_wagons[x] not in working_at and start.parked_wagons[x] not in shunting_wagons and start.parked_wagons[x] in to_do_wagons:
                shunting_wagons.append(start.parked_wagons[x])
            if start.parked_wagons[x] in working_at:
                break
        for wagon in working_at: # put the working_at to the shunting wagons
            shunting_wagons.append(wagon)

        for wagon in shunting_wagons: #removes wagon from the starting trail
            start.remove_wagon(wagon)

        if working_at[0].target_stop != None:
            for stop in home_station.stop_north: # looking where to find the possible trails for the stop of the working_at_wagons
                if stop == working_at[0].target_stop:
                    target = "north"
            for stop in home_station.stop_south:
                if stop == working_at[0].target_stop:
                    target = "south"
            for stop in home_station.stop_west:
                if stop == working_at[0].target_stop:
                    target = "west"
            for stop in home_station.stop_east:
                if stop == working_at[0].target_stop:
                    target = "east"
            for trail in home_station.trails:
                if trail not in forbitten:
                    if trail.left_end == target or trail.right_end == target: # checks if the target trail is empty or the wagons in it have the same target stop
                        if trail.parked_wagons == [] or trail.parked_wagons[-1].target_stop == working_at[-1].target_stop:
                            possible_end_trails.append(trail)
                        else:
                            if working_at[-1].target_stop != None: # checks if the wagons already in the trail will leave the station bevor the working_at_wagons have to leave...
                                departure_time = int(working_at[-1].target_stop.departure_time)
                                cardinal_direction = working_at[-1].target_stop.cardinal_direction
                                allowed = True
                                for wagon in trail.parked_wagons:
                                    if wagon.target_stop != None:
                                        if wagon.target_stop.cardinal_direction != cardinal_direction:
                                            allowed = False
                                        if int(wagon.target_stop.departure_time) < departure_time:
                                            allowed = False
                                        if wagon in to_do_wagons:
                                            allowed = False
                            if allowed == True: #... if so the trail is still a possible end.
                                possible_end_trails.append(trail)

        if start == start_trail and start_trail in possible_end_trails: # checks if the start_trail is also the target trail. if so, no shunting is needed.
            for wagon in shunting_wagons:
                start_trail.park_wagon(wagon)
            for wagon in working_at:
                to_do_wagons.remove(wagon)
                working_at.remove(wagon)
                if wagon.target_stop != None:
                    stayed = f"Let {wagon.name} at {start_trail.name} for continue driving to {wagon.target_stop.name}"
                    ways.append(stayed)
            shunting_wagons = []
        else: # checks if there are already wagons with the same target ready to be driven. if so, the trail with the wagons become the only possible target trail.
            found_way = []
            for end in possible_end_trails:
                if end.parked_wagons != []:
                    if working_at[-1].target_stop == end.parked_wagons[0].target_stop:
                        possible_end_trails = []
                        possible_end_trails.append(end)
                        break

            for end in possible_end_trails: # searching for the shortest way of all possible targets and chooses the nearest target trail
                check_end = best_way(home_station, start, end.name)
                if check_end == None:
                    continue
                elif found_way == []:
                    found_way = check_end
                elif len(found_way) > len(check_end):
                    found_way = check_end

            if found_way != []: # if an allowed trail was found as possible target trail all wagons with that target are parked at the target trail
                working_at.reverse()
                for wagon in working_at:
                    found_way[-1].park_wagon_r(wagon)
                    to_do_wagons.remove(wagon)
                    shunting_wagons.remove(wagon)
                    target_found = f"park wagon {wagon.name} on {found_way[-1].name} for continue driving to {wagon.target_stop.name}"
                    ways.append(target_found)
                working_at = []
                ways.append(found_way) # the moved way is saved at ways for the shunting journal
                start = found_way[-1] # the end trail becomes the new start so we can move on from that trail

                if shunting_wagons == [] and to_do_wagons != []: # checks if there are still wagons to do at the trail the train has arrived when no wagons are left in the shunting group
                    back_to_start = best_way(home_station, start, start_trail.name) # searches for the shortest way back to the start
                    back = "drive back to start_trail"
                    ways.append(back) # saves in the shunting journal, that we moved back to the start trail
                    ways.append(back_to_start)
                    start = back_to_start[-1]
            
                if shunting_wagons != []: # checks if there are wagons in the shunting group that we not already worked at.
                    if start_trail.parked_wagons != []: # checks if there are wagons on the start trail that has the same target as the last wagon in the shunting group
                        if shunting_wagons[-1].target_stop == start_trail.parked_wagons[0]: # if so, it dirves back to the start trail
                            back_to_start = best_way(home_station, start, start_trail.name)
                            for wagon in shunting_wagons:
                                start_trail.park_wagon_r(wagon)
                            back = "drive back to start_trail"
                            ways.append(back)
                            ways.append(back_to_start)
                            start = back_to_start[-1]

                shunting_wagons.reverse() # if not it parks the wagon at the current trail befor the wagon we worked at last time to form a new working at group when the while loop starts again
                for wagon in shunting_wagons:
                    start.park_wagon_r(wagon)

            if found_way == []: # checks if no target trail can be reached and looks for trails to park the wagons for later shunting operations
                possible_end_trails = []
                for trail in home_station.trails:
                    if trail.left_end == None and trail.right_end == None:
                        if working_at[-1].dangures_goods == True and trail.allow_dangures == True:
                            possible_end_trails.append(trail)
                        if working_at[-1].dangures_goods == False and trail.allow_dangures == False:
                            possible_end_trails.append(trail)
                            
                for end in possible_end_trails: # if it found one it searches for the shortest way to the nearest target
                    check_end = best_way(home_station, start, end.name)
                    if check_end == None:
                        continue
                    elif found_way == []:
                        found_way = check_end
                    elif len(found_way) > len(check_end):
                        found_way = check_end
            
                if found_way != []: # if it found a way it will move the wagons to it and park the wagons
                    working_at.reverse()
                    for wagon in working_at:
                        found_way[-1].park_wagon_r(wagon)
                        found_way[0].remove_wagon(wagon)
                        to_do_wagons.remove(wagon)
                        shunting_wagons.remove(wagon)
                        target_found = f"park wagon {wagon.name} on {found_way[-1].name}"
                        ways.append(target_found)
                    working_at = []

                    ways.append(found_way)
                    start = found_way[-1]
                    if shunting_wagons == [] and to_do_wagons != []:
                        back_to_start = best_way(home_station, start, start_trail.name)
                        back = "drive back to start_trail"
                        ways.append(back)
                        ways.append(back_to_start)
                        start = back_to_start[-1]
                
                    if shunting_wagons != []:
                        if start_trail.parked_wagons != []:
                            if shunting_wagons[-1].target_stop == start_trail.parked_wagons[0]:
                                back_to_start = best_way(home_station, start, start_trail.name)
                                for wagon in shunting_wagons:
                                    start_trail.park_wagon_r(wagon)
                                back = "drive back to start_trail"
                                ways.append(back)
                                ways.append(back_to_start)
                                start = back_to_start[-1]

                    shunting_wagons.reverse()
                    for wagon in shunting_wagons:
                        start.park_wagon_r(wagon)

        if found_way == []: # if it still find no way the code is stucked in a dead end. it gives up all all other operations and write an error in the shunting journal
            error = f"Can´t create a shunting plan becouse we found no allowed place for {working_at[-1].name}"
            ways.append(error)
            to_do_wagons = []

        shunting_wagons = [] # clears the shunting wagons and the possible_end_trails for a clean restart of the while_loop
        possible_end_trails = []

    parked_wagons = [] # writes the position of every wagon in the station.
    for trail in home_station.trails:
        if trail.parked_wagons != []:
            current_trail = f"At {trail.name} are following wagons:"
            parked_wagons.append(current_trail)
            named_list= []
            for wagon in trail.parked_wagons:
                if wagon.target_stop != None:
                    wagon_with_target = f"{wagon.name} for {wagon.target_stop.name}"
                else:
                    wagon_with_target = f"{wagon.name} with no target stop"
                named_list.append(wagon_with_target)
            parked_wagons.append(named_list)
            
    return ways, parked_wagons
            
    



    

    

