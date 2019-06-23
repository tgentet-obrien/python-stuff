import sys

# Calculate the age of a dog in dog years, from human years
def dog(age):
    # Parse age as a float
    age = float(age)
    total = 0

    # If the age is greater than or equal to 2
    if age > 2:
        # Calculate age - 2, multiplied by 2, then add 21
        total = (age - 2) * 4 + 21
    # Else if the age is greater than 0
    elif age > 0:
        # Calculate the age divided by 21 multiplied by 100 to calculate the rough age
        total = round((age / 2) * 21, 1)
    else:
        print("Don't be silly, dogs cannot be 0")

    # Prep age in years
    age = str(int(total)) + " years"

    # Calculate the amount of months by getting everything after the decimal and dividing it by 1/12
    months = float(str(total - int(total))[1:]) / (1.0/12.0)

    # If months is greater than 0
    if months > 0:
        # Add the amount of months to the age
        age += " and " + str(int(months)) + " months"

    # Print the age
    print(age)

def main(argv):
    if argv[0] in ("-a", "--age"):
        dog(argv[1])

if __name__ == "__main__":
   main(sys.argv[1:])