# IT-Developer-
Internship


** TASK-1 NUMBER GAME ** 
Key changes to incorporate scoring:
total_score and rounds_played variables: These are initialized to keep track of the user's overall performance.
Score calculation: Inside the winning condition (else block):
attempts_taken is calculated.
score_this_round is determined. Here, we're giving a higher score for guessing in fewer attempts. The formula max_attempts - attempts_taken + 1 ensures that a correct guess on the first attempt yields the maximum score (max_attempts), and a guess on the last attempt yields a score of 1.
total_score is updated by adding score_this_round.
Displaying the score:
The score for the current round is displayed immediately after a correct guess.
The total_score is shown after each round.
The final score and the number of rounds played are displayed when the user decides to stop playing.
Now, when you run this code, you'll get a score based on how quickly you can guess the number in each round!


