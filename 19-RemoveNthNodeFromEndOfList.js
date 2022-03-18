"use strict";
console.log('start');

class LinkedList {
    constructor (array){
        this.value=array[0];
        
        if (array.length>1){
            this.next = new LinkedList(array.splice(1,array.length),false);
        } else {
            this.next = null;
        }
    }
}

LinkedList.prototype.toArray = function () {
    let newArray = [];
    let node = this;
    while (node.next){
        newArray.push(node.value);
        node.next ? node = node.next : '';
    }
    newArray.push(node.value);
    return newArray;
}

var removeNthFromEnd2 = function(head, n) {
    let listLength = -1;
    let node = head;
    node.value ? listLength++:'';
    while(node){
        listLength++;
        node=node.next;
    }
    node =head;
    console.log(listLength,n,listLength==n);
    if (listLength<=n){
        return node.next ? node.next : [];
    }
    for(let i=0;i< listLength-n-1;i++){
        node=node.next;
    }
    console.log(node);
    node.next = node.next ? node.next.next : null;
    return head;
};

var removeNthFromEnd = function(head, n) {
    let node = head;

    for (let i=0;i<n;i++){
        node = node ? node.next : null;
    }
    if(!node){
        return head.next;
    }
    let node2 = head;

    while (node.next){
        node = node ? node.next : null;
        node2 = node2.next;
    }
    node2.next = node2.next ? node2.next.next : null;
    return head;
};


let tests=[];
let solutions = [];
tests.push([new LinkedList([1,2,3,4,5]),8]);
solutions.push([1,2,3,5]);
tests.push([new LinkedList([1]),1]);
solutions.push([]);
tests.push([new LinkedList([1,2]),1]);
solutions.push([1]);
tests.push([new LinkedList([1,2]),2]);
solutions.push([2]);

for(let i=0;i<tests.length;i++){
    let result = removeNthFromEnd(tests[i][0],tests[i][1]);
    if(result){
        let newResult = result.toArray();

    } else {
        let newResult = result;
    }
    console.log('Test',i,'||',result,solutions[i]);
}