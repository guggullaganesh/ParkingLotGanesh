import sys
import random
import os
import datetime

class ParkingLot:

    nearest = 1
    car_colour = {}
    car_slot = {}
    near = 0
    slot = 0
    leftslot = 0

    def set_slot(self,slot):
        self.slot = slot

    def get_slot(self):
        return "\n\nCreated a parking lot with :-> {} slots :\n" .format(self.slot)

    def parkCar(self, key, value):
        if int(self.slot) >= 1:
            if self.leftslot >=1:
                self.near=self.leftslot
            else:
                self.near=self.nearest
            print("Allocated slot number: {}\n" .format(self.near))
            if self.leftslot >= 1:
                self.nearest=self.nearest+1
            else:
                self.nearest=self.near+1
            self.car_colour[key.strip()] = value.strip()
            self.car_slot[self.near] = key.strip()
            self.slot=int(self.slot)-1
        else:
            print("Sorry, parking lot is full")

    def parkCarDel(self,position):
        k=self.car_slot[position]
        del self.car_colour[k]
        del self.car_slot[position]
        self.slot = int(self.slot) + 1
        self.leftslot=position
        print("Slot number {} is free\n" .format(position))

    def regColour(self,colour):
        cnt = 0
        for ky, vl in self.car_colour.items():
            if colour in vl:
                print(ky)
                cnt = cnt + 1
        if cnt==0:
            print("registration_numbers_for_cars_with_colour {} Not Found\n" .format(colour))

    def carSlotNumForColur(self,colour):
        cnt = 0
        for ky, vl in self.car_colour.items():
            if colour in vl:
                for sk, sl in self.car_slot.items():
                    if ky in sl:
                        print(sk)
                        cnt = cnt + 1
        if cnt==0:
            print("slot_numbers_for_cars_with_colour {} Not Found\n".format(colour))

    def carSlotNumForReg(self,reg):
        cnt=0
        for ky, vl in self.car_slot.items():
            if reg in vl:
                print(ky)
                cnt=cnt+1
        if cnt==0:
            print("slot_number_for_registration_number {} Not Found\n".format(reg))

    def parkingStatus(self):
        for ke, va in self.car_slot.items():
            print(ke,'\t',va,'\t',self.car_colour[va],'\t')





print("Please enter the commands : ")
input=sys.stdin
for line in input:
    line=line.strip()
    words=line.split()
    args_cnt=len(words)
    if words[0] == 'create_parking_lot':
        pLot1 = ParkingLot()
        pLot1.set_slot(words[1])
        print(pLot1.get_slot())
    elif words[0] == 'park':
        pLot1.parkCar(words[1],words[2])
    elif words[0] == 'leave':
        pLot1.parkCarDel(int(words[1]))
    elif words[0] == 'status':
        pLot1.parkingStatus()
    elif words[0] == 'registration_numbers_for_cars_with_colour':
        pLot1.regColour(words[1])
    elif words[0] == 'slot_numbers_for_cars_with_colour':
        pLot1.carSlotNumForColur(words[1])
    elif words[0] == 'slot_number_for_registration_number':
        pLot1.carSlotNumForReg(words[1])
    else:
        print("Wrong Command Given")


