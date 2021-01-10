#import os and csv
import os
import csv

#assign csv file to path
poll_csv = os.path.join('Resources', 'election_data.csv')

#define variables
total_votes = 0

#d = {candidate, count of votes} ------ d. values -> list of values in a dict.
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    

    for row in csvreader:
        total_votes += 1

        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    print("Election Results:")
    print("-------------------------------")
    print("Total Votes: ", total_votes)
    print("-------------------------------")

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percent = float(votes)/float(total_votes)*100
    
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percent:.3f}% ({votes})\n"
        print(voter_output, end="")

    print("-------------------------------")
    print("Winner: ", winning_candidate)

with open('analysis/election_results.txt', 'w', newline='') as textfile:
    writer = csv.writer(textfile)
    writer.writerow(["Election Results:"])
    writer.writerow(["-------------------------------"])
    writer.writerow(["Total Votes: " + str(total_votes)])    
    writer.writerow(["-------------------------------"])
    writer.writerow([candidate_votes])
    writer.writerow(["-------------------------------"])
    writer.writerow(["Winner: " + winning_candidate])
    


