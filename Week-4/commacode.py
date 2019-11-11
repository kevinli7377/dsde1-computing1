spam = ['apples','bananas','tofu','cats']

def comma(somelist): 
    for i in range(len(somelist)-1): #indexes from 0 to 3. Len is 4. Up to 3. Does not include 3.
        print(somelist[i]+',')
    print('and '+somelist[i+1])



if __name__=='_main_':
    main()

def main():
    comma(spam)

main()