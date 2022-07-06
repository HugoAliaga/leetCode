
/* Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807. */
console.log('Starting code')
function ListNode (x) {
    this.value = x;
    this.next = null;
  }

function linkedListFromArray (arr) {
    let list = new ListNode(arr[0]);
    let element = list;
    for (let i = 1; i < arr.length; i++){
        element.next = new ListNode(arr[i]);
        element = element.next;
    }
    return list
}

var addTwoNumbers = function(l1, l2) {
    // console.log(l1,l2)
    let carry = 0;
    let sum = 0;
    let addNumbers = new ListNode(0);
    let element = addNumbers;
    while(l1!=null||l2!=null||carry>0){
        if(l1!=null){
            sum += l1.value;
            l1=l1.next;
        }
        if(l2!=null){
            sum += l2.value;
            l2=l2.next;
        }
        sum += carry;
        
        element.value = sum %10;
        element.next=new ListNode(0);
        carry =parseInt(sum/10);
        sum=0

        element = element.next
    }
    return addNumbers;
};
const l1 = linkedListFromArray([2,4,3]);
const l2 = linkedListFromArray([6,4]);

const result = addTwoNumbers(l1,l2);
console.log('result',result);