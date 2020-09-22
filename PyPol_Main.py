# Py Poll
# I met w/ my tutor on Monday 9/22 at 12:00 Noon.  Very helpful.
# Output file added.


# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "election_data.csv")

# Title
print("")
print("Election Results")
print("")
print("-----------------------------")
Candidate_Votes = {}
Candidate_List = []
Total_Votes = 0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        Total_Votes = Total_Votes+1
        if row[2] not in Candidate_List:
           Candidate_List.append(row[2])
           Candidate_Votes[row[2]] = 1
        else:
            Candidate_Votes[row[2]] += 1

    print ("Total Votes: ",Total_Votes)
    Winner = ""
    WinningVotes = 0
    for candidate in Candidate_List:
        print(f"{candidate}:{round(Candidate_Votes[candidate]/Total_Votes*100,2)}% ({Candidate_Votes[candidate]})")
        if Candidate_Votes[candidate]>WinningVotes:
            Winner=candidate
            WinningVotes=Candidate_Votes[candidate]
    print ("-----------------------------")
    print(f"Winner: {Winner}")



    # print (Candidate_Votes)
    
print ("-----------------------------")

output_path = os.path.join("..", "Resources", "newpoll.csv")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    csvwriter.writerow(["Election Results"])   

    csvwriter.writerow(["Total Votes:"])
    csvwriter.writerow([(Total_Votes)])

    csvwriter.writerow(["Results:"])
    csvwriter.writerow([(f"{candidate}:{round(Candidate_Votes[candidate]/Total_Votes*100,2)}% ({Candidate_Votes[candidate]})")])
    
    csvwriter.writerow(["Winner:"])
    csvwriter.writerow({Winner})

