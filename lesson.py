def menu(entree="beef", drink="beer", dessert="ice"):
    print(entree)
    print(drink)
    print(dessert)


# この記法だと順番間違えられない
# menu('beef', 'beer', 'ice')
# menu(entree='beef',  drink='ice', dessert='beer')

menu()
print("######")
menu(entree="chiken", drink='beer')
