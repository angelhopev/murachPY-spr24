'''
Angel Hope D. Valdez
1 Feb 2024
Exercise 6-1
'''
#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
                # score_total += score
                # counter += 1 
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    total = 0
    for score in scores:
        total += score
    # calculate average score
    average = round(total / len(scores)) # don't forget to round up

    # min and max
    low_score = min(scores)
    high_score = max(scores)

    # median
    median_index = len(scores) // 2
    if len(scores) % 2 == 1:  # odd
        median_score = scores[median_index]
    else:                     # even
        middle1 = scores[median_index]
        middle2 = scores[median_index-1]
        median_score = (middle1 + middle2)/2
        
    # format and display the result
    print()
    print("Total:           ", total)
    print("Number of Scores:", len(scores))
    print("Average Score:   ", average)
    print("Low Score:       ", low_score)
    print("High Score:      ", high_score)
    print("Median Score:    ", median_score)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
