
beatles = []
print("Step 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for i in range(2):
    üye = input("Lütfen eklenecek üyeyi girin (Stu Sutcliffe / Pete Best): ")
    beatles.append(üye)
print("Step 3:", beatles)

del beatles[-2:] 
print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

print("The Fab", len(beatles))
