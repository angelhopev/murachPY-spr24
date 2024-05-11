def calculate_batting_average(hits, at_bats):
    return round(hits / at_bats, 3)

def main():
    print("=" * 64)
    print("Baseball Team Manager".center(64))
    print()
    print("This program calculates the batting average for a player based")
    print("on the player's official number of at bats and hits.")
    print("=" * 64)
    
    print()
    player_name = input("Player's name: ")
    at_bats = int(input("Official number of at bats: "))
    hits = int(input("Number of hits: "))

    batting_average = calculate_batting_average(hits, at_bats)
    
    print()
    print(f"{player_name}'s batting average is {batting_average}")

if __name__ == "__main__":
    main()
