# Luhn Algorithm Credit Card Validator
# Partner Name: Robert Del Papa
# Partner Login ID: rdelpapa
#
# Course Name: COSC 1423
#
# Description:
# This program checks if a user-entered 15 or 16-digit credit card number is valid
# using the Luhn algorithm (a checksum formula used to validate credit card numbers).
# It also identifies the type of credit card (e.g., Visa, MasterCard, American Express)
# based on the first few digits of the card number.
#
# Date Created: 10/12/2022
# Date Last Modified: 10/20/2022

# Function to check if a credit card number is valid using the Luhn algorithm
def is_valid(cc_num):
    total = 0  # Store the sum for validation
    length = len(cc_num)  # Get length of the card number
    reverse = cc_num[::-1]  # Reverse the digits for easier processing

    # Loop through each digit in the reversed list
    for i in range(length):
        digit = reverse[i]
        # Double every second digit (i.e., odd indices in reversed list)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:  # Subtract 9 if the result is two digits
                digit -= 9
        total += digit  # Add digit to total sum

    # Card is valid if total modulo 10 is zero
    return total % 10 == 0

# Function to identify the type of credit card based on starting digits
def cc_type(cc_num):
    cctype = "Unknown"  # Default type

    # Ensure there are at least two digits to check
    if len(cc_num) < 2:
        return cctype

    d1 = cc_num[0]  # First digit
    d2 = cc_num[1]  # Second digit

    # Check card type based on known starting digit patterns
    if d1 == 1:
        cctype = "Airlines"
    elif d1 == 2:
        cctype = "Airlines and future industry assignments"
    elif d1 == 3:
        if d2 == 4 or d2 == 7:
            cctype = "American Express"
        else:
            cctype = "Travel, entertainment, banking / financial"
    elif d1 == 4:
        cctype = "Visa"
    elif d1 == 5:
        if 0 <= d2 <= 5:
            cctype = "MasterCard"
        else:
            cctype = "Banking and financial"
    elif d1 == 6:
        if len(cc_num) > 3 and d2 == 0 and cc_num[2] == 1 and cc_num[3] == 1:
            cctype = "Discover"
        elif d2 == 4 and cc_num[2] == 4:
            cctype = "Discover"
        elif d2 == 5:
            cctype = "Discover"
        else:
            cctype = "Banking and retail"
    elif d1 == 7:
        cctype = "Petroleum and other future industry assignments"
    elif d1 == 8:
        cctype = "Healthcare, telecommunications, and future industry assignments"
    elif d1 == 9:
        cctype = "National assignment"

    return cctype

# Main loop of the program
def main():
    while True:
        # Ask user to enter a credit card number
        credit_card = input("Enter 15 or 16 digit credit card number: ").strip()

        # Check if input is all digits and of correct length
        if credit_card.isdigit() and 15 <= len(credit_card) <= 16:
            cc_num = [int(digit) for digit in credit_card]  # Convert input into list of integers

            # Check validity using Luhn algorithm
            if is_valid(cc_num):
                print(f"Valid {cc_type(cc_num)} credit card number")
            else:
                print("Invalid credit card number")
        else:
            print("Error: Please enter a 15 or 16 digit number.")
            break  # Exit if format is incorrect

        # Ask user if they want to validate another card
        cont = input("Do you want to continue (y/n): ").strip().lower()
        if cont != 'y':
            break  # Exit loop if user doesn't want to continue

# Run the program
if __name__ == "__main__":
    main()
