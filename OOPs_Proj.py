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
            pass
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()


obj= Chatbot()


