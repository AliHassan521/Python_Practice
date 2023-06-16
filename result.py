name = input("Enter your name : ")
Fname = input("Enter your father name : ")
Cname = input("Enter your college name : ")
Eng = int(input("Enter your english marks : "))
if Eng >= 80:
    Egrd = "A+"
elif Eng >= 75:
    Egrd = "A"
elif Eng >= 70:
    Egrd = "B+"
elif Eng >= 65:
    Egrd = "B"
elif Eng >= 60:
    Egrd = "B-"
elif Eng >= 55:
    Egrd = "C+"
elif Eng >= 50:
    Egrd = "C"
elif Eng >= 33:
    Egrd = "D"
else:
    Egrd = "..."
Urdu = int(input("Enter your urdu marks : "))
if Urdu >= 80:
    Ugrd = "A+"
elif Urdu >= 75:
    Ugrd = "A"
elif Urdu >= 70:
    Ugrd = "B+"
elif Urdu >= 65:
    Ugrd = "B"
elif Urdu >= 60:
    Ugrd = "B-"
elif Urdu >= 55:
    Ugrd = "C+"
elif Urdu >= 50:
    Ugrd = "C"
elif Urdu >= 33:
    Ugrd = "D"
else:
    Ugrd = "..."
Math = int(input("Enter your math marks : "))
if Math >= 80:
    Mgrd = "A+"
elif Math >= 75:
    Mgrd = "A"
elif Math >= 70:
    Mgrd = "B+"
elif Math >= 65:
    Mgrd = "B"
elif Math >= 60:
    Mgrd = "B-"
elif Math >= 55:
    Mgrd = "C+"
elif Math >= 50:
    Mgrd = "C"
elif Math >= 33:
    Mgrd = "D"
else:
    Mgrd = "..."
Chem = int(input("Enter your chemistry marks : "))
if Chem >= 80:
    Cgrd = "A+"
elif Chem >= 75:
    Cgrd = "A"
elif Chem >= 70:
    Cgrd = "B+"
elif Chem >= 65:
    Cgrd = "B"
elif Chem >= 60:
    Cgrd = "B-"
elif Chem >= 55:
    Cgrd = "C+"
elif Chem >= 50:
    Cgrd = "C"
elif Chem >= 33:
    Cgrd = "D"
else:
    Cgrd = "..."
Phy = int(input("Enter your physics marks : "))
if Phy >= 80:
    Pgrd = "A+"
elif Phy >= 75:
    Pgrd = "A"
elif Phy >= 70:
    Pgrd = "B+"
elif Phy >= 65:
    Pgrd = "B"
elif Phy >= 60:
    Pgrd = "B-"
elif Phy >= 55:
    Pgrd = "C+"
elif Phy >= 50:
    Pgrd = "C"
elif Phy >= 33:
    Pgrd = "D"
else:
    Pgrd = "..."
Bio = int(input("Enter your biology marks : "))
if Bio >= 80:
    Bgrd = "A+"
elif Bio >= 75:
    Bgrd = "A"
elif Bio >= 70:
    Bgrd = "B+"
elif Bio >= 65:
    Bgrd = "B"
elif Bio >= 60:
    Bgrd = "B-"
elif Bio >= 55:
    Bgrd = "C+"
elif Bio >= 50:
    Bgrd = "C"
elif Bio >= 33:
    Bgrd = "D"
else:
    Bgrd = "..."
total = Eng + Urdu + Math + Chem + Phy + Bio
if total >= 480:
    tgrd = "A+"
elif total >= 450:
    tgrd = "A"
elif total >= 420:
    tgrd = "B+"
elif total >= 390:
    tgrd = "B"
elif total >= 360:
    tgrd = "B-"
elif total >= 330:
    tgrd = "C+"
elif total >= 300:
    tgrd = "C"
elif total >= 250:
    tgrd = "D"
else:
    Bgrd = "..."
# per = (total / 600) * 100
            
print()
print()
print("................................Result Card...........................")
print()
print()
print("Name                  ",name)
print("Father name           ",Fname)
print("College name          ",Cname)
print()
print("_________________________________________________________________")
print("Subject          |T.Marks        |O.Marks         |Grade        ")
print("_________________________________________________________________")
print("English          |100        ","   |",Eng,"            |",Egrd)
print("_________________________________________________________________")
print("Urdu             |100        ","   |",Urdu,"            |",Ugrd)
print("_________________________________________________________________")
print("Math             |100        ","   |",Math,"            |",Mgrd)
print("_________________________________________________________________")
print("Chemistry        |100        ","   |",Chem,"            |",Cgrd)
print("_________________________________________________________________")
print("Physics          |100        ","   |",Phy,"            |",Pgrd)
print("_________________________________________________________________")
print("Biology          |100        ","   |",Bio,"            |",Bgrd)
print("_________________________________________________________________")
print("Total            |600        ","   |",total,"           |",tgrd)
print()
if tgrd == "A+":
    print("..........Excellent.........")
elif tgrd == "A":
    print("..........Great.........")
elif tgrd == "B+":
    print("..........Good.........")
elif tgrd == "B":
    print("..........Satisfy.........")
elif tgrd == "B-":
    print("..........Improve.........")
elif tgrd == "C+":
    print("..........Not satisfy.........")
elif tgrd == "C":
    print("..........Not Enough.........")
elif tgrd == "D":
    print("..........Just Pass.........")
else:
    print("..........Fail.........")
print()    
