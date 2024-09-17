

class Profil:
    def __init__(self, name):
        self.name = name
        self.password = None
        self.id = None
        self.trailplan = None
        self.stations = []
        self.perm_read = []
        self.perm_write = []


    def add_station(self, station):
        if isinstance(station, Station) == False:
            print(f"{station} is not a station")
        else:
            already_exist = False
            for st in self.stations:
                if st.name == station.name:
                    already_exist = True
            if already_exist == True:
                print(f"{station.name} is already a station of {self.name}")
            else:
                self.stations.append(station)
                print(f"{station} was added to {self.name}´s profil")

    def remove_station(self, station):
        if isinstance(station, Station) == False:
            print(f"{station} is not a station")
        else:
            if station not in self.stations:
                print(f"{station} not found")
            else:
                self.stations.remove(station)
                print(f"{station} was removed from {self.name}´s profil")

class Station:
    def __init__(self, name, forbitten_trails=[]):
        self.name = name
        self.stop_north = []
        self.stop_east = []
        self.stop_south = []
        self.stop_west = []
        self.trails = []
        self.rail_points = []
        self.trainplan = []
        self.forbitten_trails = forbitten_trails

    def add_forbitten_trails(self, name):
        if name not in self.forbitten_trails:
            self.forbitten_trails.append(name)

    def remove_forbitten_trails(self,name):
        if name in self.forbitten_trails:
            self.forbitten_trails.remove(name)

    def add_train(self,train):
        if isinstance(train, Train)==False:
            print(f"{train.name} is no train")
        else:
            day_found = False
            for day in self.trainplan:
                if train.date in day.keys():
                    day[train.date].append(train)
                    day_found = True
            if day_found == False:
                self.trainplan.append({train.date : [train]})

                    
                

    def add_stop(self, stop, location):
        if location != "north" and location != "south" and location != "east" and location != "west":
            print(f"{location} is an invalid input")
        else:
            if isinstance(stop, (Station, Stop)) == False:
                print(f"{stop} is not a valid stop")
            else:
                if location == "north":
                    if stop not in self.stop_north:
                        self.stop_north.append(stop)
                    else:
                        print(f"{stop} is already a stop {self.name}")
                if location == "east":
                    if stop not in self.stop_east:
                        self.stop_east.append(stop)
                    else:
                        print(f"{stop} is already a stop {self.name}")
                if location == "south":
                    if stop not in self.stop_south:
                        self.stop_south.append(stop)
                    else:
                        print(f"{stop} is already a stop {self.name}")
                if location == "west":
                    if stop not in self.stop_west:
                        self.stop_west.append(stop)
                    else:
                        print(f"{stop} is already a stop {self.name}")

    def remove_stop(self, stop):
        if isinstance(stop, (Station, Stop)) == False:
            print(f"{stop} is not a valid stop")
        if stop in self.stop_north:
            self.stop_north.remove(stop)
        if stop in self.stop_east:
            self.stop_east.remove(stop)
        if stop in self.stop_south:
            self.stop_south.remove(stop)
        if stop in self.stop_west:
            self.stop_west.remove(stop)
            

    def add_trail(self, trail):
        if isinstance(trail, Trail) == False:
            print(f"{trail} is not a trail")
        else:
            if trail in self.trails:
                print(f"{trail} is already a trail of {self.name}")
            else:
                self.trails.append(trail)

    def remove_trail(self, trail):
        if isinstance(trail, Trail) == False:
            print(f"{trail} is not a trail")
        else:
            if trail not in self.trails:
                print(f"{trail} is not a trail of {self.name}")
            else:
                self.trails.remove(trail)

    def add_rail_point(self, rail_point):
        if isinstance(rail_point, Rail_point) == False:
            print(f"{rail_point} is not a rail point")
        else:
            if rail_point in self.rail_points:
                print(f"{rail_point} is already a rail_point of {self.name}")
            else:
                self.rail_points.append(rail_point)

    def remove_trail(self, rail_point):
        if isinstance(rail_point, Rail_point) == False:
            print(f"{rail_point} is not a rail point")
        else:
            if rail_point not in self.rail_points:
                print(f"{rail_point} is not a rail point of {self.name}")
            else:
                self.trails.remove(rail_point)

class Stop:
    def __init__(self, name,cardinal_direction, departure_time):
        self.name = name
        self.cardinal_direction = cardinal_direction
        self.trails = []
        self.departure_time = departure_time

    def add_trail(self, trail):
        if isinstance(trail, Trail) == False:
            print(f"{trail} is not a trail")
        else:
            self.trails.append(trail)

    def remove_trail(self, trail):
        if isinstance(trail, Trail) == False:
            print(f"{trail} is not a trail")
        else:
            if trail not in self.trails:
                print(f"{trail} is not a trail of {self.name}")
            else:
                self.trails.remove(trail)

class Trail:
    def __init__(self, name, length,maintrail=False, left_end=None, right_end=None, allow_dangures=False):
        self.name = name
        self.length = length
        self.left_end = left_end
        self.right_end = right_end
        allow_dangures = allow_dangures
        self.parked_wagons = []
        self.maintrail = False
        self.attached = []

    def park_wagon_r(self, wagon):
        if isinstance(wagon, Wagon):
            if wagon not in self.parked_wagons:
                self.parked_wagons.insert(0, wagon)

    def park_wagon(self, wagon):
        if isinstance(wagon, Wagon):
            if wagon not in self.parked_wagons:
                self.parked_wagons.append(wagon)

    def remove_wagon(self, wagon):
        if isinstance(wagon, Wagon):
            if wagon in self.parked_wagons:
                self.parked_wagons.remove(wagon)


class Rail_point:
    def __init__(self, name) -> None:
        self.name = name
        self.possible_ways = []
        self.attached = []
        self.tilled = False
    
    def atach_target(self, target, distance):
        if isinstance(target,(Trail, Rail_point)) == False:
            print("only rail points and trails can be atached")
        else:
            if self in target.attached:
                print(f"{target} is already atached")
            else:
                self.attached.append(target)
                target.attached.append(self)
                self.possible_ways.append({target : distance})

class Train:
    def __init__(self, name, came_from, date):
        self.name = name
        self.came_from = came_from
        self.date = date
        self.wagons = []

    def add_waggon(self, wagon):
        if isinstance(wagon, Wagon):
            if wagon in self.wagons:
                print(f"{wagon.name} is already in the train")
            else:
                self.wagons.append(wagon)
        else:
            print(f"{wagon} is not a waggon")

    def remove_wagon(self, wagon):
        if isinstance(wagon, Wagon):
            if wagon not in self.wagons:
                print(f"{wagon.name} is not in the train")
            else:
                self.wagons.remove(wagon)
        else:
            print(f"{wagon} is not a waggon")

class Wagon:
    def __init__(self,name, length, target_stop=None, dangures_goods=False):
        self.name = name
        self.length = length
        self.dangures_goods = dangures_goods
        self.target_stop = target_stop
        
