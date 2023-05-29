import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Calculate the debt amount based on the number of days since the script was last run
def calculate_debt_amount(initial_debt, debt_increment, days_passed):
    return initial_debt + (debt_increment * days_passed)

# Example usage
initial_debt = 120000
debt_increment = 21000
days_passed = 0

# Check if debt information is stored in a file
if os.path.exists('debt.txt'):
    with open('debt.txt', 'r') as file:
        days_passed = int(file.read())

# Calculate the current debt amount
current_debt = calculate_debt_amount(initial_debt, debt_increment, days_passed)

# Create the email message
message = Mail(
    from_email='ceo@creativenetworklive.com',
    to_emails='sbstnbnvdsa@gmail.com',
    subject='You owe me $$$$',
    html_content=f'<strong>You owe me ${current_debt}</strong>')

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)

# Update the number of days passed and store it in the file
days_passed += 1
with open('debt.txt', 'w') as file:
    file.write(str(days_passed))
