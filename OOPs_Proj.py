class Chatbot:
    def __init__(self):
        self.username = ""
        self.password =""
        self.logged_in = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbot ! how would you like to proceed? 
                           1.press1 to signup
                           2.press2 to signin
                           3.press3 to write a post
                           4.press4 to message a friend
                           5.press anyother key to exit
                           """)
        if user_input == '1':
            self.Signup()
        elif user_input == '2':
            self.Signin()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()
    def Signup(self):
        email = input("Enter your email: ")
        password = input("Setup your password: ")
        self.username = email
        self.password = password
        print('You have signedup Sucessfully')
        self.menu()

    def Signin(self):
        if self.username == "" and self.password == "":
            print('Print Signup first')
        else:
            uname = input("Enter Your email/username here")
            passw = input("Enter your password here")
            if self.username == uname and self.password == passw:
                print("You have logged in successfully")
                self.logged_in = True
            else:
                print("Invalid credentials, please try again")
        print('\n')
        self.menu()

 
obj= Chatbot()


