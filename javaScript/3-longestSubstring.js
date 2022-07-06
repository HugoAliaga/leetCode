console.log('Starting code')

var lengthOfLongestSubstring = function(str) {
    subString='';
    longestSubstring = '';
    maxLength = 0;
    for (let i=0;i<str.length;i++){
        if(subString.includes(str[i])){
            subString = subString.split(str[i])[1];
            subString+=str[i];
        } else {
            subString+=str[i];
        }
        if(subString.length > maxLength){
            maxLength = subString.length;
            longestSubstring = subString;
        }
    }
    console.log(longestSubstring);
    return maxLength;
};

const result = lengthOfLongestSubstring('asdtpotato');
console.log('result',result);