import socket
import socks
import requests

web = input(">>>>")
while True:
    ip='localhost' #your proxy's ip
    port = 0000 #your proxy's port
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
    socket.socket = socks.socksocket # بعد از این لاین دیگه همه چی از پروکسی رد میشه
    url = web
    print(requests.get(url).text) 
