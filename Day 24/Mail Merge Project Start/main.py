#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
    
    
names_path = "Mail Merge Project Start/Input/Names/invited_names.txt"
letter_path = "Mail Merge Project Start/Input/Letters/starting_letter.txt"
output_path = "Mail Merge Project Start/Output/ReadyToSend"

with open(letter_path) as letter_file:
    letter_content = letter_file.read()
    
with open(names_path) as names_file:
    name_content = names_file.readlines()
    for name in name_content:
        name = name.strip()
        personal_letter = letter_content.replace("[name]", name)
        print(personal_letter)
        
        with open(f"C:\\Users\\bpete\\Code\\Day 24\\Mail Merge Project Start\\Output\\ReadyToSend\\letter for {name}.txt", mode="w") as complete_letter:
            complete_letter.write(personal_letter)
        
    