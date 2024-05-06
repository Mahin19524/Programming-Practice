import tkinter as tk
import random
import time

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game"""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    """Play the game with user's choice"""
    global user_score, computer_score
    
    # Disable buttons during the game
    for button in choice_buttons:
        button.config(state=tk.DISABLED)
    
    # Simulate computer's choice with a delay
    computer_choice_label.config(text="Computer's choice: Thinking...")
    root.update()
    time.sleep(1)
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    computer_choice_label.config(text=f"Computer's choice: {computer_choice.capitalize()}")
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=result)
    
    # Update scores
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    update_scores()
    
    # Enable buttons after the game
    for button in choice_buttons:
        button.config(state=tk.NORMAL)
    
    # Check if game is over
    if user_score == max_score or computer_score == max_score:
        end_game()

def update_scores():
    """Update the scores on the GUI"""
    user_score_label.config(text=f"Your score: {user_score}")
    computer_score_label.config(text=f"Computer's score: {computer_score}")

def end_game():
    """Display end of game message"""
    global user_score, computer_score
    if user_score > computer_score:
        winner = "You"
    elif user_score < computer_score:
        winner = "Computer"
    else:
        winner = "It's a tie"
    end_message = f"Game Over!\n\nFinal Scores:\nYour score: {user_score}\nComputer's score: {computer_score}\n\n{winner} wins!"
    result_label.config(text=end_message)
    retry_button.pack()

def reset_game():
    """Reset the game"""
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_scores()
    result_label.config(text="")
    retry_button.pack_forget()

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Define colors
bg_color = "#f0f0f0"
button_color = "#a8a8a8"

# Set window size and background color
root.geometry("400x450")
root.configure(bg=bg_color)

# Initialize scores and max score
user_score = 0
computer_score = 0
max_score = 3

# Create GUI elements
instruction_label = tk.Label(root, text="Select your choice:", font=('Arial', 14), bg=bg_color)
instruction_label.pack(pady=10)

choices_frame = tk.Frame(root, bg=bg_color)
choices_frame.pack()

choice_buttons = []
choices = ['rock', 'paper', 'scissors']
for choice in choices:
    button = tk.Button(choices_frame, text=choice.capitalize(), font=('Arial', 12), bg=button_color,
                       width=10, padx=5, pady=5, command=lambda ch=choice: play_game(ch))
    button.pack(side=tk.LEFT, padx=10)
    choice_buttons.append(button)

result_label = tk.Label(root, text="", font=('Arial', 16), bg=bg_color)
result_label.pack(pady=20)

user_score_label = tk.Label(root, text=f"Your score: {user_score}", font=('Arial', 12), bg=bg_color)
user_score_label.pack()

computer_score_label = tk.Label(root, text=f"Computer's score: {computer_score}", font=('Arial', 12), bg=bg_color)
computer_score_label.pack()

computer_choice_label = tk.Label(root, text="", font=('Arial', 12), bg=bg_color)
computer_choice_label.pack()

retry_button = tk.Button(root, text="Play Again", font=('Arial', 12), bg=button_color, command=reset_game)

# Start the GUI event loop
root.mainloop()
