import string

print('Please type a letter: ')
l = str(input()).lower()

if l not in string.ascii_lowercase:
  print('Please try again; one letter only.')
elif len(l) == 0:
  print('Please try again; one letter necessary.')
else:
  n = ord(l) - 96
  
  val = 64
  val += 1
  ch = chr(val)
  print((n - 1) * ' ' + ch)
  
  for i in range(1, n):
    val += 1
    ch = chr(val)
    print((n - i - 1) * ' ' + ch + (2 * i - 1) * ' ' + ch)
  
  for i in reversed(range(1, n - 1)):
    val -= 1
    ch = chr(val)
    print((n - i - 1) * ' ' + ch + (2 * i - 1) * ' ' + ch)
  
  val = 65
  ch = chr(val)
  print((n - 1) * ' ' + ch)
