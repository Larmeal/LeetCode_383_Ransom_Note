# a manual  algorithm  type
class Solution_algorithm:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alphabet = {}
        # divided magazine to letter in the List 
        maga = [n for n in magazine]
        
        # Loop in magazine argument for saving to alphabet Dict
        for i in maga:
            # if not any letter in Dict, added to Dict and equal 1
            if i not in alphabet:
                alphabet[i] = 1
            # if in the list has more character letters than 1, added to the same key and +1 in value
            else:
                alphabet[i] += 1

        # Loop in ransomNote to check-in Dict that has some letters of ransomNote in maga 
        for j in ransomNote:
            # if not has any letter in Dict, returned False
            if j not in alphabet:
                return False
            # if some letter exist in Dict that mean not equal to zero
            elif alphabet[j] == 0:
                return False
            # minused one of value of key that mean has some elements in ransomNote is constructure of magazine
            alphabet[j] -= 1
        
        return True


# a function algorithm type
class Solution_function:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Loop in set(ransom Note) because we don't need to duplicate letters in the loop
        for i in set(ransomNote):
            # if number of letter of magazine less than ransomNote that mean some of letters in ransomNote don't be to consturction
            if magazine.count(i) < ransomNote.count(i):
                return False
        
        return True
        
print(Solution_algorithm().canConstruct("ab", "bab")) 