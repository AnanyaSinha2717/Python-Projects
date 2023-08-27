from Caesar_art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's' , 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k' , 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end=False
while end==False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    def caesar(text,shift,direction):
        t=''
        #shorter code         
        if direction=='decode':
            shift*=(-1)
        for i in list(text):
            if i not in alphabet:
                t+=i
            else:
                if shift not in range(alphabet.index(i),len(alphabet)):
                    shift=shift%26
                
                c=alphabet[alphabet.index(i)+shift]                
                t+=c
        print(f"the {direction}d text is {t}")
        
    caesar(text,shift,direction)
    
    ask=input("Do you want to try again? Y/N: ").lower()
    if ask=='y':
        end=False
    else:
        end=True

#longer code        
'''
        if direction=='encode':
            for i in list(text):
                if shift not in range(alphabet.index(i),len(alphabet)):
                    shift=shift%26
                e=alphabet[alphabet.index(i)+shift]
                t+=e
            print(f"The encoded text is '{t}'")
        elif direction=='decode':
            for i in list(text):
                if shift not in range(alphabet.index(i),len(alphabet)):
                    shift=shift%26
                d=alphabet[alphabet.index(i)-shift]
                t+=d
            print(f"The decoded text is '{t}'")
         '''   
 
