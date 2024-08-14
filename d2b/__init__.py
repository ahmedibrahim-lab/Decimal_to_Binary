# Define function
def decimal_to_binary(decimal):
    
    # Check for empty string
    if not decimal:  
        raise ValueError("Input cannot be empty.")
    
    # Check for invalid inputs
    if not all(char in '0123456789' for char in decimal):
        raise ValueError("Input must be a valid number.")
    
    # Initialise variables
    binary_array = []
    decimal = int(decimal)
    
    while decimal > 0:
        remainder = decimal % 2
        binary_array.append(str(remainder))
        decimal = (decimal - remainder) // 2
        
    binary_array.reverse()
    
    binary = ''.join(binary_array)
        
    return binary     
    
def main():
    
    # Get input from user
    decimal = input("Enter the number you want to convert to binary: ")
    print("Number is: " + decimal)

    # Validation loop
    while not all(char in '0123456789' for char in decimal):
        decimal = input("Sorry but that is not a valid input. Please try again: ")

    result = decimal_to_binary(decimal)
    print("Binary sequence is:", result)

if __name__ == '__main__':
    main()
