def word_frequency_counter(file_path):
    word_freq = {}
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        for word in words:
            cleaned_word = ''.join(char for char in word if char.isalnum()).lower()
            if cleaned_word in word_freq:
                word_freq[cleaned_word] += 1
            else:
                word_freq[cleaned_word] = 1
    return word_freq

file_path = 'sample.txt'
frequencies = word_frequency_counter(file_path)

for word, freq in frequencies.items():
    print(f'{word}: {freq}')