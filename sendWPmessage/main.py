import pywhatkit
pywhatkit.start_server()
# try:
#     pwk.sendwhatmsg("+90(5319165256)","Merhabalar, bu bir deneme mesajıdır...", 17,29)
#     print("mesaj gönderildi")
# except:
#     print("mesa gönderilirken bir hata oluştu")
#
# import pywhatkit

# using Exception Handling to avoid
# unprecedented errors
try:

    # sending message to receiver
    # using pywhatkit
    pywhatkit.sendwhatmsg("+905466031235",
                          "Hello from GeeksforGeeks",
                          17, 37,10,20)
    print("Successfully Sent!")
    pywhatkit.send
except:
    # handling exception
    # and printing error message
    print("An Unexpected Error!")