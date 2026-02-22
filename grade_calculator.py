

def calculate_grade(marks):

    if marks >= 90 and marks <= 100:
        return "A", "Excellent Work!"
    
    elif marks >= 80 and marks <= 89:
        return "B", "Very Good! Keep it up"
    
    elif marks >= 70 and marks <= 79:
        return "C", "Good effort"
    
    elif marks >= 60 and marks <= 69:
        return "D", "You can do better"
    
    else:
        return "F", "Don’t give up! Try again"


name = input("Enter student name: ")


while True:
    try:
        marks = int(input("Enter marks (0-100): "))

        if marks >= 0 and marks <= 100:
            break
        else:
            print("Invalid marks! Please enter between 0 and 100.")

    except ValueError:
        print("Invalid input! Please enter numeric value.")


grade, message = calculate_grade(marks)

print("\nRESULT FOR", name.upper())
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)
