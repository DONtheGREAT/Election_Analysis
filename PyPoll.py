# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path. the file we will be bringing in to read from. We imported the module function needed to read it in Python.
file_to_load = os.path.join("D:/","election_analysis","Resources", "election_results.csv")
# Assign a variable to save the file to a path. this where we will be writing to for our code so that this file can referenced as a txt file in other codes possibly in the future.
file_to_save = os.path.join("D:/","analysis", "election_analysis.txt")

# Initialize a total vote counter. the csv file does not containa column for total votes so you have to define what total votes are. For this file it will be the rows. Go to for row line!
total_votes = 0

# Candidate Options list[], this i where we will list our candidates and make sure they don't repeat themselves. Go to "candidate name not in" line.
candidate_options = []
# Declare the empty dictionary {}
candidate_votes = {}

# Open the election results and read the file. From here on out until we make it back to this margin, the file to load will be read for everything below.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Print the header row.
    headers = next(file_reader)
    
# Print each row in the CSV file. This defines a row as a vote.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

# Print the candidate name from each row. this tells python where to start a list of candidate names.
        candidate_name = row[2]

        # if the candidate does not match any existing candidate. Counts each name into the options list ONCE. 
        if candidate_name not in candidate_options:

            # Add it to the list of candidates. Adds unseen name to the list.
            candidate_options.append(candidate_name)

            # begin tracking that candidates vote count. START counting that names votes.
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidates count. Pulled it one margin to remove it from the if statement. If not it will only count once since the if statement is only counting names once.
        candidate_votes[candidate_name] += 1

# Print the candidate list.
print(candidate_votes)

# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of cnadidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.