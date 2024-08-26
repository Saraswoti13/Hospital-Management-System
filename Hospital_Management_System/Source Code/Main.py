from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 'Diabetes', 20, '07012345678','B1 234'), Patient('Mike','Jones', 'Gastritis', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 'Migraine', 15, '07123456789','C1 ABC')]

    discharged_patients = []
    

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- View Patients/Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin details')
        print(' 6- View all the patients from the same family')
        print(' 7- Patient Records')
        print(' 8- Get Management Report')
        print(' 9- Relocate patients from one doctor to another')
        print('10- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
         #ToDo1
            admin.doctor_management(doctors)

        elif op == '2':
            # 2- View or discharge patients
            #ToDo2
            print('Choose the operation:')
            print(' 1- view patients')
            print(' 2- Discharge patients')
            opt = int(input('Option: '))
            if opt == 1:
                admin.view_patient(patients)

            # ToDo3
            elif opt == 2:
                op = input('Do you want to discharge a patient(Y/N): ').lower()

                if op == 'yes' or op == 'y':
                    admin.discharge_patient(patients, discharged_patients)
                elif op == 'no' or op == 'n':
                    break
                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            # 3 - view discharged patients
            #ToDo4
            admin.view_discharged_patient(discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin details
            admin.update_details()

        elif op == '6':
            admin.same_family(patients)

        elif op == '7':
            print('Choose any operation: ')
            print('1. Store Records ')
            print('2. Load Records ')

            op = input('Options: ')

            if op == '1':
                admin.store_patientsrecords(patients, 'patients.txt')
            elif op == '2':
                admin.load_patientsrecords('patients.txt')
            else:
                print('Invalid Option: Try Again!')

        elif op == '8':
            # 8 - Management
            print('Choose an operation: ')
            print('1-Total number of doctors')
            print('2-Total number of patients per doctors ')
            print('3-Total appointments per doctor')
            print('4-Total number of patient based on illness')
            op = input('Input: ')
                
            if op == '1':
                admin.total_doctors(doctors)
                    
            elif op == '2':
                admin.patients_per_doctor(doctors)
                    
            elif op == '3':
                admin.appointment_management(patients, doctors)
            
            elif op == '4':
                admin.patient_illness(patients)
                    
            else:
                print("Invalid Option: Try Again!")

        elif op == '9':
            admin.relocate_doctor(patients, doctors)

        elif op == '10':
            # 6 - Quit
            #ToDo5
            print("---Operation Terminated---")
            break
        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
