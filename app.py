#Tupla-Armazernar informações fixas
product = ("Mesa", "Móvel", 50)
print (f"seu item é uma {product[0]} que se classifica como um {product[1]} do valor de {product[2]:.2f} reais.")

#Listas com duplicatas
food = ["pizza", "pizza", "bolo", "salgados"]
print ("Lisa com duplicatas:", food )

#Conjunto:Romover duplicatas
food_list = set(food)
print ("Lista sem duplicatas usando conjunto:", food_list)

#Reverso conjunto -> lista
foods = list(food_list)
print (foods)



