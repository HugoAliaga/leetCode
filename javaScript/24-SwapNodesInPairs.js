"use strict";
console.log('start');
const ListNode = require('./linkedList');

var swapPairs = function(head) {
    let solution = new ListNode();
    let ans = solution;
    let headNext;
    if(head){headNext = head.next;}

    let counter = 0;
    while(headNext){
        solution.next = headNext;
        headNext = headNext.next;
        solution = solution.next;
        solution.next = head;
        solution=solution.next;
        solution.next=null;
        head = headNext;
        if(headNext){headNext = headNext.next};
    }
    solution.next = head;
    return ans.next;
};

let tests = [];
let solutions = [];

tests.push([1,2,3,4,5]);
solutions.push([2,1,4,3,5]);

tests.push([1,2,3,4,5,6]);
solutions.push([2,1,4,3,6,5]);

tests.push([1,2,3,4,5,6,7]);
solutions.push([2,1,4,3,6,5,7]);

tests.push([1,2]);
solutions.push([2,1]);

tests.push([1]);
solutions.push([1]);

tests.push([]);
solutions.push([]);

for (let i=0; i<tests.length;i++){
    let LN = new ListNode();
    LN.createFromArray(tests[i]);
    let result = swapPairs(LN);
    if(result){result = result.toArray();}
    console.log('Test',i,'||',result,solutions[i],result==solutions[i] ? 'PASS':'FAIL');
}