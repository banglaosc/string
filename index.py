gali = "swor buka gada"

name = 'Goni'

first_letter = name[0].lower()

first_pos1 = gali.find(first_letter)

last_pos2 = gali.find(' ',first_pos1)
 
print(gali[first_pos1:last_pos2])

