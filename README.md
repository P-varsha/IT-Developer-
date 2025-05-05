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

** TASK-3 ATM INTERFACE **

Explanation:

BankAccount Class:
__init__(self, account_number, pin, balance=0): Initializes the account with an account number, PIN, and initial balance (defaulting to 0).
withdraw(self, amount):
Checks if the withdrawal amount is positive and not exceeding the current balance.
If valid, deducts the amount from the balance and displays a success message with the remaining balance.
Returns True if the withdrawal is successful, False otherwise.
Handles cases of invalid or insufficient amounts.
deposit(self, amount):
Checks if the deposit amount is positive.
If valid, adds the amount to the balance and displays a success message with the new balance.
Returns True if the deposit is successful, False otherwise.
Handles cases of invalid amounts.
check_balance(self): Displays the current account balance.
verify_pin(self, entered_pin): Compares the entered PIN with the account's PIN and returns True if they match, False otherwise.
ATM Class:
__init__(self, account): Initializes the ATM with a BankAccount object, establishing the connection.
display_menu(self): Prints the ATM menu options to the user.
run(self):
Greets the user and implements a PIN verification process with a maximum of 3 attempts. If the PIN is incorrect after 3 tries, the ATM session ends.
Enters a loop to continuously display the menu and process user choices until the user chooses to exit.
Withdrawal (Choice '1'): Prompts for the withdrawal amount, validates the input as a positive number, and calls the withdraw() method of the BankAccount object.
Deposit (Choice '2'): Prompts for the deposit amount, validates the input as a positive number, and calls the deposit() method of the BankAccount object.
Check Balance (Choice '3'): Calls the check_balance() method of the BankAccount object.
Exit (Choice '4'): Prints a thank you message and breaks out of the loop.
Handles invalid menu choices.
if __name__ == "__main__": block:
Creates a sample BankAccount instance for a user.
Creates an ATM instance, passing the user_account to connect it to the account.
Calls the run() method of the ATM object to start the ATM interface.

