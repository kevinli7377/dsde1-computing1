def displayInventory(inv1):
    print('Inventory')
    Item_total=0
    for k,v in actualinv.items(): #.items() prints both keys and values)
        print(str(v)+ ' ' + k)
        Item_total += v
    print('Total items:'+str(Item_total))

dragonLoot=['gold coin', 'dagger','gold coin','gold coin','ruby']

def addToInventory(inventoryv,addeditems):
    for loot in dragonLoot:
         if loot not in actualinv:
            actualinv[loot]=1
         else:
             actualinv[loot] += 1


actualinv ={'gold coin':42,'rope':1}
dragonLoot= ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(actualinv,dragonLoot)
displayInventory(actualinv)
