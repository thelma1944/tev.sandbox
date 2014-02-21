import imaplib
import email

def extract_body(payload):
    if isinstance(payload,str):
        return payload
    else:
        return '\n'.join([extract_body(part.get_payload()) for part in payload])

conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)

#  Added baastet's user name & password.
#  TEV 12/29/2012 @1411 hrs

conn.login("baastet.project", "meowpurr")
conn.select()
typ, data = conn.search(None, '(UNSEEN)')
try:
    for num in data[0].split():
        typ, msg_data = conn.fetch(num, '(RFC822)')
        for message in messages:
                subject=msg['subject']                   
                print(subject)
                payload=msg.get_payload()
                body=extract_body(payload)
                print(body)
        
finally:
    try:
        conn.close()
    except:
        pass
    conn.logout()