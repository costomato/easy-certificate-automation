import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from dotenv import load_dotenv
load_dotenv()

pdf_dir = os.getcwd() + "/certificates"

csv_file = "sorted.csv"
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    csv_data = list(reader)

smtp_server = "smtp.office365.com"
smtp_port = 587
smtp_username = os.getenv("SMTP_USERNAME")
smtp_password = os.getenv("SMTP_PASSWORD")

smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.starttls()
smtp.login(smtp_username, smtp_password)

for pdf_file in os.listdir(pdf_dir):
    if pdf_file.endswith(".pdf"):
        pdf_name = os.path.splitext(pdf_file)[0]
        print(f"\nSearch name for {pdf_name}...")
        for row in csv_data:
            if pdf_name in row["UNIVERSITY MAIL ID:"]:
                print(f"Found {pdf_name} in CSV file...")
                email = pdf_name
                pdf_path = os.path.join(pdf_dir, pdf_file)
                msg = MIMEMultipart()
                msg['Subject'] = "Certificate of Participation - Hackeye Data Security Seminar"
                msg['From'] = smtp_username
                msg['To'] = email
                body = f'''Dear {row["NAME"]},

We hope this email finds you well. We wanted to thank you for attending our recent data security seminar, which we held on May 3, 2023. We appreciate your participation and engagement in the discussions, and we hope that you found the seminar informative and useful.

As promised, we are pleased to provide you with a certificate of participation for your attendance at the seminar. Attached to this email, you will find your certificate in PDF format. Please feel free to save and print this certificate for your records.

We encourage you to continue to stay engaged with our community and to participate in future events and activities. If you have any questions or feedback about the seminar, or if you would like to learn more about our club, please do not hesitate to reach out to us.

Thank you again for your participation, and we look forward to seeing you at our future events!

Best regards,
Kaustubh
Technical Head, Hackeye cybersecurity club
'''
                msg.attach(MIMEText(body))

                with open(pdf_path, 'rb') as f:
                    attach = MIMEApplication(f.read(),_subtype="pdf")
                    attach.add_header('Content-Disposition','attachment',filename=str(pdf_file))
                    msg.attach(attach)

                print(f"Sending email to {email}...")
                smtp.sendmail(smtp_username, email, msg.as_string())
                print(f"Email sent to {email} successfully!\n")

smtp.quit()