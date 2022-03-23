class ListNode {
    constructor (value=null){
        this.val=value;
        this.next = null;
    }
}

ListNode.prototype.toArray = function () {
    let newArray = [];
    let node = this;
    while (node.next){
        newArray.push(node.val);
        node.next ? node = node.next : '';
    }
    newArray.push(node.val);
    return newArray;
}

ListNode.prototype.createFromArray = function (array) {
    let head = this;
    if (array.length>0){
        head.val = array[0];

        for (let i=1;i<array.length;i++){       
            head.next = new ListNode(array[i]);
            head=head.next;
        }
    }
}

module.exports = ListNode;