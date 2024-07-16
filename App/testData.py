import pandas as pd

# Create a dictionary with card names
data = {
    "Card Name": [
        "Black Lotus",
        "Mox Sapphire",
        "Ancestral Recall",
        "Time Walk",
        "Timetwister"
    ]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel("cards.xlsx", index=False)

print("Example Excel file 'cards.xlsx' created.")