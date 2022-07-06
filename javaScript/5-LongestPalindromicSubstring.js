console.log('start')
function checkIfPalindrome (s) {
    let limit = s.length/2;
    if(s.length %2 !=0){
        limit = Math.ceil(s.length/2);
    } 
    for (i=0;i<limit;i++){
        if (s[i]!=s[s.length-1-i]){
            return false;
        }
    }
    return true;
}

function formPalindrome (s,preWord,postWord){
    let thisBest = '';
    let newWord = '';
    let tempBest = '';
    // Odd word 
    if(postWord.length>0 && preWord.length >0){
        //console.log(preWord[preWord.length-1], s , postWord[0],preWord[preWord.length-1] + s + postWord[0]);
        newWord = preWord[preWord.length-1] + s + postWord[0];
        if(checkIfPalindrome(newWord)){
            thisBest = newWord;
            tempBest = formPalindrome(newWord,preWord.substring(0,preWord.length-1),postWord.substring(1))
            if(tempBest.length>thisBest.length){
                thisBest=tempBest;
            }
        }
    }
    return thisBest;
}


var longestPalindrome = function(s) {
    let word = ''
    let preWord = '';
    let postWord = '';
    let longestPal = s[0];
    let tempBest = '';
    for (let i =0;i<s.length;i++){
        word = s[i];
        preWord = s.substring(0,i);
        postWord = s.substring(i+1);
        tempBest = formPalindrome(s[i],preWord,postWord);
        if(tempBest.length>longestPal.length){
            longestPal=tempBest;
        }
        word = s.substring(i,i+2);
        preWord = s.substring(0,i);
        postWord = s.substring(i+2);
        tempBest = formPalindrome(word,preWord,postWord);
        if(checkIfPalindrome(word) && word.length>longestPal.length){
            longestPal=word
        }
        if(tempBest.length>longestPal.length){
            longestPal=tempBest;
        }
    }
    return longestPal;
};

function longestPalindromeB(s) {
    let longestPal = s[0];
    for (let i=0; i<s.length; i++){
        let l=i-1;
        let r= i+1;
        while(l>=0 && r<s.length && s[l]==s[r]){
            // console.log(s[l],s[i],s[r],s.substring(l,r+1))
            if(s.substring(l,r+1).length>longestPal.length){
                longestPal = s.substring(l,r+1);
            }
            l--;
            r++;
        }

        if(s[i]==s[i+1]){
            if(s.substring(i,i+2).length>longestPal.length){
                longestPal = s.substring(i,i+2);
            }
            l=i-1;
            r= i+2;
            while(l>=0 && r<s.length && s[l]==s[r]){
                if(s.substring(l,r+1).length>longestPal.length){
                    longestPal = s.substring(l,r+1);
                }
                l--;
                r++;
            }
        }
    }
    return longestPal;
}


console.log(longestPalindromeB("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"));
console.log('result',longestPalindromeB("babab"));
console.log('result',longestPalindromeB("cbbd"));
console.log('result',longestPalindromeB("aaaa"));


