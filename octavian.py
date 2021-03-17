allLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def openfile (fileName):
  file = open(fileName)
  return file.read()
def shiftLetters (shiftNumber):
    shiftedLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    i = 0
    while i < int(shiftNumber):
      shiftedLetters.append(shiftedLetters.pop(0))  
      i += 1
    return shiftedLetters
def encryptCypher (cypher,shiftedLetters):
  print(cypher)
  x=''
  for lett in cypher:
    if lett.isalpha() == True:
      lett = lett.lower()
      shiftplace = shiftedLetters[allLetters.index(lett)]
      x += shiftplace
    else:
      x += lett
  return x
print(encryptCypher(openfile(input('Name the file you want to encrypt: ')), shiftLetters(input('How much do you want this to be shifted by?: '))))