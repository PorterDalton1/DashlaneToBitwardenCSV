# folder,favorite,type,name,notes,fields,login_uri,login_username,login_password,login_totp
# Social,1,login,Twitter,,,twitter.com,me@example.com,password123,
# ,,login,My Bank,Bank PIN is 1234,"PIN: 1234
# Question 1: Blue",https://www.wellsfargo.com/home.jhtml,john.smith,password123456,
# ,,login,EVGA,,,https://www.evga.com/support/login.asp,hello@bitwarden.com,fakepassword,TOTPSEED123
# ,,note,My Note,"This is a secure note.


# username,username2,username3,title,password,note,url,category,otpSecret


from os import read
from numpy import empty
import pandas as pd


usernames = [];

uname1 = readFile["username"].tolist()
uname2 = readFile["username2"].tolist()
uname3 = readFile["username3"].tolist()

notes = readFile["note"].tolist()

for i in range(0, len(uname1), 1):
    if (pd.notna(uname1[i])):
        if (pd.notna(uname2[i])):
            if (pd.notna(uname3[i])):
                usernames.append[uname3[i]]
            else:
                usernames.append(uname2[i])
                if not (pd.notna(notes[i])):
                    notes[i] = "Email: " + str(uname1[i])
                else:
                    notes[i] = "Email: " + str(uname1[i]) + "   " + notes[i]
        else:
            usernames.append(uname1[i])
    else:
        usernames.append(pd.np.nan)


print(len(usernames), len(uname1))
for i in range(len(notes)):
    if pd.notna(notes[i]):
        print(str(i+2) + ": " + notes[i])


emptyDict = {};
# ["folder", "favorite", "type", "name", "notes", "fields", "login_uri", "login_username", "login_password", "login_totp"]:
emptyDict["folder"] = readFile["category"].tolist();
emptyDict["favorite"] = [pd.np.nan for i in range(len(uname1))]
emptyDict["type"] = ["login" for i in range(len(uname1))]
emptyDict["name"] = readFile["title"].tolist()
emptyDict["notes"] = notes
emptyDict["fields"] = [pd.np.nan for i in range(len(uname1))]
emptyDict["login_uri"] = readFile["url"].tolist()
emptyDict["login_username"] = usernames
emptyDict["login_password"] = readFile["password"].tolist()
emptyDict["login_totp"] = [pd.np.nan for i in range(len(uname1))]

for i in emptyDict.keys():
    print(i + ": " + str(len(emptyDict[i])))
    
exportFile = pd.DataFrame.from_dict(emptyDict)

print(exportFile)

exportFile.to_csv("output.csv", index=False)
