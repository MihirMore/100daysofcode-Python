#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

with open(".//Input//Names//invited_names.txt") as invited:
    names = invited.readlines()
invited_list = []
for item in names:
    invited_list.append(item.strip())


for name in invited_list:
    with open(".//Input//Letters//starting_letter.txt") as draft:
        content = draft.read()        
    new_draft = content.replace("[name]",f"{name}")      
    
    with open(f".//Output//ReadyToSend//{name}.txt", "w") as invite:
        invite.write(new_draft)

print("Your invitations are ready!") 