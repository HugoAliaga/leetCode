console.log('starting')

var convert = function(s, numRows) {
    let result = '';
    let indexes ='';
    let i=0;
    let j=0;
    while (i+j<numRows){
        if(i==Math.floor(numRows/2)){
            while (j<s.length && i+j<s.length){
                result+=s[i+j];
                indexes+=i+j+','
                j+=Math.ceil(numRows/2);
            }
        } else {
            while(j<Math.ceil(s.length/(numRows+1)) && i+4*j<s.length){
                result+=s[i+4*j];
                indexes+=i+4*j+','
                j++;
            }
        }

        i++;
        j=0;
    }
    return result;
};

console.log('result',convert('PAYPALISHIRING',3));
console.log('PAHNAPLSIIGYIR');