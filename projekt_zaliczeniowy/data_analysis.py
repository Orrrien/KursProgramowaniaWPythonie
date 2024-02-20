import json
from geopy import distance
from datetime import datetime
import matplotlib


class Stop:
    def __init__(self, zespol, slupek, nazwa_zespolu,
                 id_ulicy, szer_geo, dlug_geo, kierunek, obowiazuje_od):
        self.zespol = zespol
        self.slupek = slupek
        self.nazwa_zespolu = nazwa_zespolu
        self.id_ulicy = id_ulicy
        self.szer_geo = szer_geo
        self.dlug_geo = dlug_geo
        self.kierunek = kierunek
        self.obowiazuje_od = obowiazuje_od

    def position(self):
        return self.szer_geo, self.dlug_geo

    def id(self):
        return self.zespol, self.slupek


# funkcja zliczająca liczbę autobusów w promieniu 0,5 km od punktu
#   (w przypadku tej analizy: liczbę autobusów które przekroczyły prędkość 50km/h
def speed_location(point_list, point):
    if point not in point_list:
        point_list.append([point, 1])
    for i in range(len(point_list)):
        if distance.distance(point_list[i][0], point) < 0.5 and point_list[i][0] != point:
            point_list[i][1] += 1
    return point_list


# funkcja obliczająca w jakim czasie autobus przemieścił się między dwoma punktami
def calculate_time(bus_list, index):
    format = '%Y-%m-%d %H:%M:%S'
    time1 = datetime.strptime(bus_list[index - 1].get('Time'), format)
    time2 = datetime.strptime(bus_list[index].get('Time'), format)
    time = time2 - time1
    time = time.total_seconds() / 3600
    return time


# funkcja zwracająca pozycję autobusu jako krotkę
def position(bus_list, index):
    pos = (bus_list[index].get('Lat'), bus_list[index].get('Lon'))
    return pos


# funkcja obliczająca odległość między dwoma kolejnymi punktami (z response)
def calculate_distance(bus_list, index):
    pos1 = position(bus_list, index - 1)
    pos2 = position(bus_list, index)
    dis = distance.distance(pos1, pos2).km
    return dis


# funkcja zliczająca ile w sumie zostało zarejestrowanych autobusów podczas zbierania danych
def number_of_buses(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return len(data)


# funkcja znajdująca przystanek po danym id
def find_stop(bus_stop_list, id):
    for stop in bus_stop_list:
        if stop.id() == id:
            return stop
    return None


# funkcja zwracająca listę wszystkich przystanków (obiektów klasy Stop)
def bus_stop_list(filename):
    bus_stop_list = []
    with open(filename, 'r') as file:
        data = json.load(file)
    l = data.get('result')
    for stop in l:
        values = stop.get('values')
        bus_stop = Stop(values[0].get('value'), values[1].get('value'), values[2].get('value'),
                        values[3].get('value'), values[4].get('value'), values[5].get('value'),
                        values[6].get('value'), values[7].get('value'))
        bus_stop_list.append(bus_stop)
    return bus_stop_list


def bus_routes(filename, bus_stop_list):
    bus_routes = ['dummy_line', ['dummy_stop']]
    with open(filename, 'r') as file:
        data = json.load(file)
    i = 1
    dummy_stop = Stop('0', '0', '0', '0', '0', '0', '0', '0')
    for line in data:
        l = [line, [dummy_stop]]
        bus_routes.append(l)
        for route in data.get(line):
            for stop in data.get(line).get(route):
                bus_stop = find_stop(bus_stop_list, (data.get(line).get(route).get(stop).get('nr_zespolu'), data.get(line).get(route).get(stop).get('nr_przystanku')))
                bus_routes[i][1].append(bus_stop)
        i += 1
    return bus_routes


# funkcja wykonująca analizę prędkości autobusów:
#   - przekroczenie 50km/h
#   - nieprzekroczenie nigdy 30km/h
def bus_speed_check(filename):
    point_list = []
    speed_counter = 0
    slow_counter = 0
    with open(filename, 'r') as file:
        data = json.load(file)
    for bus_list in data:
        speeding = False
        slow = True
        for j in range(1, len(bus_list)):
            dis = calculate_distance(bus_list, j)
            time = calculate_time(bus_list, j)
            if time != 0:
                vel = dis / time
            else:
                vel = 0
            if vel > 30:
                slow = False
            if vel > 50:
                speeding = True
                point_list = speed_location(point_list, position(bus_list, j))
        if speeding:
            speed_counter += 1
        if slow:
            slow_counter += 1
    return speed_counter, point_list, slow_counter


filename = 'bus_positions_divided.json'
filename2 = 'bus_positions_divided2.json'
bus_stop_loc_filename = 'bus_stop_loc.json'
bus_route_filename = 'bus_route_clean.json'

tup1 = bus_speed_check(filename)
tup2 = bus_speed_check(filename2)

bus_stop_list = bus_stop_list(bus_stop_loc_filename)
bus_routes = bus_routes(bus_route_filename, bus_stop_list)


speeding1 = tup1[0]
point_list1 = tup1[1]
slow1 = tup1[2]
all_buses1 = number_of_buses(filename)

speeding2 = tup2[0]
point_list2 = tup2[1]
slow2 = tup2[2]
all_buses2 = number_of_buses(filename2)

point_list_sorted1 = sorted(point_list1, key=lambda x: x[1], reverse=True)
point_list_sorted2 = sorted(point_list2, key=lambda x: x[1], reverse=True)
