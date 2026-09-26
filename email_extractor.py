import re

#Files
input_file = "contact_data.txt"
output_file = "extracted_emails.txt"

with open(input_file, "r") as file:
    text = file.read()

# Find email addresses
emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

# Remove duplicate email addresses
emails = list(set(emails))

# Save the extracted emails
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

# Display the result
print("Email extraction completed!")
print("Emails found:", len(emails))

print("\nExtracted email addresses:")

for email in emails:
    print(email)

print("\nSaved to:", output_file)
