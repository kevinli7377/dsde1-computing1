stuff= {'rope':1,'torch':6,'gold coins':42, 'phones':53,'medicine':34}

def displayInventory(inv):
    print('Inventory')
    Item_total=0
    for k,v in inv.items(): #.items(0 prints both keys and values)
        print(str(v)+ ' ' + k)
        Item_total += v
    print('Total items:'+str(Item_total))

displayInventory(stuff)