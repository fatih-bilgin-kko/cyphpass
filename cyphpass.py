import random
import numpy as np
class Base():
    alphabets={
            'EN': ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'ı', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '\\', "'"],
            'TR': ['A', 'a', 'B', 'b', 'C', 'c', 'Ç', 'ç', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'Ğ', 'ğ', 'H', 'h', 'I', 'ı', 'İ', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'Ö', 'ö', 'P', 'p', 'R', 'r', 'S', 's', 'Ş', 'ş', 'T', 't', 'U', 'u', 'Ü', 'ü', 'V', 'v', 'Y', 'y', 'Z', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '\\', "'"],
            'FR': ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'ı', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z','À', 'à', 'Â', 'â', 'Æ', 'æ', 'Ç', 'ç', 'É', 'é', 'Ê', 'ê', 'Ë', 'ë', 'Î', 'î', 'Ï', 'ï', 'Ô', 'ô', 'Œ', 'œ', 'Ù', 'ù', 'Û', 'û', 'Ü', 'ü', 'Ÿ', 'ÿ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '\\', "'"], 
            'DE': ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'ı', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', 'Ä', 'ä', 'Ö', 'ö', 'Ü', 'ü', 'ß', 'ß0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '\\', "'"],
            'ES': ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'ı', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'Ñ', 'ñ', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', 'Á', 'á', 'É', 'é', 'Í', 'í', 'Ó', 'ó', 'Ú', 'ú', 'Ü', 'ü', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '\\', "'"],
            'IT': ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'ı', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'Z', 'z', 'À', 'à', 'È', 'è', 'É', 'é', 'Ì', 'ì', 'Ò', 'ò', 'Ù', 'ù', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '\\', "'"],
            'PT': ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'ı', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y','Z', 'z', 'Á', 'á', 'Â', 'â', 'Ã', 'ã', 'Ç', 'ç', 'É', 'é', 'Ê', 'ê', 'Í', 'í', 'Ó', 'ó', 'Ô', 'ô', 'Õ', 'õ', 'Ú', 'ú', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '\\', "'"],
            'PL': ['A', 'a', 'Ą', 'ą', 'B', 'b', 'C', 'c', 'Ć', 'ć', 'D', 'd', 'E', 'e', 'Ę', 'ę', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'ı', 'J', 'j', 'K', 'k', 'L', 'l', 'Ł', 'ł', 'M', 'm', 'N', 'n', 'Ń', 'ń', 'O', 'o', 'Ó', 'ó', 'P', 'p', 'R', 'r', 'S', 's', 'Ś', 'ś', 'T', 't', 'U', 'u', 'W', 'w', 'Y', 'y', 'Z', 'z', 'Ź', 'ź', 'Ż', 'ż', 'ż0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '\\', "'"],
            'HU': ['A', 'a', 'Á', 'á', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'É', 'é', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'ı', 'Í', 'í', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'Ó', 'ó', 'Ö', 'ö', 'Ő', 'ő', 'P', 'p', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'Ú', 'ú', 'Ü', 'ü', 'Ű', 'ű', 'V', 'v', 'Z', 'z', 'ű0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '\\', "'"],
            'DA': ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'ı', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v','W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', 'Æ', 'æ', 'Ø', 'ø', 'Å', 'å0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '\\', "'"], 
            'NO': ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'ı', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', 'Æ', 'æ', 'Ø', 'ø', 'Å', 'å0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '\\', "'"],
            'SV': ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'ı', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', 'Å', 'å', 'Ä', 'ä', 'Ö', 'ö0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '\\', "'"], 
            'CS': ['A', 'a', 'Á', 'á', 'B', 'b', 'C', 'c', 'Č', 'č', 'D', 'd', 'Ď', 'ď', 'E', 'e', 'É', 'é', 'Ě', 'ě', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'ı', 'Í', 'í', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'Ň', 'ň', 'O', 'o', 'Ó', 'ó', 'P', 'p', 'R', 'r', 'Ř', 'ř', 'S', 's', 'Š', 'š', 'T', 't', 'Ť', 'ť', 'U', 'u', 'Ú', 'ú', 'Ů', 'ů', 'V', 'v', 'Y', 'y', 'Ý', 'ý', 'Z', 'z', 'Ž', 'ž', 'ž0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '\\', "'"],
            'ET': ['A', 'a', 'B', 'b', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'ı', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'R', 'r', 'S', 's', 'Š', 'š', 'T', 't', 'U', 'u', 'V', 'v', 'Z', 'z', 'Ž', 'ž', 'Õ', 'õ', 'Ä', 'ä', 'Ö', 'ö', 'Ü', 'ü', 'ž0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '\\', "'"],
            'LV': ['A', 'a', 'Ā', 'ā', 'B', 'b', 'C', 'c', 'Č', 'č', 'D', 'd', 'E', 'e', 'Ē', 'ē', 'F', 'f', 'G', 'g', 'Ģ', 'ģ', 'H', 'h', 'I', 'ı', 'Ī', 'ī', 'J', 'j', 'K', 'k', 'Ķ', 'ķ', 'L', 'l', 'Ļ', 'ļ', 'M', 'm', 'N', 'n', 'Ņ', 'ņ', 'O', 'o', 'P', 'p', 'R', 'r', 'S', 's', 'Š', 'š', 'T', 't', 'U', 'u', 'Ū', 'ū', 'V', 'v', 'Z', 'z', 'Ž', 'ž', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '\\', "'"]
            }
class Cypher(Base):
    """
    Don't forget save your keys and keywords for decyphering
    """  
    def __init__(self, message) -> None:
        self.message = message
    class ROTN:
        def __init__(self, parent):
            self.parent = parent  # Cypher sınıfı örneğine referans

        def ROTn(self, alp_code, n):
            alp = Base.alphabets[alp_code]
            cyp_mes = []
            for c in self.parent.message:
                if c in alp:
                    new_index = (alp.index(c) + 2 * n) % len(alp)
                    cyp_mes.append(alp[new_index])
                else:
                    cyp_mes.append(c)  
            return ''.join(cyp_mes)
        
        def rev_ROTn(self, alp_code, n): 
            return self.ROTn(alp_code, -1 * n)
        
        def custom_ROT(self, alp_code, equation):
            alp = Base.alphabets[alp_code]
            def calculate_rotation(x):
                if x in alp:
                    index = alp.index(x)
                    rotation = eval(equation, {"index": index})
                    return alp[rotation % len(alp)]
                else:
                    return x
            cyp_mes = list(map(calculate_rotation, self.parent.message))
            return ''.join(cyp_mes)
    def ceaser(self, alp_code):
        alp = Base.alphabets[alp_code]
        cyp_mes = [alp[len(alp) - 1 - alp.index(c)] if c in alp else c for c in self.message]
        return ''.join(cyp_mes)

    class Vigenere:
        def __init__(self, parent):
            self.parent = parent  # Cypher sınıfı örneğine referans
        
        def encrypt_vigenere(self, message, keyword, alp_code="EN"):
            cyp_mes = ""
            for i in range(len(message)):
                if message[i] in Base.alphabets[alp_code]:
                    shift = Base.alphabets[alp_code].index(keyword[i % len(keyword)])
                    cyp_mes += Base.alphabets[alp_code][(Base.alphabets[alp_code].index(message[i]) + shift) % len(Base.alphabets[alp_code])]
                else:
                    cyp_mes += message[i]
            return cyp_mes
        
        def decrypt_vigenere(self, message, keyword, alp_code="EN"):
            decyp_mes = ""
            for i in range(len(message)):
                if message[i] in Base.alphabets[alp_code]:
                    shift = Base.alphabets[alp_code].index(keyword[i % len(keyword)])
                    decyp_mes += Base.alphabets[alp_code][(Base.alphabets[alp_code].index(message[i]) - shift) % len(Base.alphabets[alp_code])]
                else:
                    decyp_mes += message[i]
            return decyp_mes
        
    class Morse:
        def ___init___(self,parent):
            self.parent = parent
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
        
    class HillCipher:
        def __init__(self, parent):
            self.parent = parent
            self.key_matrix = None

        def generate_key_matrix(self, size):
            """
            Verilen boyutta rastgele bir key matrisi oluşturur.
            Matrisi invertible (tersi alınabilir) olacak şekilde garanti etmeye çalışır.
            """
            while True:
                # Rastgele bir matris oluştur
                matrix = np.random.randint(0, 256, size=(size, size))
                if self.is_invertible(matrix):
                    self.key_matrix = matrix
                    return matrix

        def is_invertible(self, matrix):
            """
            Verilen matrisin tersinin alınabilir olup olmadığını kontrol eder.
            """
            det = int(round(np.linalg.det(matrix)))
            det_mod_inv = self.mod_inverse(det % 256, 256)
            return det_mod_inv is not None

        def mod_inverse(self, a, m):
            """
            a'nın mod m'deki tersini bulur.
            """
            for x in range(1, m):
                if (a * x) % m == 1:
                    return x
            return None

        def encrypt(self, plaintext):
            if self.key_matrix is None:
                raise ValueError("Anahtar matrisi oluşturulmadı.")
            
            # Metni bloklar halinde alıp şifreler
            block_size = self.key_matrix.shape[0]

            # Metni blok boyutuna tamamlayın
            while len(plaintext) % block_size != 0:
                plaintext += '\x00'  # Null karakteri dolgu olarak kullanılır

            # Şifreleme işlemi
            ciphertext = ""
            for i in range(0, len(plaintext), block_size):
                block = [ord(char) for char in plaintext[i:i + block_size]]
                encrypted_block = np.dot(self.key_matrix, block) % 256
                ciphertext += ''.join(chr(int(num)) for num in encrypted_block)
            
            return ciphertext

        def decrypt(self, ciphertext):
            if self.key_matrix is None:
                raise ValueError("Anahtar matrisi oluşturulmadı.")

            # Şifrelenmiş metni bloklar halinde çözer
            block_size = self.key_matrix.shape[0]

            # Anahtar matrisinin mod 256'da tersini al
            det = int(round(np.linalg.det(self.key_matrix)))
            det_inv = self.mod_inverse(det % 256, 256)
            adjugate = np.round(np.linalg.inv(self.key_matrix) * det).astype(int) % 256
            inverse_matrix = (det_inv * adjugate) % 256

            # Çözme işlemi
            plaintext = ""
            for i in range(0, len(ciphertext), block_size):
                block = [ord(char) for char in ciphertext[i:i + block_size]]
                decrypted_block = np.dot(inverse_matrix, block) % 256
                plaintext += ''.join(chr(int(num)) for num in decrypted_block)
            
            # Dolgu karakterleri (\x00) kaldır
            return plaintext.rstrip('\x00')
        
    def key_maker(self, alp_code="EN"):
        characters = Base.alphabets[alp_code]
        chars = Base.alphabets[alp_code][:]
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
    class File:
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

class Password(Base):
    def __init__(self,length,alp_code):
        self.length = length
        self.password = ""
        self.lower = list(filter(lambda x: x.islower, Base.alphabets[alp_code]))
        self.lower_upper = list(filter(lambda x: x.isalpha, Base.alphabets[alp_code]))
        self.alnum = list(filter(lambda x: x.isalnum, Base.alphabets[alp_code]))
        self.alnum_spesign = Base.alphabets[alp_code]

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


