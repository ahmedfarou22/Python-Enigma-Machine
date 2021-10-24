class rotor: # a data type that represents a rotor it takes in a number and outputs a number
    def __init__(self,rotor_in,rotor_out,rotor_notch):
        self.rotor_in =  rotor_in
        self.rotor_out = rotor_out
        self.rotor_notch = rotor_notch
    
    def __auto_rotate___(self):
        self.rotor_in = self.rotor_in[1:] + self.rotor_in[:1]
        self.rotor_out = self.rotor_out[1:] + self.rotor_out[:1]
    

    def __work_rotor__(self,number):
        value_b = 0  ## declaring a few varibles value_b will store the value of the input before any shifts
        value = 0  # will store the value of the iput after rotations
        
        # value_b = self.rotor_in[number]  ## this part of the work rotor cheaks the value inputed to the rotor notch and if they are the same it will rotate the rotor 
        # if value_b == self.rotor_notch:
        #     print("the number value is " + value_b + " the rotor notch is " + self.rotor_notch + " there for i the program will rotate the rotor befor working it")
        #     self.rotor_in = self.rotor_in[1:] + self.rotor_in[:1]
        #     self.rotor_out = self.rotor_out[1:] + self.rotor_out[:1]
        
        value = self.rotor_in[number]     ### work the rotor (easy)
        for i in range(len(self.rotor_out)):
            if self.rotor_out[i] == value:
                return i
        


def __Man_reflector__(number): ## a refector with hardcoded values

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

def __iput_output__(number_or_letter):
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




# # a = __iput_output__("s") ### input letter and conver to number

# firstrotor = rotor(["e","k","m","f","l","g","d","q","v","z","n","t","o","w","y","h","x","u","s","p","a","i","b","r","c","j"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],"p")

# firstrotor.__auto_rotate___()
# b = firstrotor.__work_rotor__(8)

# print(b)







message = input("what is the message you want to encript ")
result = ""
for letter in message:
    a = __iput_output__(letter) ### input letter and conver to number s is working
    firstrotor = rotor(["e","k","m","f","l","g","d","q","v","z","n","t","o","w","y","h","x","u","s","p","a","i","b","r","c","j"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],"p")
    firstrotor.__auto_rotate___()
    b = firstrotor.__work_rotor__(a)
    secondrotor =rotor(["a","j","d","k","s","i","r","u","x","b","l","h","w","t","m","c","q","g","z","n","p","y","f","v","o","e"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],"y")
    c = secondrotor.__work_rotor__(b)
    thirdrotor = rotor(["b","d","f","h","j","l","c","p","r","t","x","v","z","n","y","e","i","w","g","a","k","m","u","s","q","o"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],"w")
    d = thirdrotor.__work_rotor__(c)
    e = __Man_reflector__(d)
    forthrotor = rotor(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],["b","d","f","h","j","l","c","p","r","t","x","v","z","n","y","e","i","w","g","a","k","m","u","s","q","o"],"z")
    f = forthrotor.__work_rotor__(e)
    fifthrotor =rotor(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],["a","j","d","k","s","i","r","u","x","b","l","h","w","t","m","c","q","g","z","n","p","y","f","v","o","e"],"e")
    g = fifthrotor.__work_rotor__(f)
    sixthroto = rotor(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],["e","k","m","f","l","g","d","q","v","z","n","t","o","w","y","h","x","u","s","p","a","i","b","r","c","j"],"u")
    sixthroto.__auto_rotate___()
    h = sixthroto.__work_rotor__(g)
    i = __iput_output__(h)
    result = result + i
print(result)

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h)
# print(i)