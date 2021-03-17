allLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']
def shiftLetters (shiftNumber):
    i=0
    shiftedLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']
    while i < int(shiftNumber):
      shiftedLetters.append(shiftedLetters.pop(0))  
      i=i+1
    return shiftedLetters
def encryptCypher (cypher,shiftedLetters):
  x=''
  for lett in cypher:
    place = allLetters.index(lett)
    shiftplace = shiftedLetters[place]
    x= x + shiftplace
  return x
print(encryptCypher(input('What message do you want to encypt?: '), shiftLetters(input('How much do you want this to be shifted by?: '))))