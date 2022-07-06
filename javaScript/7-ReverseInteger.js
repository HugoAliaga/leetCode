console.log('starting')

var reverse = function(x) {
    let reversedNumber = '';
    if(x<0){
        reversedNumber='-'
    }
    for(let i=0; i<x.toString().length;i++){
        reversedNumber+=x.toString()[x.toString().length-1-i];
    }
    if(Math.abs(parseInt(reversedNumber))>2**31 && parseInt(reversedNumber)<0||parseInt(reversedNumber)>2**31-1){
        return 0;
    }
    return parseInt(reversedNumber);
};
console.log('result',reverse(-2147483648));