def display_separator():
    print("=" * 64)

def display_title():
    display_separator()
    print("Baseball Team Manager".center(64))
    print("MENU OPTIONS")
    print("1 – Display lineup")
    print("2 – Add player")
    print("3 – Remove player")
    print("4 – Move player")
    print("5 – Edit player position")
    print("6 – Edit player stats")
    print("7 - Exit program")
    print()
    print("POSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    display_separator()

def display_menu():
    return input("Menu option: ")

def display_lineup(lineup):
    print("{:<6} {:<10} {:<4} {:<4} {:<5} {:<5}".format("", "Player", "POS", "AB", "H", "AVG"))
    print("-" * 45)
    for index, player in enumerate(lineup, start=1):
        name, position, at_bats, hits = player
        average = round(hits / at_bats, 3) if at_bats != 0 else 0
        print(f"{index:<6} {name:<10} {position:<4} {at_bats:<4} {hits:<4} {average:<5}")

def add_player(lineup, positions):
    name = input("Name: ")
    position = input("Position: ").upper()
    while position not in positions:
        print("Invalid position. Try again.")
        print("POSITIONS")
        print(", ".join(positions))
        position = input("Position: ").upper()
    at_bats = int(input("At bats: "))
    hits = int(input("Hits: "))
    lineup.append([name, position, at_bats, hits])
    print(f"{name} was added.")

def remove_player(lineup):
    index = int(input("Lineup number: ")) - 1
    if 0 <= index < len(lineup):
        del lineup[index]
        print("Player removed.")
    else:
        print("Invalid lineup number.")

def move_player(lineup):
    current_index = int(input("Current lineup number: ")) - 1
    new_index = int(input("New lineup number: ")) - 1
    if 0 <= current_index < len(lineup) and 0 <= new_index < len(lineup):
        player = lineup.pop(current_index)
        lineup.insert(new_index, player)
        print(f"{player[0]} was moved.")
    else:
        print("Invalid lineup numbers.")

def edit_player_position(lineup, positions):
    index = int(input("Lineup number: ")) - 1
    if 0 <= index < len(lineup):
        position = input("New position: ").upper()
        while position not in positions:
            print("Invalid position. Try again.")
            print("POSITIONS")
            print(", ".join(positions))
            position = input("New position: ").upper()
        lineup[index][1] = position
        print(f"{lineup[index][0]}'s position updated.")
    else:
        print("Invalid lineup number.")

def edit_player_stats(lineup):
    index = int(input("Lineup number: ")) - 1
    if 0 <= index < len(lineup):
        name, position, at_bats, hits = lineup[index]
        print(f"You selected {name} AB={at_bats} H={hits}")
        new_at_bats = int(input("At bats: "))
        new_hits = int(input("Hits: "))
        lineup[index][2] = new_at_bats
        lineup[index][3] = new_hits
        print(f"{name} was updated.")
    else:
        print("Invalid lineup number.")

def calculate_batting_average(at_bats, hits):
    if at_bats == 0:
        return 0
    return round(hits / at_bats, 3)

def read_lineup_from_file(filename):
    lineup = []
    with open(filename, 'r') as file:
        for line in file:
            player_data = line.strip().split(',')
            name = player_data[0]
            position = player_data[1]
            at_bats = int(player_data[2])
            hits = int(player_data[3])
            lineup.append([name, position, at_bats, hits])  # Append only four elements
    return lineup

def save_lineup_to_file(filename, lineup):
    with open(filename, 'w') as file:
        for player in lineup:
            name, position, at_bats, hits = player
            file.write(f"{name},{position},{at_bats},{hits}\n")

def main():
    positions = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')
    lineup = read_lineup_from_file('lineup07.txt')

    display_title()
    while True:
        menu_option = display_menu()

        if menu_option == '1':
            display_lineup(lineup)
            print()
        elif menu_option == '2':
            add_player(lineup, positions)
            print()
        elif menu_option == '3':
            remove_player(lineup)
            print()
        elif menu_option == '4':
            move_player(lineup)
            print()
        elif menu_option == '5':
            edit_player_position(lineup, positions)
            print()
        elif menu_option == '6':
            edit_player_stats(lineup)
            print()
        elif menu_option == '7':
            save_lineup_to_file('new_lineup.txt', lineup)  # Save lineup to a new file
            print("Bye!")
            break
        else:
            print("Not a valid option. Please try again.")
            print()

if __name__ == "__main__":
    main()
