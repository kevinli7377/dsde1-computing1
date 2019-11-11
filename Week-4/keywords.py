'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
def welcome_message(in1='user_name', in2='place'):

    #nostring returned
     if in1=='user_name' and in2=='place':
         #return 'Hello and welcome!'
    
    #keyword argument
     elif in1=='user_name':
         return 'Hello,' + in1 + 'and welcome'

    #place provided
     elif in1=='place' or in2=='place':
         return 'Hello and welcome to' + in2

    #username and place provided
     elif in1=='user_name' and in2=='place':
         return 'Hello,' + in1 + 'and welcome to' + in2


  


    #while True:
        #message=input()
        #if message in ():
            #return 'Hello and welcome!'
    
    #elif message in ('user_name',):
         #return 'Hello,' + in1 + 'and welcome'

     #elif message in (in2,) or (,in2):
         #return 'Hello and welcome to' + in2

    # elif message in (in1,in2)
         #return 'Hello,' + in1 + 'and welcome to' + in2

# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>

def list_average(listofno,avg_type= 'mean'):
     #from statistics import mode
     #from statistics import mean
     
     #if avg_type=mean
          #return mean(listofno)

     if (listofno, avg_type='mean'):
         return (sum(listofno)/len(listofno))

     elif (listofno, avg_type='median'):
        
         orderedlist= listofno.sort()
         if len(num_list) % 2 == 0:
             first_median= listofno[len(listofno)//2]
             second_median= listofno [len(listofno)//2-1]
             final_median= (first_median + second_median) / 2
             return final_median
         else:
             final_median= listofno[len(listofno)//2 + 0.5]
             return final_median

     elif (listofno, avg_type='mode'):
          import collections
          data= collections.Counter(listofno) #creates list of freq.
          data1= dict(data)
          print(data1)
          max_value = max(list(data.values()))
          mode_val = [num for num, freq in data1.items() if freq ==max]

          if len(mode_val) == len(num_list):
             print ('No mode in the list')
            
          else:
              print('The mode of the list is: ' + ','.join(map(str,modal_val))) #join cobmines all terms in a list together with the var specified in front'
#Map collects the inputs and puts them into individual lists

if __name__ == '_main_':
     list_average([1,4,7,3,7,4,9,8,12,21],'median')


    


# Create a function called list_average()
# without using any libraries to do the maths for you 
# (the point of this exercise is to practice interacting 
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list