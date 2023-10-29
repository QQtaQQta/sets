#1
numbers = [1, 2, 3, 4, 1, 2, 3, 4, 5]
unique_numbers = set(numbers)
count = len(unique_numbers)
print(count)

#2
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_numbers = set(list1) & set(list2)
count = len(common_numbers)
print(count)

#3
list1 = [5, 2, 8, 1, 4]
list2 = [7, 1, 5, 4, 3]
common_numbers = sorted(set(list1) & set(list2))
print(common_numbers)

#4
sequence = input("Введите последовательность чисел через пробел: ")
numbers = sequence.split()
seen_numbers = set()
for number in numbers:
    if number in seen_numbers:
        print("YES")
    else:
        print("NO")
        seen_numbers.add(number)
        
#5
word_set = set()
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        words = line.split()
        word_set.update(words)

num_unique_words = len(word_set)
print(f"Тут {num_unique_words} разных слов")