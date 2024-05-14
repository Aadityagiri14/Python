from art import logo
print(logo)

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def cc(text, shift, choice):
    output=""
    if choice=="decode":
        shift*=-1
    for i in text:
        if i in alphabet:
            ind=alphabet.index(i)+shift
            output+=alphabet[ind]
        else:
            output+=i
    print(f"The {choice}d message is: {output}")
    
Again="yes"
while Again=="yes":
    choice=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))%26
     
    cc(text,shift,choice)
    Again=input("\n\nType 'yes' to continue: ")
    
else:
    print("Caesar Cipher is over.")