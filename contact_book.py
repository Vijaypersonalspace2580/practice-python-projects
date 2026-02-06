try:
    def add_contacts():
        name = str(input('Enter name: '))
        name=name.lower()
        phone_number = int(input('Enter phone number: '))
        l = len(str(phone_number))
        if l == 10:
            repeat_contact = 0
            for i, j in phone_book.items():
                if i == name or j == phone_number:
                    repeat_contact += 1
            if repeat_contact == 0:
                phone_book[name]=phone_number
                swapped_phone_book[phone_number]=name
            else:
                print('Contact existed')
                add_contacts()
        else:
            print('Invalid phone number')
            add_contacts()
    def search_contact():
        choice = str(input('do you search by name or phone number(n/p): '))
        if choice == 'n':
            name = str(input('Enter name: '))
            name = name.lower()
            print(phone_book[name])
        elif choice == 'p':
            phone_number = str(input('Enter phone number: '))
            if len(str(phone_number)) == 10:
                print(swapped_phone_book[phone_number])
            else:
                print('Invalid phone number')
                search_contact()
        else:
            print('Invalid option')
            search_contact()
    def delete_contact():
        choice = str(input('do you delete by name or phone number(n/p): '))
        if choice == 'n':
            name = str(input('Enter name: '))
            name = name.lower()
            del phone_book[name]
        elif choice == 'p':
            phone_number = str(input('Enter phone number: '))
            if len(str(phone_number)) == 10:
                del swapped_phone_book[phone_number]
            else:
                print('Invalid phone number')
                delete_contact()
        else:
            print('Invalid option')
            delete_contact()
        display_contacts()
    def display_contacts():
        for i,j in phone_book.items():
            print(i,j)
    phone_book={}
    swapped_phone_book={}
    n=int(input('Enter how many contacts do you add: '))
    print('Enter name and phone number:')
    for i in range(n):
        add_contacts()
    swapped_phone_book={}
    s='y'
    while(s=='y' or s=='Y'):
        print('1.Add contact')
        print('2.Search contact')
        print('3.Delete contact')
        print('4.Display all contacts')
        option=int(input('Enter your option(1,2,3,4): '))
        if option==1:
            add_contacts()
        elif option==2:
            search_contact()
        elif option==3:
            delete_contact()
        elif option==4:
            display_contacts()
        else:
            print('Invalid option')
        s=str(input("Do you want choose any other service(y/n)="))
except:
    print('Invalid input')