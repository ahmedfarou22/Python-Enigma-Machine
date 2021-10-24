class rotor: # a data type that represents a rotor it takes in a number and outputs a number
    def __init__(self,rotor_in,rotor_out,rotor_notch):
        self.rotor_in =  rotor_in
        self.rotor_out = rotor_out
        self.rotor_notch = rotor_notch
    
    def __auto_rotate___(self):
        self.rotor_in = self.rotor_in[1:] + self.rotor_in[:1]
        self.rotor_out = self.rotor_out[1:] + self.rotor_out[:1]
    

    def __rotate_next__(self):
        if self.rotor_out[0] == self.rotor_notch:  
            return 1
        else:
            return 0
    
    def __set_rotor__(self,setn):
        self.rotor_in = self.rotor_in[setn:] + self.rotor_in[:setn]
        self.rotor_out = self.rotor_out[setn:] + self.rotor_out[:setn]

    
    def __work_rotor__(self,number,rotatenext):
        if rotatenext == 1:
            self.rotor_in = self.rotor_in[1:] + self.rotor_in[:1]
            self.rotor_out = self.rotor_out[1:] + self.rotor_out[:1]
        
        value = 0  # will store the value of the iput 
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


def __plug_board__(letter):
    inputt  =  []
    outputt =  []
    print("configure the plug board")
    for i in range(0,13):
        match = input("match 2 letters together Example <AB>: ")
        inputt.append(match[0])
        outputt.append(match[1])
    
    for k in range(0,13):
        inputt.append(outputt[k])
        outputt.append(inputt[k])
    
    for i in range(len(inputt)):
        if letter == inputt[i]:
            return outputt[i]





# a = __iput_output__("o") ### input letter and conver to number s is working


# ###################### rotor 1 settings ###############
# firstrotor = rotor(["e","k","m","f","l","g","d","q","v","z","n","t","o","w","y","h","x","u","s","p","a","i","b","r","c","j"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],"q")
# firstrotor.__set_rotor__(15)
# firstrotor.__auto_rotate___()
# b = firstrotor.__work_rotor__(a,0)
# r1 = firstrotor.__rotate_next__()

# ###################### rotor 2 settings ###############
# secondrotor =rotor(["a","j","d","k","s","i","r","u","x","b","l","h","w","t","m","c","q","g","z","n","p","y","f","v","o","e"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],"e")
# secondrotor.__set_rotor__(0)
# c = secondrotor.__work_rotor__(b,r1)
# r2 = secondrotor.__rotate_next__()


# ###################### rotor 3 settings ###############
# thirdrotor = rotor(["b","d","f","h","j","l","c","p","r","t","x","v","z","n","y","e","i","w","g","a","k","m","u","s","q","o"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],"#")
# thirdrotor.__set_rotor__(0)
# d = thirdrotor.__work_rotor__(c,r2)


# ###################### refelctor ###############
# e = __Man_reflector__(d)


# ###################### rotor 4 settings ###############
# forthrotor = rotor(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],["b","d","f","h","j","l","c","p","r","t","x","v","z","n","y","e","i","w","g","a","k","m","u","s","q","o"],"#")
# forthrotor.__set_rotor__(0)
# f = forthrotor.__work_rotor__(e,r2)


# ###################### rotor 5 settings ###############
# fifthrotor =rotor(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],["a","j","d","k","s","i","r","u","x","b","l","h","w","t","m","c","q","g","z","n","p","y","f","v","o","e"],"#")
# fifthrotor.__set_rotor__(0)
# g = fifthrotor.__work_rotor__(f,r1)


# ###################### rotor 6 settings ###############
# sixthroto = rotor(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],["e","k","m","f","l","g","d","q","v","z","n","t","o","w","y","h","x","u","s","p","a","i","b","r","c","j"],"#")
# sixthroto.__set_rotor__(15)
# sixthroto.__auto_rotate___()
# h = sixthroto.__work_rotor__(g,0)

# i = __iput_output__(h)


# # print(a)
# # print(b)
# # print(c)
# # print(d)
# # print(e)
# # print(f)
# # print(g)
# # print(h)
# print(i)