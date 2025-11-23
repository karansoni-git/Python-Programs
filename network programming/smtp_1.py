import smtplib

sender_email = input("Enter Your Email : ")
receiver_email = input("Enter Receiver Email : ")
subject = input("Enter Subject : ")
message = input("Enter Message : ")

fullMsg = f"Subject :{subject}\n\nMessage :{message}"

smtpObj = smtplib.SMTP("smtp.gmail.com",587)

smtpObj.starttls()

smtpObj.login(sender_email,"ajbtlfbuzdcyikhh")

smtpObj.sendmail(sender_email,receiver_email,fullMsg)

print("Email sent successfully")
