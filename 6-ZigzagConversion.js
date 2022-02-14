console.log('starting')

var convert = function(s, numRows) {
    if (numRows==0){
        return s;
    }
    let result = '';
    let word=[];
    let direction = 1;
    for (let j=0; j<numRows; j++){
        word[j]='';
    }
    let i=0;
    let j=0;
    while (i<s.length){
        word[j]+=s[i]
        j+=direction;
        if(j>=numRows){
            direction = -1;
            j =numRows-2;
        }
        if(j<=0){
            direction = 1;
            j = 0;
        }   
        i++
    }

    for (let j=0; j<word.length; j++){
        if(typeof word[j] != 'undefined'){

            result+=word[j];
        }
    }
    return result;
};

console.log('result',convert('PAYPALISHIRING',3));
console.log('PINALSIGYAHRPI');