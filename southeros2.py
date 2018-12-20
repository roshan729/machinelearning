# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:46:43 2018

@author: 762309
"""

import random
class southeros:
    def __init__(self,ruler = 'None',allies = None,non_allies = None,competing_kingdoms = None):
        self.ruler = ruler
        self.allies = []
        self.list_of_allies = {}
        self.non_allies = []
        self.competing_kingdoms = []
        self.kingdoms = ['LAND','WATER','ICE','AIR','FIRE','SPACE']
        self.kingdom_emblems = {'LAND': 'panda','WATER': 'octopus','ICE': 'mammoth','AIR': 'owl','FIRE': 'dragon','SPACE': 'gorilla'}
        self.messages = ['Summer is coming',
                         'a1d22n333a4444p',
                         'oaaawaala',
                         'zmzmzmzaztzozh',
                         'Go risk it all',
                         "Let's swing the sword together",
                         "Die or play the tame of thrones"
                         "Ahoy! Fight for me with men and money",
                         "Drag on Martin!",
                         "When you play the tame of thrones you win or you die.",
                         "What could we say to the Lord of Death? Game on?",
                         "Turn us away and we will burn you first",
                         "Death is so terribly final while life is full of possibilities.",
                         "You Win or You Die",
                         "His watch is Ended",
                         "Sphinx of black quartz judge my dozen vows",
                         "Fear cuts deeper than swords My Lord.",
                         "Different roads sometimes lead to the same castle.",
                         "A DRAGON IS NOT A SLAVE.",
                         "Do not waste paper",
                         "Go ring all the bells",
                         "Crazy Fredrick bought many very exquisite pearl emerald and diamond jewels.",
                         "The quick brown fox jumps over a lazy dog multiple times.",
                         "We promptly judged antique ivory buckles for the next prize.",
                         "Walar Morghulis: All men must die"]
        self.non_competing_kingdoms = ['LAND','WATER','ICE','AIR','FIRE','SPACE']
        
    def check_ruler_and_allies(self):
        print(self.ruler)
        print('Allies of Ruler?')
        if self.list_of_allies == {}:
            print('None')
        else:
            print(*self.list_of_allies[self.ruler])
            
    def generate_competing_kingdoms(self,kingdoms_competing):
        for i in self.kingdoms:
            if i in kingdoms_competing.upper():
                self.competing_kingdoms.append(i)
                self.non_competing_kingdoms.remove(i)
    
    def generate_message(self,sender,receiver):
        message = sender+" "+receiver+" "+random.choice(self.messages)
        return message
    
    def check_allies(self,sender,receiver,message,allies,non_allies):
        receiver_emblem = self.kingdom_emblems[receiver]
        v_check = 0
        for i in receiver_emblem:
            #Check if each letter of kingdom emblem is present in message
            if i in message.lower() and receiver_emblem.count(i) <= message.lower().count(i):
                v_check+=1
            else:
                break
        if v_check == len(receiver_emblem):
            #Add to list of kingdoms who have pledged their allegiance
            self.allies.append(receiver.upper())
            allies.append(receiver.upper())
            print(receiver.upper() + ' is now an ally')
        else:
            #Add to list of kingdoms who have not pledged their allegiance
            non_allies.append(receiver.upper())
            print(receiver.upper() + ' is not an ally')
    
    def send_message(self):
        for sender in self.competing_kingdoms:
            allies = []
            non_allies = []
            for receiver in self.non_competing_kingdoms:
                #Check if receiver is already someone's ally or not
                if receiver in self.allies:
                    print(f"{receiver} cannot be an ally for you")
                else:
                    print(f"{sender} has sent the following message to {receiver}:-",end = '')
                    message = self.generate_message(sender,receiver)
                    print(message)
                    self.check_allies(sender,receiver,message,allies,non_allies)
            #Add all the allies of the competing kingdom
            self.list_of_allies[sender] = allies
            print(f"Allies of {sender} are: ",end='')
            print(*allies)
    
    #Check the ballot to see who has how many kingdoms        
    def check_ballot(self):
        max_allies = -1
        ruler = ''
        #Count the ballot to find out highest votes
        for key,value in self.list_of_allies.items():
            #Find out the highest votes for first kingdom which received votes
            print(f"Check for kingdom {key}")
            if ruler == '' and len(value) > 0:
                ruler = key
                max_allies = len(value)
            elif ruler != '' and len(value) > max_allies:                
                total_allies = len(value)
                if total_allies > max_allies:
                    max_allies = total_allies
                    ruler = key
            print(f"Ruler after check for {key} is {ruler} with votes of {max_allies}")
        
        print(f"Final ruler is {ruler} and max allies is {max_allies}")
        #Eliminate kingdoms who do not have highest number of allies
        for key,value in self.list_of_allies.items():
            if len(value) < max_allies:
                print(len(value))
                print(max_allies)
                print(key)
                print(f"Eliminate previous ruler {key}")
                self.competing_kingdoms.remove(key)
        #If more than one kingdom have maximum allies
        print(self.competing_kingdoms)
        if len(self.competing_kingdoms) > 1:
            return 1
        else:                  
            return ruler            
                
print("Welcome to Southeros. Do you want to know who the ruler is? Choose Yes or No")
n = input()
if n.lower() in ['y','yes','1']:
    A = southeros()
    A.check_ruler_and_allies()
    check_kingdoms_competing = 'Y'
    print("Enter the kingdoms competing to be the ruler from the following kingdoms: ",end='')
    print(*A.non_competing_kingdoms)
    kingdoms_competing = input()
    if kingdoms_competing != '':
        A.generate_competing_kingdoms(kingdoms_competing)
        print("The competing kingdoms are: ",end='')
        print(*A.competing_kingdoms)
    else:
        print("No kingdom is competing")
        exit
    while A.ruler == 'None':
        A.send_message()
        print("Allies after ballot are:-")
        print(A.list_of_allies)
        ballot = A.check_ballot()
        if ballot != 1:
            A.ruler = ballot
            print("Southeros has a ruler")
            print("Do you want to see who is ruling now? Yes or No")
            n = input()
            if n.lower() in ['y','yes','1']:
                A.check_ruler_and_allies()
        else:
            print("Continue ballot")
            