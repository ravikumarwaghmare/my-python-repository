"""Python Function practice"""


def full_name(fname,sname='No Surname'):
    print(fname + "  " + sname)
    

"""Positinal Arguments"""
full_name('Ajay','Dev')


""" Keyword Arguments"""
full_name(sname='Devagan',fname='Ajay')


""" Default value"""
full_name('Ajay')



"""Python Function practice"""


def full_name_return(fname,sname='No Surname'):
    fullname= "First Name is " + fname + " Surname Name is " + sname
    return fullname

""" Returns values"""

fname = full_name_return('Ajay','Dev')

print (fname) 



"""Python Function practice"""


def full_name_return_dict(fname,sname='No Surname'):
    fullname_dict= {'fname': fname, 'sname': sname}
    return fullname_dict

""" Returns values"""

fname = full_name_return_dict('Ajay','Dev')

print (fname) 


""" Passing list to Functions"""
def fname_list(fname):
    for name in fname:
        print("Hello "+name)
    
    
users=['Ajay','Salman','Vivek']
    
fname_list(users)



""" Passing an Arbitrary number of Arguments"""

"""When you do not know number of aruments passed 
to function"""

""" Collecting and arbitrary number of arguments"""


def make_pizza(size,*toppings):
    print("Making a "+ size + "Pizza")
    
    print("Toppings: ")
    
    for topping in toppings:
        print("- "+ topping)
        

make_pizza('Large','Onion','Black Olive', "Cottage cheese")
"""
Making a LargePizza
Toppings: 
- Onion
- Black Olive
- Cottage cheese
"""




""" Collecting an Arbitrary number of Keyword Arguments """

def build_profile(first, last, **user_info):
    profile = {'first': first, 'last': last}
    
    for key,value in user_info.items():
        profile[key] = value
        
    return profile
    
user0 = build_profile('Ajay', 'Devagan', location='Mumbai', field='Bllywood')


print(user0)
"""{'first': 'Ajay', 'last': 'Devagan', 'location': 'Mumbai', 'field': 'Bllywood'}"""












