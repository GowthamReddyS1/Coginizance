print("2D list of student's information")
s = [ [1, 'x', 0],
      [2, 'y', 0],
      [3, 'z', 0]]
for i in range(3):    
     for j in range(1):
        s[i][j+1]=str(input("Enter the {0}st Student Name  ".format( int(i+1) ) ) )
for i in range(3):    
     for j in range(1):
        s[i][j+2]=str(input("Enter the {0}st Student Marks  ".format( int(i+1) ) ) )          
print("{:<10} {:<10} {:<10}".format('Roll no','Name','Marks') )
for i in range(3):            
    print(s[0][i],end=" "*10)
print()
for i in range(3):            
    print(s[1][i],end=" "*10) 
print()
for i in range(3):            
    print(s[2][i],end=" "*10)     
print()
print("The second row from the data is " )
print( s[1][0] , s[1][1] , s[1][2] )