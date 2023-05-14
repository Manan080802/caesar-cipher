from art import logo
from replit import clear
print(f"{logo} \n")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
  ciper_text=""
  for letter in text:
    
    postion = alphabet.index(letter)
  
    new_postion = postion+shift
    if(new_postion>25):
      new_postion=new_postion-26
      new_letter = alphabet[new_postion]
      ciper_text+=new_letter
    else:
      new_letter = alphabet[new_postion]
      ciper_text+=new_letter
      
  print(f"The encoded text is {ciper_text}")
def decrypt(text,shift):
  plan_text=""
  for letter in text:
    postion = alphabet.index(letter)
    new_postion = postion-shift
    if(new_postion<0):
      new_postion=new_postion+26
      new_letter = alphabet[new_postion]
      plan_text+=new_letter
    else:
      new_letter = alphabet[new_postion]
      plan_text+=new_letter
  print(f"The decoded text is {plan_text}")    
    
while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if(direction.lower()=="encode"):
    encrypt(text,shift)
    response =  input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if(response=="yes"):
      
      clear()
    else:
      print("goodby")
      break
  elif(direction.lower()=="decode"):
    decrypt(text,shift)
    response =  input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if(response=="yes"):
      clear()
    else:
      print("goodby")
      break
  else:
    print("It is not possible")
    break
    