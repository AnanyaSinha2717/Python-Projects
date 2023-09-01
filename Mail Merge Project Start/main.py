#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open('./Input/Names/invited_names.txt', 'r') as file1:
    names = file1.readlines()
    for i in range(len(names)):
        name = names[i].strip()
        names[i] = name

    with open('./Input/Letters/starting_letter.txt', 'r+') as file2:
        content = file2.read()
        for i in names:
            with open(f'./Output/ReadyToSend/letter_for_{i}', 'w') as final:
                letter = content.replace('[name]', i)
                final.write(letter)
                print(letter)