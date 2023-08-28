def min_coins(unique_coins, target):
    min_coin_count = [float('inf')] * (target + 1)
    min_coin_count[0] = 0

    for i in range(1, target + 1):
        for unique_coin in unique_coins:
            if i - unique_coin >= 0:
                min_coin_count[i] = min(min_coin_count[i], 1 + min_coin_count[i - unique_coin])

    return min_coin_count[target]

def text_file(input, output):
    with open(input, "r") as input_file:
        coin_count, target_val = map(int, input_file.readline().split())
        coin_values = list(map(int, input_file.readline().split()))

    min_coin_result = min_coins(coin_values, target_val)

    with open(output, "w") as output_file:
        output_file.write(f"{min_coin_result}")

text_file("Input3_1.txt", "Output3_1.txt")
text_file("Input3_2.txt", "Output3_2.txt")
