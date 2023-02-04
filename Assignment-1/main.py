# Abdullah Hasani
# ahh190004
# NLP HW 1

# assumes sysarg is data/data.csv
import sys  # to get the system parameter
import os  # used by method 1
import re  # for regex
import pickle  # for pickling


# Defines Person class w/ 5 params describing an employee
class Person:
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    def display(self):
        print("\nEmployee ID: " + self.id)
        print('\t\t' + self.first + ' ' + self.mi + ' ' + self.last)
        print('\t\t' + self.phone)


# readfile takes param for filepath
def readfile(filepath):
    # Open and read CSV file
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        text_in = f.read()
    print("\nThe current file reads:")
    print(text_in)  # Output file contents
    return text_in


# processing takes raw text returned from readfile in param
def processing(contents):
    people = {}  # init dict of people

    # regex for ID and phone number format
    ID_REGEX = '^[A-Z]{2}\d{4}$'
    PHONE_REGEX = '^\d{3}-\d{3}-\d{4}$'

    # Text processing
    split = contents.split('\n')  # split by newline char
    split.pop(0)  # remove header

    # Text clean up
    formatted = []
    for line in split:
        parts = line.split(',')
        parts[0] = parts[0].title()  # First name
        parts[1] = parts[1].title()  # Last name
        if parts[2] == '':
            parts[2] = 'X'
        parts[2] = parts[2].upper()  # Middle initial (Or 'X')

        # use regex for ID
        idmatch = re.match(ID_REGEX, parts[3])
        while not idmatch:
            print("ID invalid: " + parts[3])
            print("ID is two letters followed by 4 digits")
            parts[3] = input("Please enter a valid id: ")
            idmatch = re.match(ID_REGEX, parts[3])

        # use regex for phone
        phonematch = re.match(PHONE_REGEX, parts[4])
        phone = ''
        if not phonematch:
            for i in parts[4]:
                if i.isdigit():
                    phone = phone + i
        parts[4] = phone[:3] + '-' + phone[3:6] + '-' + phone[6:]
        formatted.append(parts)

        # create a Person object and save object to dict of persons
        person = Person(parts[0], parts[1], parts[2], parts[3], parts[4])
        if parts[3] in people:  # Check for duplicate id
            print("Error: Duplicate ID found.")
        else:
            people[parts[3]] = person
    return people


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
    else:
        filepath = sys.argv[1]
        print("The file path is " + filepath)
        contents = readfile(filepath)
        people_dict = processing(contents)

        with open("persons.pickle", "wb") as file:
            pickle.dump(people_dict, file)  # save the dictionary as a pickle file.

        with open("persons.pickle", "rb") as file:
            people_dict = pickle.load(file)  # open pickle file for read
            print("\n\nEmployee list:")
            for person in people_dict.values():
                person.display()  # print each person using the Person display() method
