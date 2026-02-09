def alt_caps(original_string):
   new_string = ""
   capitalized_fact = original_string.upper()
   notcapital = original_string.lower()
   for i in range(len(original_string)):
       if i % 2 == 0:
           new_string += capitalized_fact[i]
       else:
           new_string += notcapital[i]
   return new_string

print(alt_caps("Alternating Capitalization"))