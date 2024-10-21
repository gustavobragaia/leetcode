class Solution:
    def romanToInt(self, s: str) -> int:
        sumS = 0
        numRom = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for i in range(len(s)):  # Itera sobre os índices da string
            if i > 0 and numRom[s[i]] > numRom[s[i - 1]]:
                # Se o valor atual for maior que o anterior, subtraímos duas vezes o valor anterior (já somado antes)
                sumS += numRom[s[i]] - 2 * numRom[s[i - 1]]
            else:
                # Caso contrário, apenas somamos o valor atual
                sumS += numRom[s[i]]
        return sumS
