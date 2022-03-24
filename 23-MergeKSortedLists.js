"use strict";
console.log('start');
const ListNode = require('./linkedList');

var mergeKLists = function(lists) {
    let newList = new ListNode();
    let ans = newList;

    while(true){
        let minVal=Infinity;
        let listToUse;
        for(let i=0;i<lists.length;i++){
            if(lists[i] && minVal>lists[i].val){
                minVal=lists[i].val;
                listToUse=i;
            }
        }
        if(minVal<Infinity){
            newList.next = lists[listToUse];
            lists[listToUse]=lists[listToUse].next;
            newList=newList.next;
        } else {
            break;
        }
    }
    return ans.next;
}

var mergeKLists2 = function(lists) {
    let newArray = [];
    let newList = new ListNode();
    let ans = newList;

    for (let i=0;i<lists.length;i++){
        while(lists[i]){
            newArray.push(lists[i].val);
            lists[i]=lists[i].next;
        }
    }
    newArray.sort((a,b)=>a-b);

    for(let i=0;i<newArray.length;i++){
        newList.next = new ListNode();
        newList = newList.next;
        newList.val = newArray[i];
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
    let result = mergeKLists2(tests[i]).toArray();
    console.log('Test',i,'||',result,results[i],result==results[i] ? 'PASS':'FAIL');
}