def getValid(pompt):
    while True:
        try:
            days = int(input(f'enter {pompt}  :'))
            return days
            break
        except ValueError:
            print('invalid value')
'''take input from user if user give then show welcome msg on screen  '''
def getname():
  name = input('enter your name :\n').strip().title()
  msg= f"Hello {name}. Welcome to our guide tour. "
  print(msg)
getname()
'''take input from user if user give mountain or beach then print well wishes'''
def getdestination():    
    destination = input('enter your destination :\n').strip().lower()
    if destination == "mountain":
        print('you can choose Mountain. enjoy ypu mountain trip')
    elif destination == "beach":
        print('you can choose Beach. enjoy you beach trip')
    else :
        print('please choose  between mountain or Beach')
getdestination()

'''in this we take a budget if the budget of the 
user is between 500 to 200 the print promt to user  your trip was great 
if budget comes under 200 to zero then print average 
if user budget more then 500 the print luxury '''
def getBuget():
    budget = getValid('budget')
    return budget
    if budget >= 500 :
        print("you trip was luxury")
    elif 200 >= budget and budget < 500 :
        print("you trip was good")
    elif 0 >= budget and budget < 200 :
        print("you trip was average")
    else:
        print("please enter your range between 0 to above")
bude = getBuget()
'''acording to budget one day -> user chosen buget like 
if you chosse 200 buget the its 2 days buget will multipy by day'''
def getDay(bud):
    day = getValid('days')
    if day > 0:
       totalbd = bud *day
       mas = f'your {day} day price is {totalbd}'
       print(mas)
getDay(bude)

 
