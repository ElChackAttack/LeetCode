# Date: 25/05/22

class Solution:

    def getHint(self, secret: str, guess: str) -> str:
        secret_dict = self.createDictionary(secret)
        guess_dict = self.createDictionary(guess)
        cows = 0
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                secret_dict[secret[i]] -= 1
                guess_dict[guess[i]] -= 1
        for i in secret:
            if secret_dict[i] > 0 and i in guess_dict and guess_dict[i] > 0:
                cows += 1
                secret_dict[i] -= 1
                guess_dict[i] -= 1
        return str(bulls)+'A'+str(cows)+'B'

    def createDictionary(self, string: str) -> dict:
        new_dictionary = {}
        for c in string:
            new_dictionary.setdefault(c, 0)
            new_dictionary[c] += 1
        return new_dictionary
