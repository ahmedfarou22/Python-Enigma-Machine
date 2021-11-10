import time
class rotor: # a data type that represents a rotor it takes in a number and outputs a number
    def __init__(self,rotor_in,rotor_out,rotor_notch):
        self.rotor_in =  rotor_in # a list 
        self.rotor_out = rotor_out # a list
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
        if letter == inputt[i]:
            return outputt[i]

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
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"] 
    if number_or_letter in alphabet:
        #this is a letter lets convert to a number 
        for i in range(len(alphabet)):
            if alphabet[i] == number_or_letter:
                value = i
                return i

    elif number_or_letter not in alphabet:
        ## this is an intger lets convert it to a letter
         value = alphabet[number_or_letter]
         return value

################### 5 rotors ###############

rotor_dictionary = {
  "I"   : rotor(["e","k","m","f","l","g","d","q","v","z","n","t","o","w","y","h","x","u","s","p","a","i","b","r","c","j","B","Y","C","H","G","L","F","M","N","A","O","E","P","U","X","D","W","V","K","J","I","R","S","Z","T","Q","4","5","7","3","6","2","8","9","1","0"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"],"q"),
  "II"  : rotor(["a","j","d","k","s","i","r","u","x","b","l","h","w","t","m","c","q","g","z","n","p","y","f","v","o","e","C","X","J","B","O","Q","P","W","A","I","M","U","V","N","H","T","E","F","Z","G","S","R","K","Y","L","D","0","3","5","4","2","1","6","9","8","7"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"],"e"),
  "III" : rotor(["b","d","f","h","j","l","c","p","r","t","x","v","z","n","y","e","i","w","g","a","k","m","u","s","q","o","G","H","J","F","I","B","A","R","U","Q","T","S","P","V","W","Y","O","Z","X","C","N","L","M","K","D","E","2","3","4","7","6","9","5","8","0","1"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"],"v"),
  "IV"  : rotor(["o","p","q","r","x","w","v","y","u","t","a","b","z","c","d","h","s","i","j","k","l","e","g","m","n","f","G","A","X","F","H","I","J","E","V","W","D","T","U","B","O","N","Q","S","C","R","L","Y","Z","M","P","K","1","3","2","9","8","7","6","0","5","4"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"],"u"),
  "V"   : rotor(["i","k","z","w","v","u","j","t","s","r","q","l","m","n","c","d","o","p","e","f","y","x","g","h","b","a","Z","Y","X","W","V","U","T","S","R","Q","P","O","N","M","L","K","J","I","H","G","F","E","D","C","B","A","9","8","7","6","5","4","3","2","1","0"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"],"b")
}


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
    inputt = []
    outputt = []
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

            elif len(match) < 0:
                print(" soory i did not uderstand that")
                continue

            elif match[0] in inputt:
                print("you already assined this before")
            elif match[1] in inputt:
                print("you already assined this before")
            
            elif match[0] in outputt:
                print("you already assined this before")
            elif match[1] in outputt:
                print("you already assined this before")
            else:
                inputt.append(match[0])
                outputt.append(match[1])
                break
    for k in range(0,31):
        inputt.append(outputt[k])
        outputt.append(inputt[k])


if y_n == "2":
    inputt  =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',"0","1","2","3","4","5","6","7","8","9"]
    outputt =  ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',"9","8","7","6","5","4","3","2","1","0"]

elif y_n == "1":
    print ("you did not configure a plug board we will proceed without a plug board")
    inputt  =  ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
    outputt =  ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]




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
    if any(c in inputt for c in message):
        break
        
    else:
        print("Your input contains values that are not suported please try agin")
        continue
result = ""




###################### create all rotors and give them set values ###############

firstrotor = rotor_dictionary[choose_the_first_rotor]
firstrotor.__set_rotor__(set_rotor_one)

secondrotor =rotor_dictionary[choose_the_second_rotor]
secondrotor.__set_rotor__(set_rotor_two)

thirdrotor = rotor_dictionary[choose_the_third_rotor]
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
