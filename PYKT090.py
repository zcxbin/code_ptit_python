
with open("CONTACT.in", "r") as files:
    emails = files.readlines()

contacts = []

for email in emails:
    email = email.lower().strip()
    if email not in contacts:
        contacts.append(email)

contacts.sort()
for email in contacts:
    print(email)
