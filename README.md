# Win-Loss table Generator README

## Introduction
This script creates a win-loss matrix for teams based on their head-to-head records. It reads a dictionary of team records, iterating through each team's wins and losses, and compiles a matrix where rows represent teams and columns represent their opponents.


## How it Works
The script initializes an empty DataFrame with teams as both the index and columns. It then populates this DataFrame by iterating through each team's record, placing wins horizontally across and losses vertically down. Diagonal cells are filled with '--' to denote non-applicable self-matchups.


## Output
The output is a Pandas DataFrame:
- Rows: Teams.
- Columns: Opponents.
- Cell values: Wins (across) and Losses (down).
- Diagonal cells (same team matchups) are marked as '--'.

