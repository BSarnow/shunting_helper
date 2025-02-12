from classes import Station, Stop, Trail, Rail_point, Profil, Train, Wagon
from menu_functions import save_profile, save_station, clear_profiles, clear_stations, delete_profile, delete_station, load_profile, load_station, show_profiles, show_stations
from shunting_functions import best_way, shunting
import os
import time
import pickle
profil = None
home_station = None

def main ():
    clear_profiles()
    Testprofil = Profil("Rootprofil", "Shura001")
    BahnhofA = Station("BahnhofA", "A5")
    BahnhofB = Stop("BahnhofB","south", "1245")
    Salzwerk = Stop("Salzwerk","west", "0820")
    Metallverarbeitung = Stop("Metallverarbeitung","south", "1520")
    Chemiefirma = Stop("Chemiefirma","east", "0920")
    trail_A11 = Trail("A11", 300, True, None, "south")
    trail_A12 = Trail("A12", 300, True, None, "south")
    trail_A13 = Trail("A13", 300, True, None, "south")
    trail_A14 = Trail("A14", 300, True, None, "south")
    trail_A15 = Trail("A15", 150, False,)
    trail_A16 = Trail("A16", 150, False, None, None, True)
    trail_A115 = Trail("A115", 250, False, None, None, True)
    trail_A116 = Trail("A116", 250, False,)
    trail_A3 = Trail("A3", 500, True, "east", "west")
    trail_A4 = Trail("A4", 700, True, "east", "west")
    trail_A5 = Trail("A5", 720, True, "east", "west")
    rail_point_W1 = Rail_point("W1")
    rail_point_W2 = Rail_point("W2")
    rail_point_W1.atach_target(trail_A3, 50)
    rail_point_W1.atach_target(rail_point_W2, 25)
    rail_point_W2.atach_target(trail_A4, 25)
    rail_point_W2.atach_target(trail_A5, 25)
    rail_point_w3 = Rail_point("W3")
    rail_point_W4 = Rail_point("W4")
    rail_point_w3.atach_target(trail_A5, 0)
    rail_point_w3.atach_target(rail_point_W4, 75)
    rail_point_W5 = Rail_point("W5")
    rail_point_W4.atach_target(rail_point_W5, 10)
    rail_point_W4.atach_target(trail_A14, 50)
    rail_point_W6 = Rail_point("W6")
    rail_point_W9 = Rail_point("W9")
    rail_point_W6.atach_target(trail_A5, 0)
    rail_point_W6.atach_target(rail_point_W9, 30)
    rail_point_W7 = Rail_point("W7")
    rail_point_W7.atach_target(trail_A16, 0)
    rail_point_W7.atach_target(trail_A116, 0)
    rail_point_W8 = Rail_point("W8")
    rail_point_W5.atach_target(rail_point_W8, 10)
    rail_point_W5.atach_target(trail_A115, 0)
    rail_point_W8.atach_target(rail_point_W7, 10)
    rail_point_W8.atach_target(trail_A15, 0)
    rail_point_W10 = Rail_point("W10")
    rail_point_W11 = Rail_point("W11")
    rail_point_W9.atach_target(rail_point_W10, 20)
    rail_point_W9.atach_target(rail_point_W11, 20)
    rail_point_W10.atach_target(trail_A13, 20)
    rail_point_W10.atach_target(trail_A14, 20)
    rail_point_W11.atach_target(trail_A11, 20)
    rail_point_W11.atach_target(trail_A12, 20)
    rail_point_W12 = Rail_point("W12")
    rail_point_W13 = Rail_point("W13")
    rail_point_W12.atach_target(trail_A3, 10)
    rail_point_W12.atach_target(trail_A4, 10)
    rail_point_W13.atach_target(trail_A5, 50)
    rail_point_W13.atach_target(rail_point_W12,40)
    BahnhofA.add_trail(trail_A3)
    BahnhofA.add_trail(trail_A4)
    BahnhofA.add_trail(trail_A5)
    BahnhofA.add_trail(trail_A11)
    BahnhofA.add_trail(trail_A12)
    BahnhofA.add_trail(trail_A13)
    BahnhofA.add_trail(trail_A14)
    BahnhofA.add_trail(trail_A15)
    BahnhofA.add_trail(trail_A16)
    BahnhofA.add_trail(trail_A115)
    BahnhofA.add_trail(trail_A116)
    BahnhofA.add_rail_point(rail_point_W1)
    BahnhofA.add_rail_point(rail_point_W2)
    BahnhofA.add_rail_point(rail_point_w3)
    BahnhofA.add_rail_point(rail_point_W4)
    BahnhofA.add_rail_point(rail_point_W5)
    BahnhofA.add_rail_point(rail_point_W6)
    BahnhofA.add_rail_point(rail_point_W7)
    BahnhofA.add_rail_point(rail_point_W8)
    BahnhofA.add_rail_point(rail_point_W9)
    BahnhofA.add_rail_point(rail_point_W10)
    BahnhofA.add_rail_point(rail_point_W11)
    BahnhofA.add_rail_point(rail_point_W12)
    BahnhofA.add_rail_point(rail_point_W13)
    BahnhofA.add_stop(BahnhofB, "south")
    BahnhofA.add_stop(Salzwerk, "west")
    BahnhofA.add_stop(Chemiefirma, "east")
    BahnhofA.add_stop(Metallverarbeitung, "south")
    wagon_25_80_4351_007_0 = Wagon("25 80 4351 007-0",27, Metallverarbeitung)
    wagon_42_80_2468_001_0 = Wagon("42 80 2468 001-0", 15, Salzwerk)
    wagon_42_80_2468_010_3 = Wagon("42 80 2468 010-3", 15, Salzwerk)
    wagon_25_80_4293_526_2 = Wagon("25 80 4293 526-2", 31, BahnhofB)
    wagon_83_80_5400_002_0 = Wagon("83 80 5400 002-0", 15, Chemiefirma, True)
    wagon_25_80_4293_789_4 = Wagon("25 80 4293 789-4", 31, BahnhofB)
    wagon_83_80_4371_007_9 = Wagon("83 80 4371 007-9", 54, None, True)
    train_55166 = Train("55166", "south", 13092024)
    train_55166.add_waggon(wagon_25_80_4351_007_0)
    train_55166.add_waggon(wagon_42_80_2468_001_0)
    train_55166.add_waggon(wagon_42_80_2468_010_3)
    train_55166.add_waggon(wagon_25_80_4293_526_2)
    train_55166.add_waggon(wagon_83_80_5400_002_0)
    train_55166.add_waggon(wagon_25_80_4293_789_4)
    train_55166.add_waggon(wagon_83_80_4371_007_9)
    BahnhofA.add_train(train_55166)
    Testprofil.add_station(BahnhofA)
    save_profile(Testprofil)
    print("this is just a placeholder")
    profil = load_profile("Rootprofil")
    home_station = profil.stations[0]
    for wagon in home_station.trainplan[0][13092024][0].wagons:
        if wagon.target_stop != None:
            print(wagon.target_stop.name)


    testlauf = shunting(home_station, home_station.trainplan[0][13092024][0])
    for position in testlauf[0]:
        if isinstance(position, str):
            print(position)
        if isinstance(position, list):
            named_list = []
            for item in position:
                named_list.append(item.name)
            print(named_list)
    for position in testlauf[1]:
        print(position)
    
 
main()
