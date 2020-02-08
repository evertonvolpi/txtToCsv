import csv

try:
    #  infiles:
    txtBoys = open('2000_BoysNames.txt' , 'rt')
    txtGirls = open('2000_GirlsNames.txt' , 'rt')

    # outfiles:
    csvBoys = open('2000_BoysNames.csv', 'w')
    csvGirls = open('2000_GirlsNames.csv', 'w')

    # function that creates .csv from .txt:
    def csvFromTxt (txtIn, csvOut):
        # csv writer:
        writer = csv.writer(csvOut, lineterminator="\n")
        # .csv header:
        writer.writerow(['First Name']+['Count'])

        # loop that extracts and splits the lines from .txt and include the information in .csv:
        for line in txtIn:
            row = line.split(" ")
            name = row[0]
            number = (row[1])[0:-1]
            writer.writerow([name]+[number])

    # function call
    csvFromTxt(txtBoys, csvBoys)
    csvFromTxt(txtGirls, csvGirls)

    # .txt close
    txtBoys.close()
    txtGirls.close() 
    # .csv close
    csvBoys.close()
    csvGirls.close() 

except:
    print("File .txt wasn't found. Check the source of the file on lines 4 and 5.")  
