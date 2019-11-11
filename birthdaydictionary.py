birthdays = {'Alice':'Apr 1','Bob':'Dec 12', 'Carol':'Mar 4'}

while True:
     print('Enter a name: (blank to quit)')
     name = input()

     if name=='':
             break
     elif name in birthdays:
             print(birthdays[name] + ' is the birthday of ' +name)
     else:
             print('I do not have birthdays information for '+name)
             print('What is their birthdays?')
             bday=input()
             birthdays[name]=bday #adds the name and birthday to the dictionary
             print('Birthday database updated.')
         
      

