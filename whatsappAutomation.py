import pywhatkit


number=str(input('input the phone number that the message is to be sent to '))
message=str(input('input the message that you want to send '))
hour=int(input('input the hour you want to send the messge '))
min=int(input('input the minute you want to send the messge '))


pywhatkit.sendwhatmsg(number,message,hour,min,32)