# def Caesar_cipher_endpoint(list:str):
d=["dani"]
x=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in d:
    z=((x.index(i))+2) % len(x)
    x=x[z]
    print(x) 
for i in d:
   
    print(d[z])
    



    