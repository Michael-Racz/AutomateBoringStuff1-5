# 05/23/2020 Racz
# ABSWP CH5
# Fantasy Game inventory
#
#

#keys are string values describing the item, 
#value is the integer saying how many of that item the player has
#write a displayInventory() that would take any possible inventory,display

stuff = {'rope':1,'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory')
    item_total = 0
    for  i ,v in inventory.items():
        #this is where the code goes
        print(str(v) + ' ' + str(i))
        item_total += v
    print('Total number of items: ' +str(item_total))
    print()
#Taking this out to expand on the program
#displayInventory(stuff)

def addToInventory(inventory, addedItems):    
    #Parse the new items and check if they are already in inventory
    for newLoot in addedItems:
        #if the items are in the inventory
        if newLoot in inventory.keys():
            inventory[newLoot] += 1
        #not in inventory yet
        else:
            inventory.setdefault(newLoot, 1)
    return inventory
   
#Project 2: Getting loot into the inventory
inv = {'gold coin': 42,'rope':1}
displayInventory(inv)
dragonLoot = ['Firm Handshake', 'dagger', 'gold coin', 'ruby']
inv = addToInventory(inv,dragonLoot)
displayInventory(inv)