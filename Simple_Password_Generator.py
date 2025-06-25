# Objective: Creating a Simple Password Generator

# Import the secrets module - It's more secure than random module for generating passwords
import secrets 

#Import string module to access pre-built sets of characters (letters, digits, punctuation)
import string

#Function to Generate Password
def generate_password(length: int) -> str:
  """Return a Cryptographically-Secure Random Password."""

  # Combine all allowed character types: Letters (A-Z, a-z), Digits (0-9), and Symbols
  pool= string.ascii_letters + string.digits + string.punctuation

  #Randomly choose 'length' number of characters from the pool and join them together into a string
  return ''.join(secrets.choice(pool) for i in range(length))
  
# Main Function: Where the Program Starts
def main():
  """Runs the Password Generator Interactively."""
  
  #Prints the Title of the Program with Decorative Formatting
  print(". . . . . ╰──╮ Simple Password Generator ╭──╯ . . . . .")



  #Outer Loop: Keeps the program running until the user decides to exit
  while True:
    #Inner Loop: Keep asking for the password length until a valid number is entered
    while True:
      try:
        #Ask the user for the desired length of the password
        length = int (input("\nEnter the Desired Length of the Password: "))
        
        #Make sure the length is at least 4 characters
        if length < 4:
          print("Password Length should be at least 4 Characters.")
        else:
          #Generate and Print the Password if the input is valid
          print("Generated Password:", generate_password(length))
          break # Exit the inner loop and move on to the next step
      except ValueError:
        # If the user enters a non-integer value, print an error message and ask again
       print("Invalid Input. Password must contain at least 4 characters. Please enter a valid number!")

#After generating the password, ask the user if they want to generate another one
    again = input("\nWould you like to Generate Another Password? (Yes 👍 or No 👎): ").lower()
    #If the user doesn't want to generate another password, exit the outer loop and end the program
    if not again.startswith('y'):
      print ("Thank You for Using the Password Generator, GoodBye 👋!")
      break # Exit the outer loop and end the program

#Entry Point: This line ensures the program runs only when the file is executed directly, not when imported as a module
if __name__ == "__main__":
  main()
