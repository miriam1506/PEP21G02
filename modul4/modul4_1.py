
shop1 = {'mere':10,'pere':15,'prune':6,'ananas':20}
shop2 = {'mere':11,'pere':15,'prune':6}
shop3 = {'mere':10,'pere':16,'prune':7,'papaya':25}

need_to_buy= {'mere':2,'pere':3,'prune':6}

def best_buy(shops: dict, cart: dict):
    for product, quanty in cart.items():
        print(product, quanty)

best_buy(shops=available_shops, cart=need_to_buy)

def best_buy(shops: dict, cart: dict):
        for product, quanty in cart.items():
            print(product, quanty)
best_buy(shops=available_shops, cart=need_to_buy)

