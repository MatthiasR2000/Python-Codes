import numpy as nppip

# 1. LISTEN (LISTS)
# Listen sind die grundlegenden Datenstrukturen in Python.
my_list = [1, 2, 3, 4, 5]
print("Liste:", my_list)

# Zugriff auf Elemente
print("Erstes Element:", my_list[0])

# Hinzufügen von Elementen
my_list.append(6)
print("Liste nach Hinzufügen:", my_list)

# Entfernen von Elementen
my_list.remove(3)
print("Liste nach Entfernen:", my_list)

# Iteration
print("Iteration über Liste:")
for item in my_list:
    print(item)

# 2. ARRAYS (array Modul)
import array

# Arrays haben einen festen Datentyp
my_array = array.array('i', [1, 2, 3, 4, 5])
print("\nArray:", my_array)

# Zugriff auf Elemente
print("Erstes Element im Array:", my_array[0])

# Hinzufügen von Elementen
my_array.append(6)
print("Array nach Hinzufügen:", my_array)

# Iteration
print("Iteration über Array:")
for item in my_array:
    print(item)

# 3. NUMPY ARRAYS (für Vektoren und Matrizen)
import numpy as np

# Ein Numpy-Array (Vektor)
my_vector = np.array([1, 2, 3, 4, 5])
print("\nNumpy-Array (Vektor):", my_vector)

# Operationen auf Arrays
print("Vektor * 2:", my_vector * 2)

# Mehrdimensionale Arrays (Matrizen)
my_matrix = np.array([[1, 2], [3, 4]])
print("Numpy-Array (Matrix):\n", my_matrix)

# Zugriff auf Elemente
print("Element [0,1] der Matrix:", my_matrix[0, 1])

# 4. DICTIONARIES (MAPS)
# Dictionaries speichern Schlüssel-Wert-Paare.
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nDictionary:", my_dict)

# Zugriff auf Werte
print("Wert für Schlüssel 'a':", my_dict['a'])

# Hinzufügen eines Paares
my_dict['d'] = 4
print("Dictionary nach Hinzufügen:", my_dict)

# Iteration über Schlüssel und Werte
print("Iteration über Dictionary:")
for key, value in my_dict.items():
    print(key, value)

# 5. LISTEN VON DICTIONARIES
# Eine Kombination aus Listen und Dictionaries.
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30}
]
print("\nListe von Dictionaries:")
for person in data:
    print(person['name'], person['age'])

# 6. COLLECTIONS (defaultdict)
from collections import defaultdict

# defaultdict initialisiert Werte automatisch
my_defaultdict = defaultdict(int)
my_defaultdict['a'] += 1
print("\nDefaultdict:", my_defaultdict)

# 7. SETS
# Sets speichern einzigartige Elemente.
my_set = {1, 2, 3, 4, 5}
print("\nSet:", my_set)

# Hinzufügen eines Elements
my_set.add(6)
print("Set nach Hinzufügen:", my_set)

# Entfernen eines Elements
my_set.remove(3)
print("Set nach Entfernen:", my_set)

# 8. TUPLES
# Tuples sind unveränderliche Listen.
my_tuple = (1, 2, 3, 4, 5)
print("\nTuple:", my_tuple)

# Zugriff auf Elemente
print("Erstes Element im Tuple:", my_tuple[0])

# 9. FROZENSET
# Frozensets sind unveränderliche Sets.
my_frozenset = frozenset([1, 2, 3, 4, 5])
print("\nFrozenset:", my_frozenset)

# 10. STACKS UND QUEUES (collections.deque)
from collections import deque

# Ein Stack (LIFO) mit deque
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
print("\nStack:", stack)
stack.pop()
print("Stack nach Pop:", stack)

# Eine Queue (FIFO) mit deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print("\nQueue:", queue)
queue.popleft()
print("Queue nach Popleft:", queue)