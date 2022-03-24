"use strict";
console.log('start');
const ListNode = require('./linkedList');

var mergeKLists = function(lists) {
    let newList = new ListNode();
    let ans = newList;

    while(true){
        let minVal=Infinity;
        let listToUse;
        let foundList = false;
        for(let i=0;i<lists.length;i++){
            if(lists[i]){
                if(minVal>lists[i].val){
                    minVal=lists[i].val;
                    listToUse=i;
                    foundList = true;
                }
            }
        }
        if(foundList){
            newList.next = lists[listToUse];
            lists[listToUse]=lists[listToUse].next;
            newList=newList.next;
        } else {
            break;
        }
    }


    return ans.next;
}

let tests = [];
let results = [];

tests.push([[1,4,5],[1,3,4],[2,6]]);
results.push([1,1,2,3,4,4,5,6]);

for(let i=0;i<tests.length;i++){
    for (let j=0;j<tests[i].length;j++){
        let newLN = new ListNode();
        newLN.createFromArray(tests[i][j]);
        tests[i][j]=newLN;
    }
    let result = mergeKLists(tests[i]).toArray();
    console.log('Test',i,'||',result,results[i],result==results[i] ? 'PASS':'FAIL');
}