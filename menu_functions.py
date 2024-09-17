from classes import Station, Stop, Trail, Rail_point, Profil
import os
import time
import pickle

def save_station(station):
    if isinstance(station, Station) == False:
        print(f"{station} is not a station")
    else:
        if os.path.exists("./saves/saved_stations.pkl") == False:
            station_list = [station]
            with open("./saves/saved_stations.pkl", "wb") as save_stations:
                pickle.dump(station_list, save_stations)
        else:
            with open("./saves/saved_stations.pkl", "rb") as load_stations:
                station_list = pickle.load(load_stations)
            for item in station_list:
                if item.name == station.name:
                    station_list.remove(item)
            station_list.append(station)
            with open("./saves/saved_stations.pkl","wb") as save_stations:
                pickle.dump(station_list, save_stations)

def show_stations():
    if os.path.exists("./saves/saved_stations.pkl"):
        with open("./saves/saved_stations.pkl", "rb") as load_stations:
            station_list = pickle.load(load_stations)
        return station_list
    
def load_station(station_name):
    station_list = show_stations()
    for item in station_list:
        if station_name == item.name:
            return item
    print(f"profil {station_name} not found")

def clear_stations():
    question_1 = input("Are you sure about that?: ")
    if question_1 == "yes":
        if os.path.exists("./saves/saved_stations.pkl"):
            os.remove("./saves/saved_stations.pkl")

def delete_station(station):
    if os.path.exists("./saves/saved_stations.pkl") == False:
        print("No stations found")
    else:
        with open("./saves/saved_stations.pkl", "rb") as load_stations:
            station_list = pickle.load(load_stations)
        found = False
        for item in station_list:
            if station.name == item.name:
                found = True
                station_list.remove(item)
            with open("./saves/saved_stations.pkl","wb") as save_stations:
                pickle.dump(station_list, save_stations)
        if found == True:
            pass
        else:
            print(f"A station named {station.name} does not exist")

def save_profile(name):
    if isinstance(name, Profil) == False:
        print(f"{name} is not a profil")
    else:
        if os.path.exists("./saves/loading_profiles.pkl") == False:
            profil_list = [name]
            with open("./saves/loading_profiles.pkl", "wb") as save_profil:
                pickle.dump(profil_list, save_profil)
        else:
            with open("./saves/loading_profiles.pkl", "rb") as load_profil:
                profil_list = pickle.load(load_profil)
            for profil in profil_list:
                if name.name == profil.name:
                    profil_list.remove(profil)
            profil_list.append(name)
            with open("./saves/loading_profiles.pkl","wb") as save_profil:
                pickle.dump(profil_list, save_profil)

def show_profiles():
    if os.path.exists("./saves/loading_profiles.pkl"):
        with open("./saves/loading_profiles.pkl", "rb") as load_profil:
            profil_list = pickle.load(load_profil)
        return profil_list
    
def load_profile(name):
    profil_list = show_profiles()
    for profil in profil_list:
        if name == profil.name:
            return profil
    print(f"profil {name} not found")

def clear_profiles():
    if os.path.exists("./saves/loading_profiles.pkl"):
        os.remove("./saves/loading_profiles.pkl")

def delete_profile(name):
    if os.path.exists("./saves/loading_profiles.pkl") == False:
        print("No profiles found")
    else:
        with open("./saves/loading_profiles.pkl", "rb") as load_profil:
            profil_list = pickle.load(load_profil)
        found = False
        for item in profil_list:
            if name == item.name:
                found = True
                profil_list.remove(item)
            with open("./saves/loading_profiles.pkl","wb") as save_profil:
                pickle.dump(profil_list, save_profil)
        if found == True:
            pass
        else:
            print(f"A profil named {name.name} does not exist")

###############################

def save_trailplan(name):
    if isinstance(name, Profil) == False:
        print(f"{name} is not a profil")
    else:
        if os.path.exists("./saves/loading_profiles.pkl") == False:
            profil_list = [name]
            with open("./saves/loading_profiles.pkl", "wb") as save_profil:
                pickle.dump(profil_list, save_profil)
        else:
            with open("./saves/loading_profiles.pkl", "rb") as load_profil:
                profil_list = pickle.load(load_profil)
            for profil in profil_list:
                if name.name == profil.name:
                    profil_list.remove(profil)
            profil_list.append(name)
            with open("./saves/loading_profiles.pkl","wb") as save_profil:
                pickle.dump(profil_list, save_profil)

def show_profiles():
    if os.path.exists("./saves/loading_profiles.pkl"):
        with open("./saves/loading_profiles.pkl", "rb") as load_profil:
            profil_list = pickle.load(load_profil)
        return profil_list
    
def load_profile(name):
    profil_list = show_profiles()
    for profil in profil_list:
        if name == profil.name:
            return profil
    print(f"profil {name} not found")

def clear_profiles():
    if os.path.exists("./saves/loading_profiles.pkl"):
        os.remove("./saves/loading_profiles.pkl")

def delete_profile(name):
    if os.path.exists("./saves/loading_profiles.pkl") == False:
        print("No profiles found")
    else:
        with open("./saves/loading_profiles.pkl", "rb") as load_profil:
            profil_list = pickle.load(load_profil)
        found = False
        for item in profil_list:
            if name == item.name:
                found = True
                profil_list.remove(item)
            with open("./saves/loading_profiles.pkl","wb") as save_profil:
                pickle.dump(profil_list, save_profil)
        if found == True:
            pass
        else:
            print(f"A profil named {name.name} does not exist")
def show_profil_stops(name):
    profil = load_profile(name)
    if isinstance(profil, Profil):
        for stop in profil.stops:
            name = list(stop.keys())[0].name
            print(name)