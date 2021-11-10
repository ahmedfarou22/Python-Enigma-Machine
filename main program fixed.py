import ctypes 

class _MapEntry :
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
            return str(str(self.key)+" : "+ str(self.value))

class Array :
        def __init__( self, size ):
            assert size > 0, "Array size must be > 0"
            self._size = size 
            PyArrayType = ctypes.py_object * size 
            self._elements = PyArrayType()
            self._itemCount =0
     

        def __len__( self ):
            return self._size
        
        def __print__(self):
            for i in range(self._itemCount):
                print(self._elements[i], end =" ")

        def insertLast(self, item):
            if self._size > self._itemCount:
                self._elements[self._itemCount] = item
                self._itemCount +=1
            else:
                print("Array is full")
        
        def insertAll(self, item):
            for letter in item: 
                if self._size > self._itemCount:
                    self._elements[self._itemCount] = letter
                    self._itemCount +=1
                    
                else:
                    print("Array is full")
        
        def __get_value__ (self,keyy):
            for item in self._elements:
                if keyy == item.key:
                    return item.value
        
        def linearSearch(self, term):
            for x in range(0,self._itemCount):
                if self._elements[x]== term:
                    return 1
            else:
                return 0
            
class rotor: # a data type that represents a rotor it takes in a number and outputs a number
    def __init__(self,rotor_in,rotor_out,rotor_notch):
        self.rotor_in =  rotor_in._elements # a list 
        self.rotor_out = rotor_out._elements # a list
        self.rotor_notch = rotor_notch # a letter 
    
    # def __inverse_rotor__(self):
    #      self.rotor_notch = "#"
    #      return rotor(self.rotor_out, self.rotor_in, self.rotor_notch)

    def __auto_rotate___(self): # this function rotates the rotor once this is helpfull because after every letter is pressed the first rotor must rotate once
        self.rotor_in = self.rotor_in[1:] + self.rotor_in[:1]      #rotate the rotor_in once 
        self.rotor_out = self.rotor_out[1:] + self.rotor_out[:1]   #rotate the rotor_out once 
    

    def __rotate_next__(self): # this function cheaks if the notch is at index zero if it is it returs 1 which is then used to rotate the next rotor before working it
        if self.rotor_out[0] == self.rotor_notch:  
            return 1
        else:
            return 0
    
    def __set_rotor__(self,setn): # this function is used to set the rotors before starting the machine it works by rotating the input and the output lists a certain number of unites
        self.rotor_in = self.rotor_in[setn:] + self.rotor_in[:setn]
        self.rotor_out = self.rotor_out[setn:] + self.rotor_out[:setn]

    
    def __work_rotor__(self,number,rotatenext): # this is the main function it has 2 main parts
        if rotatenext == 1: # part one cheak if the rotor before sent 1 if it did then rotate the rotor once before execting the rest of the function
            self.rotor_in = self.rotor_in[1:] + self.rotor_in[:1]
            self.rotor_out = self.rotor_out[1:] + self.rotor_out[:1]
        
        value = 0  # part 2 of the function working the rotor 
        value = self.rotor_in[number]     # store the value of the letter that is iputed in a varuble named value
        for i in range(len(self.rotor_out)): # loop around the rotor out and when the program finds the corsponding value return it
            if self.rotor_out[i] == value:
                return i
    
    def __work_inverse_rotor__(self,number,rotatenext): # this is the main function it has 2 main parts
        if rotatenext == 1: # part one cheak if the rotor before sent 1 if it did then rotate the rotor once before execting the rest of the function
            self.rotor_in = self.rotor_in[1:] + self.rotor_in[:1]
            self.rotor_out = self.rotor_out[1:] + self.rotor_out[:1]
        
        value = 0  # part 2 of the function working the rotor 
        value = self.rotor_out[number]     # store the value of the letter that is iputed in a varuble named value
        for i in range(len(self.rotor_in)): # loop around the rotor out and when the program finds the corsponding value return it
            if self.rotor_in[i] == value:
                    return i
    
def __plug_board__(letter,inputt,outputt):    # simple yet effective plug board
    # this plugboard works in a very simple way 
    # it has 2 lists input and output 
    # it cheaks the letter has what index in the input list and returns the value of the output list at the same index 
    for i in range(len(inputt)):
        if letter == inputt._elements[i]:
            return outputt._elements[i]

def __Man_reflector__(number): ## a reflector with hardcoded values
    # the easiest part of the program it takes a value and returns a diffrent one
    if number == 0:
        return 24
    
    if number == 1:
        return 17
    
    if number == 2:
        return 20
    
    if number == 3:
        return 7

    if number == 4:
        return 16

    if number == 5:
        return 18

    if number == 6:
        return 11

    if number == 7:
        return 3

    if number == 8:
        return 15

    if number == 9:
        return 23

    if number == 10:
        return 13

    if number == 11:
        return 6

    if number == 12:
        return 14
    
    if number == 13:
        return 10

    if number == 14:
        return 12

    if number == 15:
        return 8

    if number == 16:
        return 4

    if number == 17:
        return 1

    if number == 18:
        return 5

    if number == 19:
        return 25

    if number == 20:
        return 2

    if number == 21:
        return 22

    if number == 22:
        return 21
    
    if number == 23:
        return 9

    if number == 24:
        return 0
    
    if number == 25:
        return 19

    if number == 26:
        return 27
    if number == 27:
        return 26
    if number == 28:
        return 29
    if number == 29:
        return 28
    if number == 30:
        return 31
    if number == 31:
        return 30
    if number == 32:
        return 33
    if number == 33:
        return 32
    if number == 34:
        return 35
    if number == 35: 
        return 36
    if number == 36:
        return 35 
    if number == 37:
        return 38
    if number == 38:
        return 37
    if number == 39:
        return 40
    if number == 40:
        return 39
    if number == 41:
        return 42
    if number == 42:
        return 41
    if number == 43:
        return 44
    if number == 44:
        return 43
    if number == 45:
        return 46
    if number == 46:
        return 45
    if number == 47:
        return 48
    if number == 48:
        return 47
    if number == 49:
        return 50
    if number == 50:
        return 49
    if number == 51:
        return 52
    if number == 52:
        return 51
    if number == 53:
        return 54
    if number == 54:
        return 53
    if number == 55:
        return 56
    if number == 56:
        return 55
    if number == 57:
        return 58
    if number == 58:
        return 57
    if number == 59:
        return 60
    if number == 60:
        return 59
    if number == 61:
        return 61

def __iput_output__(number_or_letter): # to make the program easier all the rotars take in a number and output a number this function turns letters to numbers and numbers to letters
    value = 0
    alphabet = rotor_out 

    if number_or_letter in alphabet._elements:
        #this is a letter lets convert to a number 
        for i in range(len(alphabet._elements)):
            if alphabet._elements[i] == number_or_letter:
                value = i
                return i

    elif number_or_letter not in alphabet._elements:
        ## this is an intger lets convert it to a letter
         value = alphabet._elements[number_or_letter]
         return value



############## fixed arrays ######################
rotor_out = Array(62)
rotor_out.insertAll("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")



rotor_one_in = Array(62)
rotor_one_in.insertAll("ekmflgdqvzntowyhxuspaibrcjBYCHGLFMNAOEPUXDWVKJIRSZTQ4573628910")


rotor_two_in = Array(62)
rotor_two_in.insertAll("ajdksiruxblhwtmcqgznpyfvoeCXJBOQPWAIMUVNHTEFZGSRKYLD0354216987")

rotor_three_in = Array(62)
rotor_three_in.insertAll("bdfhjlcprtxvznyeiwgakmusqoGHJFIBARUQTSPVWYOZXCNLMKDE2347695801")

rotor_four_in = Array(62)
rotor_four_in.insertAll("opqrxwvyutabzcdhsijklegmnfGAXFHIJEVWDTUBONQSCRLYZMPK1329876054")

rotor_five_in = Array(62)
rotor_five_in.insertAll("ikzwvujtsrqlmncdopefyxghbaZYXWVUTSRQPONMLKJIHGFEDCBA9876543210")

outputtt = Array(62)
outputtt.insertAll("nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM9876543210")







################### 5 rotors ############### fixed 
entry1 = _MapEntry("I",  rotor(rotor_one_in,rotor_out,"q"))
entry2 = _MapEntry("II", rotor(rotor_two_in,rotor_out,"e"))
entry3 = _MapEntry("III",rotor(rotor_three_in,rotor_out,"v"))
entry4 = _MapEntry("IV", rotor(rotor_four_in,rotor_out,"u"))
entry5 = _MapEntry("V",  rotor(rotor_five_in,rotor_out,"b"))



map1 = Array(5)
map1.insertLast(entry1)
map1.insertLast(entry2)
map1.insertLast(entry3)
map1.insertLast(entry4)
map1.insertLast(entry5)



# ==========================================================  program Starts Here =============================================================================

##################### configure the plug board ###############

print("plug board configuration")

while True:
    y_n = str(input("you have 3 options press 1 continue witout a plugboard press 2 to continue with a predefined plugboard or press 3 to configure your own plugboard : "))
    if y_n == "1":
        break
    elif y_n == "2":
        break
    elif y_n == "3":
        break
    else:
        print("please enter 1 2 or 3 : ")
        continue

if y_n == "3":
    inputt = Array(62)
    outputt = Array(62)
    for i in range(0,31):
        while True:
            match = input("match 2 letters together Example <AB>: ") 
            if len(match) > 2:
                print("please enter 2 values only")
                continue
            elif len(match) == 1:
                print(" please use two letters together")
                continue
            
            elif len(match) == 0:
                print(" please use two letters together")
                continue
            
            elif match[0] == match[1]:
                print(" do not be smart ha afshak")
                continue
            
            elif len(match) < 0:
                print(" soory i did not uderstand that")
                continue

            elif inputt.linearSearch(match[0]) == 1:
                print("you already assined this before")

            
            elif inputt.linearSearch(match[1]) == 1:
                print("you already assined this before")
            
            elif outputt.linearSearch(match[0]) == 1:
                print("you already assined this before")

            
            elif outputt.linearSearch(match[1]) == 1:
                print("you already assined this before")            

            else:
                inputt.insertLast(match[0])
                outputt.insertLast(match[1])
                break

    for k in range(0,31):
        inputt.insertLast(outputt._elements[k])
        outputt.insertLast(inputt._elements[k])

if y_n == "2":
    inputt  =  rotor_out
    outputt = outputtt

elif y_n == "1":
    print ("you did not configure a plug board we will proceed without a plug board")
    inputt  =  rotor_out
    outputt = rotor_out




###################### choose the 3 rotors ############### with validation on input
while True:
    choose_the_first_rotor  = input("first position: choose a  rotor from the one of the five > I, II, III, IV, V : ").upper()
    if choose_the_first_rotor == "I":
        break
    if choose_the_first_rotor == "II":
        break
    if choose_the_first_rotor == "III":
        break
    if choose_the_first_rotor == "IV":
        break
    if choose_the_first_rotor == "V":
        break
    else:
        print("Sorry I did not understand that please enter I, II, III, IV, or V")

while True:
    choose_the_second_rotor = input("second position: choose a  rotor from the one of the five > I, II, III, IV, V : ").upper()
    if choose_the_second_rotor == "I":
        break
    if choose_the_second_rotor == "II":
        break
    if choose_the_second_rotor == "III":
        break
    if choose_the_second_rotor == "IV":
        break
    if choose_the_second_rotor == "V":
        break
    else:
        print("Sorry I did not understand that please enter I, II, III, IV, or V")

while True:
    choose_the_third_rotor  = input("third position: choose a  rotor from the one of the five > I, II, III, IV, V : ").upper()
    if choose_the_third_rotor == "I":
        break
    if choose_the_third_rotor == "II":
        break
    if choose_the_third_rotor == "III":
        break
    if choose_the_third_rotor == "IV":
        break
    if choose_the_third_rotor == "V":
        break
    else:
        print("Sorry I did not understand that please enter I, II, III, IV, or V")



###################### set values to the 3 rotors ############### with validations
while True:
    try:
        set_rotor_one    = int(input("what number do you want to set rotor 1 to ? "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue

    if set_rotor_one < 0:
        print("Sorry, your response must not be negative.")
        continue
     
    if set_rotor_one > 62:
        print("Sorry, your response is bigger than 62.")
        continue   

    else:
        break


while True:
    try:
        set_rotor_two    = int(input("what number do you want to set rotor 2 to ? "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue

    if set_rotor_two < 0:
        print("Sorry, your response must not be negative.")
        continue
     
    if set_rotor_two > 62:
        print("Sorry, your response is bigger than 62.")
        continue   

    else:
        break


while True:
    try:
        set_rotor_three  = int(input("what number do you want to set rotor 3 to ? "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue

    if set_rotor_three < 0:
        print("Sorry, your response must not be negative.")
        continue
     
    if set_rotor_three > 62:
        print("Sorry, your response is bigger than 62.")
        continue   

    else:
        break




while True: # take the message and validate any spcial caracters
    message = str(input("what is the message you want to encript/decript "))
    if any(c in rotor_out._elements for c in message):
        break
        
    else:
        print("Your input contains values that are not suported please try agin")
        continue
result = ""




###################### create all rotors and give them set values ###############

firstrotor = map1.__get_value__(choose_the_first_rotor)
firstrotor.__set_rotor__(set_rotor_one)

secondrotor =map1.__get_value__(choose_the_second_rotor)
secondrotor.__set_rotor__(set_rotor_two)

thirdrotor = map1.__get_value__(choose_the_third_rotor)
thirdrotor.__set_rotor__(set_rotor_three)



# loop the entire message
for letter in message:
    if letter == " ":
        result = result + " "
    else:
        a = __plug_board__(letter,inputt,outputt)
        b = __iput_output__(a) 
        ################ rotor 1 ################
        firstrotor.__auto_rotate___()
        c = firstrotor.__work_rotor__(b,0)
        r1 = firstrotor.__rotate_next__()

        ################ rotor 2 ################
        d = secondrotor.__work_rotor__(c,r1)
        r2 = secondrotor.__rotate_next__()

        ################ rotor 3 ################
        e = thirdrotor.__work_rotor__(d,r2)

        ################ reflector ################
        f = __Man_reflector__(e)
        ################ rotor 4 ################
        g = thirdrotor.__work_inverse_rotor__(f,0)

        ################ rotor 5 ################
        h = secondrotor.__work_inverse_rotor__(g,0)

        ################ rotor 6 ################
        i = firstrotor.__work_inverse_rotor__(h,0)

        ############## input #####################
        j = __iput_output__(i)
        k = __plug_board__(j,inputt,outputt)
        result = result + k
print(result)

# to test memory use uncomment the line under
# import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
