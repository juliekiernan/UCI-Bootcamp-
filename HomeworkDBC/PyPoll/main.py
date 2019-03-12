import os
import csv

PyPollPath = os.path.join('..', "PyPoll", "PyPoll_HW2.csv")
#define variables
candidates = []
num_votes = []
percent_votes = []
total_votes = 0

with open(PyPollPath, newline="") as PyPollData:
    pollreader = csv.reader(PyPollData, delimiter=",")
    # Read each row of data after the header
    pollheader = next(pollreader)

    for row in pollreader:
        total_votes += 1 # add votes

        # If candidate is not on list, add name to list, otherwise add to existing name
        if row[2] not in candidates: candidates.append(row[2])
        index = candidates.index(row[2])
        num_votes.append(1)
        else:
        index = candidates.index(row[2])
        num_votes[index] += 1

    # Add to percent_votes list 
    for votes in num_votes:
    percentage = (votes/total_votes) * 100
    # percentage = round(percentage)
    percentage = "%.3f%%" % percentage
    percent_votes.append(percentage)

    # Find the winner
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Display results
print("Election Results")
print("----------")
print(f"Total Votes: {str(total_votes)}")
print("----------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("----------")
print(f"Winner: {winning_candidate}")
print("----------")

# Export to .txt file
file_to_output = "output.txt"
