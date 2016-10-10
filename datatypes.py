def data_type(n=None):#data function calls a parameter
  
  if type(n) == str:
    return len(n) #return the length of the varible if it is a string else no value
    
  elif n == None:
    return "no value"
    
  elif type(n) == bool:
    return n
    
  elif type(n) == int:
    if n < 100:
      return 'less than 100'
    elif n == 100:
      return "equal to 100"
    else:
      return 'more than 100'
      
  elif type(n) == list:
    if len(n) >= 3:
      return n[2]
    else:
    

  return None
https://github.com/alindikoray/mycode.git

https://github.com/alindikoray/mycode/blob/master/datatypes.py