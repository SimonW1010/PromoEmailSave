import time, traceback
import datetime
import email
import imaplib
import mailbox

def check_email():
    EMAIL_ACCOUNT = ## Gmail account example: test@gmail.com
    PASSWORD = ## Gmail App Password (Check Readme for instructions)

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(EMAIL_ACCOUNT, PASSWORD)
    mail.list()
    mail.select('inbox')

    result, data = mail.uid('search', None, "UNSEEN") # (ALL/UNSEEN)
    i = 0
    i = len(data[0].split())

    email_list = ""
    all_csv = ""

    file = open("email_list.txt","r")
    reader = csv.reader(file)

    for row in reader:
        c = row[0]
        all_csv += c

    if i == 0:
        print("No emails")

    else:
        for x in range(i):
            latest_email_uid = data[0].split()[x]
            result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            # result, email_data = conn.store(num,'-FLAGS','\\Seen') 
            # this might work to set flag to seen, if it doesn't already
            raw_email = email_data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
        

            # Header Details
            date_tuple = email.utils.parsedate_tz(email_message['Date'])
            if date_tuple:
                local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
                local_message_date = "%s" %(str(local_date.strftime("%a, %d %b %Y %H:%M:%S")))
            email_from_raw = str(email_message['From'])

            email_from = email_from_raw.split("<")[1].split(">")[0]

            mail.uid('STORE', latest_email_uid, '-FLAGS', '\SEEN')

            if email_from not in all_csv:
                email_list += email_from+"\n"

        w_file = open("email_list.txt","w") 
        w_file.write(email_list)


def every(delay, task):
    next_time = time.time() + delay
    while True:
        time.sleep(max(0, next_time - time.time()))
        try:
            task()
        except Exception:
            traceback.print_exc()
            # in production code you might want to have this instead of course:
            # logger.exception("Problem while executing repetitive task.")
        # skip tasks if we are behind schedule:
        next_time += (time.time() - next_time) // delay * delay + delay

every(5, check_email)
