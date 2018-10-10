import csv

filename = 'reactfulData.csv'

def openCSV():
    with open('reactfulData.csv', newline = '') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = ' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))

def dictReader():
    with open('reactfulData.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['structpayload_utctimestamp'], row['structpayload_unique_visitor_session_id'], row['structpayload_sessionId'], row['structpayload_objectType'], row['structpayload_objectId'], row['structpayload_sourceType'] )

def dictWriter():
    # with open('reactfulData.csv', mode='r') as infile:
    #     reader = csv.reader(infile)
    #     with open('coors_new.csv', mode='w') as outfile:
    #         writer = csv.writer(outfile)
    #         mydict = dict((rows[0], rows[1]) for rows in reader)

    dict = {'country': '', 'region': '', 'type': '', 'device': '', 'page': '', 'reaction': ''}

def readCSV(filename):
    file = open(filename, "reactfulData.csv")
    reader = csv.reader(file, delimiter=";")

    rownum = 0
    a = []

    for row in reader:
        a.append(row)
        rownum += 1

    file.close()
    return a

def main():
    # openCSV()
    dictReader()
    # readCSV(filename)


main()
