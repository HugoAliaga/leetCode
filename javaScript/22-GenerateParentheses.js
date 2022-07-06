"use strict";
console.log('start');

var generateParenthesis = function (n) {
    let res = [];

    const dfs = function (str,open,close) {
        if (open<close) return;
        if (open+close==2*n) {
            res.push(str);
            return;
        }
        
        if(open<n) dfs(str+'(',open+1,close);
        if (close<n) dfs(str+')',open,close+1);
        
    }

    dfs('',0,0);
    return res;
}



let tests = [];
let results = [];

tests.push(1);
results.push(['()']);

tests.push(2);
results.push(['()()','(())']);
tests.push(3);
results.push([ '()()()', '(()())', '()(())', '(())()', '((()))' ]);

for (let i = 0; i< tests.length;i++){
    let result =  generateParenthesis(tests[i]);
    console.log('Test',i,'||',result,results[i],result==results[i] ? 'PASS':'FAIL');
}