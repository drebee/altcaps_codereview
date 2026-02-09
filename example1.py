def alt_caps(original_string):
   new_string = ""
   letter_count = 0
   for char in original_string:
       if char.isalpha():
           if letter_count % 2 == 0:
               new_string += char.lower()
           else:
               new_string += char.upper()
           letter_count += 1
       else:
           new_string += char
   return new_string

print(alt_caps("Alternating Capitalization"))
