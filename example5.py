def alt_caps(original_string, direction = 1):
   new_string = ""
   cap = direction
   for character in original_string:
       if cap == 1:
           new_character = character.upper()
           new_string = new_string + new_character
           cap = 0
       elif cap == 0:
           new_character = character.lower()
           new_string = new_string + new_character
           cap = 1
   print(new_string)

print(alt_caps("Alternating Capitalization"))