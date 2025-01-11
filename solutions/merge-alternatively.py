class Solution:
    def mergeAlternatively(self, word1:str, word2:str) -> str:
        mergedOutput = []
        for a,b in zip(word1,word2):
            mergedOutput.append(a)
            mergedOutput.append(b)
        
        #zip() combines the elements of word1 and word2 into pairs (tuples). 
        #It returns an iterator where each item is a tuple of corresponding elements from the two input sequences.
        #If the sequences are of different lengths, zip() stops when the shorter sequence is exhausted.
        mergedOutput.extend( word1[len(word2):] or word2[len(word1):])
        #handle the merging of the remaining characters from word1 or word2 (if one word is longer than the other) and convert the result list to a string
        #return mergedOutput
        return ''.join(mergedOutput)
        
        #join() concatenates all elements in the merged list into a single string
        #'' specifies that the elements should be joined without any additional characters between them (no spaces).
    
sol = Solution()
result = sol.mergeAlternatively("abc","xyz123")
print(result)