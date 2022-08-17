def letterCombinations(digits: str) -> list[str]:
    res = []
    characters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv",
                    "wxyz"]
    numbers = {}
    j = 0
    for x in range(2,10):
        numbers[x] = characters[j]
        j += 1

    for i in range(2, 9):
        for j in range(i+1, 10):
            print(numbers[i], numbers[j])
            # for c in numbers[i]:
            #     for y in numbers[j]:
            #         res.append([i, j])
    
    print(res)

letterCombinations("23")