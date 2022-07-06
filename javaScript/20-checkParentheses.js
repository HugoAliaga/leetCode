"use strict";
console.log('start');

let openMap = ['(','[','{'];
let opposites = {
    '(':')',
    '[':']',
    '{':'}'
}
var isValid = function(s) {
    let check = '';
    for (let i=0;i<s.length;i++){
        if(openMap.includes(s[i])){
            check += s[i];
        } else {
            if ( s[i]== opposites[check[check.length-1]]) {
                check = check.substring(0,check.length-1);
            } else {
                return false;
            }
        }

    }
  return check.length == 0;  
};

let tests =[];
let solutions = [];

tests.push('()');
solutions.push(true);

tests.push("()[]{}");
solutions.push(true);

tests.push('(]');
solutions.push(false);

tests.push("([)]");
solutions.push(false);

for (let i = 0; i < tests.length; i++){
    let result = isValid(tests[i]);
    console.log('Test',i,'||',result,solutions[i],result==solutions[i] ? 'PASS':'FAIL');
}