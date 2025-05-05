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


** TASK-2 STUDENT GRADE CALCULATOR **
How this code addresses your requirements:

Input: Take marks obtained (out of 100) in each subject.
The script first prompts the user for the number of subjects.
It then uses a loop to ask for the marks obtained in each subject.
Input validation is included to ensure that the marks entered are within the valid range (0-100) and are numeric.
Calculate Total Marks: Sum up the marks obtained in all subjects.
The sum() function is used to calculate the total_marks from the subject_marks list.
Calculate Average Percentage: Divide the total marks by the total number of subjects to get the average percentage.
The average_percentage is calculated by dividing total_marks by num_subjects. It includes a check to avoid division by zero if the user enters 0 subjects (though the initial prompt should prevent this).
Grade Calculation: Assign grades based on the average percentage achieved.
A series of if-elif-else statements are used to assign a grade based on the following percentage ranges:
90-100: A+
80-89: A
70-79: B
60-69: C
50-59: D
Below 50: F
Display Results: Show the total marks, average percentage, and the corresponding grade to the user.
The script prints the calculated total_marks, average_percentage (formatted to two decimal places), and the assigned grade in a clear "Results" section.

** TASK-3 

