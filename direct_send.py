import smtplib
from email.message import EmailMessage
import time
import pandas as pd

f = open("secret.txt", "r")
gmail_user = str(f.readline())
gmail_password = str(f.readline())
email_cc = str(f.readline())
f.close()

data = pd.read_csv("TeamsList.csv")
TableNames = ["Cohort", "Name", "Email", "Team", "StartupTree"]

def create_email(x):
    # name, incompleted, track, boardlink
    str_form = (
        "Hello again! Hope you've been well!\n\nFollowing up with a second reminder to complete the 'Submit FA20 metrics report' (was due December 13) on your monday board.\n\nI've included Jacques and the basement email for if you have any questions!\n\nHere is the link to your Monday board: {}.\n\nHave a great weekend and winter break, see you next quarter!\n\nWarm regards,\nMadeline Tjoa"
    )
    return str_form.format(
        x["MondayBoardLink"]
    )

def send_mail(message_string, send_to, subject,cc):
    msg = EmailMessage()
    msg.set_content(message_string)

    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = send_to
    msg['Cc'] = cc

    try:
        # Send the message via our own SMTP server.
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.quit()
        print("email sent")
    except:
        print("something wrong")

def send_to_startups(data):
    for index, row in data.iterrows():
        time.sleep(1)
        if (row['Send'] == "Yes") and ("@" in row["Email"]):
            subject = "Reminder to complete Submission Requirement on Monday Board"
            send_mail(row['customized_script'], row["Email"], subject, email_cc)


data['customized_script'] = data.apply(create_email, axis=1)

send_to_startups(data)
#
# print(data.iloc[0])
# test_data = data.iloc[0]

# send_mail(test_data['customized_script'], "mjtjoa@ucsd.edu", "hello", email_cc)
