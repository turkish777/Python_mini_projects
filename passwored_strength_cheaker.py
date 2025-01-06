import re 

def passwored_strengtha_cheaker(passwored):
    stringth = 0 
    
    if len(passwored) >= 8:
        stringth += 1
    if re.search('[a-z]' , passwored):
        stringth += 1
    if re.search('[A-Z]' , passwored):
        stringth += 1
    if re.search('[0-9]' , passwored):
        stringth += 1
    if re.search('[!@#$%^&*()]' , passwored):
        stringth += 1
        
    return stringth


def main():
    passwored = input("Enter u passwored: ")
    strength = passwored_strengtha_cheaker(passwored)
    
    if strength == 5:
        print("very Strong passwored")
    elif strength == 4:
        print("strong passwored")
    elif strength == 3:
        print("Medium passwored! ")
    elif strength == 2:
        print("weak passwored! ")
    else:
        print("Very weak! passwored ")
        
        
        
if __name__ == "__main__":
    main()
        

