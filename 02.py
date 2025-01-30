from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# 从.env中读取邮箱账号和密码
import os

mailUser = os.getenv("MAIL_USER")
mailPass = os.getenv("MAIL_PASS")
receiver = os.getenv("MAIL_RECEIVER")

qqMall = smtplib.SMTP_SSL("smtp.qq.com", 465)
qqMall.login(mailUser, mailPass)
sender = mailUser
message = MIMEMultipart()
message["Subject"] = Header("--xx")
message["From"] = Header(f"xx<{sender}>")
message["To"] = Header(f"<{receiver}>")

textContent = "xxxx"
mailContent = MIMEText(textContent, "plain", "utf-8")

filePath = "E:\\mycode\\ai-jiangxin\\jiangxinzuoye.png"
with open(filePath, "rb") as imageFile:
    fileContent = imageFile.read()

attachment = MIMEImage(fileContent)
attachment.add_header("Content-Disposition", "attachment", filename=".jpg")


message.attach(mailContent)
message.attach(attachment)

qqMall.sendmail(sender, receiver, message.as_string())
print("邮件发送成功")

