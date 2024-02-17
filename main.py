import smtplib
import random
import credentials as cred
import datetime as dt

now = dt.datetime.now()
if now.weekday() == 0:
    with open('quotes.txt', 'r') as quote_file:
        quotes = quote_file.readlines()
        quote = random.choice(quotes).strip()

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls() # Makes connection secure

        connection.login(user=cred.EMAIL, password=cred.PASSWORD)
        connection.sendmail(
            from_addr=cred.EMAIL,
            to_addrs=cred.EMAIL,
            msg=f'Subject:Monday Motivation!\n\n\n{quote}'
        )
