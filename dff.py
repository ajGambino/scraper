import pandas as pd

# Read the input CSV
ppg_df = pd.read_csv('ppg.csv')

# Combine 'first_name' and 'last_name' into 'Name'
ppg_df['Name'] = ppg_df['first_name'] + ' ' + ppg_df['last_name']

# Keep only 'Name' and 'ppg_projection', rename 'ppg_projection' to 'Projection'
dff_df = ppg_df[['Name', 'ppg_projection']].rename(columns={'ppg_projection': 'Projection'})

# Save to a new CSV file
dff_df.to_csv('dff.csv', index=False)

print("New CSV file 'dff.csv' created successfully.")
