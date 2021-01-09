#import os and csv
import os
import csv

#assign csv file to path
poll_csv = os.path.join('Resources', 'election_data.csv')

#define variables
total_votes = 0

#d = {candidate, count of votes} ------ d. values -> list of values in a dict.
d = {}
with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:

        total_votes += 1
        #Will not neet line 21 when replacing 'khan' w/ variable for candidate
        if row[2] == 'Khan':
            if 'Khan' in d.keys():
                d['Khan'] += 1
            if 'Khan' not in d.keys():
                d['Khan'] = 1

print(d)

        


        