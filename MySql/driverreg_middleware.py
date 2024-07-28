import re
from tkinter import messagebox

class Driver_mid:
    def __init__(self, fname, lname, address,  email, phone_num, license_plate, password, usertype=''):
        self.__fname = fname
        self.__lname = lname
        self.__address = address
        self.__email = email
        self.__phone_num = phone_num
        self.__license = license_plate
        self.__password = password
        self.__usertype = usertype


    @property
    def firstname(self):
        return self.__fname


    @property
    def lastname(self):
        return self.__lname


    @property
    def address(self):
        return self.__address


    @property
    def email(self):
        return self.__email


    @property
    def phone_num(self):
        return self.__phone_num


    @property
    def license(self):
        return self.__license


    @property
    def password(self):
        return self.__password

    @property
    def usertype(self):
        return self.__usertype


    @firstname.setter
    def set_firstname(self, firstname):
        self.__fname = firstname


    @lastname.setter
    def set_lastname(self, lastname):
        self.__lname = lastname


    @address.setter
    def set_address(self, address):
        self.__address = address

    @email.setter
    def set_email(self, email):
        self.__email = email


    @phone_num.setter
    def set_phonenum(self, phonenum):
        self.__phone_num = phonenum


    @license.setter
    def set_license(self, license):
        self.__license = license


    @password.setter
    def set_password(self, password):
        self.__password = password

    @usertype.setter
    def set_usertype(self, usertype):
        self.__usertype =usertype


    def __str__(self):
        return self.firstname + ' ' + self.lastname + ' ' + self.address + ' ' + self.email + ' ' + self.phone_num + ' ' + self.license + ' ' + self.password + ' ' + self.usertype


##### ----- Validation Part ----- #####

    def is_valid_fname(self, name):
        if not re.match(r'^[A-Z]', name):
            messagebox.showerror('Name Error', 'Name must start with capital letter.')
            return False
        elif re.search(r'\d', name):
            messagebox.showerror('Name Error', 'Name should not content any numbers.')
            return False
        elif len(name) < 3:
            messagebox.showerror('Name Error', 'Length of name should be greater than or equals to 3.')
            return False
        else:
            return True

    def is_valid_lname(self, name):
        if not re.match(r'^[A-Z]', name):
            messagebox.showerror('Last name Error', 'Last name should be always start with capital letter.')
            return False
        elif re.search(r'\d', name):
            messagebox.showerror('Last name Error', 'Last name should not content any numbers.')
            return False
        elif len(name) < 4:
            messagebox.showerror('Last name Error', 'Length of last name should be greater than or equals to 4.')
            return False
        else:
            return True

    def is_valid_address(self, address):
        if not re.match(r'^[A-Z]', address):
            messagebox.showerror('Address Error', 'Address name should always start with capital letter.')
            return False
        elif len(address) < 4:
            messagebox.showerror('Address Error', 'Length of address name should be greater than or equals to 4.')
            return False
        else:
            return True

    def is_valid_number(self, number):
        # Check if the input string is a 10-digit number starting with 9, with the second digit in the range 6 to 8
        if re.fullmatch(r'^9[6-8]\d{8}$', number) is not None:
            # If it is, return True
            return True
        else:
            # If it is not, return False
            messagebox.showerror('Contact Number Error', 'Contact numbers should be of 10 digits.\n'
                                                         'Insert only numbers.\n'
                                                         'Contact numbers should start with first digit 9 and seconf digit 6-8.')
            return False

    def is_valid_email(self, email):
        # Use a regular expression to check if the email address is valid
        regex = '^[a-z][\w\.-]*@(gmail|icloud)\.com$'
        if re.search(regex, email):
            # If the email address is valid, return True
            return True
        else:
            # If the email address is not valid, return False
            messagebox.showerror('Email Error', 'All the characters must be in small letter.\n'
                                                'Email should contain @gmail.com or @icloud.com at the end of email.\n')
            return False

    def is_valid_password(self, password):
        # Use a regular expression to check if the email address is valid
        regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
        if re.search(regex, password):
            # If the email address is valid, return True
            return True
        else:
            # If the email address is not valid, return False
            messagebox.showerror('Password Error', 'Password should contain 8 characters long.\n'
                                                   'Password should contain atleast 1 numbers, capital and small letter,'
                                                   'and special symbols.')
            return False

    def is_valid_licence(self, licence):
        # Check if the input string is a 5-digit number
        if re.fullmatch(r'^[0-9]\d{4}$', licence) is not None:
            # If it is, return True
            return True
        else:
            # If it is not, return False
            messagebox.showerror('Licence Number Error', 'LLicence numbers should be of 5 digits.')
            return False