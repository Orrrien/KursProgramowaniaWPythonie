import time
import requests
import json
from datetime import datetime, timedelta


# funkcja pobierająca dane o loaklizacji autobusów
def get_bus_location(url, api_key):
    data = []
    params = {
        'resource_id': 'f2e5503e-927d-4ad3-9500-4ab9e55deb59',
        'apikey': api_key,
        'type': 1
    }
    for i in range(60):
        response = requests.get(url, params)
        data.append(response.json())
        time.sleep(60)

    return data


# funkcja pobierająca dane o trasach autobusów
def get_bus_route(url, api_key):
    data = []
    params = {
        'apikey': api_key,
    }

    response = requests.get(url, params)
    data.append(response.json())
    return data


def get_bus_stop_location(url, api_key):
    data = []
    params = {
        #'id': 'ab75c33d-3a26-4342-b36a-6e5fef0a3ac3',
        'apikey': api_key,
    }

    response = requests.get(url, params)
    data.append(response.json())
    return data


# funkcja zapisaująca dane do pliku .json
def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


# funkcja formatująca plik tak aby zawierał jedną listę słowników (response)
def clean_file(filename, result_file):
    bus_list = []
    with open(filename, 'r') as file:
        bus_data = json.load(file)
        with open(result_file, 'w') as result_file:
            for i in range(len(bus_data)):
                for j in range(len(bus_data[i]["result"])):
                    if type(bus_data[i]["result"]) != list:
                        break
                    bus_list.append(bus_data[i]["result"][j])
            json.dump(bus_list, result_file, indent=4)

    return result_file


def clean_route_file(filename, result_file):
    with open(filename, 'r') as file:
        bus_data = json.load(file)
        with open(result_file, 'w') as result_file:
            bus_route_dict = bus_data[0]["result"]
            json.dump(bus_route_dict, result_file, indent=4)

    return result_file

# funkcja formatująca plik tak aby zawierał listę L list l, gdzie lista l zawiera
#   wszystkie słowniki (response) dotyczące jednego pojazdu, posortowane po czasie
def divide_by_vehicle(result_file, sorted_filename, start_hour):
    with open(result_file, 'r') as file:
        vehicles = []
        sorted_data = []
        data = json.load(file)
        with open(sorted_filename, 'w') as sorted_file:
            for i in range(len(data)):
                line_nr = data[i].get('Lines')
                veh_id = data[i].get('VehicleNumber')
                id = (line_nr, veh_id)
                format = '%Y-%m-%d %H:%M:%S'
                timestr = data[i].get('Time')
                time = datetime.strptime(timestr, format)
                if time.hour < start_hour:
                    continue
                if id not in vehicles:
                    vehicles.append(id)
                    list = [data[i]]
                    sorted_data.append(list)
                else:
                    id = vehicles.index(id)
                    sorted_data[id].append(data[i])
            for i in range(len(sorted_data)):
                sorted_data[i] = sorted(sorted_data[i], key=lambda d: d['Time'])
            json.dump(sorted_data, sorted_file, indent=4)



api_key = 'e44d6e67-41b1-4e29-afb5-02ca18deb69c'
bus_pos_url = 'https://api.um.warszawa.pl/api/action/busestrams_get/?'
bus_route_url = 'https://api.um.warszawa.pl/api/action/public_transport_routes/?'
bus_stop_url = 'https://api.um.warszawa.pl/api/action/busestrams_get/?'
bus_stop_location_url = 'https://api.um.warszawa.pl/api/action/dbstore_get/?ab75c33d-3a26-4342-b36a-6e5fef0a3ac3'

bus_positions = get_bus_location(bus_pos_url, api_key)
bus_positions2 = get_bus_location(bus_pos_url, api_key)
bus_route = get_bus_route(bus_route_url, api_key)
bus_stop_location = get_bus_stop_location(bus_stop_url, api_key)

filename = 'bus_positions.json'
result_filename = 'bus_positions_clean.json'
sorted_filename = 'bus_positions_divided.json'
start_hour = 13

filename2 = 'bus_positions_2.json'
result_filename2 = 'bus_positions_clean2.json'
sorted_filename2 = 'bus_positions_divided2.json'
start_hour2 = 16

bus_timetable_filename = 'bus_timetable.json'
bus_timetable_clean_filename = 'bus_timetable_clean.json'
bus_route_filename = 'bus_route.json'
bus_route_clean_filename = 'bus_route_clean.json'
bus_stop_location_filename = 'bus_stop_location.json'

save_to_json(bus_route, bus_route_filename)
clean_route_file(bus_route_filename, bus_route_clean_filename)

save_to_json(bus_stop_location, bus_stop_location_filename)

save_to_json(bus_positions, filename)
save_to_json(bus_positions2, filename2)

clean_file(filename, result_filename)
divide_by_vehicle(result_filename, sorted_filename, start_hour)

clean_file(filename2, result_filename2)
divide_by_vehicle(result_filename2, sorted_filename2, start_hour2)


























"""
counter = 0
with open('test1-1-j.json', 'r') as file1:
    data = json.load(file1)
    for i in range(len(data)):
        if type(data[i]) != dict:
            #data.pop(i)
            continue
        print(data[i]["Lines"])
        if data[i]["Lines"] == "213":
            counter += 1
    print(counter)

    #print(bus_data[0]["result"][0])
    
"""
