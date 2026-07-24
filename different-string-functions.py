x = "batman"
#ends with fuction 
print(x.endswith("ana")) #false
print(x.endswith("man")) #true

#capitlaize function 
print(x.capitalize())
print(x.capitalize()) 

#replace function 

print(x.replace("bat", "cat")) #replaces bat with cat

#-------------------------------------------------------#

y = "i am studying python in my dungeon" 

#replace function 
print(y.replace("python", "javascript")) #replaces python with javascript
print(y.replace("dungeon", "castle")) #replaces dungweon with castle
print(y.replace("i", "batman")) #now im batman

#-------------------------------------------------------#

#find function 

z = "fear of being average" 

print(z.find("being")) #finds the index of being (basically the position of the first letter)
print(z.find("average")) #finds the index of average (basically the position of the first letter)

#-------------------------------------------------------#

#count function 

print(z.count("a")) #counts the number of 'a'
print(z.count("fear")) #also counts the full word 'fear'
print(z.count("batman")) #batman = zero times since it is not in the string


