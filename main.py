#"Zadanie 1"
shopping_dictionary ={
    "piekarnia" : ['chleb', 'pączek', 'bułki'],
    "warzywniak" : ['marchew', 'seler', 'rukola']
}
for shop, food in shopping_dictionary.items():
    print(f"Idę do {shop.title()}, kupuję tu następujące rzeczy: {food}")
shopping_cart = len(food)*2
print(f"W sumie kupuję {shopping_cart} produktów")


#Zadanie 2
lista = {x for x in range(5, 105, 5)}
lista_cubes = {x**3 for x in range(5, 105, 5)}
print(lista)
print(lista_cubes)

