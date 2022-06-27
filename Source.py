#Ahmed Mohammed Ahmed Ali
#TP059731
#Intake: APU1F2002SE
#Resit Assignment

#*******************************************************************************
#***************************** Functions ***************************************

#***************************** Function 1 - Seating arrangment(seat status) ****

def boatseat_view(boatNo):    
    if boatNo == '1':
        boatview= open('#B1.txt','r')
        print('Seat_ID\tAvailbility')
        print(boatview.read())
        print('\n* NOTE:\n0 => Available\n1 => Taken\n')
        chck_proceed = input("Would you like to continue? (y/n): ")
        if chck_proceed == 'y':
            mainmenu()
        else:
            print("You've exit the program!\n- END")
            sys.exit(0)
    elif boatNo == '2':
        boatview= open('#B2.txt','r')
        print('Seat_ID\tAvailbility')
        print(boatview.read())
        print('\n* NOTE:\n0 => Available\n1 => Taken\n')
        chck_proceed = input("Would you like to continue? (y/n): ")
        if chck_proceed == 'y':
            mainmenu()
        else:
            print("You've exit the program!\n- END")
            sys.exit(0)
    elif boatNo == '3':
        boatview= open('#E3.txt','r')
        print('Seat_ID\tAvailbility')
        print(boatview.read())
        print('\n* NOTE:\n0 => Available\n1 => Taken\n')
        chck_proceed = input("Would you like to continue? (y/n): ")
        if chck_proceed == 'y':
            mainmenu()
        else:
            print("You've exit the program!\n- END")
            sys.exit(0)
    elif boatNo == '4':
        boatview= open('#E4.txt','r')
        print('Seat_ID\tAvailbility')
        print(boatview.read())
        print('\n* NOTE:\n0 => Available\n1 => Taken\n')
        chck_proceed = input("Would you like to continue? (y/n): ")
        if chck_proceed == 'y':
            mainmenu()
        else:
            print("You've exit the program!\n- END")
            sys.exit(0)
    elif boatNo == '5':
        boatview= open('#E5.txt','r')
        print('Seat_ID\tAvailbility')
        print(boatview.read())
        print('\n* NOTE:\n0 => Available\n1 => Taken\n')
        chck_proceed = input("Would you like to continue? (y/n): ")
        if chck_proceed == 'y':
            mainmenu()
        else:
            print("You've exit the program!\n- END")
            sys.exit(0)
    elif boatNo == '6':
        boatview= open('#E6.txt','r')
        print('Seat_ID\tAvailbility')
        print(boatview.read())
        print('\n* NOTE:\n0 => Available\n1 => Taken\n')
        chck_proceed = input("Would you like to continue? (y/n): ")
        if chck_proceed == 'y':
            mainmenu()
        else:
            print("You've exit the program!\n- END")
            sys.exit(0)
    elif boatNo == '7':
        boatview= open('#E7.txt','r')
        print('Seat_ID\tAvailbility')
        print(boatview.read())
        print('\n* NOTE:\n0 => Available\n1 => Taken\n')
        chck_proceed = input("Would you like to continue? (y/n): ")
        if chck_proceed == 'y':
            mainmenu()
        else:
            print("You've exit the program!\n- END")
            sys.exit(0)
    elif boatNo == '8':
        boatview= open('#E8.txt','r')
        print('Seat_ID\tAvailbility')
        print(boatview.read())
        print('\n* NOTE:\n0 => Available\n1 => Taken\n')
        chck_proceed = input("Would you like to continue? (y/n): ")
        if chck_proceed == 'y':
            mainmenu()
        else:
            print("You've exit the program!\n- END")
            sys.exit(0)
    elif boatNo == '9':
        boatview= open('#E9.txt','r')
        print('Seat_ID\tAvailbility')
        print(boatview.read())
        print('\n* NOTE:\n0 => Available\n1 => Taken\n')
        chck_proceed = input("Would you like to continue? (y/n): ")
        if chck_proceed == 'y':
            mainmenu()
        else:
            print("You've exit the program!\n- END")
            sys.exit(0)
    elif boatNo == '10':
        boatview= open('#E10.txt','r')
        print('Seat_ID\tAvailbility')
        print(boatview.read())
        print('\n* NOTE:\n0 => Available\n1 => Taken\n')
        chck_proceed = input("Would you like to continue? (y/n): ")
        if chck_proceed == 'y':
            mainmenu()
        else:
            print("You've exit the program!\n- END")
            sys.exit(0)
    else:
        print("Error! Invalid input.\n<Please restart.>")
        sys.exit(0)

#***************************** EXTRA Function 1 - Tesing for seat_check() ****

def seat_checkTest(seatno, boatno):
    if boatno =='1':
        fchecks_r = open('checkings_list.txt','r')
        fboat_r=open('#B1.txt','r')
        fboat_content=str(fboat_r.readlines())
        fboat_r.close()
        fbtlst=fboat_content.split()
        for line in fchecks_r:
            line=line.rstrip()
            if(not seatno in line and not boatno in line):
                continue
            else:
                print("Sorry, this seat has been taken.\n<Please restart.>")
                sys.exit(0)
        else:
            print('Seat is available!')
            fchecks_r.close()
            '''if (seatno =='b1' or seatno=='B1'):
                fbtlst.remove(fbtlst[1])
                fbtlst.insert(1,'1')
                outp=fbtlst[0]+'\t'+fbtlst[1]+'\n'+fbtlst[2]+'\t'+fbtlst[3]+'\n'+fbtlst[4]+'\t'+fbtlst[5]+'\n'+fbtlst[6]+'\t'+fbtlst[7]+'\n'
                fboat_w=open('#B1.txt','w')
                fboat_w.write(outp)
                fboat_w.close()
            elif(seatno =='b2' or seatno=='B2'):
                fbtlst.remove(fbtlst[3])
                fbtlst.insert(3,'1')
                outp=fbtlst[0]+'\t'+fbtlst[1]+'\n'+fbtlst[2]+'\t'+fbtlst[3]+'\n'+fbtlst[4]+'\t'+fbtlst[5]+'\n'+fbtlst[6]+'\t'+fbtlst[7]+'\n'
                fboat_w=open('#B1.txt','w')
                fboat_w.write(outp)
                fboat_w.close()
            elif(seatno =='b3' or seatno=='B3'):
                fbtlst.remove(fbtlst[5])
                fbtlst.insert(5,'1')
                outp=fbtlst[0]+'\t'+fbtlst[1]+'\n'+fbtlst[2]+'\t'+fbtlst[3]+'\n'+fbtlst[4]+'\t'+fbtlst[5]+'\n'+fbtlst[6]+'\t'+fbtlst[7]+'\n'
                fboat_w=open('#B1.txt','w')
                fboat_w.write(outp)
                fboat_w.close()
            elif(seatno =='b4' or seatno=='B4'):
                fbtlst.remove(fbtlst[7])
                fbtlst.insert(7,'1')
                outp=fbtlst[0]+'\t'+fbtlst[1]+'\n'+fbtlst[2]+'\t'+fbtlst[3]+'\n'+fbtlst[4]+'\t'+fbtlst[5]+'\n'+fbtlst[6]+'\t'+fbtlst[7]+'\n'
                fboat_w=open('#B1.txt','w')
                fboat_w.write(outp)
                fboat_w.close()'''
                
    return seatno, boatno

#***************************** Function 2 - Seat Check *********************
        
def seat_check(seat, boat):
    #Business Class:
    if boat =='1':
        boatfile_r = open('#B1.txt','r')
        fcontent= str(boatfile_r.read())
        flst = fcontent.split()
        if(seat=='B1' or seat=='b1'):
            if flst[1]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[1])
                flst.insert(1,'1')
                print("Seat available")
        elif(seat=='B2' or seat=='b2'):
            if flst[3]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[3])
                flst.insert(3,'1')
                print("Seat available!")
        elif(seat=='B3' or seat=='b3'):
            if flst[5]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[5])
                flst.insert(5,'1')
                print("Seat available")
        elif(seat=='B4' or seat=='b4'):
            if flst[7]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[7])
                flst.insert(7,'1')
                print("Seat available")
                
        outp=flst[0]+'\t'+flst[1]+'\n'+flst[2]+'\t'+flst[3]+'\n'+flst[4]+'\t'+flst[5]+'\n'+flst[6]+'\t'+flst[7]
        boatfile_w=open('#B1.txt','w+')
        boatfile_w.write(outp)            
        
    elif boat =='2':
        boatfile_r = open('#B2.txt','r')
        fcontent= str(boatfile_r.read())
        flst = fcontent.split()
        if(seat=='B1' or seat=='b1'):
            if flst[1]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[1])
                flst.insert(1,'1')
                print("Seat available")
        elif(seat=='B2' or seat=='b2'):
            if flst[3]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[3])
                flst.insert(3,'1')
                print("Seat available!")
        elif(seat=='B3' or seat=='b3'):
            if flst[5]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[5])
                flst.insert(5,'1')
                print("Seat available")
        elif(seat=='B4' or seat=='b4'):
            if flst[7]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[7])
                flst.insert(7,'1')
                print("Seat available")
                
        outp=flst[0]+'\t'+flst[1]+'\n'+flst[2]+'\t'+flst[3]+'\n'+flst[4]+'\t'+flst[5]+'\n'+flst[6]+'\t'+flst[7]+'\n'
        boatfile_w=open('#B2.txt','w+')
        boatfile_w.write(outp)
        #Economy Class:
    elif boat=='3':
        boatfile_r = open('#E3.txt','r')
        fcontent= str(boatfile_r.read())
        flst = fcontent.split()
        if(seat=='E1' or seat=='e1'):
            if flst[1]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[1])
                flst.insert(1,'1')
                print("Seat available!")
        elif(seat=='E2' or seat=='e2'):
            if flst[3]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[3])
                flst.insert(3,'1')
                print("Seat available!")
        elif(seat=='E3' or seat=='e3'):
            if flst[5]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[5])
                flst.insert(5,'1')
                print("Seat available!")
        elif(seat=='E4' or seat=='e4'):
            if flst[7]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[7])
                flst.insert(7,'1')
                print("Seat available!")
        elif(seat=='E5' or seat=='e5'):
            if flst[9]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[9])
                flst.insert(9,'1')
                print("Seat available!")
        elif(seat=='E6' or seat=='e6'):
            if flst[11]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[11])
                flst.insert(11,'1')
                print("Seat available!")
        elif(seat=='E7' or seat=='e7'):
            if flst[13]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[13])
                flst.insert(13,'1')
                print("Seat available!")
        elif(seat=='E8' or seat=='e8'):
            if flst[15]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[15])
                flst.insert(15,'1')
                print("Seat available!")
                
                
        outp=flst[0]+'\t'+flst[1]+'\n'+flst[2]+'\t'+flst[3]+'\n'+flst[4]+'\t'+flst[5]+'\n'+flst[6]+'\t'+flst[7]+'\n'+flst[8]+'\t'+flst[9]+'\n'+flst[10]+'\t'+flst[11]+'\n'+flst[12]+'\t'+flst[13]+'\n'+flst[14]+'\t'+flst[15]+'\n'
        boatfile_w=open('#E3.txt','w+')
        boatfile_w.write(outp)
    elif boat=='4':
        boatfile_r = open('#E4.txt','r')
        fcontent= str(boatfile_r.read())
        flst = fcontent.split()
        if(seat=='E1' or seat=='e1'):
            if flst[1]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[1])
                flst.insert(1,'1')
                print("Seat available!")
        elif(seat=='E2' or seat=='e2'):
            if flst[3]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[3])
                flst.insert(3,'1')
                print("Seat available!")
        elif(seat=='E3' or seat=='e3'):
            if flst[5]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[5])
                flst.insert(5,'1')
                print("Seat available!")
        elif(seat=='E4' or seat=='e4'):
            if flst[7]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[7])
                flst.insert(7,'1')
                print("Seat available!")
        elif(seat=='E5' or seat=='e5'):
            if flst[9]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[9])
                flst.insert(9,'1')
                print("Seat available!")
        elif(seat=='E6' or seat=='e6'):
            if flst[11]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[11])
                flst.insert(11,'1')
                print("Seat available!")
        elif(seat=='E7' or seat=='e7'):
            if flst[13]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[13])
                flst.insert(13,'1')
                print("Seat available!")
        elif(seat=='E8' or seat=='e8'):
            if flst[15]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[15])
                flst.insert(15,'1')
                print("Seat available!")
                
                
        outp=flst[0]+'\t'+flst[1]+'\n'+flst[2]+'\t'+flst[3]+'\n'+flst[4]+'\t'+flst[5]+'\n'+flst[6]+'\t'+flst[7]+'\n'+flst[8]+'\t'+flst[9]+'\n'+flst[10]+'\t'+flst[11]+'\n'+flst[12]+'\t'+flst[13]+'\n'+flst[14]+'\t'+flst[15]+'\n'
        boatfile_w=open('#E4.txt','w+')
        boatfile_w.write(outp)
    elif boat=='5':
        boatfile_r = open('#E5.txt','r')
        fcontent= str(boatfile_r.read())
        flst = fcontent.split()
        if(seat=='E1' or seat=='e1'):
            if flst[1]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[1])
                flst.insert(1,'1')
                print("Seat available!")
        elif(seat=='E2' or seat=='e2'):
            if flst[3]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[3])
                flst.insert(3,'1')
                print("Seat available!")
        elif(seat=='E3' or seat=='e3'):
            if flst[5]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[5])
                flst.insert(5,'1')
                print("Seat available!")
        elif(seat=='E4' or seat=='e4'):
            if flst[7]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[7])
                flst.insert(7,'1')
                print("Seat available!")
        elif(seat=='E5' or seat=='e5'):
            if flst[9]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[9])
                flst.insert(9,'1')
                print("Seat available!")
        elif(seat=='E6' or seat=='e6'):
            if flst[11]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[11])
                flst.insert(11,'1')
                print("Seat available!")
        elif(seat=='E7' or seat=='e7'):
            if flst[13]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[13])
                flst.insert(13,'1')
                print("Seat available!")
        elif(seat=='E8' or seat=='e8'):
            if flst[15]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[15])
                flst.insert(15,'1')
                print("Seat available!")
                
                
        outp=flst[0]+'\t'+flst[1]+'\n'+flst[2]+'\t'+flst[3]+'\n'+flst[4]+'\t'+flst[5]+'\n'+flst[6]+'\t'+flst[7]+'\n'+flst[8]+'\t'+flst[9]+'\n'+flst[10]+'\t'+flst[11]+'\n'+flst[12]+'\t'+flst[13]+'\n'+flst[14]+'\t'+flst[15]+'\n'
        boatfile_w=open('#E5.txt','w+')
        boatfile_w.write(outp)
    elif boat=='6':
        boatfile_r = open('#E6.txt','r')
        fcontent= str(boatfile_r.read())
        flst = fcontent.split()
        if(seat=='E1' or seat=='e1'):
            if flst[1]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[1])
                flst.insert(1,'1')
                print("Seat available!")
        elif(seat=='E2' or seat=='e2'):
            if flst[3]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[3])
                flst.insert(3,'1')
                print("Seat available!")
        elif(seat=='E3' or seat=='e3'):
            if flst[5]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[5])
                flst.insert(5,'1')
                print("Seat available!")
        elif(seat=='E4' or seat=='e4'):
            if flst[7]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[7])
                flst.insert(7,'1')
                print("Seat available!")
        elif(seat=='E5' or seat=='e5'):
            if flst[9]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[9])
                flst.insert(9,'1')
                print("Seat available!")
        elif(seat=='E6' or seat=='e6'):
            if flst[11]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[11])
                flst.insert(11,'1')
                print("Seat available!")
        elif(seat=='E7' or seat=='e7'):
            if flst[13]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[13])
                flst.insert(13,'1')
                print("Seat available!")
        elif(seat=='E8' or seat=='e8'):
            if flst[15]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[15])
                flst.insert(15,'1')
                print("Seat available!")
                
                
        outp=flst[0]+'\t'+flst[1]+'\n'+flst[2]+'\t'+flst[3]+'\n'+flst[4]+'\t'+flst[5]+'\n'+flst[6]+'\t'+flst[7]+'\n'+flst[8]+'\t'+flst[9]+'\n'+flst[10]+'\t'+flst[11]+'\n'+flst[12]+'\t'+flst[13]+'\n'+flst[14]+'\t'+flst[15]+'\n'
        boatfile_w=open('#E6.txt','w+')
        boatfile_w.write(outp)
    elif boat=='7':
        boatfile_r = open('#E7.txt','r')
        fcontent= str(boatfile_r.read())
        flst = fcontent.split()
        if(seat=='E1' or seat=='e1'):
            if flst[1]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[1])
                flst.insert(1,'1')
                print("Seat available!")
        elif(seat=='E2' or seat=='e2'):
            if flst[3]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[3])
                flst.insert(3,'1')
                print("Seat available!")
        elif(seat=='E3' or seat=='e3'):
            if flst[5]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[5])
                flst.insert(5,'1')
                print("Seat available!")
        elif(seat=='E4' or seat=='e4'):
            if flst[7]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[7])
                flst.insert(7,'1')
                print("Seat available!")
        elif(seat=='E5' or seat=='e5'):
            if flst[9]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[9])
                flst.insert(9,'1')
                print("Seat available!")
        elif(seat=='E6' or seat=='e6'):
            if flst[11]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[11])
                flst.insert(11,'1')
                print("Seat available!")
        elif(seat=='E7' or seat=='e7'):
            if flst[13]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[13])
                flst.insert(13,'1')
                print("Seat available!")
        elif(seat=='E8' or seat=='e8'):
            if flst[15]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[15])
                flst.insert(15,'1')
                print("Seat available!")
                
                
        outp=flst[0]+'\t'+flst[1]+'\n'+flst[2]+'\t'+flst[3]+'\n'+flst[4]+'\t'+flst[5]+'\n'+flst[6]+'\t'+flst[7]+'\n'+flst[8]+'\t'+flst[9]+'\n'+flst[10]+'\t'+flst[11]+'\n'+flst[12]+'\t'+flst[13]+'\n'+flst[14]+'\t'+flst[15]+'\n'
        boatfile_w=open('#E7.txt','w+')
        boatfile_w.write(outp)
    elif boat=='8':
        boatfile_r = open('#E8.txt','r')
        fcontent= str(boatfile_r.read())
        flst = fcontent.split()
        if(seat=='E1' or seat=='e1'):
            if flst[1]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[1])
                flst.insert(1,'1')
                print("Seat available!")
        elif(seat=='E2' or seat=='e2'):
            if flst[3]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[3])
                flst.insert(3,'1')
                print("Seat available!")
        elif(seat=='E3' or seat=='e3'):
            if flst[5]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[5])
                flst.insert(5,'1')
                print("Seat available!")
        elif(seat=='E4' or seat=='e4'):
            if flst[7]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[7])
                flst.insert(7,'1')
                print("Seat available!")
        elif(seat=='E5' or seat=='e5'):
            if flst[9]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[9])
                flst.insert(9,'1')
                print("Seat available!")
        elif(seat=='E6' or seat=='e6'):
            if flst[11]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[11])
                flst.insert(11,'1')
                print("Seat available!")
        elif(seat=='E7' or seat=='e7'):
            if flst[13]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[13])
                flst.insert(13,'1')
                print("Seat available!")
        elif(seat=='E8' or seat=='e8'):
            if flst[15]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[15])
                flst.insert(15,'1')
                print("Seat available!")
                
                
        outp=flst[0]+'\t'+flst[1]+'\n'+flst[2]+'\t'+flst[3]+'\n'+flst[4]+'\t'+flst[5]+'\n'+flst[6]+'\t'+flst[7]+'\n'+flst[8]+'\t'+flst[9]+'\n'+flst[10]+'\t'+flst[11]+'\n'+flst[12]+'\t'+flst[13]+'\n'+flst[14]+'\t'+flst[15]+'\n'
        boatfile_w=open('#E8.txt','w+')
        boatfile_w.write(outp)
    elif boat=='9':
        boatfile_r = open('#E9.txt','r')
        fcontent= str(boatfile_r.read())
        flst = fcontent.split()
        if(seat=='E1' or seat=='e1'):
            if flst[1]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[1])
                flst.insert(1,'1')
                print("Seat available!")
        elif(seat=='E2' or seat=='e2'):
            if flst[3]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[3])
                flst.insert(3,'1')
                print("Seat available!")
        elif(seat=='E3' or seat=='e3'):
            if flst[5]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[5])
                flst.insert(5,'1')
                print("Seat available!")
        elif(seat=='E4' or seat=='e4'):
            if flst[7]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[7])
                flst.insert(7,'1')
                print("Seat available!")
        elif(seat=='E5' or seat=='e5'):
            if flst[9]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[9])
                flst.insert(9,'1')
                print("Seat available!")
        elif(seat=='E6' or seat=='e6'):
            if flst[11]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[11])
                flst.insert(11,'1')
                print("Seat available!")
        elif(seat=='E7' or seat=='e7'):
            if flst[13]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[13])
                flst.insert(13,'1')
                print("Seat available!")
        elif(seat=='E8' or seat=='e8'):
            if flst[15]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[15])
                flst.insert(15,'1')
                print("Seat available!")
                
                
        outp=flst[0]+'\t'+flst[1]+'\n'+flst[2]+'\t'+flst[3]+'\n'+flst[4]+'\t'+flst[5]+'\n'+flst[6]+'\t'+flst[7]+'\n'+flst[8]+'\t'+flst[9]+'\n'+flst[10]+'\t'+flst[11]+'\n'+flst[12]+'\t'+flst[13]+'\n'+flst[14]+'\t'+flst[15]+'\n'
        boatfile_w=open('#E9.txt','w+')
        boatfile_w.write(outp)
    elif boat=='10':
        boatfile_r = open('#E10.txt','r')
        fcontent= str(boatfile_r.read())
        flst = fcontent.split()
        if(seat=='E1' or seat=='e1'):
            if flst[1]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[1])
                flst.insert(1,'1')
                print("Seat available!")
        elif(seat=='E2' or seat=='e2'):
            if flst[3]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[3])
                flst.insert(3,'1')
                print("Seat available!")
        elif(seat=='E3' or seat=='e3'):
            if flst[5]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[5])
                flst.insert(5,'1')
                print("Seat available!")
        elif(seat=='E4' or seat=='e4'):
            if flst[7]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[7])
                flst.insert(7,'1')
                print("Seat available!")
        elif(seat=='E5' or seat=='e5'):
            if flst[9]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[9])
                flst.insert(9,'1')
                print("Seat available!")
        elif(seat=='E6' or seat=='e6'):
            if flst[11]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[11])
                flst.insert(11,'1')
                print("Seat available!")
        elif(seat=='E7' or seat=='e7'):
            if flst[13]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[13])
                flst.insert(13,'1')
                print("Seat available!")
        elif(seat=='E8' or seat=='e8'):
            if flst[15]=='1':
                print("Sorry, that seat's taken.")
                sys.exit(0)
            else:
                flst.remove(flst[15])
                flst.insert(15,'1')
                print("Seat available!")
                
                
        outp=flst[0]+'\t'+flst[1]+'\n'+flst[2]+'\t'+flst[3]+'\n'+flst[4]+'\t'+flst[5]+'\n'+flst[6]+'\t'+flst[7]+'\n'+flst[8]+'\t'+flst[9]+'\n'+flst[10]+'\t'+flst[11]+'\n'+flst[12]+'\t'+flst[13]+'\n'+flst[14]+'\t'+flst[15]+'\n'
        boatfile_w=open('#E10.txt','w+')
        boatfile_w.write(outp)
        
            
    else:
        print("Error! Invalid input.\n<Please restart.>")
        sys.exit(0)
        
    boatfile_w.close()        
    boatfile_r.close()
    #boatfile_a.close()
    return seat, boat

#***************************** Function 3 - ticket puchase ********************

def ticket_purchase():
    choiceP = input("PURCHASING MODULE\nPlease select an option\nB – to purchase ticket for Business class\nE – to purchase ticket for Economy class\nM – to return to Main Menu\n")
    if(choiceP=='B' or choiceP =='b'):
        
        print("Please enter the following: ")
        name = input('Your name:')
        cust_id= "#C"+str(random.randint(1,9999))
        gender= input("Your gender (M/F/X): ")
        if(gender!='M' and gender!='F' and gender!='X'):
            print("Error! Please select either M - Male, F - Female, X- Non-binary/Prefer not to say.\n<Please restart.>")
            sys.exit(0)
        age=int(input("Please enter your age: "))
        if age<10:
            print("Children below the age of 10 are not advised to take this tour.\n<Please restart.>")
            sys.exit(0) 
        boat_id = input("Chosen boat's ID (Choose: 1-2): ")
        if(int(boat_id)<1 or int(boat_id)>2):
            print("Error!")
            sys.exit(0)
            
        #elif boat_id=='1':

        #elif boat_id=='2':
           
        seat_id = input("Seat ID (Choose: B1-B4): ")
        if(seat_id!='b1' and seat_id!='b2' and seat_id!='b3' and seat_id!='b4' and seat_id!='B1' and seat_id!='B2' and seat_id!='B3' and seat_id!='B4'):
            print("Error! Invalid input.\n<Please restart.>")
            sys.exit(0)
            
        seat_check(seat_id, boat_id)
            
        dep_time = input("\nDeparture times:\n'8' - 8AM\n'10' - 10AM\n'12' - 12PM\n'2' - 2PM\n\nSelect your option: ")
        if(dep_time=='8' or dep_time=='10'):
            timeform= " :00 AM"
        elif(dep_time=='12' or dep_time=='2'):
            timeform= " :00 PM"
        else:
            print("Error! Invalid input.\n<Please restart.>")
            sys.exit(0)
        dep_month = int(input("\nDate: \nMonth of departure (Choose: 1-12): "))
        if(dep_month>12 or dep_month<1):
            print("Error! Choose from 1 to 12.\n<Please restart.>")
            sys.exit(0)
        else:
            dep_day= int(input("Day of departure (Choose:1-31): "))
            if (dep_day<1 or dep_day>31):
                print("Error! Choose from 1 to 31.\n<Please restart.>")
                sys.exit(0)
            else:
                pass
        checkings_list_a = open('checkings_list.txt','a')
        checkings_list_a.write("\n"+name+"\t"+cust_id+" \t"+gender+" \t"+str(age)+" \t"+boat_id+"\t"+seat_id+"\t"+dep_time+"\t"+dep_Date(dep_day, dep_month))
        checkings_list_a.close()
        #seatstr1='0'
        #seatstr2='0'
        #seatstr3='0'
        #seatstr4='0'
        if boat_id=='1':
            boatfr=open('#B1.txt','r')
            seatlst = (boatfr.read()).split()
            if seatlst[1]=='0':
                seatstr1= "B1 - 0"
            elif seatlst[1]=='1':
                seatstr1= "B1 - 1"
            if seatlst[3]=='0':
                seatstr2= "B2 - 0"
            elif seatlst[3]=='1':
                seatstr2= "B2 - 1"
            if seatlst[5]=='0':
                seatstr3= "B3 - 0"
            elif seatlst[5]=='1':
                seatstr3= "B3 - 1"
            if seatlst[7]=='0':
                seatstr4= "B4 - 0"
            elif seatlst[7]=='1':
                seatstr4= "B4 - 1"
        elif boat_id=='2':
            boatfr=open('#B2.txt','r')
            seatlst = (boatfr.read()).split()
            if seatlst[1]=='0':
                seatstr1= "B1 - 0"
            elif seatlst[1]=='1':
                seatstr1= "B1 - 1"
            if seatlst[3]=='0':
                seatstr2= "B2 - 0"
            elif seatlst[3]=='1':
                seatstr2= "B2 - 1"
            if seatlst[5]=='0':
                seatstr3= "B3 - 0"
            elif seatlst[5]=='1':
                seatstr3= "B3 - 1"
            if seatlst[7]=='0':
                seatstr4= "B4 - 0"
            elif seatlst[7]=='1':
                seatstr4= "B4 - 1"

        boatfr.close()        
        print("\n<< You've successfully checked in! >>\n See you there!\n")
        print("\tYour ticket:\n")
        # Ticket layout
        print("""*************************************************************
        * Boat ID: #"""+boat_id+""" Date: """+dep_Date(dep_day, dep_month)+"""  Time: """+dep_time+timeform+"""
*************************************************************
                        * BUSINESS CLASS *
*************************************************************
                    * """+seatstr1+""" * """+seatstr2+""" *
*************************************************************
                    * """+seatstr3+""" * """+seatstr4+""" *
*************************************************************""")
        mainmenu()
        
        
    elif(choiceP=='E' or choiceP =='e'):
        
        print("Please enter the following: ")
        name = input('Your name:')
        cust_id= "#C"+str(random.randint(1,9999))
        gender= input("Your gender (M/F/X): ")
        if(gender!='M' and gender!='F' and gender!='X'):
            print("Error! Please select either M - Male, F - Female, X- Non-binary/Prefer not to say.\n<Please restart.>")
            sys.exit(0)
        age=int(input("Please enter your age: "))
        if age<10:
            print("Children below the age of 10 are not advised to take this tour.\n<Please restart.>")
            sys.exit(0)
        boat_id = input("Chosen boat's ID (Choose: 3-10): ")
        if(int(boat_id)<3 or int(boat_id)>10):
            print("Error!")
            sys.exit(0)
        seat_id = input("Please enter Seat ID (Choose: E1-E8: ")
        if(seat_id!='E1' and seat_id!='E2' and seat_id!='E3' and seat_id!='E4' and seat_id!='E5' and seat_id!='E6' and seat_id!='E7' and seat_id!='E8' and seat_id!='e1' and seat_id!='e2' and seat_id!='e3' and seat_id!='e4' and seat_id!='e5' and seat_id!='e6' and seat_id!='e7' and seat_id!='e8'):
            print("Error! Invlaid input.\n<Please restart.>")
            sys.exit(0)

        seat_check(seat_id, boat_id)
            
        dep_time = input("Departure times:\n'8' - 8AM\n'10' - 10AM\n'12' - 12PM\n'2' - 2PM\n\nSelect your option: ")
        if(dep_time=='8' or dep_time=='10'):
            timeform= " :00 AM"
        elif(dep_time=='12' or dep_time=='2'):
            timeform= " :00 PM"
        else:
            print("Error! Invalid input.\n<Please restart.>")
            sys.exit(0)
        dep_month = int(input("\nDate: \nMonth of departure (Choose: 1-12): "))
        if(dep_month>12 or dep_month<1):
            print("Error! Choose from 1 to 12.\n<Please restart.>")
            sys.exit(0)
        else:
            dep_day= int(input("Day of departure (Choose:1-31): "))
            if (dep_day<1 or dep_day>31):
                print("Error! Choose from 1 to 31.\n<Please restart.>")
                sys.exit(0)
            else:
                pass
        checkings_list_a = open('checkings_list.txt','a')
        checkings_list_a.write("\n"+name+"\t"+cust_id+" \t"+gender+" \t"+str(age)+" \t"+boat_id+"\t"+seat_id+"\t"+dep_time+"\t"+dep_Date(dep_day, dep_month))
        checkings_list_a.close()
        #seatstr1='0'
        #seatstr2='0'
        #seatstr3='0'
        #seatstr4='0'
        #seatstr5='0'
        #seatstr6='0'
        #seatstr7='0'
        #seatstr8='0'
        if boat_id=='3':
            boatfr=open('#E3.txt','r')
            seatlst = (boatfr.read()).split()
            if seatlst[1]=='0':
                eseatstr1= "E1 - 0"
            elif seatlst[1]=='1':
                eseatstr1= "E1 - 1"
            if seatlst[3]=='0':
                eseatstr2= "E2 - 0"
            elif seatlst[3]=='1':
                eseatstr2= "E2 - 1"
            if seatlst[5]=='0':
                eseatstr3= "E3 - 0"
            elif seatlst[5]=='1':
                eseatstr3= "E3 - 1"
            if seatlst[7]=='0':
                eseatstr4= "E4 - 0"
            elif seatlst[7]=='1':
                eseatstr4= "E4 - 1"
            if seatlst[9]=='0':
                eseatstr5= "E5 - 0"
            elif seatlst[9]=='1':
                eseatstr5= "E5 - 1"
            if seatlst[11]=='0':
                eseatstr6= "E6 - 0"
            elif seatlst[11]=='1':
                eseatstr6= "E6 - 1"
            if seatlst[13]=='0':
                eseatstr7= "E7 - 0"
            elif seatlst[13]=='1':
                eseatstr7= "E7 - 1"
            if seatlst[15]=='0':
                eseatstr8= "E8 - 0"
            elif seatlst[15]=='1':
                eseatstr8= "E8 - 1"
        elif boat_id=='4':
            boatfr=open('#E4.txt','r')
            seatlst = (boatfr.read()).split()
            if seatlst[1]=='0':
                eseatstr1= "E1 - 0"
            elif seatlst[1]=='1':
                eseatstr1= "E1 - 1"
            if seatlst[3]=='0':
                eseatstr2= "E2 - 0"
            elif seatlst[3]=='1':
                eseatstr2= "E2 - 1"
            if seatlst[5]=='0':
                eseatstr3= "E3 - 0"
            elif seatlst[5]=='1':
                eseatstr3= "E3 - 1"
            if seatlst[7]=='0':
                eseatstr4= "E4 - 0"
            elif seatlst[7]=='1':
                eseatstr4= "E4 - 1"
            if seatlst[9]=='0':
                eseatstr5= "E5 - 0"
            elif seatlst[9]=='1':
                eseatstr5= "E5 - 1"
            if seatlst[11]=='0':
                eseatstr6= "E6 - 0"
            elif seatlst[11]=='1':
                eseatstr6= "E6 - 1"
            if seatlst[13]=='0':
                eseatstr7= "E7 - 0"
            elif seatlst[13]=='1':
                eseatstr7= "E7 - 1"
            if seatlst[15]=='0':
                eseatstr8= "E8 - 0"
            elif seatlst[15]=='1':
                eseatstr8= "E8 - 1"
        elif boat_id=='5':
            boatfr=open('#E5.txt','r')
            seatlst = (boatfr.read()).split()
            if seatlst[1]=='0':
                eseatstr1= "E1 - 0"
            elif seatlst[1]=='1':
                eseatstr1= "E1 - 1"
            if seatlst[3]=='0':
                eseatstr2= "E2 - 0"
            elif seatlst[3]=='1':
                eseatstr2= "E2 - 1"
            if seatlst[5]=='0':
                eseatstr3= "E3 - 0"
            elif seatlst[5]=='1':
                eseatstr3= "E3 - 1"
            if seatlst[7]=='0':
                eseatstr4= "E4 - 0"
            elif seatlst[7]=='1':
                eseatstr4= "E4 - 1"
            if seatlst[9]=='0':
                eseatstr5= "E5 - 0"
            elif seatlst[9]=='1':
                eseatstr5= "E5 - 1"
            if seatlst[11]=='0':
                eseatstr6= "E6 - 0"
            elif seatlst[11]=='1':
                eseatstr6= "E6 - 1"
            if seatlst[13]=='0':
                eseatstr7= "E7 - 0"
            elif seatlst[13]=='1':
                eseatstr7= "E7 - 1"
            if seatlst[15]=='0':
                eseatstr8= "E8 - 0"
            elif seatlst[15]=='1':
                eseatstr8= "E8 - 1"
        elif boat_id=='6':
            boatfr=open('#E6.txt','r')
            seatlst = (boatfr.read()).split()
            if seatlst[1]=='0':
                eseatstr1= "E1 - 0"
            elif seatlst[1]=='1':
                eseatstr1= "E1 - 1"
            if seatlst[3]=='0':
                eseatstr2= "E2 - 0"
            elif seatlst[3]=='1':
                eseatstr2= "E2 - 1"
            if seatlst[5]=='0':
                eseatstr3= "E3 - 0"
            elif seatlst[5]=='1':
                eseatstr3= "E3 - 1"
            if seatlst[7]=='0':
                eseatstr4= "E4 - 0"
            elif seatlst[7]=='1':
                eseatstr4= "E4 - 1"
            if seatlst[9]=='0':
                eseatstr5= "E5 - 0"
            elif seatlst[9]=='1':
                eseatstr5= "E5 - 1"
            if seatlst[11]=='0':
                eseatstr6= "E6 - 0"
            elif seatlst[11]=='1':
                eseatstr6= "E6 - 1"
            if seatlst[13]=='0':
                eseatstr7= "E7 - 0"
            elif seatlst[13]=='1':
                eseatstr7= "E7 - 1"
            if seatlst[15]=='0':
                eseatstr8= "E8 - 0"
            elif seatlst[15]=='1':
                eseatstr8= "E8 - 1"
        elif boat_id=='7':
            boatfr=open('#E7.txt','r')
            seatlst = (boatfr.read()).split()
            if seatlst[1]=='0':
                eseatstr1= "E1 - 0"
            elif seatlst[1]=='1':
                eseatstr1= "E1 - 1"
            if seatlst[3]=='0':
                eseatstr2= "E2 - 0"
            elif seatlst[3]=='1':
                eseatstr2= "E2 - 1"
            if seatlst[5]=='0':
                eseatstr3= "E3 - 0"
            elif seatlst[5]=='1':
                eseatstr3= "E3 - 1"
            if seatlst[7]=='0':
                eseatstr4= "E4 - 0"
            elif seatlst[7]=='1':
                eseatstr4= "E4 - 1"
            if seatlst[9]=='0':
                eseatstr5= "E5 - 0"
            elif seatlst[9]=='1':
                eseatstr5= "E5 - 1"
            if seatlst[11]=='0':
                eseatstr6= "E6 - 0"
            elif seatlst[11]=='1':
                eseatstr6= "E6 - 1"
            if seatlst[13]=='0':
                eseatstr7= "E7 - 0"
            elif seatlst[13]=='1':
                eseatstr7= "E7 - 1"
            if seatlst[15]=='0':
                eseatstr8= "E8 - 0"
            elif seatlst[15]=='1':
                eseatstr8= "E8 - 1"
        elif boat_id=='8':
            boatfr=open('#E8.txt','r')
            seatlst = (boatfr.read()).split()
            if seatlst[1]=='0':
                eseatstr1= "E1 - 0"
            elif seatlst[1]=='1':
                eseatstr1= "E1 - 1"
            if seatlst[3]=='0':
                eseatstr2= "E2 - 0"
            elif seatlst[3]=='1':
                eseatstr2= "E2 - 1"
            if seatlst[5]=='0':
                eseatstr3= "E3 - 0"
            elif seatlst[5]=='1':
                eseatstr3= "E3 - 1"
            if seatlst[7]=='0':
                eseatstr4= "E4 - 0"
            elif seatlst[7]=='1':
                eseatstr4= "E4 - 1"
            if seatlst[9]=='0':
                eseatstr5= "E5 - 0"
            elif seatlst[9]=='1':
                eseatstr5= "E5 - 1"
            if seatlst[11]=='0':
                eseatstr6= "E6 - 0"
            elif seatlst[11]=='1':
                eseatstr6= "E6 - 1"
            if seatlst[13]=='0':
                eseatstr7= "E7 - 0"
            elif seatlst[13]=='1':
                eseatstr7= "E7 - 1"
            if seatlst[15]=='0':
                eseatstr8= "E8 - 0"
            elif seatlst[15]=='1':
                eseatstr8= "E8 - 1"
        elif boat_id=='9':
            boatfr=open('#E9.txt','r')
            seatlst = (boatfr.read()).split()
            if seatlst[1]=='0':
                eseatstr1= "E1 - 0"
            elif seatlst[1]=='1':
                eseatstr1= "E1 - 1"
            if seatlst[3]=='0':
                eseatstr2= "E2 - 0"
            elif seatlst[3]=='1':
                eseatstr2= "E2 - 1"
            if seatlst[5]=='0':
                eseatstr3= "E3 - 0"
            elif seatlst[5]=='1':
                eseatstr3= "E3 - 1"
            if seatlst[7]=='0':
                eseatstr4= "E4 - 0"
            elif seatlst[7]=='1':
                eseatstr4= "E4 - 1"
            if seatlst[9]=='0':
                eseatstr5= "E5 - 0"
            elif seatlst[9]=='1':
                eseatstr5= "E5 - 1"
            if seatlst[11]=='0':
                eseatstr6= "E6 - 0"
            elif seatlst[11]=='1':
                eseatstr6= "E6 - 1"
            if seatlst[13]=='0':
                eseatstr7= "E7 - 0"
            elif seatlst[13]=='1':
                eseatstr7= "E7 - 1"
            if seatlst[15]=='0':
                eseatstr8= "E8 - 0"
            elif seatlst[15]=='1':
                eseatstr8= "E8 - 1"
        elif boat_id=='10':
            boatfr=open('#E10.txt','r')
            seatlst = (boatfr.read()).split()
            if seatlst[1]=='0':
                eseatstr1= "E1 - 0"
            elif seatlst[1]=='1':
                eseatstr1= "E1 - 1"
            if seatlst[3]=='0':
                eseatstr2= "E2 - 0"
            elif seatlst[3]=='1':
                eseatstr2= "E2 - 1"
            if seatlst[5]=='0':
                eseatstr3= "E3 - 0"
            elif seatlst[5]=='1':
                eseatstr3= "E3 - 1"
            if seatlst[7]=='0':
                eseatstr4= "E4 - 0"
            elif seatlst[7]=='1':
                eseatstr4= "E4 - 1"
            if seatlst[9]=='0':
                eseatstr5= "E5 - 0"
            elif seatlst[9]=='1':
                eseatstr5= "E5 - 1"
            if seatlst[11]=='0':
                eseatstr6= "E6 - 0"
            elif seatlst[11]=='1':
                eseatstr6= "E6 - 1"
            if seatlst[13]=='0':
                eseatstr7= "E7 - 0"
            elif seatlst[13]=='1':
                eseatstr7= "E7 - 1"
            if seatlst[15]=='0':
                eseatstr8= "E8 - 0"
            elif seatlst[15]=='1':
                eseatstr8= "E8 - 1"

        boatfr.close()        
        print("\n<< You've successfully checked in! >>\n See you there!\n")
        print("Your ticket: ")
        # Ticket layout:
        print("""*************************************************************
    * Boat ID: """+boat_id+""" Date: """+dep_Date(dep_day, dep_month)+""" Time: """+dep_time+timeform+""" *
*************************************************************
                      * ECONOMY CLASS *
*************************************************************
                    * """+eseatstr1+""" * """+eseatstr2+""" *
*************************************************************
                    * """+eseatstr3+""" * """+eseatstr4+""" *
*************************************************************
                    * """+eseatstr5+""" * """+eseatstr6+""" *
*************************************************************
                    * """+eseatstr7+""" * """+eseatstr8+""" *
*************************************************************
""")
        mainmenu()
     
    elif(choiceP=='M' or choiceP =='m'):
        mainmenu() #return to main menu
    else:
        print("Wrong input!\n<Please restart program.>")

#***************************** Function 4 - Departure date **********************

def dep_Date(dd, mm):
    return str(dd) + " / " + str(mm) + " / 2020" 
    
            
#***************************** Function 5 - View seats and boat info *************
        
def seat_view():
    choiceV =input("\n<<===========SEATING ARRANGEMENT MODULE===========>>\nS- to select Boat ID\nT- to select Trip Time\n")
    if (choiceV=='S' or choiceV=='s'):
        boat_list = open('boat_list.txt','r')
        print('\nBoat_ID\tBoat_type\tTotal_seats\tSeat_names\n')
        print(boat_list.read())
        choice_proceed=input("\nType:\n1 - To view seating arrangement/availability in boat of choice\n2 - To select a boat ID\nChoice: ")
        if choice_proceed=='1':
            choiceBoat= input("Select a boat ID to view seating arrangement (Enter from 1 to 10): ")
            boatseat_view(choiceBoat)        
            boat_list.close()
        elif choice_proceed=='2':
            boatSelect()
        else:
            print("Wrong input!\n<Please restart program.>")
            sys.exit(0)
    elif(choiceV=='T' or choiceV=='t'):
        print('\nTrip times available:\n8. 8:00AM - 12:00PM\n10. 10AM - 2PM\n12. 12PM - 4PM\n2. 2PM - 6PM\n') #~

        fchck_r=open("checkings_list.txt","r")
        fnew=[]

        newtime=input("Choose new time [Choose:8,10,12 or 2]: ")
        if(newtime=='8' or newtime=='10'):
            newtform= ":00 AM"
        elif(newtime=='12' or newtime=='2'):
            newtform= ":00 PM"
        else:
            print("Error! Invalid input.\n<Please restart.>")
            sys.exit(0)   
        ex_name=input("Enter your name: ")
        for line in fchck_r:
            data= line.split('\t') #Works
            #print(data)
            if ex_name in data:
                data.remove(data[6])
                data.insert(6,newtime)
                newLine= data[0]+'\t'+data[1]+'\t'+data[2]+'\t'+data[3]+'\t'+data[4]+'\t'+data[5]+'\t'+data[6]+'\t'+data[7]
                fnew.append(newLine)
            else:
                fnew.append(line)
                
        fchck_r.close()
        #print(fnew)

        fchck_w=open("checkings_list.txt","w")
        for line in fnew:
            fchck_w.write(line)

        fchck_w.close()
        fcheck_rview=open("checkings_list.txt","r")
        review=fcheck_rview.read()
        fcheck_rview.close()
        if ex_name in review:
            print("Mr./Mrs./Ms. "+ex_name+" has successfully changed their scheduled tour time to: "+newtime+newtform+"!")
            Contchoice=input("Would you like to continue? (y/n): ")
            if Contchoice=='y':
                mainmenu()
            else:
                print("You've exited the system!\nGood bye!")
                sys.exit(0)
        else:
            print("User not found in database!")
            Regchoice=input("Would you like to register? (y/n): ")
            if Regchoice=='y':
                ticket_purchase()
            else:
                mainmenu()
    else:
        print("Wrong input!\n<Please restart program.>")
        sys.exit(0)

#***************************** Function 6 - Boat & Seat select *************

def boatSelect():
   
    def oldboatUpdate(old_boat,old_seat):
        
        if int(old_boat)<=2:
            oldf_r=open('#B'+old_boat+'.txt','r')
            newlist=[]
            for line in oldf_r:
                entries=line.split('\t')
                if entries[0]==old_seat:
                    entries.remove(entries[1])
                    entries.insert(1,'0\n')
                    updated_ent= entries[0]+'\t'+entries[1]
                    newlist.append(updated_ent)
                else:
                    newlist.append(line)
            oldf_r.close()
            oldf_w=open('#B'+old_boat+'.txt','w')
            for line in newlist:
                oldf_w.write(line)
            oldf_w.close()
            
        elif(int(old_boat)<=10 and int(old_boat)>2):
            oldf_r=open('#E'+old_boat+'.txt','r')
            newlist=[]
            for line in oldf_r:
                entries=line.split('\t')
                if entries[0]==old_seat:
                    entries.remove(entries[1])
                    entries.insert(1,'0\n')
                    updated_ent= entries[0]+'\t'+entries[1]
                    newlist.append(updated_ent)
                else:
                    newlist.append(line)
            oldf_r.close()
            oldf_w=open('#E'+old_boat+'.txt','w')
            for line in newlist:
                oldf_w.write(line)
            oldf_w.close()
            
        return old_boat,old_seat
            

    def newboatReg(new_boat,new_seat):
        
        if (int(new_boat)<=0 or int(new_boat)>10):
            print("Invalid boat ID!\n<Please restert.>")
            sys.exit(0)
            
        elif int(new_boat)<=2:
            if(new_seat!='B1' and new_seat!='B2' and new_seat!='B3' and new_seat!='B4'):
                print("Invalid input!\n<Please restart.>")
                sys.exit(0)
                
            nboatfile_r=open('#B'+new_boat+'.txt','r')
            nfile=[]
            for line in nboatfile_r:
                data=line.split('\t')
                #print(data)
                if(data[0]==new_seat and data[1]=='0\n'):
                    data.remove(data[1])
                    data.insert(1,'1\n')
                    new_l=data[0]+'\t'+data[1]
                    nfile.append(new_l)
                else:
                    nfile.append(line)
            nboatfile_r.close()
            nboatfile_w=open('#B'+new_boat+'.txt','w')
            for line in nfile:
                nboatfile_w.write(line)
            nboatfile_w.close()
            
        elif (int(new_boat)>2 and int(new_boat)<=10):
            if (new_seat!='E1' and new_seat!='E2' and new_seat!='E3' and new_seat!='E4' and new_seat!='E5' and new_seat!='E6' and new_seat!='E7' and new_seat!='E8'):
                print("Invalid input!\n<Please restart.>")
                sys.exit(0)
            nboatfile_r=open('#E'+new_boat+'.txt','r')
            nfile=[]
            for line in nboatfile_r:
                data=line.split('\t')
                #print(data)
                if(data[0]==new_seat and data[1]=='0\n'):
                    data.remove(data[1])
                    data.insert(1,'1\n')
                    new_l=data[0]+'\t'+data[1]
                    nfile.append(new_l)
                else:
                    nfile.append(line)
            nboatfile_r.close()
            nboatfile_w=open('#E'+new_boat+'.txt','w')
            for line in nfile:
                nboatfile_w.write(line)
            nboatfile_w.close()

        return new_boat,new_seat

    x_name=input("1. Enter your name: ")
    print("Boats:\n1 - 2: Business class (4 seats: B1-B4)\n3 - 10: Economy Class (8 Seats: E1-E4)\n")
    newboatid=input("2. Enter ID number of boat you choose: ")
    if(int(newboatid)<0 and int(newboatid)>10):
        print("Invalid input!\n<Please restart.>")
        sys.exit(0)

    newseatid=input("3. Enter ID of seat you'd like (B1, E1, etc.): ")
    ltemp=[]

    f_r=open('checkings_list.txt','r')
    for line in f_r:
        cont=line.split('\t')
        #print(cont)
        if(cont[0]==x_name):
            oldboatUpdate(cont[4],cont[5])
            cont.remove(cont[4])
            cont.insert(4,newboatid)
            cont.remove(cont[5])
            cont.insert(5,newseatid)
            newln=cont[0]+'\t'+cont[1]+'\t'+cont[2]+'\t'+cont[3]+'\t'+cont[4]+'\t'+cont[5]+'\t'+cont[6]+'\t'+cont[7]
            ltemp.append(newln)
        else:
            ltemp.append(line)
    f_r.close()
    #print(ltemp)
    fw=open('checkings_list.txt','w')
    for line in ltemp:
        fw.write(line)
    fw.close()

    newboatReg(newboatid,newseatid)

    fview_r=open('checkings_list.txt','r')
    fview_data=fview_r.read()
    fview_r.close()
    if x_name in fview_data:
        print(x_name+" has successfully changed their boat and seat!")
        mainmenu()
    else:
        print("User not found.")
        sys.exit(0)

    return newboatid, newseatid


        
#*******************************************************************************
#**************** Function 7 - Main Menu Dialogue ******************************

print("\nProgram Name: SPEED BOAT TICKETING SYSTEM\nBy: Ahmed Mohammed Ahmed Ali (TP059731)\nIntake: APU1F2002SE")
#choice1 = input("\n- Press any button to go to main menu or '0' to exit: ")
#while(choice1!='0'):
def mainmenu():
    mainchoice = input("\n<===========SPEED BOAT TICKETING SYSTEM===========> \n\n\tWelcome dear user! Let's get started.\n\nPlease select an option:\nP – to Purchase Ticket\nV – to View Seating Arrangement\nQ – to Quit the system\n")
    if (mainchoice == 'P' or mainchoice =='p'):
        ticket_purchase()
                   
    elif (mainchoice == 'V' or mainchoice =='v'):
        seat_view()
                       
    elif (mainchoice == 'Q' or mainchoice =='q'):
        print("- You've successfully quit the system.\nGood bye!")
        sys.exit(0)
        #break
    else:
        print("Wrong input!\n<Please restart program.>")
        sys.exit(0)
        #continue
        
import os
import random
from os import sys
mainmenu()
