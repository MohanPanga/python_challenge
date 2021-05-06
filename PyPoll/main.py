import os
import csv

# path to the data file
csvpath = os.path.join("Resources","election_data.csv")
print(csvpath)

with open(csvpath,'r') as csvhandle:
    election_data = csv.reader(csvhandle)
    header = next(election_data)
    # initialize total votes and lists for candidates and votes received by each candidate
    # votes received by a candidate will be captured at the same index in candidate_votes
    Total_votes = 0
    candidates =[]
    candidate_votes =[]

    for row in election_data:
        # count total votes casted
        Total_votes+= 1
        # use candidates name on the vote and find index in candidates
        # if the name of the candidate is not in the list an error is generated and name is appended to the list
        # along with name number of votes is append to the candidate_votes list
        try:
            indx = candidates.index(row[2])
        except ValueError:
            candidates.append(row[2])
            candidate_votes.append(1)
        else:
            candidate_votes[indx] += 1
 # writing to output file and terminal   
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


    
