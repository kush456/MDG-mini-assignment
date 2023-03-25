#THIS THE FINAL CODE

#importing the required modules
import random
import string
import argparse
from PIL import Image


def pwd_generator(character_type,length_pwd,types_list):
    
    #taking user inputs on their preferences of character type, password length
    character_type = input("What types of characters would you like in the password? (lowercase, uppercase, digit, special)\n")
    length_pwd = int(input("Enter the length of the password: "))
    
    #converting the character_type string into a list for later use
    types_list = [t.strip() for t in character_type.split(',') if t.strip()]
    
    #many websites and apps require user to keep a minimum number of lowercase characters, digits etc
    #so here we give the user the option to keep a minimum number of characters of a certain type
    print("Minimum number of characters you would like for each type in order:", types_list)
    print("If no minimum please enter 0")
    
    #making a list of the minimum count of each character type
    mincount = []
    for type in types_list:
        a = int(input(f"Enter minimum number of {type} characters: "))
        mincount.append(a)
        
    #making sure the user does not exceed the length using the minimum number of characters
    if sum(mincount) > length_pwd:
        print("The number of minimum characters exceeds the total length of the password, please try again")
        return
    
    #using the two lists we made and turning them to a dictionary 
    types = dict(zip(types_list, mincount))
    password = ''
    pwd = ''
    
    #accessing the minimum count of each type via the dictionary and generating the required amount of characters
    if 'lowercase' in types_list:
        pwd += string.ascii_lowercase
        for i in range(types['lowercase']):
            password += random.choice(string.ascii_lowercase)
    if 'uppercase' in types_list:
        pwd += string.ascii_uppercase
        for i in range(types['uppercase']):
            password += random.choice(string.ascii_uppercase)
    if 'digit' in types_list:
        pwd += string.digits
        for i in range(types['digit']):
            password += random.choice(string.digits)
    if 'special' in types_list:
        pwd += string.punctuation
        for i in range(types['special']):
            password += random.choice(string.punctuation)
            
    #filling in the rest of the random characters and generating the password
    char_rem = length_pwd - sum(mincount)
    if char_rem < 0:
        print("The minimum number of characters exceeds the total length of the password, please try again")
        return
    for i in range(char_rem):
        password += random.choice(pwd)  
    if 'digit' not in types_list and len(types_list)== 3:
            image= Image.open('C:/Users/Kushu/Documents/DA.jpg')
            image.show()
    elif 'lowercase' not in types_list and len(types_list)== 3:
            image= Image.open('C:/Users/Kushu/Documents/LA.jpg')
            image.show()
    elif 'uppercase' not in types_list and len(types_list)== 3:
            image= Image.open('C:/Users/Kushu/Documents/UA.jpg')
            image.show()
    elif 'special' not in types_list and len(types_list)== 3:
            image= Image.open('C:/Users/Kushu/Documents/SA.jpg')
            image.show()
    elif 'uppercase' and 'special' in types_list and len(types_list)==2:
            image= Image.open('C:/Users/Kushu/Documents/USP.jpg')
            image.show()
    elif 'digit' and 'special' in types_list and len(types_list)==2:
            image= Image.open('C:/Users/Kushu/Documents/DSP.jpg')
            image.show()
    elif 'uppercase' and 'digit' in types_list and len(types_list)==2:
            image= Image.open('C:/Users/Kushu/Documents/UDP.jpg')
            image.show()
    elif 'lowercase' and 'special' in types_list and len(types_list)==2:
            image= Image.open('C:/Users/Kushu/Documents/LSP.jpg')
            image.show()
    elif 'uppercase' and 'lowercase' in types_list and len(types_list)==2:
            image= Image.open('C:/Users/Kushu/Documents/ULP.jpg')
            image.show()
    elif 'digit' and 'lowercase' in types_list and len(types_list)==2:
            image= Image.open('C:/Users/Kushu/Documents/LDP.jpg')
            image.show()
    elif len(types_list)==1:
            image= Image.open('C:/Users/Kushu/Documents/alone.jpg')
            image.show()
    else:
            image= Image.open('C:/Users/Kushu/Documents/all.jpg')
            image.show()
    return password


#adding and passing our arguments
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a random password.')
    parser.add_argument('--types', type=str, default='lowercase,uppercase,digit,special', help='Types of characters to include in the password.')
    parser.add_argument('--length', type=int, default=12, help='Length of the password.')
    parser.add_argument('--lowercase', type=int, default=1, help='Minimum number of lowercase characters.')
    parser.add_argument('--uppercase', type=int, default=1, help='Minimum number of uppercase characters.')
    parser.add_argument('--digit', type=int, default=1, help='Minimum number of digit characters.')
    parser.add_argument('--special', type=int, default=1, help='Minimum number of special characters.')
    args = parser.parse_args()
    
    #again splitting types string into a list
    types_list = [t.strip() for t in args.types.split(',') if t.strip()]
    
    #making the mincounts list
    mincounts = [args.lowercase, args.uppercase, args.digit, args.special]
    
    #storing the length of the password
    length_pwd = args.length
    
    #this is a precheck to avoid calling the function if the length exceeds
    if sum(mincounts) > length_pwd in types_list:
        print("The number of minimum characters exceeds the total length of the password, please try again")
    else:
        password = pwd_generator(types_list, length_pwd, mincounts)
        print("Generated Password:", password)
        
        
