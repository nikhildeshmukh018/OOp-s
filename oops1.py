class employee:
    #special function/magic function/dunder method
    def __init__(self):
        print("Started Excecution of attributes")
        self.id=123
        self.salary=40000
        self.designation="Software Engineer"
        print('Attributes are initialized')

    def Travel(self,destination):
        print("This Travel function is called manually")
        print("Employee is travelling to", destination)



#creating an object of employee class
sam = employee()
print(type(sam))
# print(sam.salary)