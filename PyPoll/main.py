#import os and csv
import os
import csv

#assign csv file to path
# poll_csv = os.path.join('Resources', 'election_data.csv')

#define variables
# total_votes = 0
# candidate_name = []
# #d = {candidate, count of votes} ------ d. values -> list of values in a dict.
# d = {}
# with open(poll_csv) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     header = next(csvreader)

#     for row in csvreader:

#         total_votes += 1
#         #Will not neet line 21 when replacing 'khan' w/ variable for candidate
#         # if row[2] == candidate_name:
#         #     if cadidate_name in d.keys():
#         #         d[candidate_name] += 1
#         #     if candidate_name not in d.keys():
#         #         d[candidate_name] = 1

# print(d)

total_vote = 0
candidates = {}
poll_csv = os.path.join('Resources', 'election_data.csv')
with open(poll_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        total_vote += 1
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.update({candidate_name : 1})
        else:
            candidates[candidate_name] = candidates[candidate_name] + 1 

    print(candidates)


        