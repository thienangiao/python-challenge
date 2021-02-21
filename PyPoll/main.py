# PyPoll: To analyze poll data

import os
import csv

# Relative file location
input_file = os.path.join("Resources", "election_data.csv")

# Open and read budget_data
with open(input_file) as input_data:
    csv_reader = csv.reader(input_data, delimiter=",")

    # Store the header row
    csv_header = next(input_data)

    
    CandidateList = []
    CandidateVotes = []
    Total_votes = 0


    for row in csv_reader:
        for i in range(len(CandidateList)):

            # Count votes for each candidate
            if row[2]==CandidateList[i]:
                CandidateVotes[i]=CandidateVotes[i]+1

        # Count votes
        Total_votes = Total_votes +1 

        # Create unique candidate name list
        if row[2] not in CandidateList:
            CandidateList.append(row[2])
            # Add 1 vote to each candidate as the name is appended to CandidateList
            CandidateVotes.append(1)


CandidatePct = []

for j in range(len(CandidateList)):
    CandidatePct.append("{:.0%}".format(CandidateVotes[j]/Total_votes))

print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_votes}")
print("-------------------------")
print(f"{CandidateList[0]}: {CandidatePct[0]} ({CandidateVotes[0]})")
print(f"{CandidateList[1]}: {CandidatePct[1]} ({CandidateVotes[1]})")
print(f"{CandidateList[2]}: {CandidatePct[2]} ({CandidateVotes[2]})")
print(f"{CandidateList[3]}: {CandidatePct[3]} ({CandidateVotes[3]})")
print("-------------------------")
print("Winner: "+CandidateList[CandidateVotes.index(max(CandidateVotes))])
print("-------------------------")

# Specify the file to write to
output_file = os.path.join("analysis", "result.txt")

# Open the file using "write" mode.
with open(output_file, 'w') as txtfile:

    # Write text to file
    txtfile.write("Election Results")
    txtfile.write("\n")
    txtfile.write("-------------------------")
    txtfile.write("\n")
    txtfile.write(f"Total Votes: {Total_votes}")
    txtfile.write("\n")
    txtfile.write("-------------------------")
    txtfile.write("\n")
    txtfile.write(f"{CandidateList[0]}: {CandidatePct[0]} ({CandidateVotes[0]})")
    txtfile.write("\n")
    txtfile.write(f"{CandidateList[1]}: {CandidatePct[1]} ({CandidateVotes[1]})")
    txtfile.write("\n")
    txtfile.write(f"{CandidateList[2]}: {CandidatePct[2]} ({CandidateVotes[2]})")
    txtfile.write("\n")
    txtfile.write(f"{CandidateList[3]}: {CandidatePct[3]} ({CandidateVotes[3]})")
    txtfile.write("\n")
    txtfile.write("-------------------------")
    txtfile.write("\n")    
    txtfile.write("Winner: "+CandidateList[CandidateVotes.index(max(CandidateVotes))])  
    txtfile.write("\n")
    txtfile.write("-------------------------")

print("Result output to /PyPoll/analysis/result.txt")