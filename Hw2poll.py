import os
import csv

csvpath = os.path.join('PyPoll/Resources', 'election_data.csv')

#The total number of votes cast, count each row of column ballot id. to count no. of candidate list, iterate each row and adding each name to counting by append function. 

votecast_count = 0
each_candidates_list = []
total_candidate_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader: 

        votecast_count = votecast_count + 1
        total_candidate_list.append(row[2])

        if each_candidates_list.count(row[2]) == 0:
            each_candidates_list.append(row[2])

    
    #Election Results
    #-------------------------
    print("Election Results")
    print("-------------------------")
    
    #Total Votes: 369711
    #-------------------------
    print(f"Total Votes: {votecast_count} " )
    print("-------------------------")

    #Charles Casper Stockham: 23.049% (85213)
    #Diana DeGette: 73.812% (272892)
    #Raymon Anthony Doane: 3.139% (11606)
    #-------------------------    
    #percent calculation= (total ballot count of each candidat/total ballot count)*100
    
    #again to hold the calculated row value, took temporary cell for the previous value until the condition is met in iteration. 
    
    prev_count = 0
    for candidate in each_candidates_list:
        tmpCount = total_candidate_list.count(candidate)

        if(tmpCount > prev_count):
            prev_count = tmpCount
            tmpName = candidate

#round function will roundoff the decimal value
        print(f"{candidate} {round(((total_candidate_list.count(candidate)/votecast_count) * 100), 3)}% ({tmpCount})")
        
    
    print("-------------------------")
    print(f"Winner : {tmpName} ")
    print("-------------------------")
    

    
