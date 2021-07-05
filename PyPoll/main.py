import os
import csv

election_data = os.path.join('.', 'Resources', 'election_data.csv')

candidates = []
cand_votes = []
percent_votes = []
total_votes= 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    # reading the header
    csv_header = next(csvreader)

    for row in csvreader:
        # adding up the votes
        total_votes +=1

        # if statement to add candidate and vote to list, if already on list, add vote only
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            cand_votes.append(1)
        else:
            index = candidates.index(row[2])
            cand_votes[index] += 1

    # percentage votes
    for votes in cand_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)   

    # and the winner is
    winner = max(cand_votes)
    index = cand_votes.index(winner)
    winning_candidate = candidates[index]

# print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(cand_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# save to text (.txt) file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(cand_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))