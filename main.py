import os
import tkinter as tk
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email():
    # Read the input values from the GUI
    sender_email = sender_entry.get()
    recipient_email = recipient_entry.get()
    email_subject = subject_entry.get()
    email_title = title_entry.get()
    email_body = body_entry.get()

    # Validate inputs
    if not sender_email or not recipient_email or not email_subject or not email_body:
        result_label.config(text='All fields are required.')
        return

    # Create the email message
    message = Mail(
        from_email=sender_email,
        to_emails=recipient_email,
        subject=email_subject,
        html_content=f'<h1>{email_title}</h1><p>{email_body}</p>')

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        result_label.config(text='Email sent successfully!')
    except Exception as e:
        result_label.config(text='Error sending email: ' + str(e))

# Create the Tkinter window
window = tk.Tk()
window.title('Email Sender')
window.geometry('600x600')

# Create and position the input fields
sender_label = tk.Label(window, text='Sender Email:')
sender_label.pack()
sender_entry = tk.Entry(window)
sender_entry.pack()

recipient_label = tk.Label(window, text='Recipient Email:')
recipient_label.pack()
recipient_entry = tk.Entry(window)
recipient_entry.pack()

subject_label = tk.Label(window, text='Email Subject:')
subject_label.pack()
subject_entry = tk.Entry(window)
subject_entry.pack()

title_label = tk.Label(window, text='Email Title:')
title_label.pack()
title_entry = tk.Entry(window)
title_entry.pack()

body_label = tk.Label(window, text='Email Body:')
body_label.pack()
body_entry = tk.Entry(window)
body_entry.pack()

# Create the send button
send_button = tk.Button(window, text='Send Email', command=send_email)
send_button.pack()

# Create the label to display the result
result_label = tk.Label(window, text='')
result_label.pack()

# Run the Tkinter event loop
window.mainloop()
