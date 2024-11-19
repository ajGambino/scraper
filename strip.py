import pandas as pd

# Load the CSV
df = pd.read_csv('players.csv')

# Complete reference list of player names
reference_names = [
    "Nikola Jokic", "Luka Doncic", "Shai Gilgeous-Alexander", "Anthony Davis", "LeBron James",
    "LaMelo Ball", "Jayson Tatum", "Brandon Ingram", "Jamal Murray", "Lauri Markkanen",
    "Jaylen Brown", "Donovan Mitchell", "Evan Mobley", "John Collins", "Kyrie Irving",
    "Jalen Williams", "Cam Thomas", "Jaren Jackson Jr.", "Jarrett Allen", "Austin Reaves",
    "Derrick White", "Michael Porter Jr.", "Trey Murphy III", "Darius Garland", "Zach Collins",
    "Dennis Schroder", "Desmond Bane", "Brandon Miller", "Brandon Boston Jr.", "Collin Sexton",
    "Cameron Johnson", "Ben Simmons", "Miles Bridges", "Chris Paul", "Jrue Holiday",
    "Jordan Clarkson", "Keyonte George", "Rui Hachimura", "Al Horford", "Yves Missi",
    "Christian Braun", "Javonte Green", "Luguentz Dort", "D'Angelo Russell", "Caris LeVert",
    "Devin Vassell", "Peyton Watson", "Sandro Mamukelashvili", "Neemias Queta", "Grant Williams",
    "Scotty Pippen Jr.", "Keldon Johnson", "Russell Westbrook", "Dorian Finney-Smith",
    "Santi Aldama", "PJ Washington", "Kyle Filipowski", "Cason Wallace", "Aaron Wiggins",
    "Ziaire Williams", "Stephon Castle", "Julian Champagnie", "Klay Thompson", "Dereck Lively II",
    "Dalton Knecht", "Payton Pritchard", "Harrison Barnes", "Brandon Clarke", "Moussa Diabate",
    "Jeremiah Robinson-Earl", "Jaylen Nowell", "Josh Green", "Tre Mann", "Daniel Gafford",
    "Marcus Smart", "Ajay Mitchell", "Isaiah Collier", "Cody Martin", "Georges Niang",
    "Tre Jones", "Alex Caruso", "Jake LaRavia", "Vince Williams Jr.", "Julian Strawther",
    "Jalen Wilson", "Dillon Jones", "Jaylen Wells", "Noah Clowney", "Sam Merrill",
    "Kenrich Williams", "Naji Marshall", "Isaac Okoro", "Sam Hauser", "Jamal Cain",
    "Trey Jemison", "Cody Williams", "Trendon Watford", "Ty Jerome", "Luke Kennard",
    "Charles Bassey", "Jaden Hardy", "Jay Huff", "Cam Reddish", "Keon Johnson",
    "Christian Koloko", "Quentin Grimes", "Tidjane Salaun", "Gabe Vincent", "Drew Eubanks",
    "Vlatko Cancar", "Blake Wesley", "Maxi Kleber", "Dario Saric", "DeAndre Jordan",
    "Ousmane Dieng", "Spencer Dinwiddie", "Luke Kornet", "Brice Sensabaugh", "Seth Curry",
    "Max Christie", "Malaki Branham", "Johnny Juzang", "Vasilije Micic", "Jordan Walsh",
    "Daniel Theis", "Armel Traore", "JD Davison", "Shake Milton", "Zeke Nnaji",
    "Micah Potter", "Adam Flagler", "Taj Gibson", "Hunter Tyson", "Antonio Reeves",
    "Jeremy Sochan", "Jaxson Hayes", "Cam Spencer", "Bronny James", "Xavier Tillman",
    "Day'Ron Sharpe", "Brandon Williams", "Jason Preston", "Trey Alexander",
    "Bojan Bogdanovic", "Drew Peterson", "Jaylon Tyson", "Nikola Topic", "DaQuan Jeffries",
    "Jarred Vanderbilt", "Branden Carlson", "Dante Exum", "Harrison Ingram", "Dwight Powell",
    "Maxwell Lewis", "Alex Ducas", "Luke Travers", "Emoni Bates", "KJ Simpson",
    "Zion Williamson", "Cui Yongxi", "Isaiah Joe", "Olivier-Maxence Prosper", "Gregory Jackson",
    "Anton Watson", "Markieff Morris", "Riley Minix", "Taylor Hendricks", "Jalen Hood-Schifino",
    "Jaylen Martin", "Aaron Gordon", "Yuki Kawamura", "CJ McCollum", "Colin Castleton",
    "Dejounte Murray", "Christian Wood", "Sidy Cissoko", "Nick Richards", "Victor Wembanyama",
    "Chet Holmgren", "Ja Morant", "Kessler Edwards", "Jazian Gortman", "Max Strus",
    "Tristan Thompson", "John Konchar", "Jaylin Williams", "Herbert Jones", "Mark Williams",
    "Jordan Hawkins", "Quincy Olivari", "Tyrese Martin", "Kristaps Porzingis", "PJ Hall",
    "Spencer Jones", "Jose Alvarado", "Isaiah Hartenstein", "Craig Porter Jr.",
    "Dariq Whitehead", "Nick Smith Jr.", "Karlo Matkovic", "JT Thor", "Zach Edey",
    "David Duke Jr.", "Nic Claxton", "Baylor Scheierman", "Jared Rhoden", "Jalen Pickett",
    "Oscar Tshiebwe", "Dean Wade", "Walker Kessler", "DaRon Holmes II", "Patty Mills",
    "Svi Mykhailiuk", "Jaden Springer"
]

# Convert reference names to a set for fast lookups
reference_set = set(reference_names)

# Define a function to match the cleaned name to the reference list
def match_name(long_name):
    # Attempt to find the first name in the reference list that is contained within the long name
    for ref_name in reference_set:
        if ref_name in long_name:
            return ref_name
    return None  # Return None if no match is found

# Apply the matching function to the 'Name' column
df['Name'] = df['Name'].apply(match_name)

# Drop rows where no match was found
df = df.dropna(subset=['Name'])

# Save to a new CSV
df.to_csv('numberfire.csv', index=False)

print("Cleaned player names saved to 'numberfire.csv'.")
