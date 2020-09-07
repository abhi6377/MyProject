import pandas as pd
# iski help se excel files bnate h
import datetime
import smtplib
# ye library smt ki madad se email bhejne me madad krti h


import os
os.chdir("F:\python project")

# os.mkdir("testing")
# just for testing


# ENTER UR AUTHENTICATION DETAILS
GMAIL_ID=''
GMAIL_PSWD=''


def sendEmail(to,sub,msg):
    print(f"Email to {to} sent with subject : {sub} and message : {msg}")
    s=smtplib.SMTP('smtp.gmail.com')
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PSWD)
    s.sendmail(GMAIL_ID,to,f"Subject: {sub}\n\n{msg}")
    # ek trh se header embedd kr dia h subject ka jisme neeche msg aaega
    s.quit()


if __name__ == "__main__":
    # sendEmail(GMAIL_ID,"subject","test message")
    # exit()

    df=pd.read_excel("bday_project.xlsx")
    # print(df)
    today=datetime.datetime.now().strftime("%d-%m")
    yearnow=datetime.datetime.now().strftime("%Y")

    # strftime se date month or year me se jo display krna h vo kr skte h
    # strftime("%d-%m-%Y") 
    # the output is a string----today is string here
    # print(today)

    writeIndex=[]
    for index , item in df.iterrows():
        # print(index,item['Birthday'])

        bday=item['Birthday'].strftime("%d-%m") 
        if (today == bday) and yearnow not in str(item['Year']):
            sendEmail(item['EmailId'],"Happy Birthday",item['Dialogue'])
            writeIndex.append(index)
    # print(writeIndex)
    if len(writeIndex)!=0:
        for i in writeIndex:
            yr=df.loc[i,'Year']
        # .loc access a grp of rows and columns by labels
        # print(yr)
            df.loc[i,'Year']=str(yr) + ',' + str(yearnow)
        # print(df.loc[i,'Year'])
        # print(df)
        df.to_excel('bday_project.xlsx',index=False)
         # index=False se unnamed index krke extra coumns add ni hongey








