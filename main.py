import schedule
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime
import re
import smtplib
from email.mime.text import MIMEText

from abr import abr


def runcheck():
    
    me = "sender@email.com"
    pw = "password.complicate.12121" #Password of sender account
    r = "receiver@email.com"


    now = datetime.now()
    #ts = 1583216662
    #now = datetime.fromtimestamp(ts)
    if (now.strftime("%d")[0]) == "0":
        d = now.strftime("%d")[1]
        x = (now.strftime("%B")) + " " + d + ", " + (now.strftime("%Y"))
    else:
        x = now.strftime("%B %d, %Y")

    xt = now.strftime("%H:%M")
    f = open("C:/users/X/desktop/py/1.txt", "a+")


    w1 = "The date is " + x + " \n"
    w2 = "The time is " + xt + " \n"
    f.write(w1)

    f.write(w2)


    DRIVER_PATH = ('C:/chromedriver')
    options = Options()
    options.add_argument('headless')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get("https://api.ontario.ca/api/drupal/page%2F2020-ontario-immigrant-nominee-program-updates?fields=nid,field_body_beta,body")


    ss = driver.page_source
    
    if x in ss:
        upc = ss.count(x)
       
        if upc <= 1:
            f.write("There is an update today \n")
        if upc > 1:
            f.write("There are updates today \n")
            
        s = ss.find("h4")
##        print("update number 1 is at position " + str(s))
        s1 = s + 6
        e = (ss.find("/h4")) - 4
##        print("update number 1 ends at position " + str(e))
        u1 = ss[s1:e]
        updates = {"blank"}
        
        if  u1 not in updates:
            i = 1
            while i < upc:
                if "&amp;#x2019;s" in u1:
                    u = u1.replace("&amp;#x2019;","'")
                else:
                    u = u1

                theupdate = u
                    
                if "&lt;abbr" in u:
##                    print("Running abr for " + str(i) + " times")
                    theupdate = abr(u)
                else:
                    theupdate = u

##                print(str(i) + ": " + theupdate)

                msgcontent = theupdate
                tst = 'plain'
                msg = MIMEText(msgcontent,tst)
                msg['Subject'] = "Update"
                msg['From'] = me
                    

                try:
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.ehlo()
                    server.login(me, pw)
                    server.sendmail(me, r, msg.as_string())
                    server.sendmail(me, r, msg.as_string())
                    f.write("Email sent with update \n \n")

                except:
                    f.write ("Something went wrong with email \n \n")
                    
                updates.add(u)
##                print("There are " +str(len(updates)-1)+" updates accounted for")
                
                s2 = e+7
                s = ss.find("h4",s2)
##                print("Update number " + str(i+1) + " found at position " + str(s))
                s1 = s + 6
                e = (ss.find("/h4",s2)) - 4
##                print("update number" + str(i+1)+ "ends at position " + str(e))
                u1 = ss[s1:e]
                #print("u1 number " + str(i) + " is " + str(s))
                i += 1
            

    else:
        f.write("There are no updates \n \n")

    driver.quit()

    f.write("The code ends here")
    f.write("""
    ------------------------------------------------------------------------
    ------------------------------------------------------------------------

    """)

    f.close()
    
    
runcheck()



