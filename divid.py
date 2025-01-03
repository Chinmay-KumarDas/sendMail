import pandas as pd

# Read the Excel file
df = pd.read_excel('./Community Poster 5 Aug.xlsx')  # Update with your file path

# Extract email addresses from the third column (index 2)
email_addresses = df.iloc[:, 2].dropna().tolist()  # Assumes emails are in the 3rd column

# Divide email addresses into batches of 500
batch_size = 500
for i in range(0, len(email_addresses), batch_size):
    batch = email_addresses[i:i + batch_size]
    with open(f'batch_{i // batch_size + 1}.txt', 'w') as f:
        for email in batch:
            f.write(email + '\n')

print(f'Divided email addresses into {len(email_addresses) // batch_size + (1 if len(email_addresses) % batch_size > 0 else 0)} files.')
