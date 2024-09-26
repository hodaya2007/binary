bin= [1,2,4,8,16,32,64,128] #מערך של מספרים
num=int (input("הכנס מספר"))
i=7 ## גודל המערך
newnum=0## שווה למספר החדש
bina="00000000"
while i!=0 or num!= newnum:
    if bin[i]>num:
        i=i-1
    else:
        newnum+=bin[i]
        if newnum>num:
            newnum=newnum-bin[i]
            i=i-1
        else:
            bina = bina[:i] + "1" + bina[i+1:]
if num!=newnum:
    bina=bina+1
print (bina)
for x in range(len(bina)): ## החלפה
    if bina[x]== "1":
        bina = bina[:x] + "0" + bina[x+1:]
    else:
        bina = bina[:x] + "1" + bina[x+1:]
print (bina)
i=0
bTemp=1
while i!=8:
    if int(bina[i])+ bTemp==2:
        bina = bina[:i] + "0" + bina[i+1:]
        
    elif int(bina[i])==0 and bTemp==1:
        bina = bina[:i] + "1" + bina[i+1:]
        bTemp=0
    i=i+1
print (bina)
        