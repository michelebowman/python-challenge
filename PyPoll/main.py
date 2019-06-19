import os
import csv
from collections import Counter

#Path to collect data from file
pypoll_csv = os.path.join("Resources", "election_data.csv")

#Set variables
cast_votes = []
candidate = []


#open file to use for data
with open(pypoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        #Add cast_votes and candidate data
          cast_votes.append(row[0])
          candidate.append(row[2])
           
total_votes = len(cast_votes)


#Set up counter to count candidate votes
candidate_name = candidate
counter_1 = Counter(candidate_name)

print(f"TotalVotes:  {total_votes}")
print("Election Results")
print("-------------------------") 
print("Total Votes:" + " " + str(total_votes))
print("-------------------------")


#Calculate the % of votes for candidates
percent_list=[]
for key,value in counter_1.items():
  percent_votes =round((value/total_votes)*100, 2)
  percent_list.append(percent_votes)
  print(f"{key}: {(percent_votes):.3f} % ({value})  " )
  
max_value = max(counter_1.values())
max_keys = [k for k, v in counter_1.items() if v == max_value]
print("--------------------------")
print(f"Winner: {max_keys}")
print("--------------------------")


#Write output to txt file
with open ('election_results.txt', 'w') as text:
  text.write("Election Results\n")
  text.write("---------------------------------------\n") 
  text.write("Total Votes:" + " " + str(total_votes) + "\n")
  text.write("---------------------------------------\n")  
  text.write(f'{key}: {(percent_votes):.3f} % ({value})  \n' )
  text.write("---------------------------------------\n")
  text.write("Winner:" + " " + str(max_keys) + "\n") 
  text.write("---------------------------------------\n")    