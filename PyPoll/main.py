import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
print(csvpath)

with open(csvpath,'r') as csvhandle:
    election_data = csv.reader(csvhandle)
    header = next(election_data)
    Total_votes = 0
    candidates =[]
    candidate_votes =[]

    for row in election_data:
        Total_votes+= 1
        try:
            indx = candidates.index(row[2])
        except ValueError:
            candidates.append(row[2])
            candidate_votes.append(1)
        else:
            candidate_votes[indx] += 1
    

print('---------------------------------------------')
print('Election Results')
print('---------------------------------------------')
print(f'Total Votes: {Total_votes}')
for candidate in candidates:
    indx1 = candidates.index(candidate)
    print(f'{candidate} : {round(candidate_votes[indx1]/Total_votes*100,5)}% ({candidate_votes[indx1]})')


