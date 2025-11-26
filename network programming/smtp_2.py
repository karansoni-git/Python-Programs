import smtplib

sender = "karanparekh1011@gmail.com"
receiver = input("Enter Receiver Email : ")
subject = input("Enter Subject : ")
message = input("Enter Your Message : ")

fullMsg = f"Subject :{subject}\n{message}"

smtpObj = smtplib.SMTP("smtp.gmail.com",587)

smtpObj.starttls()

smtpObj.login(sender,"nodlpvzyowchxrbb")

smtpObj.sendmail(sender,receiver,fullMsg)

print("Email sent successfully!")

smtpObj.quit()