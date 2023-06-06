def balance(x):
    stack=[]
    open=[]
    close=[]
    for i in range(0,len(x)):
        if(x[i]=='[' or x[i]=='{' or x[i]=='('):
            open.append(x[i])
        elif(x[i]==']' or x[i]=='}' or x[i]==')'):
            close.append(x[i])
    for j in range(0,True):
        if(open[j]=='[' and close[j]==']'):
            pass
        elif(open[j]=='(' and close[j]==')'):
            pass
        elif(open[j]=='{' and close[j]==')'):
            pass
        elif(open[j]=='{' and close[j]==')'):
            pass
        else:
                stack.append()
    if(len(stack==0)):
        print("balanced")
    else:
        print("unbalanced")

x=input("enter the expression")
balance(x)