


#The total number of votes cast

#A complete list of candidates who received votes

#the percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote


import os
import csv

csvpath = '/Users/keesunghahm/Documents/Homework/python-challenge/PyPoll/Resources/election_data.csv'
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)  # Skip the header row

    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------")

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")

        if votes > max_votes:
            max_votes = votes
            winner = candidate

    print("--------------------------")
    print(f"Winner: {winner}")
    print("--------------------------")

    # Create the analysis directory if it doesn't exist
    analysis_dir = os.path.join(os.path.dirname(__file__), 'analysis')
    os.makedirs(analysis_dir, exist_ok=True)

    # Create the text file and write the output
    textpath = os.path.join(analysis_dir, 'election_analysis.txt')
    with open(textpath, "w") as textfile:
        textfile.write("Election Results\n")
        textfile.write("--------------------------\n")
        textfile.write(f"Total Votes: {total_votes}\n")
        textfile.write("---------------------------\n")

        for candidate, votes in candidates.items():
            percentage = (votes / total_votes) * 100
            textfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        textfile.write("--------------------------\n")
        textfile.write(f"Winner: {winner}\n")
        textfile.write("--------------------------\n")

print("Text file created successfully.")