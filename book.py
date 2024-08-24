class Contact:
    def __init__(self, name, phone, email, address, notes=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.notes = notes

    def update(self, name=None, phone=None, email=None, address=None, notes=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address
        if notes:
            self.notes = notes

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}, Notes: {self.notes}"
    
class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def update_contact(self, name, **kwargs):
        for contact in self.contacts:
            if contact.name == name:
                contact.update(**kwargs)
                return f"Updated contact: {name}"
        return f"Contact not found: {name}"

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return f"Deleted contact: {name}"
        return f"Contact not found: {name}"

    def view_contacts(self):
        return "\n".join(str(contact) for contact in self.contacts)
address_book = AddressBook()

# Add a contact
contact1 = Contact(name="John Doe", phone="123-456-7890", email="john.doe@example.com", address="123 Elm Street")
address_book.add_contact(contact1)

# Update a contact
address_book.update_contact("John Doe", phone="098-765-4321")

# View all contacts
print(address_book.view_contacts())

# Delete a contact
address_book.delete_contact("John Doe")

# View all contacts again
print(address_book.view_contacts())





class Email:
    def __init__(self, sender, recipient, subject, body, timestamp, status="unread"):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.timestamp = timestamp
        self.status = status

    def mark_as_read(self):
        self.status = "read"

    def __str__(self):
        return f"From: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\n\n{self.body}"

class User:
    def __init__(self, username, email_address):
        self.username = username
        self.email_address = email_address
        self.inbox = []
        self.sent = []

    def receive_email(self, email):
        self.inbox.append(email)

    def send_email(self, recipient, subject, body, timestamp):
        email = Email(self.email_address, recipient.email_address, subject, body, timestamp)
        recipient.receive_email(email)
        self.sent.append(email)

    def __str__(self):
        return f"User: {self.username}, Email: {self.email_address}"

class EmailClient:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email_address):
        if email_address not in self.users:
            self.users[email_address] = User(username, email_address)
        else:
            print("Email address already exists.")

    def send_email(self, sender_address, recipient_address, subject, body, timestamp):
        if sender_address in self.users and recipient_address in self.users:
            sender = self.users[sender_address]
            recipient = self.users[recipient_address]
            sender.send_email(recipient, subject, body, timestamp)
        else:
            print("Sender or recipient not found.")

    def get_inbox(self, email_address):
        if email_address in self.users:
            user = self.users[email_address]
            return user.inbox
        else:
            print("User not found.")
            return []

    def get_sent(self, email_address):
        if email_address in self.users:
            user = self.users[email_address]
            return user.sent
        else:
            print("User not found.")
            return []

client = EmailClient()
client.add_user("Alice", "alice@example.com")
client.add_user("Bob", "bob@example.com")

import datetime
timestamp = datetime.datetime.now()
client.send_email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", timestamp)

inbox = client.get_inbox("bob@example.com")
for email in inbox:
    print(email)

sent_emails = client.get_sent("alice@example.com")
for email in sent_emails:
    print(email)
