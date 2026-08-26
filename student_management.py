import os
import csv
import re
from datetime import datetime as date
import random
from random import choice
if not os.path.exists("students.csv"):
    open("students.csv", "w", newline='').close()
if not os.path.exists("class_wise_data.csv"):
    open("class_wise_data.csv", "w", newline='').close()
if not os.path.exists("classes.csv"):
    open("classes.csv", "w", newline='').close()
file_exist=os.path.isfile("students.csv") and os.path.getsize("students.csv")>0
file_exist_class_data=os.path.isfile("class_wise_data.csv") and os.path.getsize("class_wise_data.csv")>0
class Read_class_wise_data:
    def read_class_data(self):
        with open("class_wise_data.csv",'r',newline='') as class_wise_data_csv:
            reader=csv.DictReader(class_wise_data_csv)
            class_wise_data={}
            for i in reader:
                if i['BRANCH'] not in class_wise_data.keys():
                    class_wise_data[i['BRANCH']]={}
                    class_wise_data[i['BRANCH']][i['YEAR']]={}
                    class_wise_data[i['BRANCH']][i['YEAR']][i['SECTION']]=[]
                    class_wise_data[i['BRANCH']][i['YEAR']][i['SECTION']].append(i['STUDENT_ID'])
                else:
                    if i['YEAR'] not in class_wise_data[i['BRANCH']].keys():
                        class_wise_data[i['BRANCH']][i['YEAR']] = {}
                        class_wise_data[i['BRANCH']][i['YEAR']][i['SECTION']] = []
                        class_wise_data[i['BRANCH']][i['YEAR']][i['SECTION']].append(i['STUDENT_ID'])
                    else:
                        if i['SECTION'] not in class_wise_data[i['BRANCH']][i['YEAR']].keys():
                            class_wise_data[i['BRANCH']][i['YEAR']][i['SECTION']] = []
                            class_wise_data[i['BRANCH']][i['YEAR']][i['SECTION']].append(i['STUDENT_ID'])
                        else:
                            if i['STUDENT_ID'] not in class_wise_data[i['BRANCH']][i['YEAR']][i['SECTION']]:
                                class_wise_data[i['BRANCH']][i['YEAR']][i['SECTION']].append(i['STUDENT_ID'])
        return class_wise_data
class Read_classes_data:
    def read_classes(self):
        try:
            with open("classes.csv",'r',newline='') as classes_read_csv:
                reader=csv.DictReader(classes_read_csv)
                classes_data={}
                for i in reader:
                    if i['BRANCH'] not in classes_data.keys():
                        classes_data[i['BRANCH']]={}
                        classes_data[i['BRANCH']][i['YEAR']]=[]
                        classes_data[i['BRANCH']][i['YEAR']].append(i['SECTION'])
                    else:
                        if i['YEAR'] not in classes_data[i['BRANCH']].keys():
                            classes_data[i['BRANCH']][i['YEAR']] = []
                            classes_data[i['BRANCH']][i['YEAR']].append(i['SECTION'])
                        else:
                            if i['SECTION'] not in classes_data[i['BRANCH']][i['YEAR']]:
                                classes_data[i['BRANCH']][i['YEAR']].append(i['SECTION'])
        except FileNotFoundError as f:
            print(f)
        else:
            return classes_data
class Read_students_data:  # read students.csv file
    def read(self):
        with open("students.csv","r",newline='') as student_read_csv:
            reader=csv.DictReader(student_read_csv)
            student_data={}
            for i in reader:
                student_data[i["ID"]]=i
        return student_data
class Register_student: # Register student in college
    def __init__(self,file,class_file_exist,student_reader,class_wise_data,sections_data):
        self.reader = student_reader
        self.main_class_wise_data = class_wise_data
        self.main_section_data = sections_data
        self.file=file
        self.class_file=class_file_exist
    def verify_Id(self): # ID verification
        while(True):
            self.id_list =list(self.reader.keys())
            self.Id =str("V" + str(date.today().year) + str(random.randint(1000, 9999)))# Generate ID for student
            self.valid=False
            for i in self.id_list:
                if(i==self.Id):
                    self.valid=True
            if self.valid!=True:
                print(f"Student Id={self.Id}")
                return True
    def verify_password(self):
        while True:
            self.Password=input("Enter Password:")
            if(len(self.Password)>=8):
                return True
            else:
                print("password contain minimum 8 characters")
    def verify_Name(self): # Verification of name
        while(True):
            self.Name = input("Enter Student Name:")
            name_pattern = r"^[A-Za-z]+[A-Za-z\s]*[A-Za-z]+$"
            if re.fullmatch(name_pattern, self.Name):
                return True
            else:
                print("Error:Invalid name format.Try again")
    def verify_Dob(self): # Verify date of birth
        while(True):
            self.Dob = input("Enter Student Date of birth(dd-mm-yyyy):")
            try:
                birth_date = date.strptime(self.Dob, "%d-%m-%Y").strftime("%Y-%m-%d")
                birth_year =int( birth_date.split('-')[0])
                current_year = date.today().year
                age=current_year - birth_year
                if(age>=17 and age<=25 and birth_year<=current_year):
                    return True
                elif(birth_year>current_year):
                    print("Error:Invalid year.Try again")
                else:
                    print("Age is out of range.Age must between 17 and 25")
                    return False
            except ValueError:
                print("Error=Invalid Date Format(dd-mm-yyyy) ex:01-01-2000.Try again")
    def verify_Gender(self):   #verification of gender
        while(True):
            self.Gender = input("Enter Student Gender(Male,Female,Other):").lower()
            if(self.Gender=="male" or self.Gender=="female" or self.Gender=="other"):
                return True
            else:
                print("Error:Invalid Gender.Try again")
    def verify_Department(self): # Department verification
        while(True):
            self.Department = input("Enter Student Department(CSE,ECE,EEE,OTHER):").lower()
            if(self.Department=="cse" or self.Department=="eee" or self.Department=="ece"):
                return True
            elif self.Department=="other":
                print("We can provide only CSE,ECE,EEE")
                choice=input("Do you want to continue with CSE,ECE,EEE (yes/no):").lower()
                if choice=="no":
                    return False
            else:
                print("Error:Invalid Department.Try again")
    def verify_Year(self):  # Verify studying year
        while(True):
            try:
                self.Year = int(input("Enter Student Year(1,2,3,4):"))
                if(self.Year>=1 and self.Year<=4):
                    return True
                else:
                    print("Error:Invalid Year.Try again")
            except ValueError:
                print("Error: Invalid input data.Try again")
    def verify_Email(self): # Email verification
        while(True):
            self.Email = input("Enter Student Email(ex:abc123.@gmail.com):").lower()
            email_pattern=r"^[a-z0-9]+[-._a-z0-9]*(@gmail.com)$"
            if re.fullmatch(email_pattern,self.Email):
                return True
            else:
                print("Error:Invalid Email ex:abc123.@gmail.com.Try again")
    def verify_Phone_no(self):  # Phone number verification
        while(True):
            self.Phone_no = input("Enter Student Phone No:")
            phone_no_pattern=r"\d{10}"
            if re.fullmatch(phone_no_pattern,self.Phone_no):
                return True
            else:
                print("Error:Invalid Phone Number.Try again")
    def add_student_section(self):
        for i in self.main_section_data[self.Department][self.Year]:
            if len(self.main_class_wise_data[self.Department][self.Year][i])<=60 and self.Id not in self.main_class_wise_data[self.Department][self.Year][i]:
                with open("class_wise_data.csv", "a", newline='') as class_wise_data_csv:
                    class_wise_data_writer = csv.DictWriter(class_wise_data_csv,fieldnames=['BRANCH', 'YEAR', 'SECTION', 'STUDENT_ID'])
                    if not self.class_file:
                        class_wise_data_writer.writeheader()
                    class_wise_data_writer.writerow({'BRANCH':self.Branch,'YEAR':self.Year,'SECTION':i,'STUDENT_ID':self.Student_ID})
                return True
        else:
            return False
    def student_database(self):
        with open("students.csv","a",newline='') as student_write_file:
            student_writer = csv.DictWriter(student_write_file,fieldnames=['ID','PASSWORD','NAME','DOB','GENDER','DEPARTMENT','YEAR','EMAIL','PHONE_NO'])
            if not self.file: # Header only at once if file not exist or file execute at first time
                student_writer.writeheader()
            student_writer.writerow({'ID':self.Id,
                                     'PASSWORD':self.Password,
                                     'NAME':self.Name,
                                     'DOB':self.Dob,
                                     'GENDER':self.Gender,
                                     'DEPARTMENT':self.Department,
                                     'YEAR':self.Year,
                                     'EMAIL':self.Email,
                                     'PHONE_NO':self.Phone_no})
            print("Student details saved in database successfully")
class Update_details:
    def __init__(self,reader):
        self.main_data=reader
        while True:
            self.details_list=['id','password','name','dob','gender','department','year','email','phone_no']
            for i in self.details_list:
                print(i.capitalize())
            self.choice=input("Enter which you want to update details:").lower()
            if self.choice=='id':
                print("Id not updated")
                self.option=input("Do you want to continue with another option(yes/no):")
                if(self.option!='yes'):
                    break
            elif self.choice in self.details_list[1::]:
                self.id=input("Enter Student ID:")
                self.password=input("Enter Student Password:")
                if self.id in list(self.main_data.keys()) and self.password==self.main_data[self.id]['PASSWORD']:
                    if(self.choice=='password'):
                        while True:
                            self.new_password=input("Enter Student new Password:")
                            if(self.new_password!=self.password) and len(self.new_password)>=8:
                                self.main_data[self.id]['PASSWORD']=self.new_password
                                break
                            else:
                                print("Invalid password or new password is equal to previous password")
                    if(self.choice=='name'):
                        while True:
                            self.old_name=input("Enter Student old Name:")
                            name_pattern = r"^[A-Za-z]+[A-Za-z\s]*[A-Za-z]+$"
                            if re.fullmatch(name_pattern,self.old_name) and self.old_name==self.main_data[self.id]['NAME']:
                                while True:
                                    self.new_name=input("Enter Student new Name:")
                                    if re.fullmatch(name_pattern,self.new_name) and self.new_name!=self.old_name:
                                        self.main_data[self.id]['NAME']=self.new_name
                                        break
                                    else:
                                        print("Error:Invalid Name format or your new name same as previous name.Try again")
                                break
                            else:
                                print("Error:Invalid Name format or name did not match with your previous name.Try again")
                    if(self.choice=='dob'):
                        while True:
                            self.old_dob = input("Enter Student old Date of birth(dd-mm-yyyy):")
                            if(self.old_dob==self.main_data[self.id]['DOB']):
                                while True:
                                    try:
                                        self.new_dob=input("Enter Student new Date of birth(dd-mm-yyyy):")
                                        birth_date = date.strptime(self.new_dob, "%d-%m-%Y").strftime("%Y-%m-%d")
                                        birth_year = int(birth_date.split('-')[0])
                                        current_year = date.today().year
                                        age = current_year - birth_year
                                        if (age >= 17 and age <= 25 and birth_year <= current_year) and self.new_dob!=self.old_dob:
                                            self.main_data[self.id]['DOB']=self.new_dob
                                            break
                                        elif (birth_year > current_year):
                                            print("Error:Invalid year.Try again")
                                        else:
                                            print("Age is out of range.Age must between 17 and 25 or your new DOB same as previous DOB")
                                    except ValueError:
                                        print("Error=Invalid Date Format(dd-mm-yyyy) ex:01-01-2000.Try again")
                                break
                            else:
                                print("Date of birth did not match with your previous DOB.Try again")
                    if(self.choice=='gender'):
                        while True:
                            self.old_gender = input("Enter Student old Gender:").lower()
                            if(self.old_gender==self.main_data[self.id]['GENDER']):
                                while True:
                                    self.new_gender=input("Enter Student new Gender:").lower()
                                    if(self.new_gender=='male' or self.new_gender=='female' or self.new_gender=='other') and self.new_gender!=self.old_gender:
                                        self.main_data[self.id]['GENDER']=self.new_gender
                                        break
                                    else:
                                        print("Error:Invalid Gender or your new gender same as previous gender.Try again")
                                break
                            else:
                                print("Gender will not match with previous Gender.Try again")
                    if(self.choice=='department'):
                        while True:
                            self.old_department = input("Enter Student old Department:").lower()
                            if(self.old_department==self.main_data[self.id]['DEPARTMENT']):
                                while True:
                                    self.new_department=input("Enter Student new Department:").lower()
                                    if(self.new_department=='cse' or self.new_department=='eee' or self.new_department=='ece') and self.new_department!=self.old_department:
                                        self.main_data[self.id]['DEPARTMENT']=self.new_department
                                        break
                                    else:
                                        print("Error:Invalid Department(Cse,Ece,Eee) or your new department same as previous department.Try again")
                                break
                            else:
                                print("Department cannot match with your previous Department.Try again")
                    if self.choice=='year':
                        try:
                            self.old_year = int(input("Enter Student old Year:"))
                            if(self.old_year==self.main_data[self.id]['YEAR']):
                                while True:
                                    self.new_year=int(input("Enter Student new Year:"))
                                    if(self.new_year>=1 and self.new_year<=4) and self.new_year!=self.old_year:
                                        self.main_data[self.id]['YEAR']=self.new_year
                                        break
                                    else:
                                        print("Error:Invalid Year or your new year same as previous year.Try again")
                                break
                            else:
                                print("Year cannot match with your previous Year.Try again")
                        except ValueError:
                            print("Error:Invalid input.Try again")
                    if self.choice=='email':
                        email_pattern=r"^[a-z0-9]+[-._a-z0-9]*(@gmail.com)$"
                        while True:
                            self.old_email=input("Enter Student old Email:").lower()
                            if re.fullmatch(email_pattern,self.old_email) and self.old_email==self.main_data[self.id]['EMAIL']:
                                while True:
                                    self.new_email=input("Enter Student new Email:").lower()
                                    if re.fullmatch(email_pattern,self.new_email) and self.new_email!=self.old_email:
                                        self.main_data[self.id]['EMAIL']=self.new_email
                                        break
                                    else:
                                        print("Error:Invalid Email format or your new email same as previous email.Try again")
                                break
                            else:
                                print("Your email cannot match with your previous Email.Try again")
                    if self.choice=='phone_no':
                        phone_no_pattern = r"\d{10}"
                        while True:
                            self.old_phone_no=input("Enter Student old Phone Number:")
                            if re.fullmatch(phone_no_pattern,self.old_phone_no) and self.old_phone_no==self.main_data[self.id]['PHONE_NO']:
                                while True:
                                    self.new_phone_no=input("Enter Student new Phone Number:")
                                    if re.fullmatch(phone_no_pattern,self.new_phone_no) and self.new_phone_no!=self.old_phone_no:
                                        self.main_data[self.id]['PHONE_NO']=self.new_phone_no
                                        break
                                    else:
                                        print("Error:Invalid Phone Number or it is equal to your previous phone number.Try again")
                                break
                            else:
                                print("Your phone_number cannot match with your previous Phone Number.Try again")
                    self.option=input("Do you want to update another details(yes/no):").lower()
                    if(self.option!='yes'):
                        break
                else:
                    print("Invalid Authentication")
                    self.option=input("Do you want to try again(yes/no):").lower()
                    if(self.option!='yes'):
                        break
            else:
                print("Select perfect choice are given")
                self.option = input("Do you want to try again(yes/no):").lower()
                if (self.option != 'yes'):
                    break
        with open("students.csv","w",newline='') as student_write_file:
            student_writer = csv.DictWriter(student_write_file,fieldnames=['ID','PASSWORD','NAME','DOB','GENDER','DEPARTMENT','YEAR','EMAIL','PHONE_NO'])
            student_writer.writeheader()
            for i in self.main_data.keys():
                student_writer.writerow(self.main_data[i])
            print("Student details updated in database successfully")
class Delete_student:
    def __init__(self,reader):
        self.main_data=reader
        while(True):
            self.id=input('Enter Student ID:')
            self.password=input('Enter Student Password:')
            if(self.id in list(self.main_data.keys())) and (self.password==self.main_data[self.id]['PASSWORD']):
                while True:
                    self.confirm=input(f"Are you sure to delete this student {self.id} {self.main_data[self.id]['NAME']} (yes/no):").lower()
                    if(self.confirm=='no'):
                        print("Student deletion is failed")
                        break
                    elif(self.confirm=='yes'):
                        del self.main_data[self.id]
                        print("Student deleted Successfully from database")
                        break
                    else:
                        print("Invalid Choice.Try again")
                break
            else:
                print("Student does not exist. or Invalid Authentication.")
                self.option=input("Do you want to try again(yes/no):").lower()
                if self.option!='yes':
                    break
        with open("students.csv","w",newline='') as student_write_file:
            student_writer = csv.DictWriter(student_write_file,fieldnames=['ID','PASSWORD','NAME','DOB','GENDER','DEPARTMENT','YEAR','EMAIL','PHONE_NO'])
            student_writer.writeheader()
            for i in self.main_data.keys():
                student_writer.writerow(self.main_data[i])
class Search_student:
    def __init__(self,reader):
        self.main_data=reader
        self.id=input('Enter Student ID:')
        if self.id in list(self.main_data.keys()):
            for i in self.main_data[self.id].keys():
                print(f"{i}={self.main_data[self.id][i]}")
        else:
            print("Student not found")
class Department_wise_list:
    def __init__(self,student_reader):
        self.main_data=student_reader
        self.department_wise_list={}
        for i in self.main_data.keys():
            if self.main_data[i]['DEPARTMENT'] not in self.department_wise_list.keys():
                self.department_wise_list[self.main_data[i]['DEPARTMENT']]=[]
                self.department_wise_list[self.main_data[i]['DEPARTMENT']].append(self.main_data[i])
            else:
                self.department_wise_list[self.main_data[i]['DEPARTMENT']].append(self.main_data[i])
    def department_list(self):
        while True:
            self.department=input("Enter which department list students you want(Cse,Ece,Eee):").lower()
            if self.department in self.department_wise_list.keys():
                if(self.department=='cse'):
                    for i in self.department_wise_list['cse']:
                        print(i)
                elif (self.department=='eee'):
                    for i in self.department_wise_list['eee']:
                        print(i)
                elif (self.department=='ece'):
                    for i in self.department_wise_list['ece']:
                        print(i)
                break
            else:
                if(self.department not in self.department_wise_list.keys() and self.department in ['cse','eee','ece']):
                    print("Department is empty")
                    break
                else:
                    print("Invalid Department.Try again")
def Register(register_obj):
    if(register_obj.verify_Id() and
            register_obj.verify_password() and
            register_obj.verify_Name() and
            register_obj.verify_Dob() and
            register_obj.verify_Gender() and
            register_obj.verify_Department() and
            register_obj.verify_Year() and
            register_obj.verify_Email() and
            register_obj.verify_Phone_no()):
        if(o.add_student_section()):
            register_obj.student_database()
        else:
            print(f"All seats are filled in this {o.Department}")
            print("Thank you for visit my college")
    else:
        print("This student is not eligible for this college")
        print("I hope you are understand.Thank you")
obj=Read_students_data() # read the date of students.csv
read_data=obj.read()
o=Register_student(file_exist,read_data)
Register(o)
