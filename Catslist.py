catnames= []
while True:
         print('Enter the name of cat '+str(len(catnames)+1 + ' (Or enter nothing to stop.):')
         catnames = input()
     if name == ''
          break
     catnames= catnames + [name] #list concatentations
print('The cat names are:')
for name in catnames:
     print (''+ name)
     