class Solution:
    def fullJustify(self, words, maxWidth):
        ans = []
        # Build each line
        while words:
            line = []
            length = 0
            while words and length<maxWidth and length+len(words[0])<=maxWidth:
                length += len(words[0])
                line.append(words.pop(0))
                if length<maxWidth:
                    length+=1
                    line.append(' ')
            if line[-1]==' ' and words and len(line)>2:
                line.pop()
                length-=1
            i=1
            while length<maxWidth and words:
                if i>len(line)-1:
                    i=1
                
                length+=1
                line[i]+=' '
                i+=2
            while length<maxWidth:
                length+=1
                line[-1]+=' '
            ans.append(''.join(line))
            length=0
            if words and len(words[0])>maxWidth:
                ans.append(words.pop(0))
        return ans


tests = []
solutions = []

tests.append([["This", "is", "an", "example", "of", "text", "justification."],16])
solutions.append([
   "This    is    an",
   "example  of text",
   "justification.  "
])

tests.append([["What","must","be","acknowledgment","shall","be"],16])
solutions.append([
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
])

tests.append([["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20])
solutions.append([
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
])
for i in range(len(tests)):
    ans = Solution().fullJustify(tests[i][0],tests[i][1])
    print('T',i,'R',ans,solutions[i])