# Import dependencies
import csv
import os

# Assign a variable to election_resulsts.csv's path
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to election_analysis.txt's (new file) path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Create list to store candidates and counties
candidate_options = []
counties = []

# Create dictionary to store cadidates (key) and candidate vote totals (value)
candidate_votes = {}

# Create dictionary to store counties (key) and county votes (value)
county_votes = {}

# Create variables to store the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Create variables to store county with most votes and number of votes
county_most_votes = ""
county_most_votes_num = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Create a csv reader object
    file_reader = csv.reader(election_data)
    
    # save the first row as headers
    headers = next(file_reader)
    
    # Loop through each row in the CSV file
    for row in file_reader:
        # Determine to the total vote count (count the number of loops)
        total_votes += 1
        
        # Get the candidate name from each row
        candidate_name = row[2]

        # Get the county name from each row
        county_name = row[1]

        # If the candidate does not match any existing candidate, add to
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            
            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # If the county does not match any existing county, add to
        # the county list.
        if county_name not in counties:
            # Add the county name to the county list
            counties.append(county_name)
            
            # And begin tracking that county's voter count
            county_votes[county_name] = 0
        
        # Add a vote to that county's count
        county_votes[county_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Format election result text
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\n"
        f"County Votes:\n")
    
    # Print the final vote count to the terminal
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Loop through counties
    for county in county_votes:
        # Retrieve vote count and percentage
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # save formatted county vote results
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each county's voter count and percentage to the terminal
        print(county_results)

        # Save the county results to the text file
        txt_file.write(county_results)

        # Determine county with most votes
        # Cycle through each county's vote total and keep the largest
        if (votes > county_most_votes_num):
            county_most_votes_num = votes
            county_most_votes = county

    # Print the county with the most votes to the terminal
    county_votes_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {county_most_votes}\n"
        f"-------------------------\n")
    print(county_votes_summary)

    # Save the county with most votes results to the text file
    txt_file.write(county_votes_summary)

    # Loop through candidates
    for candidate in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Save formatted candidate vote results
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        
        #  Save the candidate results to the text file
        txt_file.write(candidate_results)
        
        # Determine winning vote count, winning percentage, and winning candidate
        # Cycle through each candidate's vote total and keep the largest
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)