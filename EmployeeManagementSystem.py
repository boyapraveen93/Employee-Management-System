#EmployeeManagementSystem.py

#EmpMenu
def menu():
    print("-"*70)
    print("\tE M P L O Y E E  I N F O R M A T I O N  S Y S T E M")
    print("-" * 70)
    print("\t\t1.Add Employee")
    print("\t\t2.Delete Employee")
    print("\t\t3.Update Employee")
    print("\t\t4.View Single Employee")
    print("\t\t5.View All Employees")
    print("\t\t6.Search Employee")
    print("\t\t7.Exit")
    print("-" * 70)


#EmpAdd
import pickle
def addEmployee():
    with open("employeeproj.pick","ab") as fp:
        try:
            #accept the Employee from Key Board
            print("------------------------------------")
            empno=int(input("\tEnter Employee Number:"))
            empname=input("\tEnter Employee Name:")
            empsal=float(input("\tEnter Employee Salary:"))
            print("------------------------------------")
            lst=list() #Empty List for adding Employee Values--Iterable Object
            lst.append(empno)
            lst.append(empname)
            lst.append(empsal)
            #save Iterable Object Data in File
            pickle.dump(lst,fp)
            print("\tEmployee data saved in file")
        except ValueError:
            print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS FOR EMPNO AND SAL")


#EmpDelete
import pickle
def deleteEmployee():
    # Get all the Records from File in Put them in List in list
    records = []  # Outer List
    with open("employeeproj.pick", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    # Locating the Record for Updating the Salary
    res = False
    empno = int(input("\tEnter Employee Number for Deleting:"))
    for i in range(len(records)):
        if (records[i][0] == empno):
            recindex = i
            res = True
            break
    print("-" * 70)
    if (res):
       records.pop(recindex)
       # rewrite Modified Records value to existing File
       with open("employeeproj.pick", "wb") as fp:
           for record in records:
               pickle.dump(record, fp)
       print("\t\tEmployee Record Deleted--verify")
    else:
        print("\tEmployee Number does not exist in File")
    print("-" * 70)


#EmpUpdate
import pickle
def updateEmployee():
    # Get all the Records from File in Put them in List in list
    records = []  # Outer List
    with open("employeeproj.pick", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #Locating the Record for Updating the Salary
    res=False
    empno = int(input("\tEnter Employee Number for Updating Salary:"))
    for i in range(len(records)):
        if(records[i][0]==empno):
            recindex=i
            res=True
            break
    print("-"*70)
    if(res):
        print("\tEmployee Number already exists in File")
        newsal=float(input("\t\tEnter Employee New Salary: "))
        records[recindex][2]=newsal
        #rewrite Modified Records value to existing File
        with open("employeeproj.pick","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
        print("\t\tEmployee Salary Updated--verify")
    else:
        print("\tEmployee Number does not exist in File")
    print("-" * 70)


#EmpView.py<--Module Name
import pickle
def viewSingleEmployee():
    #Get all the Records from File in Put them in List in list
    records=[] # Outer List
    with open("employeeproj.pick", "rb") as fp:
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
#Code for Getting Employee Details
    res=False
    empno = int(input("Enter Employee Number to view Details:"))
    for record in records:
        if(record[0]==empno):
            rec=record
            res=True
            break
    print("-" * 70)
    if(res):
        print("\t\tEmployee Number:{}".format(rec[0]))
        print("\t\tEmployee Name:{}".format(rec[1]))
        print("\t\tEmployee Salary:{}".format(rec[2]))
    else:
        print("\t\tEmployee Details Does Not Exist")
    print("-" * 70)

def viewAllEmployees():
    with open("employeeproj.pick","rb") as fp:
        print("-" * 70)
        print("\tENO\t\tNAME\tSALARY")
        print("-" * 70)
        while(True):
            try:
                record=pickle.load(fp)
                for val in record:
                    print("\t{}".format(val),end="\t")
                print()
            except EOFError:
                print("-"*70)
                break


#EmpSearch.py<-------Module Name
import pickle
def searchEmployee():
    # Get all the Records from File in Put them in List in list
    records = []  # Outer List
    with open("employeeproj.pick", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
# Code for Seraching Employee Details
    res = False
    empno = int(input("Enter Employee Number to Search:"))
    for record in records:
        if (record[0] == empno):
            res = True
            break
    print("-" * 70)
    if (res):
        print("\t\tEmployee Details Exist--Valid")
    else:
        print("\t\tEmployee Details Does Not Exist--Invalid")
    print("-" * 70)


#EmpMainProject <---Main Program
from EmpAdd import addEmployee
from EmpDelete import deleteEmployee
from EmpMenu import menu
from EmpSearch import searchEmployee
from EmpUpdate import updateEmployee
from EmpView import viewSingleEmployee, viewAllEmployees

while(True):
    try:
        menu()
        ch=int(input("\tEnter UR Choice:"))
        match(ch):
            case 1:
                addEmployee()
            case 2:
                deleteEmployee()
            case 3:
                updateEmployee()
            case 4:
                viewSingleEmployee()
            case 5:
                viewAllEmployees()
            case 6:
                searchEmployee()
            case 7:
                print("\t\tThx for Using CLI Project")
                break
            case _:
                print("\tUR SELECTION OF OPERATION IS WRONG-TRY AGAIN")
    except ValueError:
        print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS-TRY AGAIN")

