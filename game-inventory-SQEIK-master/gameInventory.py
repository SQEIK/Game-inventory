# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
#dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
import csv

# Displays the inventory.
def display_inventory(inventory,type_of_sort):
    max_len=len(max(inventory, key=len))+16
    s = max_len * '-'
    print(s)
    print('Your inventory:')
    print(s)
    print_table(inventory,type_of_sort)
    print(s)
    print(f'Total number of items: {sum(inventory.values())}')
    print(s)
    pass


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i]=inventory[i]+1
        else:
            inventory[i]=1
    return(inventory)


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order):
    sorted_by_value = {}
    if order == '':
        sorted_by_value = inventory.items()

    if order == 'Asc':
        a = False
        sorted_by_value = sorted(inventory.items(), key=lambda kv: kv[1], reverse=a)
    
    if order == 'Desc':
        a = True
        sorted_by_value = sorted(inventory.items(), key=lambda kv: kv[1], reverse=a)
    max_len=len(max(inventory, key=len))+5
    print('{:<{width}} {:<{width}}'.format('Counts','Item name',width=max_len))
    print((max_len +11) * '-')
    for k, v in sorted_by_value:
        print('{:<{width}} {:<{width}}'.format(v,k,width=max_len))
    pass



# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="test_inventory.csv"):
    with open('test_inventory.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            add_to_inventory(inventory,row)
    pass


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename):
    to_export=[]
    s=''
    with open(filename,'w') as csvfile:
        for i in inventory:
            for j in range(0,inventory[i]):
                to_export.append(i)
        s = ','.join(to_export)
        csvfile.write(s)
    pass


# Main function sets initial variables and stores rest of the functions
def main():
    inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inventory=add_to_inventory(inventory,dragon_loot)
    type_of_sort=input("Chose type to sort (Desc or Asc) or press enter to see inventory: ")
    import_inventory(inventory,'test_inventory.csv')
    display_inventory(inventory,type_of_sort)
    export_inventory(inventory,'test_inventory_export.csv')
    pass

main()