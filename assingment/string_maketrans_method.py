txt = "Theophilu Gyarbeng!"
mytable = txt.maketrans("1", "5")
print(txt.translate(mytable))


txt = "Theophilu Gyarbeng!"
mytable = txt.maketrans("y", "z")
print(txt.translate(mytable))



txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable)) 
