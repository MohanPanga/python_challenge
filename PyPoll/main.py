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
    
with open('Analysis/output.txt','w') as out_handle:
    out_handle.write('Election Results \n')
    out_handle.write('---------------------------------------------\n')
    print('---------------------------------------------')
    print('Election Results')
    print('---------------------------------------------')
    out_handle.write(f'Total Votes: {Total_votes}\n')
    print(f'Total Votes: {Total_votes}')
    print('---------------------------------')
    for candidate in candidates:
        indx1 = candidates.index(candidate)
        print(f'{candidate} : {round(candidate_votes[indx1]/Total_votes*100,5)}% ({candidate_votes[indx1]})')
        out_handle.write(f'{candidate} : {round(candidate_votes[indx1]/Total_votes*100,5)}% ({candidate_votes[indx1]})\n')
    winner_votes = max(candidate_votes)
    indx2 = candidate_votes.index(winner_votes)
    winner = candidates[indx2]
    print('---------------------------------')
    print(f'winner: {winner}')
    out_handle.write('---------------------------------\n')
    out_handle.write(f'winner: {winner}')
    print('---------------------------------')


    
