class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        matched_words = []
        sorted_word = sorted(self.word.lower())
        
        for word in word_list:
            if sorted(word.lower()) == sorted_word:
                matched_words.append(word)
        
        return matched_words