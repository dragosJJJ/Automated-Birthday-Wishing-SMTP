import random, pandas, datetime as dt,smtplib

#replace the example email and password and be sure the date in birthday.csv is the same with the one this message is read and the code will work.

MY_EMAIL = "testemail@gmail.com"
MY_PASSWORD = "testpassword"

birthday_data = pandas.read_csv("birthdays.csv")
birthday_data = birthday_data.to_dict(orient="records")

now = dt.datetime.now()

for dict in birthday_data:
    if dict["year"] == now.year and dict["month"] == now.month and dict["day"] == now.day:
        letter_num = random.randint(1,2)
        with open(f"letter_templates\letter_{letter_num}.txt", "r") as file:
            lines = file.read()
            lines = lines.replace("[NAME]", dict["name"])

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg= f"La multi ani!\n\n{lines}"
                )

            lines = lines.replace(dict["name"], "[NAME]")





