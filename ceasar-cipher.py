def caesar_encrypt(word, shift): 
    output = ""  
    for i in range(len(word)): 
        c = word[i] 
        output += chr((ord(c) + shift-65) % 26 + 65)  if (c.isupper()) else output += chr((ord(c) + shift - 97) % 26 + 97) 
    return output 
