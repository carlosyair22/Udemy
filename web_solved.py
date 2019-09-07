import csv
import os

#udemy_csv = "./resources/web_starter.csv"
udemy_csv=os.path.join(".","resources","web_starter.csv")

title=[]
pricer=[]
subscribers=[]
reviews=[]
reviewsP=[]
length=[]

with open(udemy_csv,"r", encoding="UTF-8") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    for row in csvreader:
        title.append(row[1])
        pricer.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        percent=round(int(row[6])/int(row[5]),2)*100
        reviewsP.append(percent)
        new_length=row[9].split(" ")
        length.append(float(new_length[0]))
merge=zip(title,pricer,subscribers,reviews,reviewsP,length)
file=os.path.join("Udemy_solved.csv")
with open(file,"w",newline="\n") as datafile:
   writer=csv.writer(datafile)
   writer.writerow(["Title","Price","Subscribers","Reviews","% Reviews","Lenght"])
   writer.writerows(merge)

