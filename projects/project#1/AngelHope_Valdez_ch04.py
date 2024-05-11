def display_separator():
    print("=" * 64)

def display_title():
    display_separator()
    print("Baseball Team Manager".center(64))
    print("MENU OPTIONS")
    print("1 – Calculate batting average")
    print("2 - Exit program")
    display_separator()

def display_menu():
    return input("Menu option: ")

def calculate_batting_average():
    print("Calculate batting average...")
    at_bats = int(input("Official number of at bats: "))
    hits = int(input("Number of hits: "))
    return round(hits / at_bats, 3)

def main():
    display_title()
    while True:
        menu_option = display_menu()

        if menu_option == '1':
            batting_average = calculate_batting_average()
            print(f"Batting average: {batting_average}")
            print()
        elif menu_option == '2':
            print("Bye!")
            break
        else:
            print("Not a valid option. Please try again.")
            print()

if __name__ == "__main__":
    main()
