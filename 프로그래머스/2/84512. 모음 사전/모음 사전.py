def generate_words():
    vowels = ['A', 'E', 'I', 'O', 'U']
    words = []
    max_length = 5
    
    def generate(word):
        words.append(word)
        if len(word) < max_length:
            for vowel in vowels:
                generate(word + vowel)
    
    generate('')
    return words
    
def solution(word):
    words = generate_words()
    answer = words.index(word)
    return answer