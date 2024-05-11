import csv

def read_players_from_file(filename):
    players = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            players.append([row[1], row[2], int(row[3]), int(row[4])])
    return players

def write_players_to_file(filename, players):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for index, player in enumerate(players, start=1):
            writer.writerow([index] + player)