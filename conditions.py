# CONDITIONS

x=4

# IF
if x<6: # replaced if(){}
    print("Yes") # indent 2/4 spaces
    
# ELSE
if x<3:
    print("Yes")
else:
    print("No")
    
# ELIF
color = "yellow"
if color=="red":
    print("red")
elif color=="pink":
    print("pink")
else:
    print("none")
    
# NESTED IF
if x==4:
    if color=="yellow":
        print("both true")
        
# LOGGICAL OPERATORS
if x==4 and color=="yellow":
    print("both true")