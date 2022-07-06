console.log('start');

const map = {
    '2':['a','b','c'],
    '3':['d','e','f'],
    '4':['g','h','i'],
    '5':['j','k','l'],
    '6':['m','n','o'],
    '7':['p','q','r','s'],
    '8':['t','u','v'],
    '9':['w','x','y','z']
};

var letterCombinations = function(digits) {
    if (digits == null)  return '';
    let results = [];
    let tempResults = [];
    for (let i = 0;i<digits.length;i++){
        if(results.length==0){
            for(let j=0;j<map[digits[i]].length;j++){
                results.push(map[digits[i]][j]);
            }
        } else {
            tempResults=[];
            for(let j=0;j<map[digits[i]].length;j++){
                for (let k=0;k<results.length;k++){
                    tempResults.push(results[k]+map[digits[i]][j]);
                }
            }
            results = tempResults;
        }
    }
    return results;
};

let tests = [];
let solutions = [];

tests.push('2');
solutions.push(['a','b','c']);

tests.push('23');
solutions.push(['ad','ae','af','bd','be','bf','cd','ce','cf']);

tests.push('234567');
solutions.push(['ad','ae','af','bd','be','bf','cd','ce','cf']);

let result = '';
for (let i =0; i<tests.length; i++){
    result = letterCombinations(tests[i]);
    console.log('Test '+i+' || ',result,solutions[i]);
}