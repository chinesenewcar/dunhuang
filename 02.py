import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def sendEmail(
    user: str,
    pwd: str,
    subject: str,
    text_content: str,
    sender: str,
    receiver: str,
    file_path: str,
):
    """
    发送邮件

    args:
        user: 邮箱账号
        pwd: smtp授权码
        subject: 邮件主题
        text_content: 邮件正文
        sender: 发件人
        receiver: 收件人
        file_path: 附件路径
    """

    qqMall = smtplib.SMTP_SSL("smtp.qq.com", 465)
    qqMall.login(user, pwd)

    message = MIMEMultipart()
    message["Subject"] = Header(subject)
    message["From"] = Header(f"{sender}<{user}>")
    message["To"] = Header(f"<{receiver}>")

    mailContent = MIMEText(text_content, "plain", "utf-8")

    with open(file_path, "rb") as imageFile:
        fileContent = imageFile.read()
    # 获得图片类型
    fileType = file_path.split(".")[-1]

    attachment = MIMEImage(fileContent)
    attachment.add_header("Content-Disposition", "attachment", filename=fileType)

    message.attach(mailContent)
    message.attach(attachment)

    qqMall.sendmail(sender, receiver, message.as_string())
    logging.info("邮件发送成功")


def main():
    # 从.env中读取邮箱账号和密码
    mailUser = os.getenv("MAIL_USER")
    mailPass = os.getenv("MAIL_PASS")
    sender = os.getenv("MAIL_SENDER")
    receiver = os.getenv("MAIL_RECEIVER")
    filePath = ".\\data\\images\\AIT.jpg"
    sendEmail(
        mailUser,
        mailPass,
        "测试邮件",
        "这是一封测试邮件",
        sender,
        receiver,
        filePath,
    )


if __name__ == "__main__":
    main()
