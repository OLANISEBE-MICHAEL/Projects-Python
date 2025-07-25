# reading the list of people
with open("Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as invited_people:
    # readlines() reads each line of the txt file and returns a list of it with \n for eacb items
    contents = invited_people.readlines()


# reading a prototype of the letter i wish to send to each of my friend
with open("Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt") as start_letter:
    letter = start_letter.read()
    for content in contents :
        # we are using the strip() method to remove all excess whitespaces or in my case new lines
        stripped_name = content.strip()
        file_path = f"Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/letter_to_{stripped_name}.txt"
        with open(file_path, mode= "w") as final:
            new_letter = letter.replace("[name]", stripped_name)
            final.write(new_letter)







