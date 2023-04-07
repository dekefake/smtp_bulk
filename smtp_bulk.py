import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr

# Replace these with your own SMTP credentials
smtp_server = "send.smtp.com"
smtp_port = 465
smtp_user = "<<redacted>>"
smtp_password = "<<redacted>>"

# Replace these with your own email details
from_email = "hello@ds-media.co"
subject = "Its time to get a website for your business"
body = "Hi, my name is Thomas and I build sexy websites. I came across your business but I couldn't find your website. I can have a new one up in one week for $1000. Interested ?"

server = smtplib.SMTP_SSL(smtp_server, smtp_port)
server.login(smtp_user, smtp_password)

# Read email addresses from CSV file
def read_emails_from_csv(filename):
    emails = []
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email = row["Email"]
            if email:  # Check if the email field is not empty
                emails.append(email)
    return emails

def is_valid_email(email):
    parsed_email = parseaddr(email)
    return parsed_email[1] == email

def send_email(to_email):
    if not is_valid_email(to_email):
        print(f"Invalid email address: {to_email}")
        return

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        server.sendmail(from_email, to_email, msg.as_string())
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

if __name__ == "__main__":
    csv_filename = "emails.csv"
    email_list = read_emails_from_csv(csv_filename)
    for email in email_list:
        send_email(email)
