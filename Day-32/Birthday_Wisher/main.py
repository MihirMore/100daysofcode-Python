import smtplib

my_email = "youremail"
password = "yourpassword"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="mihirmore.18@gmail.com", msg="Subject:Hello from python "
                                                                                   "project\n\n "
                                                                                   "This is a test email from python "
                                                                                   "project. Do not reply")
    connection.close()

import datetime as dt

now = dt.datetime.now()
week = now.weekday()
print(week)

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)