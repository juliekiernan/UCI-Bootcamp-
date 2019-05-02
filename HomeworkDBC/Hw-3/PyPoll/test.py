import os
import csv

PyPollPath = os.path.join('..', "PyPoll", "PyPoll_HW2.csv")
#define variables
candidate = []
per_votes = []
cand_votes = []

# Candidate Options and Vote Counters
total_votes = 0
candidate_options = []
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

with open(PyPollPath, newline="") as PyPollData:
    pollreader = csv.reader(PyPollData, delimiter=",")
    # Read each row of data after the header
    pollheader = next(pollreader)
    for row in pollreader:
        # track vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate = row[""]

        # get list of candidates
        if candidate not in candidate_options:
            # Add it to the list of candidates in the running
            candidate_options.append(candidate)

            # Tracking candidate voter count
            cand_votes[candidate] = 0

        # Then add a vote to that candidate's count
        cand_votes[candidate] = cand_votes[candidate] + 1
    # Determine the winner
    for candidate in cand_votes:

        # Retrieve vote count and percentage
        votes = cand_votes.get(candidate)
        per_votes = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

# Display results
print("Election Results")
print("----------")
print(f'Total Votes: {str(total_votes)}')
print("----------")
for i in range(len(candidate)):
    print(f'{candidate[i]}: {str(percent_votes[i])} ({str(cand_votes[i])})')
print("----------")
print(f'Winner: {winner}')
print("----------")

# Export to .txt file
output = open("output.txt", "w")

output.write("Election Results" '\n')
output.write("---------------------" '\n')
output.write(f"Total Votes: {str(total_votes)}" '\n')
output.write("---------------------" '\n')
for i in range(len(candidate)):
    output.write(f'{candidate[i]}: {str(percent_votes[i])} ({str(cand_votes[i])})' '\n')
output.write("---------------------" '\n')
output.write(f"Winner: {winner}" '\n')
