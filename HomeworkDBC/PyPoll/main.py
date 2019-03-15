import os
import csv

PyPollPath = os.path.join('..', "PyPoll", "PyPoll_HW2.csv")
#define variables
candidates = []
num_votes = []
per_votes = []
total_votes = 0

with open(PyPollPath, newline="") as PyPollData:
    pollreader = csv.reader(PyPollData, delimiter=",")
    # Read each row of data after the header
    pollheader = next(pollreader)

    # Read first row (track changes; if candidate is not on list, add name, otherwise add to existing name)
    for row in pollreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1

    # Add to percent_votes list 
    for votes in num_votes:
        percent = (votes/total_votes) * 100
        # percentage = round(percent)
        percent = "%.3f" % percent
        per_votes.append(percent)

        # Find the winner
        winner = max(num_votes)
        index = num_votes.index(winner)
        winning_candidate = candidates[index]

#Display results
print("Election Results")
print("----------")
print(f"Total Votes: {str(total_votes)}")
print("----------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(per_votes[i])} ({str(num_votes[i])})")
print("----------")
print(f"Winner: {winning_candidate}")
print("----------")

# Display/Export to .txt file
output = open("output.txt", "w")

output.write("Election Results" '\n')
output.write("---------------------" '\n')
output.write(f"Total Votes: {str(total_votes)}" '\n')
output.write("---------------------" '\n')
for i in range(len(candidates)):
    output.write(f"{candidates[i]}: {str(per_votes[i])} ({str(num_votes[i])})" '\n')
output.write("---------------------" '\n')
output.write(f"Winner: {winning_candidate}" '\n')

