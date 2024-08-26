from Person import Person
class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms=[], Family =False):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        #ToDo1
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.Family = Family
        
        self.__doctor = 'None'
        self.__symptom = symptoms
        self.__appointments_made = []

    def full_name(self):
        """full name is first_name and surname"""
        #ToDo2
        return f"{self.__first_name} {self.__surname}"
    
    def get_age(self):
        #ToDo3
        return self.__age
    
    def get_surname(self):
        return self.__surname 

    def get_mobile(self):
        return self.__mobile
    
    def set_mobile(self, new_mobile):
        self._mobile = new_mobile

    def get_postcode(self):
        return self.__postcode
    
    def set_postcode(self, new_poscode):
        self.__postcode = new_poscode
    
    def get_doctor(self):
        return self.__doctor
        
    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def get_symptoms(self):
        return self.__symptom
        
    def print_symptoms(self):
        """prints all the symptoms"""
        #ToDo4
        symptoms = input("Enter the symptoms: ")
        print(f'The  patient symptoms: {symptoms}.')

    def get_appointments(self):
        return self.__appointments_made
    
    def add_to_appointments(self, appointment, date):
        self.__appointments_made.append((appointment, date))

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
