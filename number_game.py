import random

def play_number_guessing_game():
    lower_bound = 1
    upper_bound = 100
    max_attempts = 10
    total_score = 0
    rounds_played = 0
    play_again = True

    print("\nWelcome to the Number Guessing Game!")

    while play_again:
        rounds_played += 1
        secret_number = random.randint(lower_bound, upper_bound)
        attempts_left = max_attempts
        print(f"\nRound {rounds_played}: I've picked a number between {lower_bound} and {upper_bound}. Good luck!")

        while attempts_left > 0:
            try:
                guess = int(input(f"Attempt {max_attempts - attempts_left + 1}/{max_attempts}: Enter your guess: "))
            except ValueError:
                print("Invalid input. Please enter a whole number.")
                continue

            attempts_left -= 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                attempts_taken = max_attempts - attempts_left
                score_this_round = max_attempts - attempts_taken + 1 # Higher score for fewer attempts
                total_score += score_this_round
                print(f"Congratulations! You guessed the number {secret_number} in {attempts_taken} attempts.")
                print(f"Score for this round: {score_this_round}")
                break

        if attempts_left == 0:
            print(f"\nYou ran out of attempts! The secret number was {secret_number}.")

        print(f"Your current total score: {total_score}")

        play_again_input = input("Do you want to play another round? (yes/no): ").lower()
        if play_again_input != 'yes':
            play_again = False
            print(f"\nThanks for playing! You played {rounds_played} rounds and your final score is {total_score}.")

if __name__ == "__main__":
    play_number_guessing_game()
