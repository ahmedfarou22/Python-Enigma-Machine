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

def __iput_output__(number_or_letter): # to make the program easier all the rotars take in a number and output a number this function turns letters to numbers and numbers to letters
    value = 0
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
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
  "I"   : rotor(["e","k","m","f","l","g","d","q","v","z","n","t","o","w","y","h","x","u","s","p","a","i","b","r","c","j"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],"q"),
  "II"  : rotor(["a","j","d","k","s","i","r","u","x","b","l","h","w","t","m","c","q","g","z","n","p","y","f","v","o","e"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],"e"),
  "III" : rotor(["b","d","f","h","j","l","c","p","r","t","x","v","z","n","y","e","i","w","g","a","k","m","u","s","q","o"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],"v"),
  "IV"  : rotor(["o","p","q","r","x","w","v","y","u","t","a","b","z","c","d","h","s","i","j","k","l","e","g","m","n","f"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],"u"),
  "V"   : rotor(["i","k","z","w","v","u","j","t","s","r","q","l","m","n","c","d","o","p","e","f","y","x","g","h","b","a"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],"b")
}



# ==========================================================  program Starts Here =============================================================================

###################### configure the plug board ###############
print("configure the plug board")
y_n = input("press y to contiune and n to exit the plug board configration ")

if y_n == "y":
    inputt = []
    outputt = []
    for i in range(0,13):
        match = input("match 2 letters together Example <AB>: ") 
        inputt.append(match[0])
        outputt.append(match[1])
    for k in range(0,13):
        inputt.append(outputt[k])
        outputt.append(inputt[k])

elif y_n == "n":
    print ("you did not configure a plug board we will proceed without a plug board")
    inputt  =  ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    outputt =  ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

else:
    print("you did not press y or n restart the program")


###################### choose the 3 rotors ###############
choose_the_first_rotor  = input("first position: choose a  rotor from the one of the five > I, II, III, IV, V : ")
choose_the_second_rotor = input("second position: choose a  rotor from the one of the five > I, II, III, IV, V : ")
choose_the_third_rotor  = input("third position: choose a  rotor from the one of the five > I, II, III, IV, V : ")

###################### set values to the 3 rotors ###############
set_rotor_one    = int(input("what number do you want to set rotor 1 to ? "))
set_rotor_two    = int(input("what number do you want to set rotor 2 to ? "))
set_rotor_three  = int(input("what number do you want to set rotor 3 to ? "))


message = input("what is the message you want to encript/decript ")
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

# I I I --- 987 --- aaaa  ---->pjon

# y V V IV 6,4,9 --- 200 hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# --> cfmbjvfwaazytmdletwbwtamjcfmbjvfwaazytmdletwbwtamjcfmbjvfwaazytmdletwbwtamjcfmbjvfwaazytmdletwbwtamjcfmbjvfwaazytmdletwbwtamjcfmbjvfwaazytmdletwbwtamjcfmbjvfwaazytmdletwbwtamjcfmbjvfwaazytmdletwbwtamj
