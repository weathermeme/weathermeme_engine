import socket
import sys
import json
import random

HOT_TRESHOLD = 80
COLD_TRESHOLD = 40
CHILLY_TRESHOLD = 60
WIND_TRESHOLD = 20
RAIN_CODE = 500
SNOW_CODE = 600
THUNDERSTORM_CODE = 200

def get_weather_info(api_key, lat, lon):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.err, msg):
        print("Failed to create socket. Error code: " + str(msg[0]) + ", Error message " + str(msg[1]))
        sys.exit()

    try:
        remote_ip = socket.gethostbyname('api.openweathermap.org')
    except socket.gaierror:
        print('Could not resolve hostname. Exiting')
        sys.exit()

    s.connect((remote_ip, 80))

    message = "GET /data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + api_key + "&units=imperial HTTP/1.1\r\nhost: api.openweathermap.org\r\n\r\n"
    try:
        s.sendall(message)
    except socket.error:
        print('Failed to send request, exiting')
        sys.exit()

    reply = s.recv(4096)

    jsonString = reply[reply.index('{') : len(reply)]

    return json.loads(jsonString)

def get_condition(weather_info):
    weather_list = weather_info['weather']
    id_list = []
    for info in weather_list:
        id_list.append(info['id'])

    for weather_id in id_list:
        print(weather_id)

    return id_list
