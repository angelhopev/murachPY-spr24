def calculate_batting_average(hits, at_bats):
    return round(hits / at_bats, 3)

def main():
    print("=" * 64)
    print("Baseball Team Manager".center(64))
    print("MENU OPTIONS")
    print("1 – Calculate batting average")
    print("2 - Exit program")
    print("=" * 64)

    while True:
        menu_option = input("Menu option: ")

        if menu_option == '1':
            print("Calculate batting average...")
            at_bats = int(input("Official number of at bats: "))
            hits = int(input("Number of hits: "))
            batting_average = calculate_batting_average(hits, at_bats)
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
