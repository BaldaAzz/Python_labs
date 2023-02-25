file=open("labs 10/10_5/input.txt", 'r')
output=open("labs 10/10_5/output.txt",'w')

for i in open ( "input.txt" ): 
   age = int (i.split()[1]) 
   if age < 40: 
      output.write (i)
      
file.close
output.close
