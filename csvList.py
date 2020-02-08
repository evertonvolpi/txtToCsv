import csv

try:
    # .csv files
    boysNames = open('2000_BoysNames.csv', 'r')
    girlsNames = open('2000_GirlsNames.csv', 'r')

    # function that reads specific .csv and prints each line in a python list
    def readCsv (csvFile):
        reader = csv.reader(csvFile)
        next(reader,None)
        for row in reader:
            print(row)

    # menu to take input from the user. Objective: choose which .csv file to read and print
    def menu ():
        choice = input("""Choose the file you want to print:
        1. Boys names  |  2. Girls names  |  3. Exit
        > """)

        if (choice == '1'):
            readCsv(boysNames)
            menu()
        elif (choice == '2'):
            readCsv(girlsNames)
            menu()
        elif (choice == '3'):
            print('Goodbye!')
        else:
            print('Invalid value.')
            menu()

    # function call
    menu()

except:
    print("File .txt wasn't found. Check the source of the file on lines 5 and 6.")  




