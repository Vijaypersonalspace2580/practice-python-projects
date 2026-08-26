import os
import csv
import re
from datetime import datetime as date
import random
if not os.path.exists("faculty.csv"):
    open("faculty.csv", "w", newline='').close()
if not os.path.exists("subjects.csv"):
    open("subjects.csv", "w", newline='').close()
if not os.path.exists("classes.csv"):
    open("classes.csv", "w", newline='').close()
if not os.path.exists("faculty_assignment.csv"):
    open("faculty_assignment.csv", "w", newline='').close()
file_exists_faculty_assignments=os.path.isfile("faculty_assignment.csv") and os.path.getsize("faculty_assignment.csv")>0
file_exists_class=os.path.isfile("classes.csv") and os.path.getsize("classes.csv")>0
file_exists_subjects=os.path.isfile("subjects.csv") and os.path.getsize("subjects.csv")>0
file_exist_faculty=os.path.isfile("faculty.csv") and os.path.getsize("faculty.csv")>0
class Read_faculty_data:  # read students.csv file
    def read_faculty(self):
        with open("faculty.csv","r",newline='') as faculty_read_csv:
            reader=csv.DictReader(faculty_read_csv)
            faculty_data={}
            for i in reader:
                faculty_data[i["ID"]]=i
        return faculty_data
class Read_subjects_data:
    def read_subjects(self):
        with open("subjects.csv","r",newline='') as subjects_read_csv:
            reader=csv.DictReader(subjects_read_csv)
            subjects_data={}
            for i in reader:
                subjects_data[i["SUBJECT_ID"]]=i
        return subjects_data
class Read_classes_data:
    def read_classes(self):
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
        return classes_data
class Read_faculty_assignment_data:
    def read_faculty_assignment(self):
        with open("faculty_assignment.csv","r",newline='') as faculty_assignment_read_csv:
            reader=csv.DictReader(faculty_assignment_read_csv)
            faculty_assignment_data={}
            for i in reader:
                list_faculty_subject = {}
                list_faculty_subject[i['SUBJECT_ID']]=i['FACULTY_ID']
                if i['BRANCH'] not in faculty_assignment_data.keys():
                    faculty_assignment_data[i['BRANCH']]={}
                    faculty_assignment_data[i['BRANCH']][i['YEAR']]={}
                    faculty_assignment_data[i['BRANCH']][i['YEAR']][i['SECTION']]=[]
                    faculty_assignment_data[i['BRANCH']][i['YEAR']][i['SECTION']].append(list_faculty_subject)
                else:
                    if i['YEAR'] not in faculty_assignment_data[i['BRANCH']].keys():
                        faculty_assignment_data[i['BRANCH']][i['YEAR']] = {}
                        faculty_assignment_data[i['BRANCH']][i['YEAR']][i['SECTION']] = []
                        faculty_assignment_data[i['BRANCH']][i['YEAR']][i['SECTION']].append(list_faculty_subject)
                    else:
                        if i['SECTION'] not in faculty_assignment_data[i['BRANCH']][i['YEAR']].keys():
                            faculty_assignment_data[i['BRANCH']][i['YEAR']][i['SECTION']] = []
                            faculty_assignment_data[i['BRANCH']][i['YEAR']][i['SECTION']].append(list_faculty_subject)
                        else:
                            faculty_assignment_data[i['BRANCH']][i['YEAR']][i['SECTION']].append(list_faculty_subject)
        return faculty_assignment_data
class Register_faculty: # Register student in college
    def __init__(self,file,reader):
        self.reader = reader #Take data from object
        self.file=file
    def verify_Name(self): # Verification of name
        while(True):
            self.Name = input("Enter faculty Name:")
            name_pattern = r"^[A-Za-z]+[A-Za-z\s]*[A-Za-z]+$"
            if re.fullmatch(name_pattern, self.Name):
                return True
            else:
                print("Error:Invalid name format.Try again")
    def verify_Dob(self):
        while(True):
            self.Dob = input("Enter faculty Date of birth(dd-mm-yyyy):")
            try:
                birth_date = date.strptime(self.Dob, "%d-%m-%Y").strftime("%Y-%m-%d")
                birth_year =int( birth_date.split('-')[0])
                current_year = date.today().year
                age=current_year - birth_year
                if(age>=23 and age<=65 and birth_year<=current_year):
                    return True
                elif(birth_year>current_year):
                    print("Error:Invalid year.Try again")
                else:
                    print("Age is out of range.Age must between 23 and 65")
                    return False
            except ValueError:
                print("Error=Invalid Date Format(dd-mm-yyyy) ex:01-01-2000.Try again")
    def verify_Gender(self):   #verification of gender
        while(True):
            self.Gender = input("Enter faculty Gender(Male,Female,Other):").lower()
            if(self.Gender=="male" or self.Gender=="female" or self.Gender=="other"):
                return True
            else:
                print("Error:Invalid Gender.Try again")
    def verify_Phone_no(self):  # Phone number verification
        while(True):
            self.Phone_no = input("Enter faculty Phone No:")
            phone_no_pattern=r"\d{10}"
            if re.fullmatch(phone_no_pattern,self.Phone_no):
                return True
            else:
                print("Error:Invalid Phone Number.Try again")
    def verify_Email(self): # Email verification
        while(True):
            self.Email = input("Enter faculty Email(ex:abc123.@gmail.com):").lower()
            email_pattern=r"^[a-z0-9]+[-._a-z0-9]*(@gmail.com)$"
            if re.fullmatch(email_pattern,self.Email):
                return True
            else:
                print("Error:Invalid Email ex:abc123.@gmail.com.Try again")
    def verify_Department(self): # Department verification
        while(True):
            self.Department = input("Enter faculty Department(CSE,ECE,EEE,OTHER):").lower()
            if(self.Department=="cse" or self.Department=="eee" or self.Department=="ece"):
                return True
            elif self.Department=="other":
                print("We have only these CSE,ECE,EEE")
                choice=input("Do you want to continue with CSE,ECE,EEE (yes/no):").lower()
                if choice=="no":
                    return False
            else:
                print("Error:Invalid Department.Try again")
    def verify_Qualification(self):
        while True:
            self.qualification=input("Enter faculty Qualification:").lower()
            self.qualification_list=['masters','phd']
            if self.qualification in self.qualification_list:
                return True
            else:
                for i in self.qualification_list:
                    print(i)
                self.option=input("Do you have any these qualifications(yes/no):").lower()
                if self.option!='yes':
                    return False
    def verify_Experience(self):
        while(True):
            try:
                self.experience=int(input("Enter faculty Experience:"))
                if(self.experience>=0 and self.experience<=40):
                    return True
                else:
                    print("Invalid Experience.Try again")
            except ValueError:
                print("Invalid input.Try again")
    def Designation(self):
        while(True):
            if((self.qualification=='masters' and (self.experience>=0 and self.experience<=5)) or (self.qualification=='phd' and (self.experience>=0 and self.experience<=5))):
                self.designation='Associate professor'
                return True
            else:
                self.designation='senior professor'
                return True
    def Join(self):
        while(True):
            self.joining_date=date.today().date()
            return True
    def verify_Id(self): # ID verification
        while(True):
            self.id_list =list(self.reader.keys())
            self.Id =str("VF" + str(date.today().year) + str(random.randint(100, 999)))
            self.valid=False
            for i in self.id_list:
                if(i==self.Id):
                    self.valid=True
            if self.valid!=True:
                print(f"Faculty Id={self.Id}")
                return True
    def verify_employee_type(self):
        while True:
            self.employee_type=input("Enter a employee type faculty(permanent/contract):").lower()
            if self.employee_type in ['permanent','contract']:
                return True
            else:
                print("Enter valid input")
    def verify_password(self):
        while True:
            self.password=input('Enter your password:').lower()
            if len(self.password)>8:
                return True
            else:
                print("Your password is very week.Try again")
    def faculty_database(self):
        with open("faculty.csv","a",newline='') as faculty_write_file:
            faculty_writer = csv.DictWriter(faculty_write_file,fieldnames=['ID','PASSWORD','NAME','DOB','GENDER','DEPARTMENT','EMAIL','PHONE_NO','QUALIFICATION','EXPERIENCE','JOINING_DATE','DESIGNATION','EMPLOYEE_TYPE'])
            if not self.file: # Header only at once if file not exist or file execute at first time
                faculty_writer.writeheader()
            faculty_writer.writerow({'ID':self.Id,
                                     'PASSWORD':self.password,
                                     'NAME':self.Name,
                                     'DOB':self.Dob,
                                     'GENDER':self.Gender,
                                     'DEPARTMENT':self.Department,
                                     'EMAIL':self.Email,
                                     'PHONE_NO':self.Phone_no,
                                     'QUALIFICATION':self.qualification,
                                     'EXPERIENCE':self.experience,
                                     'JOINING_DATE':self.joining_date,
                                     'DESIGNATION':self.designation,
                                     'EMPLOYEE_TYPE':self.employee_type})
            print("Faculty details saved in database successfully")
class Remove_faculty:
    def __init__(self,reader):
        self.faculty_main_data=reader
        while True:
            self.faculty_id=input("Enter faculty id:")
            if self.faculty_id in self.faculty_main_data.keys():
                while True:
                    self.option=input(f"Are you confirm to delete this {self.faculty_id} (yes/no):").lower()
                    if self.option=='yes':
                        del self.faculty_main_data[self.faculty_id]
                        print("Removed faculty successfully")
                        break
                    elif self.option=='no':
                        print("Removed faculty not successfully")
                        break
                    else:
                        print("Choose valid choice")
                break
            else:
                print("Faculty not exist")
                break
        with open("faculty.csv","w",newline='') as faculty_write_file:
            faculty_writer = csv.DictWriter(faculty_write_file,fieldnames=['ID','NAME','DOB','GENDER','DEPARTMENT','EMAIL','PHONE_NO','QUALIFICATION','EXPERIENCE','JOINING_DATE','DESIGNATION','EMPLOYEE_TYPE'])
            faculty_writer.writeheader()
            for i in self.faculty_main_data.keys():
                faculty_writer.writerow(self.faculty_main_data[i])
class Initializing_subjects:
    def __init__(self,file,reader):
        self.file=file
        self.main_data_subjects=reader
    def add_new_subject(self):
        while True:
            self.subject_id=str('SUB'+random.randint(100,999))
            if self.subject_id not in list(self.main_data_subjects.keys()):
                print(f"Subject id:{self.subject_id}")
                break
        self.subject_name=input("Enter subject name:").lower()
        while True:
            try:
                self.year=int(input("Enter subject is which year belongs:"))
                if(self.year>=1 and self.year<=4):
                    break
                else:
                    print("Enter valid year(1,2,3,4):")
            except ValueError:
                print("Invalid input.Try again")
        while True:
            self.branch=input("Enter subject is related to which branch(cse,ece,eee):").lower()
            if self.branch in ['cse','ece','eee']:
                break
            else:
                print("Invalid branch.Try again")
        while True:
            try:
                self.credits=int(input("Enter subject credits:"))
                if self.credits>=0 and self.credits<=4:
                    break
                else:
                    print("credits must be <= 4 and integer value")
            except ValueError:
                print("Invalid format.Try again")
        with open("subjects.csv","a",newline='') as subjects_write_file:
            subjects_writer = csv.DictWriter(subjects_write_file,fieldnames=['SUBJECT_ID','SUBJECT_NAME','YEAR','BRANCH','CREDITS'])
            if not self.file:
                subjects_writer.writeheader()
            subjects_writer.writerow({
                'SUBJECT_ID':self.subject_id,
                'SUBJECT_NAME':self.subject_name,
                'YEAR':self.year,
                'BRANCH':self.branch,
                'CREDITS':self.credits})
    def update_subject_details(self):
        self.id_subject=input("Enter subject id:")
        if self.id_subject in self.main_data_subjects.keys():
            while True:
                for i in ['SUBJECT_ID','SUBJECT_NAME','YEAR','BRANCH','CREDITS']:
                    print(i)
                self.option=input("Enter which you want to update:").lower()
                if self.option=='subject_id':
                    print("Id not updated")
                    break
                elif self.option=="subject_name":
                    while True:
                        self.old_name=input("Enter old name of subject:").lower()
                        self.new_name=input("Enter subject new name:").lower()
                        if self.old_name==self.main_data_subjects[self.id_subject]['SUBJECT_NAME'] and self.old_name!=self.new_name:
                            self.main_data_subjects[self.id_subject]['SUBJECT_NAME']=self.new_name
                            break
                        else:
                            print("Name not match with old name or new name and old name are equal")
                    break
                elif self.option=='year':
                    while True:
                        try:
                            self.old_year=int(input("Enter old name:"))
                            self.new_year=int(input("Enter new name:"))
                            if self.old_year==self.main_data_subjects[self.id_subject]['YEAR'] and self.old_year!=self.new_year and(self.new_year>=1 and self.new_year<=4):
                                self.main_data_subjects[self.id_subject]['YEAR']=self.new_year
                                break
                            else:
                                print("Year not match with old year or new year and old year are equal")
                        except ValueError:
                            print("Invalid input.Try again")
                    break
                elif self.option=='branch':
                    while True:
                        self.old_branch=input("Enter old branch:").lower()
                        self.new_branch = input("Enter new branch:").lower()
                        if self.old_branch == self.main_data_subjects[self.id_subject]['BRANCH'] and self.old_branch != self.new_branch:
                            self.main_data_subjects[self.id_subject]['BRANCH']=self.new_branch
                            break
                        else:
                            print("Branch not match with old branch or both are same")
                    break
                elif self.option=='credits':
                    while True:
                        try:
                            self.old_credits=int(input("Enter old credits:"))
                            self.new_credits =int(input("Enter new credits:"))
                            if self.old_credits == self.main_data_subjects[self.id_subject]['CREDITS'] and self.old_credits != self.new_credits and self.new_credits in [1,2,3,4]:
                                self.main_data_subjects[self.id_subject]['CREDITS']=self.new_credits
                                break
                            else:
                                print("Credits not match with old credits or both are same")
                        except ValueError:
                            print("Invalid input.Try again")
                    break
                else:
                    print("Select valid choice for update")
        else:
            print("Subject not found in database")
        with open("subjects.csv","w",newline='') as subjects_write_file:
            subjects_writer = csv.DictWriter(subjects_write_file,fieldnames=['SUBJECT_ID','SUBJECT_NAME','YEAR','BRANCH','CREDITS'])
            subjects_writer.writeheader()
            for i in self.main_data_subjects.keys():
                subjects_writer.writerow(self.main_data_subjects[i])
    def remove_subject(self):
        self.id=input("Enter subject id:")
        if self.id in self.main_data_subjects.keys():
            del self.main_data_subjects[self.id]
            print(f"Removed successfully subject is{self.id}")
        else:
            print("subject not found")
        with open("subjects.csv","w",newline='') as subjects_write_file:
            subjects_writer = csv.DictWriter(subjects_write_file,fieldnames=['SUBJECT_ID','SUBJECT_NAME','YEAR','BRANCH','CREDITS'])
            subjects_writer.writeheader()
            for i in self.main_data_subjects.keys():
                subjects_writer.writerow(self.main_data_subjects[i])
    def search_subjects(self):
        self.searching_id=input("Enter subject id:")
        if self.searching_id in self.main_data_subjects.keys():
            print(f"Subject id={self.main_data_subjects[self.searching_id]['SUBJECT_ID']}")
            print(f"Subject name={self.main_data_subjects[self.searching_id]['SUBJECT_NAME']}")
            print(f"Year={self.main_data_subjects[self.searching_id]['YEAR']}")
            print(f"Branch={self.main_data_subjects[self.searching_id]['BRANCH']}")
            print(f"Credits={self.main_data_subjects[self.searching_id]['CREDITS']}")
        else:
            print("Subject not found")
class Initializing_classes:
    def __init__(self,file,reader):
        self.file=file
        self.main_classes_data=reader
        while True:
            self.branch=input("Enter branch:").lower()
            if self.branch in ['cse','ece','eee']:
                break
            else:
                print("Enter valid branch")
        while True:
            try:
                self.year=int(input("Enter year:"))
                if self.year in[1,2,3,4]:
                    break
                else:
                    print("Enter valid year")
            except ValueError:
                print("Invalid input.Try again")
        while True:
            self.section=input("Enter section(ex:a,b,c...etc):").lower()
            self.pattern=r"[a-z]+"
            if re.fullmatch(self.pattern,self.section):
                if self.section not in self.main_classes_data[self.branch][self.year]:
                    break
                else:
                    print("This section already existed.Try again")
            else:
                print("Enter valid section format")
        with open("classes.csv",'a',newline='') as classes_write_csv:
            classes_writer=csv.DictWriter(classes_write_csv,fieldnames=['BRANCH','YEAR','SECTION'])
            if not self.file:
                classes_writer.writeheader()
            classes_writer.writerow({'BRANCH':self.branch,'YEAR':self.year,'SECTION':self.section})
class Assign_subjects_classes_to_faculty:
    def __init__(self,file,faculty_data,subjects_data,classes_data,faculty_assignment_data):
        self.file=file
        self.main_faculty_assignment_data=faculty_assignment_data
        self.faculty_data=faculty_data
        self.subjects_data=subjects_data
        self.main_classes_data=classes_data
        self.main_faculty_data={}
        for i in self.faculty_data.keys():
            if self.faculty_data[i]["DEPARTMENT"] not in self.main_faculty_data.keys():
                self.main_faculty_data[self.faculty_data[i]["DEPARTMENT"]]=[]
                self.main_faculty_data[self.faculty_data[i]["DEPARTMENT"]].append(self.faculty_data[i])
            else:
                self.main_faculty_data[self.faculty_data[i]["DEPARTMENT"]].append(self.faculty_data[i])
        self.main_subjects_data={}
        for i in self.subjects_data.keys():
            if self.subjects_data[i]['BRANCH'] not in self.main_subjects_data.keys():
                self.main_subjects_data[self.subjects_data[i]['BRANCH']]={}
                self.main_subjects_data[self.subjects_data[i]['BRANCH']][self.subjects_data[i]["YEAR"]]=[]
                self.main_subjects_data[self.subjects_data[i]['BRANCH']][self.subjects_data[i]["YEAR"]].append(self.subjects_data[i])
            else:
                if self.subjects_data[i]['YEAR'] not in self.main_subjects_data[self.subjects_data[i]['BRANCH']].keys():
                    self.main_subjects_data[self.subjects_data[i]['BRANCH']][self.subjects_data[i]["YEAR"]] = []
                    self.main_subjects_data[self.subjects_data[i]['BRANCH']][self.subjects_data[i]["YEAR"]].append(self.subjects_data[i])
                else:
                    self.main_subjects_data[self.subjects_data[i]['BRANCH']][self.subjects_data[i]["YEAR"]].append(self.subjects_data[i])
    def assign_subjects(self):
        while True:
            self.branch=input("Enter branch:").lower()
            if self.branch in ['cse','ece','eee']:
                break
            else:
                print("Invalid input.Try again")
        while True:
            try:
                self.year=int(input("Enter year:"))
                if self.year in [1,2,3,4]:
                    break
                else:
                    print("Invalid input.Try again")
            except ValueError:
                print("Invalid input format.Try again")
        self.faculty_id_list=[]
        self.subject_id_list=[]
        for i in self.main_faculty_data[self.branch]:
            self.faculty_id_list.append(i['ID'])
        for i in self.main_subjects_data[self.branch][self.year]:
            self.subject_id_list.append(i['SUBJECT_ID'])
        print("======Faculty======")
        for i in self.main_faculty_data[self.branch]:
            print(f"Faculty id={i['ID']}  Name={i["NAME"]}")
        print("======Subjects======")
        for i in self.main_subjects_data[self.branch][self.year]:
            print(f"Subject id={i["SUBJECT_ID"]}  Subject name={i['SUBJECT_NAME']}")
        print(f"======Sections in {self.year} year======")
        for i in self.main_classes_data[self.branch][self.year]:
            print(f"Section={i}")
        print("Enter required details to assign subjects and classes for faculty")
        while True:
            while True:
                self.faculty_id=input("Enter faculty id:")
                if self.faculty_id in self.faculty_id_list:
                    break
                else:
                    print("Invalid input.Try again")
            while True:
                self.subject_id=input("Enter subject id:")
                if self.subject_id in self.subject_id_list:
                    break
                else:
                    print("Invalid input.Try again")
            while True:
                self.section=input("Enter section:").lower()
                if self.section in self.main_classes_data[self.branch][self.year]:
                    break
                else:
                    print("Invalid input.Try again")
            self.section_subjects=[]
            for i in self.main_faculty_assignment_data[self.branch][self.year][self.section]:
                self.section_subjects.append(i.keys())
            if self.subject_id not in self.section_subjects:
                with open("faculty_assignment.csv",'a') as faculty_assignment_csv:
                    assignment=csv.DictWriter(faculty_assignment_csv,fieldnames=['FACULTY_ID','SUBJECT_ID','SECTION','BRANCH','YEAR'])
                    if not self.file:
                        assignment.writeheader()
                    assignment.writerow({'FACULTY_ID':self.faculty_id,'SUBJECT_ID':self.subject_id,'SECTION':self.section,'BRANCH':self.branch,'YEAR':self.year})
                print("Faculty assignment is successfully")
                break
            else:
                print(f"This {self.subject_id} subject is already assigned to this {self.section} section")
    def view_faculty_work_load(self):
        self.faculty_subjects=0
        self.id=input("Enter Faculty id:")
        if self.id in self.faculty_data.keys():
            self.faculty_branch=self.faculty_data[self.id]['DEPARTMENT']
        for i in self.main_faculty_assignment_data[self.faculty_branch].keys():
            for j in self.main_faculty_assignment_data[self.faculty_branch][i].keys():
                for k in self.main_faculty_assignment_data[self.faculty_branch][i][j].keys():
                    if self.main_faculty_assignment_data[self.faculty_branch][i][j][k]==self.id:
                        self.faculty_subjects+=1
        if self.faculty_subjects==0:
            print("No work")
        elif self.faculty_subjects>=1 and self.faculty_subjects<=4:
            print("Low")
        elif self.faculty_subjects > 4 and self.faculty_subjects <= 7:
            print("Medium")
        else:
            print("High")
def r(o):
    if(o.verify_Id() and o.verify_Name() and
            o.verify_password() and
            o.verify_Dob() and
            o.verify_Gender() and
            o.verify_Department() and
            o.verify_Email() and
            o.verify_Phone_no() and
            o.verify_Qualification() and
            o.verify_Experience() and
            o.Join() and
            o.Designation() and
            o.verify_employee_type()):
        o.faculty_database()
    else:
        print("Your not eligible for this college")
