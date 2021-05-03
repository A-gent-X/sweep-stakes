class contestant_Class:
    def __init__(self, first_name, last_name, address, email, registration_num):
        self.first_name = first_name()
        self.last_name = last_name()
        self.address = address()
        self.email = email()
        self.registation_num = registration_num()


    def create_information_list(self):
        first_name = input("\nprovide first name for records\n")
        last_name = input("\nprovide first name for records\n")
        address = input("\nprovide first name for records\n")
        email = input("\nprovide first name for records\n")
        registation_num = input("\nprovide first name for records\n")
        print(first_name, last_name, address, email, registation_num)





