class Anagram:
    def __init__(self, match_word):
        self.match_word = sorted(list(match_word.lower()))
    
    def match(self, word_list):
        result = []
        for word in word_list:
            sorted_word = sorted(list(word.lower()))
            if sorted_word == self.match_word:
                result.append(word)
        return result