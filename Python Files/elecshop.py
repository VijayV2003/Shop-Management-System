import mysql.connector as sql
import datetime
conn=sql.connect(host='localhost',user='root',passwd='manager',database='electronics')
#if conn.is_connected():
 # print("Successfully Connected")
c1=conn.cursor()
t_date=datetime.date.today()
t_time=datetime.datetime.now()
print("DATE:",t_date.day,"/",t_date.month,"/",t_date.year,"TIME:",t_time.hour ,":",t_time.minute     )
print("Welcome To SSA Electronics Shop Management System")
print('1.YES')
print('2.NO')
ch=int(input('DO YOU WANT TO CONTINUE OR NOT:'))
if ch==1:
    print('WELECOME TO SSA Electronics Shop Management System ') 
    print('1.SIGN IN')
    print('2.CREATE USER ACCOUNT')
    print('3.DELETE ACCOUNT')
    print('4.VIEW DETAILS')
    print('5.EXIT')
    ch1=int(input('ENTER YOUR CHOICE:'))
    if ch1==1:
        print("Welcome To SSA Electronics Shop Management System")
        print("1.EMPLOYEE LOGIN ")
        print("2.USER LOGIN")
        print("3.EXIT")
        choice=int(input("ENTER  UR CHOICE:"))
        if choice==1:
           f=[]
           code=int(input("ENTER  YOUR EMPLOYEE CODE_NO:"))
           name=input("ENTER YOUR EMPLOYEE NAME:")
           passw=int(input("ENTER YOUR PASSWORD:"))
           paas=int(input("REENTER YOUR PASSWORD:"))
           if passw==paas:
              c1.execute("select * from employee where emp_code={} and  password={}".format(code,paas))
              dat=c1.fetchall()
              hi=list(dat)
              if hi==f:
                  print("PASSWORD & USER CODE IS WRONG")
              else:
                  print("################### WELCOME ",name," HAVE A NICE DAY......############")
                  import purchase
        elif choice==2:
            k=[]
            cod=int(input("ENTER  YOUR USER CODE_NO:"))
            name=input("ENTER YOUR USER NAME:")
            p1=int(input("ENTER YOUR PASSWORD:"))
            p2=int(input("REENTER YOUR PASSWORD:"))
            if p1==p2:
                c1.execute("select * from users where user_code = {} and password = {}".format(cod , p2))
                dat1=c1.fetchall()
                hi1=list(dat1)
                if hi1==k:
                    print("PASSWORD &  USERCODE IS WRONG")
                    print('1.YES')
                    print('2.NO')
                    c8=int(input('DO YOU WANT TO CONTINUE OR NOT:'))
                    if c8==1:
                       import elecshop
                    else:
                       print("Thank you")
                       print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                       print("==============================================================================")
                else:
                   import purchase
        elif choice==3:
            print("Thank you")
            print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
            print("==============================================================================")
        else:
            print("Invalid choice")
            print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
            print("==============================================================================")
    elif ch1==2:
         print("1.USER ACCOUNT")
         print("2.EMPLOYEE ACCCOUNT")
         print("3.EXIT")
         ch2=int(input("Enter Your Choice:"))
         if ch2==1:
             x=[]
             print("DATE:",t_date.day,"/",t_date.month,"/",t_date.year,"TIME:",t_time.hour ,":",t_time.minute     )
             print("WELCOME TO USER ACCOUNT REGISTRATION")
             u=int(input("ENTER A USER CODE:"))
             c1.execute("select * from users where user_code="+str(u))
             hat=c1.fetchall()
             h2=list(hat)
             if h2!=x:
                 print("USER CODE ALREADY EXITS")
                 print('1.YES')
                 print('2.NO')
                 c8=int(input('DO YOU WANT TO CONTINUE OR NOT:'))
                 if c8==1:
                     import elecshop
                 else:
                     print("Thank you")
                     print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                     print("==============================================================================")

             else:
                 n=input("ENTER YOUR NAME:")
                 c=input("ENTER YOUR CITY:")
                 z=int(input("ENTER YOUR PHONE NUMBER:"))
                 pse=int(input("ENTER A PASSWORD(in 8 digits):"))
                 c1.execute("select * from users where  password="+str(pse))
                 dat=c1.fetchall()
                 h1=list(dat)
                 if h1!=x:
                     print("Password already exits")
                     print('1.YES')
                     print('2.NO')
                     c9=int(input('DO YOU WANT TO CONTINUE OR NOT:'))
                     if c9==1:
                         import elecshop
                     elif c9==2:
                         print("Thank you")
                         print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                         print("==============================================================================")
                     else:
                         print("Invalid choice")
                         print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                         print("==============================================================================")

                 else:
                     ps2=int(input("REENTER YOUR PASSWORD(in numbers):"))
                     if pse==ps2:
                         c1.execute("insert into users values({},'{}',{},'{}',{})".format(u,n,pse,c,z))
                         conn.commit()
                         print("USER ACCOUNT CREATED SUCCESSFULLY")
                         print('1.YES')
                         print('2.NO')
                         c0=int(input('DO YOU WANT TO CONTINUE OR NOT:'))
                         if c0==1:
                             import elecshop
                         elif c0==2:
                             print("Thank you")
                             print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                             print("==============================================================================")
                         else:
                             print("Invalid choice")
                             print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                             print("==============================================================================")
         if ch2==2:
             pur=0
             fd=[]
             print("DATE:",t_date.day,"/",t_date.month,"/",t_date.year,"TIME:",t_time.hour ,":",t_time.minute     )
             print("WELCOME TO EMPLOYEE ACCOUNT REGISTRATION")
             we=input("ENTER PASSWORD:")
             if we=='vijay':
                 cd=int(input("ENTER A EMPLOYEE CODE(in 4 digits):"))
                 c1.execute("select * from employee where emp_code="+str(cd))
                 hat=c1.fetchall()
                 h3=list(hat)
             if h3!=fd:
                 print("USER CODE ALREADY EXITS")
                 print('1.YES')
                 print('2.NO')
                 c10=int(input('DO YOU WANT TO CONTINUE OR NOT:'))
                 if c10==1:
                     import elecshop
                 elif c10==2:
                     print("Thank you")
                     print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                     print("==============================================================================")
                 else:
                     print("Invalid choice")
                     print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                     print("==============================================================================")


             else:
                 r=input("ENTER YOUR NAME:")
                 pre=int(input("ENTER A PASSWORD(in 8 digits):"))
                 c1.execute("select * from employee where  password="+str(pre))
                 dat=c1.fetchall()
                 h6=list(dat)
                 if h6!=fd:
                     print("Password already exits")
                     print('1.YES')
                     print('2.NO')
                     c76=int(input('DO YOU WANT TO CONTINUE OR NOT:'))
                     if c76==1:
                         import elecshop
                     elif c76==2:
                         print("Thank you")
                         print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                         print("==============================================================================")
                     else:
                         print("Invalid choice")
                         print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                         print("==============================================================================")

                 else:
                     ps4=int(input("REENTER YOUR PASSWORD(in numbers):"))
                     if pre==ps4:
                         c1.execute("insert into employee values({},'{}',{},{})".format(cd,r,pre,pur))
                         conn.commit()
                         print("EMPLOYEE ACCOUNT CREATED SUCCESSFULLY")
                         print('1.YES')
                         print('2.NO')
                         c0=int(input('DO YOU WANT TO CONTINUE OR NOT:'))
                         if c0==1:
                             import elecshop
                         elif c0==2:
                             print("Thank you")
                             print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                             print("==============================================================================")
                         else:
                             print("Invalid choice")
                             print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                             print("==============================================================================")
    elif ch1==3:
        print("1.USER ACCOUNT")
        print("2.EMPLOYEE ACCCOUNT")
        print("3.EXIT")
        ch71=int(input("Enter your Choice:"))
        if ch71==1:
            de=int(input("ENTER THE USER CODE TO BE DELETED:"))
            c1.execute("select user_code,user_name,city,ph_no from users where user_code="+str(de))
            data=c1.fetchall()
            for row in data:
                print("          User Details ")
                print("        USER_CODE:",row[0])
                print("        USER_NAME:",row[1])
                print("             CITY:",row[2])
                print("         PHONE_NO:",row[3])
                conn.commit()
            print("ARE YOU SURE ABOUT DELETING YOUR ACCOUNT:")
            print("1.YES")
            print("2.NO")
            chi8=int(input("ENTER YOUR CHOICE:"))
            if chi8==1:
                c1.execute("delete from users where user_code={}".format(de))
                print("YOUR USER ACCOUNT DELETED SUCCESSFULLY")
                print("THANK YOU FOR BEING WITH US")
                conn.commit()
            elif chi8==2:
                print("THANK YOU")
                print("=======================================================================")
            else:
                print("INVALID CHOICE")
                print("THANK YOU")
                print("=========================================================================")
        elif ch71==2:
            da=int(input("ENTER THE EMPLOYEE CODE TO BE DELETED:"))
            c1.execute("select emp_code,emp_name from employee where emp_code="+str(da))
            data2=c1.fetchall()
            for row in data2:
                print("          Employee Details ")
                print("        EMPLOYEE_CODE:",row[0])
                print("        EMPLOYEE_NAME:",row[1])
                conn.commit()
            print("ARE YOU SURE ABOUT DELETING YOUR ACCOUNT:")
            print("1.YES")
            print("2.NO")
            chi8=int(input("ENTER YOUR CHOICE:"))
            if chi8==1:
                c1.execute("delete from employee where emp_code={}".format(da))
                print("YOUR USER ACCOUNT DELETED SUCCESSFULLY")
                print("THANK YOU FOR BEING WITH US")
                conn.commit()
            elif chi8==2:
                print("THANK YOU")
                print("=======================================================================")
            else:
                print("INVALID CHOICE")
                print("THANK YOU")
                print("=========================================================================")
    elif ch1==4:
        print("1.USER DETAILS")
        print("2.EMPLOYEE DETAILS")
        print("3.EXIT")
        che34=int(input("ENTER YOUR CHOICE:"))
        if che34==1:
            j_cod=int(input("ENTER THE USER CODE WHICH DETAILS TO BE DISPLAYED:"))
            c1.execute("select user_code,user_name,city,ph_no from users where user_code={}".format(j_cod))
            dare=c1.fetchall()
            for row in dare:
                print("USER ACCOUNT DETAILS")
                print(" USER CODE:",row[0])
                print(" USER NAME:",row[1])
                print("      CITY:",row[2])
                print("  PHONE_NO:",row[3])
        elif che34==2:
            f_cod=int(input("ENTER THE EMPLOYEE CODE WHICH DETAILS TO BE DISPLAYED:"))
            c1.execute("select emp_code,user_name,purchased from employee where emp_code={}".format(f_cod))
            dare2=c1.fetchall()
            for row in dare2:
                print("EMPLOYEE ACCOUNT DETAILS")
                print(" EMPLOYEE CODE:",row[0])
                print(" EMPLOYEE NAME:",row[1])
                print("     PURCHASED:",row[2])
        elif che34==3:
            print("THANK YOU")
            print("ALL KIND OF SMALL OR BULK ORDERS CONTACT SSA ELECTRONICS SHOP")
            print("===================================================================================")
        else:
            print("INVALID CHOICE")
            print("ALL KIND OF SMALL OR BULK ORDERS CONTACT SSA ELECTRONICS SHOP")
            print("=============================================================================")
    elif ch1==5:
        print("THANK YOU")
        print("ALL KIND OF SMALL OR BULK ORDERS CONTACT SSA ELECTRONICS SHOP")
        print("=============================================================================")
    else:
        print("INVALID CHOICE")
        print("ALL KIND OF SMALL OR BULK ORDERS CONTACT SSA ELECTRONICS SHOP")
        print("=============================================================================")
    

        
elif ch==2:
    print("Thank you")
    print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
    print("==============================================================================")
else:
    print("INVALID CHOICE")
    print("ALL KIND OF SMALL OR BULK ORDERS CONTACT SSA ELECTRONICS SHOP")
    print("=============================================================================")
            
