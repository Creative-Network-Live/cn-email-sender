import os
import tkinter as tk
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Calculate the debt amount based on the number of days since the script was last run
def calculate_debt_amount(initial_debt, debt_increment, days_passed):
    return initial_debt + (debt_increment * days_passed)

def send_email():
    # Read the input values from the GUI
    sender_email = sender_entry.get()
    recipient_email = recipient_entry.get()
    initial_debt = int(initial_debt_entry.get())
    debt_increment = int(debt_increment_entry.get())

    # Validate inputs
    if not sender_email or not recipient_email:
        result_label.config(text='Sender and recipient email are required.')
        return

    # Calculate the current debt amount
    current_debt = calculate_debt_amount(initial_debt, debt_increment, 0)

    # Create the email message
    message = Mail(
        from_email=sender_email,
        to_emails=recipient_email,
        subject='You owe me $$$$',
        html_content=f'<strong>You owe me ${current_debt}</strong>')

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        result_label.config(text='Email sent successfully!')
    except Exception as e:
        result_label.config(text='Error sending email: ' + str(e))

# Create the Tkinter window
window = tk.Tk()
window.title('Debt Collector')
window.geometry('300x250')

# Create and position the input fields
sender_label = tk.Label(window, text='Sender Email:')
sender_label.pack()
sender_entry = tk.Entry(window)
sender_entry.pack()

recipient_label = tk.Label(window, text='Recipient Email:')
recipient_label.pack()
recipient_entry = tk.Entry(window)
recipient_entry.pack()

initial_debt_label = tk.Label(window, text='Initial Debt:')
initial_debt_label.pack()
initial_debt_entry = tk.Entry(window)
initial_debt_entry.pack()

debt_increment_label = tk.Label(window, text='Debt Increment:')
debt_increment_label.pack()
debt_increment_entry = tk.Entry(window)
debt_increment_entry.pack()

# Create the send button
send_button = tk.Button(window, text='Send Email', command=send_email)
send_button.pack()

# Create the label to display the result
result_label = tk.Label(window, text='')
result_label.pack()

# Run the Tkinter event loop
window.mainloop()
