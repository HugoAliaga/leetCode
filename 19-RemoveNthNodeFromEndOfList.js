console.log('start');

class LinkedList {
    constructor (array){
        this.value=array[0];
        if (array.length>1){
            this.next = new LinkedList(array.splice(1,array.length));
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

var removeNthFromEnd = function(head, n) {
    let newArray = [];
    
};

let myArray = [1,2,3,4,5];
let myLL = new LinkedList(myArray);
console.log(myLL.toArray());
let tests=[];
let solutions = [];

/* for(i=0;i<tests.length;i++){
    let result = removeNthFromEnd(tests[i][0],tests[i][1]);
    console.log('Test',i,'||',result.toArray(),solutions[i]);
} */