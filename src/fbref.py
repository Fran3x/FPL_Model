import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import time
import csv

class MatchData:
    def __init__(self) -> None:
        self.comp = ""
        self.date = ""
        self.round = ""
        self.data = {}


class PlayerData:
    def __init__(self) -> None:
        self.data = []
        self.base_url = ""
        self.matches_links = []
        self.matches = []
        self.match_stat_set = set()

def get_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    html = response.text
    parsed_html =  BeautifulSoup(html, 'html.parser')
    # print(parsed_html)
    # comments = parsed_html.find_all(string=lambda text: isinstance(text, Comment))
    comments = parsed_html.find_all('table')
    return comments
    # tables = []
    # for c in comments:
    #     print("TABLE")
    #     table_html = BeautifulSoup(c, 'html.parser')
    #     tables = table_html.find_all('table')
    # return tables

def get_table_data(url):
    status_code = 0
    while status_code != 200:
        print("Getting data for: " + url)
        response = requests.get(url)
        status_code = response.status_code
        if status_code != 200:
            time.sleep(5)
    html = response.text
    parsed_html = BeautifulSoup(html, 'html.parser')
    tables = parsed_html.find_all('table')
    return tables[0]

def get_matches_data(player):
    tables = []
    for l in player.matches_links:
        tables += [get_table_data(l)]
    matches = []
    match_stat_set = set()
    for t in tables:
        for row in t.tbody.find_all('tr'):
            data = {}
            class_name = row.get('class')
            if class_name != None and len(class_name) > 0 and 'unused_sub' not in class_name:
                continue
            columns = row.find_all('td') + row.find_all('th')
            for c in columns:
                data_stat = c.get('data-stat')
                match_stat_set.add(data_stat)
                if data_stat in ['date', 'round', 'comp', 'opponent', 'squad']:
                    for i in range(len(c.contents)):
                        a_html = BeautifulSoup(str(c.contents[i]), 'html.parser')
                        a = a_html.find_all('a')
                        if len(a) > 0:
                            if len(a[0].contents) > 0:
                                data[data_stat] = a[0].contents[0]
                elif data_stat == 'match_report':
                    continue
                else:
                    if len(c.contents) == 0:
                        continue
                    data[data_stat] = c.contents[0]
            match = MatchData()
            match.date = data['date']
            match.round = data['round']
            match.comp = data['comp']
            match.data = data
            matches += [match]
    player.matches = matches
    player.match_stat_set = match_stat_set
    
def manual_id(player_name):
    if player_name == "Alejandro Garnacho":
        return "7aa8adfe"
    if player_name == "Noni Madueke":
        return "bf34eebd"
    if player_name == "Stefan Bajcetic":
        return "32e8417f"
    if player_name == "Máximo Perrone":
        return "53552942"
    if player_name == "Ilya Zabarnyi":
        return "88968486"
    if player_name == "Hjalmar Ekdal":
        return "3d554589"
    if player_name == "Jordan Amissah":
        return "50fc4c0a"
    if player_name == "Ashley Phillips":
        return "4f21d3af"
    if player_name == "Facundo Buonanotte":
        return "468a7a91"
    if player_name == "Harrison Ashby":
        return "b391383a"
    if player_name == "Tom McGill":
        return "4eb2d015"
    if player_name == "Yasin Ayari":
        return "f173303a"
    if player_name == "Thomas Cannon":
        return "4506aec5"
    if player_name == "Lewis Hall":
        return "da011f18"
    if player_name == "Ismaila Coulibaly":
        return "d33e3242"
    if player_name == "CJ Egan-Riley":
        return "d313e8ff"
    if player_name == "Hugo Bueno":
        return "bfc3b3a0"
    if player_name == "Joe Hodge":
        return "bd8a5d95"
    if player_name == "Rico Lewis":
        return "b57e066e"
    if player_name == "Tim Iroegbunam":
        return "84c5ceea"
    if player_name == "Hannibal":
        return "ca22ccb0"
    if player_name == "Pelly-Ruddock Mpanzu":
        return "a9b1c319"
    if player_name == "William Osula":
        return "7b355808"
    if player_name == "Aribim Pepple":
        return "94c53a55"
    if player_name == "Joe Taylor":
        return "bfd3801e"
    return None

def get_epl_players():
    tables = get_data("https://fbref.com/en/comps/9/wages/Premier-League-Wages")
    table = tables[1]
    # players = {}
    players = []
    stat_names = set()
    for row in table.tbody.find_all('tr'):
        class_name = row.get('class')
        if class_name != None and len(class_name) > 0:
            continue
        columns = row.find_all('td')
        base_url = ""
        matches_link = ""
        player_id = ""
        stats = {}
        for c in columns:
            data_stat = c.get('data-stat')
            if data_stat == 'player':
                a_html = BeautifulSoup(str(c.contents[0]), 'html.parser')
                a = a_html.find_all('a')
                
                # stat_names.add(data_stat)
                if len(a) > 0:
                    player_name = a[0].contents[0]
                    base_url = "https://fbref.com" + a[0].get('href')
                    link = a[0].get('href')
                    pieces = link.split('/')
                    player_id = pieces[3]
                    # print(player_name)
                    players.append((player_id, player_name))
                else:
                    player_name = c.get_text()
                    player_id = manual_id(player_name)
                    if player_id:
                        players.append((player_id, player_name))
                    else:
                        print("NOT FOUND", player_name)
            else:
                continue
    return players
            

def main():
    players, stats = get_epl_players()

    for id, player in players.items():
        get_matches_data(player)
        with open('data/2021-22/fbref/' + id + '.csv', 'w') as outf:
            writer = csv.DictWriter(outf, fieldnames=list(player.match_stat_set))
            writer.writeheader()
            for match in player.matches:
                writer.writerow(match.data)

    with open('data/2021-22/fbref_overview.csv', 'w') as outf:
        writer = csv.DictWriter(outf, fieldnames=list(stats))
        writer.writeheader()
        for id, player in players.items():
            for data in player.data:
                writer.writerow(data)

if __name__ == '__main__':
    main()