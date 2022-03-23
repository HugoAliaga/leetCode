console.log('start');

const ListNode = require('./linkedList');

var mergeTwoLists = function(list1, list2) {

    let chosenList = new ListNode();
    let head = chosenList;

    while (list1 && list2 && list1.val != null && list2.val != null){
        if(list1.val<list2.val){
            chosenList.next = list1;
            list1 = list1.next;
        } else {
            chosenList.next = list2;
            list2 = list2.next;
        }
        chosenList = chosenList.next;
    }
    while (list1 && list1.val != null) {
        chosenList.next = list1;
        list1 = list1.next;
        chosenList = chosenList.next;
    }
    while (list2 && list2.val !=null) {
        chosenList.next = list2;
        list2 = list2.next;
        chosenList = chosenList.next;
    }

    return head.next;
};

let tests = [];
let solutions = [];

tests.push([[1,2,4],[1,3,4]]);
solutions.push([1,1,2,3,4]);

tests.push([[],[]]);
solutions.push([]);

tests.push([[0],[]]);
solutions.push([0]);

for (let i=0; i< tests.length;i++){
    const arr1 = new ListNode();
    const arr2 = new ListNode();
    arr1.createFromArray(tests[i][0]);
    arr2.createFromArray(tests[i][1]);
    let result = mergeTwoLists(arr1,arr2).toArray();
    console.log('Test',i,'||',result,solutions[i],result==solutions[i] ? 'PASS' : 'FAIL');
}