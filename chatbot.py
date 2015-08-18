import sleekxmpp
import logging
import cleverbot
#import dnspython
count = 0
def session_start(event):
    chatbot.send_presence()
    print 'Session started'
    chatbot.get_roster()

def message(msg):
    global count
    if msg['type'] in ('chat','normal'):
        print "msg recieved"
        msg1 = msg['body']
        print msg1
        if count==0:
            msg.reply("Hey. It seems my master is busy, or AFK. My name is Lapin, and I am his bot. I'll let him know you contacted him. Meanwhile you can chat with me if you want;) Have a nice day!").send()
            count = 1
        else:
            reply = cb.Ask(msg1)
            print 'reply: ' + reply +'\n'
            msg.reply(reply).send()

# Find your Facebook id from http://findmyfacebookid.com/
jid = 'your-fb-id@chat.facebook.com' 
password = 'your-fb-password'
addr = ('chat.facebook.com', 5222)
ipaddr = ('209.85.175.125',5222)

chatbot = sleekxmpp.ClientXMPP(jid,password)
sleekxmpp.use_proxy = True
chatbot.add_event_handler("session_start", session_start)
chatbot.add_event_handler("message", message)

chatbot.auto_reconnect = True
cb = cleverbot.Session()

chatbot.connect(addr)
chatbot.process(block=True)
