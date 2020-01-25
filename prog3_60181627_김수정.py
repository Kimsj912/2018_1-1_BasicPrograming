# Homework Assignment 3 
# # Name: 김수정    
# # Time Spent: 21:00

import random

class Building:
    number_of_floors = 0
    customer_list = []
    elevator = 0
    

    def __init__(self, floors, customers):
        self.number_of_floors = floors
        for customerID in range(1, customers + 1):
            new = Customer(customerID,self.number_of_floors)
            self.customer_list.append(new)
        self.customer_list.sort(key = lambda x: customerID)
        self.elevator = Elevator(floors,self.customer_list)
        self.output()

    def output(self):
        D_L=[]
        
        for customer in self.customer_list:
            if self.elevator.current_floor+1 == customer.current_floor and customer.customer_direction == 1:
                customer.in_elevator = True
                print('Customer',customer.customerID,' -> Elavator')

        print("Elevator's Current Floor : 1","     ","Elevator's direction: up")
        print("Customers:")
        for customer in self.customer_list:
            print("       ","Customer",customer.customerID,"    ","current floor :",customer.current_floor,"    ","destination floor:",customer.destination_floor)
            print("                        in Elevator :",customer.current_floor <self.elevator.current_floor+2,"    is Finished : ",self.elevator.current_floor+1 >customer.destination_floor)
            D_L.append(customer.destination_floor)
            D_L.sort()
        
        print('->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->') 
        b=""

        while (self.elevator.current_floor < self.elevator.number_of_floors-1) and b!='bye':
            CU_L=[]
            self.elevator.current_floor +=1
            if self.elevator.current_floor == self.elevator.number_of_floors-1:
                print("The Elevator is on the Top Floor New")
            print("Elevator :",self.elevator.current_floor,"->",self.elevator.current_floor+1)
            
            for customer in self.customer_list:
                if customer.in_elevator == False and self.elevator.current_floor+1 == customer.current_floor and customer.customer_direction == 1:
                    customer.in_elevator = True
                    print('Customer',customer.customerID,' -> Elavator')
                elif customer.in_elevator == False and self.elevator.current_floor+1 == customer.current_floor and customer.customer_direction == -1:
                    customer.in_elevator = True
                    print('Customer',customer.customerID,' -> Elavator')
                
                if self.elevator.current_floor+1 == customer.destination_floor and customer.in_elevator == True and customer.customer_direction == 1:
                    customer.in_elevator = False
                    print('Customer',customer.customerID,' -> Destination Floor')   
            print("Elevator's Current Floor :",self.elevator.current_floor+1,"     ","Elevator's direction: up")
            
            print("Customers:")
            for customer in self.customer_list:
                print("       ","Customer",customer.customerID,"    ","current floor :",customer.current_floor,"    ","destination floor:",customer.destination_floor)
                if customer.current_floor<customer.destination_floor:
                    if self.elevator.current_floor+1>=customer.destination_floor:
                        print("                        in Elevator :",customer.current_floor+1 <=self.elevator.current_floor+2 and self.elevator.current_floor+1 < customer.destination_floor,"    is Finished : ","True")
                    else:
                        print("                        in Elevator :",customer.current_floor+1 <=self.elevator.current_floor+2 ,"    is Finished : ","False")
                else:
                    print("                        in Elevator :",customer.current_floor+1 <=self.elevator.current_floor+2 ,"    is Finished : ","False")
                
            print('->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->')
           
            for customer in self.customer_list:
                if customer.customer_direction == 1 and customer.destination_floor<= self.elevator.number_of_floors-1:
                    CU_L.append(customer.destination_floor)
                    if len(CU_L)==len(self.customer_list) :
                        if max(CU_L)==self.elevator.current_floor+1:
                            b="bye"
        
        
        while (self.elevator.current_floor <= self.number_of_floors and self.elevator.current_floor >=1 and b!='bye'):
            CD_L=[]
            self.elevator.current_floor -= 1 
            print("Elevator :",self.elevator.current_floor+2,"->",self.elevator.current_floor+1) 
            
            for customer in self.customer_list:
                idt=customer.in_elevator == True and customer.destination_floor==self.elevator.current_floor+1
                if idt==True and customer.customer_direction == -1 :
                    customer.in_elevator = False
                    print('Customer',customer.customerID,' -> Destination Floor')
            print("Elevator's Current Floor :",self.elevator.current_floor+1,"     ","Elevator's direction: down")
            
            print("Customers:")
            for customer in self.customer_list:
                print("       ","Customer",customer.customerID,"    ","current floor :",customer.current_floor,"    ","destination floor:",customer.destination_floor)
                idt=customer.in_elevator == True or customer.destination_floor<self.elevator.current_floor+1
                if idt == False:
                    print("                        in Elevator :",idt,"    is Finished : ",True)
                else:
                    print("                        in Elevator :",idt,"    is Finished : ",False)          
            print('->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->')

            for customer in self.customer_list:
                if customer.customer_direction == -1  :
                    CD_L.append(customer.destination_floor)
                    if len(CD_L)==len(self.customer_list)-len(CU_L):
                        if min(CD_L)==self.elevator.current_floor+1:
                            b="bye"
        print()
        print()    
        print('All Customers Arrived ar Destination')

class Elevator:
    number_of_floors = 0
    register_list = []
    current_floor = 0
    up = 1
    down = -1

    def __init__(self, number_of_floors, register_list):
        self.number_of_floors = number_of_floors
        self.register_list = register_list

class Customer:
    current_floor = 0
    destination_floor = 0
    customerID = 0
    in_elevator = False
    finished = False
    customer_direction = 0

    def __init__(self, customerID, floors):
        self.customerID = customerID
        self.current_floor = random.randint(1, floors)
        self.destination_floor = random.randint(1, floors)
        while self.destination_floor == self.current_floor:
            self.destination_floor = random.randint(1, floors)
        if self.current_floor < self.destination_floor:
            self.customer_direction = 1
        else:
            self.customer_direction = -1

def identify(idt,what):
    while True:
        try:
            idt=float(idt)
            if idt==int(idt) and idt>0 :
                return int(idt)
            else:
                print("Wrong Input!!!")    
                idt=float(input("input "+what+" :"))
        except ValueError:
            print("Wrong Input")
            idt=input("input "+what+" :")

floors=identify(input("input num_of_floor:"),"num_of_floor")
customers=identify(input("input num_of_customer:"),"num_of_customer")
print()
print()
print()
building = Building(floors, customers)
