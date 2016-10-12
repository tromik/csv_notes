import csv, datetime, uuid, os

temp_file = 'csvnotes.csv'

# Define headers, current datetime
headers=['guid', 'datetime', 'note']
current_time = str(datetime.datetime.now().time().isoformat())

def file_exists(file_name):
    # Function file_exists() confirms that file exists or not
    return os.path.isfile('csvnotes.csv') # Returns TRUE or FALSE

def create_csv(file_name):
    # Function create_csv() creates the file
    file = open(file_name, 'w')
    file.close()

def genguid():
    # Generate GUID
    return uuid.uuid1() # Returns GUID

def write_csv():
    # Function write_csv

    #Check if file exists, if not create it
    if not file_exists(temp_file):
        create_csv(temp_file)

    # Open the CSV
    with open('csvnotes.csv', 'a') as csvfile:
        csvwriter = csv.DictWriter(csvfile, delimiter=',',
                                fieldnames = headers)

        # If file is empty write the headers
        if not os.path.getsize(temp_file) > 0:
            csvwriter.writeheader()

        # Input note text
        note_text = raw_input("Enter note: ")

        # Write note to CSV file
        csvwriter.writerow({'guid': genguid(), 'datetime': current_time, 'note': note_text})

        # Prompt user to enter more notes
        ans = raw_input("Enter another note? ")
        while ans.lower() != 'n':
            note_text = raw_input("Enter note: ")
            csvwriter.writerow({'guid': genguid(), 'datetime': current_time, 'note': note_text})
            ans = raw_input("Enter another note?")

def read_csv():
    with open(temp_file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader.keys()
        for row in reader:
            print(row['guid'], row['datetime'], row['note'])

write_csv()
#read_csv()
