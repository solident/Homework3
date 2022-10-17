#required stuffs
import os
import csv
#path to csv file
datapath = os.path.join('Resources', "election_data.csv")

candidate = []
percent_votes = []
numvotes = []



# votes
totalvote = 0

# Read csv 
with open(datapath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        # Add to our counter
        totalvote += 1
        if row[2] not in candidate:
            candidate.append(row[2])
            index = candidate.index(row[2])
            numvotes.append(1)
        else:
            index = candidate.index(row[2])
            numvotes[index] += 1
    # Add to percent_votes list
    for votes in numvotes:
        percentage = (votes/totalvote) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

    # Find the winning candidate
    winner = max(numvotes)
    index = numvotes.index(winner)
    winningcandidate = candidate[index]

# printing the output
print("Election Results\n")
print("------------------------\n")
print(f"Total Votes: {str(totalvote)}")
print("------------------------\n")
for i in range(len(candidate)):
    print(f"{candidate[i]}: {str(percent_votes[i])} ({str(numvotes[i])})")
print("------------------------\n")
print(f"Winner: {winningcandidate}")
print("------------------------\n")

# Exporting to text file


output_file = os.path.join('Analysis', 'pyPollresult.txt')

pyPollresult = open(output_file, "w")

line1 = "Election Results\n"
line2 = "------------------------\n"
line3 = str(f"Total Votes: {str(totalvote)}")
line4 = str("------------------------\n")
pyPollresult.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidate)):
    line = str(
        f"{candidate[i]}: {str(percent_votes[i])} ({str(numvotes[i])})")
    pyPollresult.write('{}\n'.format(line))
line5 = "------------------------\n"
line6 = str(f"Winner: {winningcandidate}")
line7 = "------------------------\n"
pyPollresult.write('{}\n{}\n{}\n'.format(line5, line6, line7))