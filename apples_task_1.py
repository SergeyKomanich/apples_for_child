"""
n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
Сколько яблок достанется каждому школьнику?
Сколько яблок останется в корзинке?
Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).

Использовать только арифметические операторы (Подсказка: понадобятся // и %)
"""

schoolchild = int(input("Enter the number of children: "))
apples = int(input("Enter the number of apples: "))

apples_for_child = apples // schoolchild     # получаем количество яблок на школьника
leftover_apples = apples % schoolchild     # получаем остаток яблок

print("Every schoolchid gets:", apples_for_child, "apples")
print("Remains in the basket: ", leftover_apples, "apples")

