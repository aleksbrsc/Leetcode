# Leetcode 804: Unique Morse Code Words (easy)
# string, hashmap

class Solution(object):
    # 4x%, 6x% time/space complexity
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        transformations = [] # list of transformations
        morse_map = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
             "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
             "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
             "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."} # char : morse char

        for word in words:
            morse_word = "" # set/reset the morse word
            for char in word:
                if char in morse_map:
                    morse_word += morse_map[char] # add the morse code equivalent of the character to the morse code word string
            transformations.append(morse_word) # add the transformed word to the list of transformations

        return len(set(transformations)) # casting to set stores the unique elements, then length returns the amount of elements (unique transformations) in the list

    # another version for test, uses set from the start instead of casting later
    # beats 90% for space complexity, but half the other time complexity due to set
    def uniqueMorseRepresentationsSet(self, words):
        transformations = set() # set of transformations
        morse_map = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
             "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
             "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
             "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."} # char : morse char

        for word in words:
            morse_word = "" # set/reset the morse word
            for char in word:
                if char in morse_map:
                    morse_word += morse_map[char] # add the morse code equivalent of the character to the morse code word string
            transformations.add(morse_word) # add the transformed word to the list of transformations

        return len(transformations) # casting to set stores the unique elements, then length returns the amount of elements (unique transformations) in the list

    # someone else's similar solution to mine using ascii instead of mapping char : morse
    # also doesn't check if its in the list but uses .lower(), realized constraint says lower case anyways, maybe should start doing that for faster runtime?
    def uniqueMorseRepresentationsOther(self, words: list[str]) -> int:
        morse_code_array = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        result = set() # also uses a set for storing unique transformations
        for word in words:
            word = word.lower() 
            transformations = ""
            for chr in word:
                transformations += morse_code_array[ord(chr) - 97] # ascii alphabet starts at 97 with a, therefore subtracting 97 from the orded char understandably gets the appropriate index
            result.add(transformations)
        return len(result)


# test cases
solution = Solution()
words = ["gin","zen","gig","msg"]
print(solution.uniqueMorseRepresentations(words))
print(solution.uniqueMorseRepresentationsSet(words))
