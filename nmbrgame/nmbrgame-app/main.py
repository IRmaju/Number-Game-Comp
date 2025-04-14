import streamlit as st
import random

# Title
st.title('Number Guessing Game')

# Game introduction
st.write("Welcome to the Number Guessing Game!")
st.write("I am thinking of a number between 1 and 100.")

# Generate a random number
number_to_guess = random.randint(1, 100)

# Input for user guess
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100)

# Button to check the guess
if st.button("Submit Guess"):
    if user_guess < number_to_guess:
        st.write("Too low! Try again.")
    elif user_guess > number_to_guess:
        st.write("Too high! Try again.")
    else:
        st.write(f"Congratulations! You guessed the right number: {number_to_guess}")
        number_to_guess = random.randint(1, 100)  # Reset the game with a new number
