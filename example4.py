def alt_caps(original_string):
   new_string = ""
   for i, character in enumerate(original_string):
       if i % 2 == 0:
           new_string += character.lower()
       else:
           new_string += character.upper()
   return new_string

print(alt_caps("Alternating Capitalization"))