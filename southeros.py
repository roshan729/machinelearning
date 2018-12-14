# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:55:44 2018

@author: 762309
"""

class southeros:
    def __init__(self,ruler = 'None',allies = None,non_allies = None):
        self.ruler = ruler
        self.allies = []
        self.non_allies = []
        self.kingdoms = ['LAND','WATER','ICE','AIR','FIRE','SPACE']
        self.kingdom_emblems = {'LAND': 'panda','WATER': 'octopus','ICE': 'mammoth','AIR': 'owl','FIRE': 'dragon','SPACE': 'gorilla'}
    def check_ruler_and_allies(self):
        print(self.ruler)
        print('Allies of Ruler?')
        if self.allies == []:
            print('None')
        else:
            print(*self.allies)
    def add_allies(self):
        print(f"Enter the ally to send message: {self.kingdoms}")
        ally_to_send_msg = input()
        if ally_to_send_msg.upper() in self.allies:
            print(f"{ally_to_send_msg.upper()} is already an ally")
            return "Enter again"
        if ally_to_send_msg.upper() in self.non_allies:
            print(f"{ally_to_send_msg} has already rejected to be your ally")
            return "Send your message to any other kingdom"
        elif ally_to_send_msg.upper() == 'SPACE':
            print(f"{ally_to_send_msg.upper()} is your kingdom")
            return "Enter again"
        if ally_to_send_msg.upper() in self.kingdoms:
            ally_emblem = self.kingdom_emblems[ally_to_send_msg.upper()]
            print(f"Enter the message you want to send to {ally_to_send_msg.upper()}")
            message = input()
            v_check = 0
            for i in ally_emblem:
                if i in message.lower() and ally_emblem.count(i) <= message.lower().count(i):
                    v_check+=1
                else:
                    break
            if v_check == len(ally_emblem):
                self.allies.append(ally_to_send_msg.upper())
                return ally_to_send_msg.upper() + ' is now an ally'
            else:
                self.non_allies.append(ally_to_send_msg.upper())
                return ally_to_send_msg.upper() + ' is not an ally'
        else:
            print(f"{ally_to_send_msg.upper()} is not a kingdom")
            
print("Welcome to Southeros. Do you want to know who the ruler is? Choose Yes or No")
n = input()
if n.lower() in ['y','yes','1']:
    A = southeros()
    A.check_ruler_and_allies()
if A.ruler == 'None':
    while len(A.allies) <3:
        if len(A.non_allies) == 3:
            print("You cannot become the ruler. You don't have enough allies")
            break
        else:
            print(A.add_allies())
        print(f"No of allies: {len(A.allies)}.")
        print(f"No of non-allies): {len(A.non_allies)}")
    if len(A.allies) == 3:
        A.ruler = 'Shan'
        print("Southeros has a ruler")
    print("Do you want to see who is ruling now? Yes or No")
    n = input()
    if n.lower() in ['y','yes','1']:
        A.check_ruler_and_allies()
