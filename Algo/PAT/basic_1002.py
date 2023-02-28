
chinese_pinyins = [
    'ling',
    'yi',
    'er',
    'san',
    'si',
    'wu',
    'liu',
    'qi',
    'ba',
    'jiu',
]

if __name__ == '__main__':
    num_chars = input()

    total = 0
    for num_char in num_chars:
        total += int(num_char)

    output = []
    for num_char in str(total):
        output.append(chinese_pinyins[int(num_char)])

    print(' '.join(output))

