import json
import pandas as pd

def create_table(json_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Extract team names
    teams = list(data.keys())
    
    # Initialize an empty dataFrame
    
    df = pd.DataFrame(index=teams, columns=teams)

    # Populate the matrix with win-loss records
    for team, opponents in data.items():
        for opponent, record in opponents.items():
            # Set the wins (reading across)
            df.at[team, opponent] = record['W']
            # Set the losses (reading down)
            df.at[opponent, team] = record['L']

    # Replace NaN with '--' to represent self-play (which is not applicable)

    df.fillna('--', inplace=True)
    return df

# Example usage:
# Assuming the JSON file is named 'team_records.json'
matrix = create_table(r"C:\Users\navjo\OneDrive\Desktop\sportsData.json")
print(matrix)
