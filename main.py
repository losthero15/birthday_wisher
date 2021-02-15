import datetime as dt
import random
import smtplib
import pandas

# Enter your name as a str
MY_NAME = "NAME"

# 0. Email server settings
MY_EMAIL = "EMAIL@EMAIL.COM"
MY_PASSWORD = "PASSWORD"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# 1. Import the birthdays.csv
data = pandas.read_csv("birthdays.csv")

birthdays_dict = data.to_dict(orient="records")

# 2. Get current month and date of the month
time = dt.datetime.now()
this_month = time.month
this_date = time.day

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

for person in birthdays_dict:
    if person["month"] == this_month and person["day"] == this_date:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
            message = file.read().replace("[NAME]", person["name"])
            message = message.replace("[MY_NAME]", MY_NAME)

        # 4. Send the letter generated in step 3 to that person's email address.

        to_email = person["email"]

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=to_email,
                msg=f"Subject:Happy Birthday!\n\n{message}."
            )
