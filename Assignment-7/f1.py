import requests


def get_season(year):
    # print("http://ergast.com/api/f1/+++/constructorStandings".replace('+++', str(year)))
    url = "http://ergast.com/api/f1/+++/constructorStandings.json?limit=1000".replace('+++', str(year))

    constructor_name = requests.get(url).json()["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"][0]["Constructor"]["name"]

    url2 = "https://ergast.com/api/f1/+++/driverStandings.json?limit=1000".replace('+++', str(year))
    
    name = requests.get(url2).json()["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["Driver"]["givenName"]
    full_name = name + ' ' + requests.get(url2).json()["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["Driver"]["familyName"]
    
    return constructor_name, full_name


def get_current_season():
    url = "http://ergast.com/api/f1/current/last/results.json"
    location = requests.get(url).json()["MRData"]["RaceTable"]["Races"][0]["Circuit"]["circuitName"]
    name = requests.get(url).json()['MRData']['RaceTable']['Races'][0]['Results'][0]['Driver']['givenName']
    full_name = name + ' ' + requests.get(url).json()['MRData']['RaceTable']['Races'][0]['Results'][0]['Driver']['familyName']

    return full_name, location


def get_driver_standings(year):
    url = "http://ergast.com/api/f1/{0}/driverStandings.json?limit=1000".format(year)
    json_data = requests.get(url).json()
    return json_data


def get_driver_standings_round(year, round):
    url = "http://ergast.com/api/f1/{0}/{1}/driverStandings.json?limit=1000".format(year, round)
    json_data = requests.get(url).json()
    return json_data


def get_constructor_standings(year):
    url = "http://ergast.com/api/f1/{0}/constructorStandings.json?limit=1000".format(year)
    json_data = requests.get(url).json()
    return json_data


def get_constructor_standings_round(year, round):
    url = "http://ergast.com/api/f1/{0}/{1}/constructorStandings.json?limit=1000".format(year, round)
    json_data = requests.get(url).json()
    return json_data


def get_driver(year, round, driver):
    url = "http://ergast.com/api/f1/{0}/{1}/drivers/{2}/results.json?limit=1000".format(year, round, driver)
    json_data = requests.get(url).json()
    return json_data


def get_constructor(year, round, constructor):
    url = "http://ergast.com/api/f1/{0}/{1}/constructors/{2}/results.json?limit=1000".format(year, round, constructor)
    json_data = requests.get(url).json()
    return json_data


def get_circuit(year, round, circuit):
    url = "http://ergast.com/api/f1/{0}/{1}/circuits/{2}/results.json?limit=1000".format(year, round, circuit)
    json_data = requests.get(url).json()
    return json_data



# Debugging Playground: 
#############################################################################################################


# recent_api ="http://ergast.com/api/f1/current/last/results"
# season_api = "http://ergast.com/api/f1/{1}/{2}/results.json?limit=1000"

# year = str(2022)
# round = str(4)

# # year = input('Enter the season year (or current: ')
# # round = input('Enter the round (or say \'last\'): ')

# url = season_api.replace('{1}', year)
# url = url.replace('{2}', round)

# season_api = "http://ergast.com/api/f1/2022/results.json?limit=1000"

# json_data = requests.get(season_api).json()

# print(json_data)

# print(get_season(2022))

# url = "http://ergast.com/api/f1/2022/constructorStandings.json?limit=1000"
# name = requests.get(url).json()["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"][0]["Constructor"]["name"]

# url2 = "https://ergast.com/api/f1/2022/driverStandings.json?limit=1000"
# name = requests.get(url2).json()["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["Driver"]["givenName"]
# full_name = name + ' ' + requests.get(url2).json()["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["Driver"]["familyName"]
# print(full_name)


# year = "who won the 2022 season?"
# year = [int(i) for i in year.split() if i.isdigit()]
# # print(year)
# year1 = ''.join(map(str, year))
# print(year1)
# constructor, driver = get_season(year1)
# print(constructor, driver)
# # dispatcher.utter_season_info('utter_season_info', tracker, year=year1, driver=driver, constructor=constructor)

# url = "http://ergast.com/api/f1/current/last/results.json"
# location = requests.get(url).json()["MRData"]["RaceTable"]["Races"][0]["Circuit"]["circuitName"]
# name = requests.get(url).json()['MRData']['RaceTable']['Races'][0]['Results'][0]['Driver']['givenName']
# full_name = name + ' ' + requests.get(url).json()['MRData']['RaceTable']['Races'][0]['Results'][0]['Driver']['familyName']

# print(location, full_name)