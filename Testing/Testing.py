import os
print('Hello, ' + os.getlogin() + '! How are you?')

if True: 
   print ("True") 
else: 
   print ("False")

   word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
 made up of multiple lines and sentences."""

# writes the paragraph to the console
print (paragraph)

def readTempDirectory():
    for file in os.listdir("C:\\temp"):
        print(file)

readTempDirectory()

x = 5
y = 10
def sum():
 sum = x + y
 return sum
print(sum())

wert = 9
if wert < 5:
    print('Wert ist kleiner als 5')
elif wert == 5:
    print('Wert ist exakt 5')
else:
    print('Wert ist größer als 5')

print ("Good bye!")

print ("I don't know if It's working")

print ("I don't know if It's working")