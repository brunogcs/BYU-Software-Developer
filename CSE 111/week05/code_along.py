import csv
import os

def read_csv(filename):
    csv_list = []
    # Open the CSV file for reading and store a reference
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        student_dict = {}
        for row_list in reader:
            student_dict.update({row_list[0]: row_list[1]})
    return student_dict

def check_id(id, student_dict):
    while True:
        id = input('Find a student name using his ID: ').replace('-', '')
        if not id.isdigit():
            print("Invalid ID Number: must be numeric")
            continue
        if len(id) != 9:
            if len(id) < 9:
                print("Invalid ID Number: too few digits")
            else:
                print("Invalid ID Number: too many digits")
            continue
        break

    name = student_dict.get(id)
    if name:
        print(f"Student Name: {name}")
    else:
        print("No such student")

    print("Goodbye")

def main():
    # absolute path
    path = os.path.dirname(os.path.abspath(__file__))

    # csv
    print("\n\n CSV File in a Dict: \n")
    filename = "students.csv"
    filepath = os.path.join(path, filename)
    student_dict = read_csv(filepath)

    #input and check ID
    check_id(student_dict)

# Call main to start this program.
if __name__ == "__main__":
    main()