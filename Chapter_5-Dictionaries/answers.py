# Fantasy Game Inventory
import pprint
import copy

inventory = { 'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12 }

def displayInventory(listing):
  total = 0

  print('\nInventory: ')
  for k, v in listing.items():
    print(f'{v} {k}')
    total += v
  
  print(f'Total number of items: {total}')


displayInventory(inventory)




# List to Dictionary Function for Fantasy Game Inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(weapons, loot):
  # prevents the original inventory from being modified
  new_inventory = copy.copy(weapons)

  for item in loot:
    new_inventory.setdefault(item, 0)
    new_inventory[item] += 1
  
  return new_inventory


displayInventory(addToInventory(inventory, dragonLoot))