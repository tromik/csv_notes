import csv, datetime, uuid, os

def file_exists(file):
    # Function file_exists() confirms that file exists or not
    return os.path.isfile('csvnotes.csv')

headers=['guid', 'datetime', 'note']
current_time = str(datetime.datetime.now().time().isoformat())

def genguid():
    return uuid.uuid1()

def write_csv():

    if file_exists:
        print "File exists!"
    else:
        print "File missing"

    with open('csvnotes.csv', 'a') as csvfile:
        csvwriter = csv.DictWriter(csvfile, delimiter=',',
                                fieldnames = headers)
        text = raw_input("Enter note: ")

        csvwriter.writeheader()
        csvwriter.writerow({'guid': genguid(), 'datetime': current_time, 'note': text})

        ans = raw_input("Enter another note? ")

        while ans.lower() != 'n':
            text = raw_input("Enter note: ")
            csvwriter.writerow({'guid': genguid(), 'datetime': current_time, 'note': text})
            ans = raw_input("Enter another note?")

def read_csv():
    with open('csvnotes.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        reader.keys()
        for row in reader:
            print(row['guid'], row['datetime'], row['note'])

write_csv()
read_csv()
