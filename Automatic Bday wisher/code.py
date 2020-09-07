import pandas as pd
import datetime
import smtplib

# ENTER UR AUTHENTICATION DETAILS
GMAIL_ID=''
GMAIL_PSWD=''


def sendEmail(to,sub,msg):
    s=smtplib.SMTP('smtp.gmail.com')
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PSWD)
    s.sendmail(GMAIL_ID,to,f"Subject: {sub}\n\n{msg}")
    s.quit()


if __name__ == "__main__":
    data=pd.read_excel("bday_project.xlsx")
#     here bday_project.xlsx is the excel file containig all the data

    today=datetime.datetime.now().strftime("%d-%m")
    yearnow=datetime.datetime.now().strftime("%Y")

    writeIndex=[]
    for index , item in data.iterrows():
        bday=item['Birthday'].strftime("%d-%m") 
        if (today == bday) and yearnow not in str(item['Year']):
            sendEmail(item['EmailId'],"Happy Birthday",item['Dialogue'])
            writeIndex.append(index)
   
    if len(writeIndex)!=0:
        for i in writeIndex:
            yr=data.loc[i,'Year']
            data.loc[i,'Year']=str(yr) + ',' + str(yearnow)
            
        data.to_excel('bday_project.xlsx',index=False)
         # with index=False, extra columns which might have been added on its own by name 'unnamed index' will be removed        








