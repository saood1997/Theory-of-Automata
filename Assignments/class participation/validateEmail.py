import re

regex = '^([a-z]|[A-Z]|\.|\-|\d)+(@gmail(\.)com|@hotmail(\.)com|@live(\.)com|@yahoo(\.)com)$'

def check(email):
    if(re.search(regex,email)):  
        print("Valid Email")           
    else:
        print("Invalid Email")



check("saood.rahman7@gamil.com")
check("SAOOD.rahman7@mail.com")
check("saood.rahman7@gamil------com")
check("saood.rahman7@@gamil.com")
check("saood.rahman7@yahoo.com")
check("saood.@rahman7@live.com")
check("saood.rahman7hotmail.com")
check("saood-rahman7@live.com")
check("rahman/7@gamil.com")
check("saood-RAHMAN7@gamil//////com")
check("RAHMAN@hotmail......com")
