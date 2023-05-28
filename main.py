import smtplib
import time
import os

# Email configuration
sender_email = os.environ.get('')
sender_password = os.environ.get('')
receiver_email = 'ceo@creativenetworklive.com'
subject = 'Payment Reminder'
body_template = 'Hello ,\n\nYou owe me ${}.\n\nRegards,\nYour Friend'

# Amount configuration
initial_amount = 21000
amount_increase = 21000

# SMTP server configuration (Gmail)
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Function to send the email
def send_email(amount):
    # Compose the email message
    body = body_template.format(amount)

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail(sender_email, receiver_email, message)

        # Print a confirmation message
        print(f"Email sent: Owed amount is ${amount}")

# Main loop
while True:
    # Calculate the current owed amount
    current_amount = initial_amount + (amount_increase * ((time.time() - time.mktime(time.gmtime(0))) // (24 * 3600)))

    # Send the email
    send_email(current_amount)

    # Wait for 24 hours
    time.sleep(24 * 3600)
