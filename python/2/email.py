# -*- coding: utf8 -*-
import smtplib

# 구글 서버
HOST = "smtp.gmail.com:587"

# 이메일 주소
me = ""
you = ""

# 사용자 인증 이메일과 패스워드
username = ''
password = ''

# 서버 연결
server = smtplib.SMTP(HOST)
server.ehlo()
server.starttls()
server.login(username, password)

msg = "\r\n".join([
  "From: ",
  "To: ",
  "Subject: ",
  "",
  ""
  ])
  
server.sendmail(me, you, msg)
server.quit();


