import random
class Cypher(): 
    """
    Don't forget save your keys and keywords for decyphering
    """  
    def __init__(self,message) -> None:
        self.message = message
        self.alphabets = {
            "EN": ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', 
                         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                         '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
                         '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':','\\','\''],
            "TR": ['A', 'a', 'B', 'b', 'C', 'c', 'Ç', 'ç', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'Ğ', 'ğ', 'H', 'h', 'İ', 'i', 'I', 'ı', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'Ö', 'ö', 'P', 'p', 'R', 'r', 'S', 's', 'Ş', 'ş', 'T', 't', 'U', 'u', 'Ü', 'ü', 'V', 'v', 'Y', 'y', 'Z', 'z', 
                         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                         '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
                         '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':','\\','\'']
        }
    def ROTn(self, alp_code, n):
        alp = self.alphabets[alp_code]
        cyp_mes = []
        for c in self.message:
            if c in alp:
                new_index = (alp.index(c) + 2 * n) % len(alp)
                cyp_mes.append(alp[new_index])
            else:
                cyp_mes.append(c)  
        return ''.join(cyp_mes)
    def rev_ROTn(self, alp_code, n):
            alp = self.alphabets[alp_code]
            cyp_mes = []
            for c in self.message:
                if c in alp:
                    new_index = (alp.index(c) - 2 * n) % len(alp)
                    cyp_mes.append(alp[new_index])
                else:
                    cyp_mes.append(c)  
            return ''.join(cyp_mes)
    def custom_ROT(self, alp_code, equation):
        alp = self.alphabets[alp_code]
        
        def calculate_rotation(x):
            if x in alp:
                index = alp.index(x)
                rotation = eval(equation,{"index": index})
                return alp[rotation % len(alp)]
            else:
                return x

        cyp_mes = list(map(calculate_rotation, self.message))
        return ''.join(cyp_mes)
    def ceaser(self, alp_code):
        alp = self.alphabets[alp_code]
        cyp_mes = [alp[len(alp) - 1 - alp.index(c)] if c in alp else c for c in self.message]
        return ''.join(cyp_mes)

    def encrypt_vigenere(self,message,keyword,alp_code="EN"):
        cyp_mes=""
        for i in range(len(message)):
            if message[i] in self.alphabets[alp_code]:
                cyp_mes+=self.alphabets[alp_code][self.alphabets[alp_code].index(message[i])+self.alphabets[alp_code].index(keyword[i%len(keyword)])%len(self.alphabets[alp_code])]
        return cyp_mes
    def decrypt_vigenere(self,message,keyword,alp_code="EN"):
        decyp_mes=""
        for i in range(len(message)):
            if message[i] in self.alphabets[alp_code]:
                decyp_mes+=self.alphabets[alp_code][self.alphabets[alp_code].index(message[i])-self.alphabets[alp_code].index(keyword[i%len(keyword)])%len(self.alphabets[alp_code])]
        return decyp_mes
    def BitToMorse(self, morse):
        cypmes = []
        while len(morse) != 0:
            if morse[:1] == "_":
                cypmes.append("11")
            elif morse[:1] == ".":
                cypmes.append(random.choice(["01", "10"]))
            else:
                cypmes.append("00")
            morse = morse[1:] 
        return "".join(cypmes)

    def MorseToBit(self,morse):
        decypmes=[]
        while len(morse)!=0:
            if morse=="_":
                decypmes.append("11")
            elif morse==".":
                decypmes.append(random.choice(["01","10"]))
            else:
                decypmes.append("00") 
            morse=morse[1:]
        return "".join(decypmes)
    def morseToString(self,morse):
        mes=""
        morsecode=morse.split()
        morsedict={".-": "A","-...": "B","-.-.": "C","-..": "D",".": "E","..-.": "F","--.": "G","....": "H","..": "I",".---": "J","-.-": "K",".-..": "L","--": "M","-.": "N","---": "O",".--.": "P","--.-": "Q",".-.": "R","...": "S","-": "T","..-": "U","...-": "V",".--": "W","-..-": "X","-.--": "Y","--..": "Z","-----": "0",".----": "1","..---": "2","...--": "3","....-": "4",".....": "5","-....": "6","--...": "7","---..": "8","----.": "9",".-.-.-": ".","--..--": ",","..--..": "?","/":" ","-.-.--":"!"}
        for i in morsecode:
            mes+=morsedict[i]
        return mes
    def stringToMorse(self,string):
        cypmes=""
        morsedict={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",".":".-.-.-",",":"--..--","?":"..--.."," ":"/","!":"-.-.--"}
        for i in string:
            cypmes+=morsedict[i.upper()]+" "
        return cypmes
    def key_maker(self, alp_code="EN"):
        characters = self.alphabets[alp_code]
        chars = self.alphabets[alp_code][:]
        random.shuffle(chars)  
        cyp_dict = {}
        for i in range(len(characters)):
            cyp_dict[characters[i]] = chars[i]
        
        return cyp_dict

    def decypher(self,key):
        decyp_mes=""
        for i in [c for c in self.message]:
            try:
                decyp_mes+=key[i]
            except KeyError:
                decyp_mes+=i
        return decyp_mes
    def cypher(self,key):
        cyp_mes=""
        for i in [c for c in self.message]:
            try:
                cyp_mes+=key[i]
            except KeyError:
                cyp_mes+=i
        return cyp_mes
    @staticmethod
    def file_cypher(file_path, key):
        with open(file_path, "r+") as file:
            message = file.read()
            cyp_mes = Cypher(message).cypher(key)
            file.seek(0)
            file.write(cyp_mes)
            file.truncate()

    @staticmethod
    def file_decypher(file_path, key):
        with open(file_path, "r+") as file:
            message = file.read()
            decyp_mes = Cypher(message).decypher(key)
            file.seek(0)
            file.write(decyp_mes)
            file.truncate()

class Password:
    def __init__(self,length,alp_code):
        self.length = length
        self.alphabets = {
            "EN": ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', 
                         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                         '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
                         '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', '\''],
            "TR": ['A', 'a', 'B', 'b', 'C', 'c', 'Ç', 'ç', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'Ğ', 'ğ', 'H', 'h', 'İ ', 'i', 'I', 'ı', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'Ö', 'ö', 'P', 'p', 'R', 'r', 'S', 's', 'Ş', 'ş', 'T', 't', 'U', 'u', 'Ü', 'ü', 'V', 'v', 'Y', 'y', 'Z', 'z', 
                         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                         '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
                         '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', '\'']
        }
        self.password = ""
        self.lower = list(filter(lambda x: x.islower, self.alphabets[alp_code]))
        self.lower_upper = list(filter(lambda x: x.isalpha, self.alphabets[alp_code]))
        self.alnum = list(filter(lambda x: x.isalnum, self.alphabets[alp_code]))
        self.alnum_spesign = self.alphabets[alp_code]

    def PIN(self):
        self.password = ""
        for i in range(self.length):
            self.password += str(random.randint(0, 9))
        return self.password

    def Textbased(self, mode=1):
        self.password=""
        if mode == 1:
            for i in range(self.length):
                self.password += random.choice(self.lower)
        elif mode == 2:
            for i in range(self.length):
                self.password += random.choice(self.lower_upper)
        elif mode == 3:
            for i in range(self.length):
                self.password += random.choice(self.alnum)
        elif mode == 4:
            for i in range(self.length):
                self.password += random.choice(self.alnum_spesign)
        return self.password


