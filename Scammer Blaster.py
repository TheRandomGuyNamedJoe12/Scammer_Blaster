import pytextnow

client = pytextnow.Client("username", sid_cookie="sid", csrf_cookie="csrf").

scammers_number = input("Scammer's Number: ")

while True:
 client.send_sms(scammers_number, "QUIT SCAMMING PEOPLE!!!")
