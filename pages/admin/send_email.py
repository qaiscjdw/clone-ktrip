import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "kasuami.team@gmail.com"

msg = MIMEMultipart()
toaddr = sys.argv[1]

# Hapus ini kalo mau send tulisan saja
###########################################################
# name_file = sys.argv[2]
# path = 'C:\\Users\\qaisc\\Desktop\\PROJECT\\send email\\'
# file = path+name_file
###########################################################

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Sukses Validasi Pembayaran'
 
body = 'Pembayaran yang anda lakukan sudah berhasil di validasi silahkan segera lakukan pembayaran selanjutnya yah! Terima Kasih:)'
msg.attach(MIMEText(body, 'plain'))
##########################################################################################
# attachment = open(file,"rb")
# part = MIMEBase('application', 'octet-stream')
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= %s" % name_file)
# msg.attach(part)
##########################################################################################

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "kasuami123")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
