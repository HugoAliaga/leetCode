console.log('starting');

var isPalindrome = function(x) {
    x=x.toString();
    for (let i=0; i<x.length/2;i++){
        if(x[i]!==x[x.length-1-i]){
            return false;
        }
    }
    return true;
};

let testArray = [123,121,-121];
function runTests(testArray){
    for(let i=0;i<testArray.length;i++){
        console.log(testArray[i],isPalindrome(testArray[i]));
    }
}
console.log('result',runTests(testArray));