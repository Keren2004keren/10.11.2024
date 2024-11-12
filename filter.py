# START
import random
import statistics

# 1
rand_list: list[int] = [random.randint(1, 100) for i in range(50)]
print(rand_list)

print(f"Bigger than 50: {list(filter(lambda num: num > 50, rand_list))}")
print(f"Dividend by 7: {list(filter(lambda num: num % 7 == 0, rand_list))}")
print(f"Two digit:{list(filter(lambda num: 10 <= num <= 99, rand_list))}")
print(f"Two digit that their tens and ones are equal:{list(filter(lambda num: num % 10 == num // 10, rand_list))}")
print(f"Sum of digits equal to 9: {list(filter(lambda num: num // 10 + num % 10 == 9, rand_list))}")
print(f"Bigger than average: {list(filter(lambda num: num > statistics.mean(rand_list), rand_list))}")
print(f"Bigger than half of the biggest number: {list(filter(lambda num: num > max(rand_list) // 2, rand_list))}")

# 2
game_list: list[str] = ["Grand Theft Auto V", "Fortnite", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]
print(f"Longer than 8 letters:{list(filter(lambda word: len(word) > 8, game_list))}")
print(f"Starts with F:{list(filter(lambda word: word.startswith("F"), game_list))}")
print(f"Only 2 words:{list(filter(lambda word: len(word.split()) == 2, game_list))}")
print(f"Only has V: {list(filter(lambda word: "v" in word.lower(), game_list))}")

# STOP