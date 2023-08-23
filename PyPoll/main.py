import os
import csv

#create paths for csv reader and writer
election_data_path=os.path.join('.','Resources',"election_data.csv")
output_path = os.path.join(".",'analysis',"PyPoll_Analysis.csv")


#open writer to create csv output
with open(output_path,'w') as analysis_csv:
    pypoll_writer = csv.writer(analysis_csv)
    #open reader to read in raw data
    with open(election_data_path,'r') as election_csv:
        election_data = csv.reader(election_csv, delimiter=',')
        #read csv header
        election_header = next(election_data)
        #dimension variables to iterate data
        candidates = []
        i = 0 
        
        #counts number of rows and gets unique candidates
        for rows in election_data:
            i+=1
            if rows[2] not in candidates:
                candidates.append(rows[2])
        #prints out total votes to both terminal and csv file
        print('Election Results')
        print('-------------------------')
        print(f'Total Votes: {i}')
        print('-------------------------')
        print('Election Results',file=analysis_csv)
        print('-------------------------',file=analysis_csv)
        print(f'Total Votes: {i}',file=analysis_csv)
        print('-------------------------',file=analysis_csv)

    #dimension variables to store vote counts for each candidate
        vote_count = 0
        prev = 0
    #default winner, will be overrwritten
        winner = candidates[0]
    
    #loops through each unique candidate, then through raw data file to count votes unique to each candidate
    for candidate in candidates:
        with open(election_data_path,'r') as election_csv:
            election_data = csv.reader(election_csv, delimiter=',')
            election_header = next(election_data)   
            for rows in election_data:
                if rows[2]==candidate:
                    vote_count=vote_count+1
            
            #prints votes and vote % of each candidate to terminal and csv file
            print(f'{candidate}: {round((float(vote_count/i))*100,3)}% ({vote_count})')
            print(f'{candidate}: {round((float(vote_count/i))*100,3)}% ({vote_count})',file=analysis_csv)
            
            #determines winner based on number of votes
            if(vote_count>prev):
                winner = candidate
            prev = vote_count
            vote_count = 0
    
    #prints winner to terminal and csv file
    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')
    print('-------------------------',file=analysis_csv)
    print(f'Winner: {winner}',file=analysis_csv)
    print('-------------------------',file=analysis_csv)

