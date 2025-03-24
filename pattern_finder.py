'''
define text
define pattern
if the entire text hasn't been searched:
  iterate to the next character of the text
  create match_count and set it to 0
  if the entire pattern hasn't been searched:
    if this character from the pattern is equal to the character from text:
      increment match_cout
  if match_count == length of pattern:
    pattern found! 
'''

text = input('text: ')
pattern = input('pattern: ')

text_low = text.lower()
pattern_low = pattern.lower()

for index in range(len(text_low) - len(pattern_low) + 1):
    if text_low[index:index + len(pattern_low)] == pattern_low:
      print(f'The pattern value of "{pattern}" can be found in text value of "{text}".')
      break
else:
   print(f'The pattern value of "{pattern}" can not be found in text value of "{text}".')

