string=str( input("Enter the string: ") )
evenplaces=""
for i in range(len(string)):
    if i%2==0:
        evenplaces= evenplaces+string[i]
print(evenplaces)
