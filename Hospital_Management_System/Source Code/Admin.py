from Doctor import Doctor
from Patient import Patient
from datetime import datetime

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

        self.patients = []

    def view(self, a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        if len(a_list) == 0:
            print("Data is empty")
        else:
            for index, item in enumerate(a_list):
                print(f'{index + 1:3}|{item}')

    def login(self):
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        #ToDo1
        return self.__username in username and self.__password == password

    def find_index(self, index, doctors):
        
            # check that the doctor id exists          
        if index in range(0, len(doctors)):
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self):
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        print("Enter doctor\'s details: ")
        first_name = input('Enter your first name: ')
        surname = input('Enter your surname: ')
        speciality = input('Enter your speciality: ')
        return first_name, surname, speciality

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")
        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op = input('Input: ')

        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4
            first_name, surname, speciality = self.get_doctor_details()

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    #ToDo5
                    break # save time and end the loop

            #ToDo6
            doctors.append(Doctor(first_name, surname, speciality))# add the doctor ...
                                                         # ... to the list of doctors
            print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1 
                    doctor_index = self.find_index(index, doctors)
                    if doctor_index != False:
                        break
                    else:
                        print("Doctor not found")

                        # doctor_index is the ID mines one (-1)
                        
                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')
        
            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            opt = int(input('Input: ')) # make the user input lowercase

            # #ToDo8
            if opt == 1:
                first_name = input('Enter a new first name: ')
                doctors[index].set_first_name(first_name)
                print("-----Successfully updated-----")
                self.view(doctors)
            elif opt == 2:
                surname = input('Enter a new surname: ')
                doctors[index].set_surname(surname)
                print("-----Successfully updated-----")
                self.view(doctors)
            elif opt == 3:
                speciality = input('Enter a new speciality: ')
                doctors[index].set_speciality(speciality)
                print("-----Successfully updated-----")
                self.view(doctors)
            else:
                print('Invalid input!!')
        

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = int(input('Enter the ID of the doctor to be deleted: '))
            #ToDo9
            if doctor_index in range(1, doctor_index + 1):
                del doctors[doctor_index - 1]
                print(f'The doctor with ID number {doctor_index} is deleted successfully.')
                self.view(doctors)
            else:
                print('The id entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |       Full Name    |  Doctor`s Full Name  | Symptoms |Age| Postcode ')
        #ToDo10
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                print(patients[patient_index].get_doctor())

                print('The patient is now assign to the doctor.') 

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge_patient(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")
        self.view(patients)
        if len(patients) != 0:
            patient_index = int(input('Please enter the patient ID: ')) - 1
        #ToDo12
        discharge_patients.append(patients[patient_index])
        del patients[patient_index]
        print("Successfully discharged.")
    
    def view_discharged_patient(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo13
        for index, item in enumerate(discharged_patients):
            print(f'{index + 1:3}|{item}')

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            #ToDo14
            username = input('Enter the new username: ')
            # validate the password
            if username == input('Enter the new username again: '):
                self.__username = username
                print('Username updated. ')
            else:
                print("New Username must be same. ")
            

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
                print("Password updated. ")
            else:
                print("New Password must be same. ")

        elif op == 3:
            #ToDo15
            address = input('Enter the new address: ')
            # validate the password
            if address == input('Enter the new address again: '):
                self.__address = address
                print('Address updated. ')
            else:
                print("New Address must be same. ")
        else:
            #ToDo16
            print('Invalid choice. You should choose between 1,2 & 3. ')

    def same_family(self,patients):
        family_link = {}
        for patient in patients:
            surname = patient.get_surname()
            if surname not in family_link:
                family_link[surname] = [patient]
            else:
                family_link[surname].append(patient)
        
        for surname, family_member in family_link.items():
            print(f'Family: {surname} ')
            print()
            print('         Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            print()
            for member in family_member:
                print(member)  
            print()
        
    def store_patientsrecords(self, patients, filename):
        with open (filename,'w') as file:
            for patient in patients:
                file.write(f"{patient.full_name()}, {patient.get_symptoms()},{patient.get_age()},{patient.get_mobile()},{patient.get_postcode()},{patient.get_doctor()}\n")
        print("Patients  data stored successfully.")
    
    def load_patientsrecords(self, filename):
        filename = 'patients.txt'
        with open (filename, 'r') as file:
            patient = []
            for line in file:
                if line[-1] == '\n':
                    patient.append(line[:-1])
                else:
                    patient.append(line)
        print(patient)
        print()        
        print("Patient Records has been loaded from file")

    def total_doctors(self, doctors):
        
        print("Management Report:")     
        total_doctors =  len(doctors)
        
        print(f"Total number of doctors in the system: {total_doctors}")
        
    def patients_per_doctor(self, doctors):
        
        print("Total number of patients per doctor: ")
        for doctor in doctors:
            print(f"{doctor.full_name()}: {len(doctor.get_patients())} patients")

    def appointment_management(self, patients, doctors):
        print("---Appointments---")
        print('Choose the operation:')
        print(' 1 - Book an appointment')
        print(' 2 - Check appointment status')
        print(' 3 - View appointments by month')

        op = input('Input: ')

        if op == "1":
            print("-----Book an appointment-----")
        
            print("-----List of patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            self.view(patients)
            try:
                p_index = int(input('Enter the ID of the patient: ')) - 1
                patient_index = self.find_index(p_index, patients)
                if patient_index == False:
                    print("Patient not found")
                    return
            except ValueError:
                print('The ID entered is incorrect')
                return

            selected_patient = patients[p_index] 

            print("-----List of doctors-----")
            print('ID |          Full name           |  Speciality')
            self.view(doctors)
            try:
                d_index = int(input('Enter the ID of the doctor: ')) - 1
                doctor_index=self.find_index(d_index,doctors)
                if doctor_index == False:
                    print("Doctor not found")
                    return
            except ValueError:
                print('The ID entered is incorrect')
                return

            selected_doctor = doctors[d_index] 

            appointment_date = input('Enter the appointment date (YYYY-MM-DD): ')
            try:
                date_obj = datetime.strptime(appointment_date, '%Y-%m-%d')
                selected_patient.add_to_appointments(selected_doctor, date_obj)
                selected_doctor.add_appointments(selected_patient, date_obj)
                print("Appointment booked. You can check your appointment status.")

            except ValueError:
                print('Invalid date format. Please use YYYY-MM-DD.')
        
        elif op == "2":
            print("-----Check appointment status-----")

            print("-----List of patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            self.view(patients)
            try:
                p_index = int(input('Enter the ID of the patient: ')) - 1
                patient_index=self.find_index(p_index,patients)
                if patient_index == False:
                    print("Patient not found")
                    return
            except ValueError:
                print('The ID entered is incorrect')
                return
            
            selected_patient = patients[p_index] # patient object
            appointments_made = selected_patient.get_appointments()

            print("-----Appointment Status-----")
            print(f"{'S.No.':5}|{'Appointments':^60}|{'Date':^20}|{'Status':^30}")
            for counter, (doctor, date) in enumerate(appointments_made):
                status = 'Approved' if selected_patient.get_doctor() == doctor.full_name() else 'Pending'
                print(f"{counter+1:>5}|{'Appointment with '+doctor.full_name():^60}|{date.strftime('%Y-%m-%d'):^20}|{status:^30}")

        elif op == "3":
            print("-----View appointments by month-----")

            print("-----List of doctors-----")
            print('ID |          Full name           |  Speciality')
            self.view(doctors)
            try:
                d_index = int(input('Enter the ID of the doctor: ')) - 1
                doctor_index=self.find_index(d_index,doctors)
                if doctor_index == False:
                    print("Doctor not found")
                    return
            except ValueError:
                print('The ID entered is incorrect')
                return

            selected_doctor = doctors[d_index] # doctor object
            month_year = input('Enter the month and year (YYYY-MM): ')
            try:
                month_year_obj = datetime.strptime(month_year, '%Y-%m')
                appointments = selected_doctor.get_appointments()
                print(f"Appointments for {selected_doctor.full_name()} in {month_year_obj.strftime('%B %Y')}:")
                print(f"{'S.No.':5}|{'Patient':^30}|{'Date':^20}")
                counter = 1
                for patient, date in appointments:
                    if date.year == month_year_obj.year and date.month == month_year_obj.month:
                        print(f"{counter:>5}|{patient.full_name():^30}|{date.strftime('%Y-%m-%d'):^20}")
                        counter += 1
                if counter == 1:
                    print("No appointments found for the given month.")
            except ValueError:
                print('Invalid month/year format. Please use YYYY-MM.')

        else:
            print('Invalid operation chosen. Check your input!')

    def patient_illness(self, patients):
        print('Total number of patients based on the illness type: ')
        symptoms_type = {}
        for patient in patients:
            symptom = patient.get_symptoms()
            
            if symptom not in symptoms_type:
                symptoms_type[symptom] = 1
            else:
                symptoms_type += 1

        for symptom, patient_count in symptoms_type.items():
            print(f'{symptom}: {patient_count} patients')

    def get_management_report(self, doctors, patients):
        print("----Management Reports----")
        print('Choose the operation: ')
        print('1. Total number of doctors in the system')
        print('2. Total number of patients per doctor')
        print('3. Total number of appointments per month per doctor') 
        print('4. Total number of patient based on illness')
        op = input('Choose an option: ')
        try:
            if op == '1':
                print(f"The total number of doctors in the system: {len(doctors)}")
            
            elif op == '2':
                for doctor in doctors:
                    # totalPatients = doctor.get_total_patients()
                    print(f"{doctor.full_name()}: {len(doctor.get_patient())} patients")
            
            elif op == '3':
                total_appointments_per_doctor = {}
                for doctor in doctors:
                    total_appointments_per_doctor[doctor.full_name()] = len(doctor.get_appointments())

            elif op == '4':
                symptoms_type = {}
                for patient in patients:
                    symptom = patient.get_symptoms()
                    if symptom not in symptoms_type:
                        symptoms_type[symptom]= 1
                    else:
                        symptoms_type[symptom] += 1

                symptoms = list(symptoms_type.keys())
                patients_count = list(symptoms_type.values())
                self.plot_pie(symptoms, patients_count, "Patient based on illness type")
            else:
                print('Invalid option')
                
        except Exception as e:
            print(e)

    def relocate_doctor(self, patients, doctors):
        
        print('----Relocate Doctor----')
        print('----List of Patients----')
        self.view(patients)

        if len(patients) != 0:
            try:
                patient_index = int(input('Enter the ID of the patient to relocate the doctor: ')) - 1
                if 0 <= patient_index < len(patients):
                    print('-----List of Doctors-----')
                    self.view(doctors)
                    new_doctor_index = int(input('Enter the ID of the new doctor: ')) - 1

                    if 0 <= new_doctor_index < len(doctors):
                        old_doctor_full_name = patients[patient_index].get_doctor()
                        patients[patient_index].link(doctors[new_doctor_index].full_name())
                        doctors[new_doctor_index].add_patient(patients[patient_index])
                        print(f"Successfully Relocated {doctors[new_doctor_index].full_name()} to {patients[patient_index]}.")
                    else:
                        print('Invalid doctor ID. Check your input again.')
                else:
                    print('Invalid patient ID. Check your input again.')
            except ValueError:
                print('Invalid input for patient or doctor. Please enter a valid option.')
        else:
            print('No patients available for relocation.')