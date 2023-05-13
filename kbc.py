lis=[
     [
      "Which movie won Oscar for the 'Best Original Song' at the 95th Academy Awards?","RRR","All that Breathes",
      "The Elephant Whispers","Black Panther:Wakanda Forever",1],
      ["What is the fullform of ICC?","International Cricket Centre","International Cricket Council","Indian Cricket Coaching",
      "None of the Above",2],
      ["In which year India launched its satellite Mangalayan to Mars","2015","2019","2011","2013",4],
      ["Who won the Rajiv Gandhi Khel Ratna Award in 2022?","Rohit Sharma","Sharath Kamal Achanta","Neeraj Chopra","Sunil Chetri",2],
      ["What is the train Number of the legendary Kalka Mail from Kalka to Howrah?","12311","12321","12312","12322",3],
       ["Which of the following countries have the highest number of timezones?","China","Russia","USA","France",4],
       ["In which year the 2nd battle of Panipat was fought?","1559","1575","1556","1567",3],
       ["In which city is the head office of the Insurance Regularity and Development Authority of India(IRDAI) situated?","Shimla","Mumbai","Chandigarh","Hyderabad",4],
       ["Which among the following is the longest railway route of India","Dibrugarh-Kanyakumari,Vivek Express","Jammu Tawi-Kanyakumari,Himsagar Express","Jammu Tawi-Tirunelveli,Ten Jammu Express","Trivandrum-Guwahati,Guwahati Express",1],
       ["By how many runs did India win the 2013 ICC Champions trophy defeating England?","5","4","3","7",1],
       ["In network security,what is attack in authentication called","fabrication","interception","modification","interruption",1],
       ["Who was the only British Prime Minister to have been assasinated in 1812","William Grenville","Spencer Perceval","Robert Peel","Robert Jenkinson",2],
       ["Where are Diesel engines manufacured in India?","Chennai","Bangalore","Chittaranjan","Varanasi",4]
     ]
levels=[1000,4000,7000,10000,50000,100000,320000,640000,1280000,2500000,500000,7500000,10000000]
count=0
for i in range(len(lis)):
    l=lis[i]
    print(" ")
    print(f"Question for Rs.{levels[i]}")
    print(l[0])
    print(f"a.{l[1]}   b.{l[2]}")
    print(f"c.{l[3]}   d.{l[4]}")
    reply=input("Selected Answer is:")
    if(reply=='a'):
        r=1
    if(reply=='b'):
        r=2
    if(reply=='c'):
        r=3
    if(reply=='d'):
        r=4
    if(l[5]==r):
        print("Congratulations!!!It's the Correct Answer")
        print(f"You won Rs.{levels[i]}")
        count+=1
    else:
        print("Wrong Answer")
        break
if(count>2 and count<=6):
    print(f"You are going home by taking an amount of Rs.{levels[2]}")
elif(count>6 and count<=12):
    print(f"You are going home by taking an amount of Rs.{levels[6]}")
elif(count==13):
    print(f"You are going home by taking an amount of Rs.{levels[12]}")

else:
    print("You are going home taking an amount of Rs.0")

    
