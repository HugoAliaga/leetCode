
console.log('start');

var threeSumClosest = function(nums, target) {
    if(nums.length<3) return [];
    nums.sort((a,b)=>a-b);
    let sum = 0;
    let result =Infinity;
    let j=0;
    let k=0;

    for(let i=0; i<nums.length;i++){
        if(nums[i-1]==nums[i]) continue;
        j = i + 1;
        k = nums.length - 1;
        while(k>j){
            sum = nums[i] + nums[j] + nums[k];
            if(Math.abs(sum-target)<Math.abs(result-target)){
                result = sum;
            }
            if (sum==target){
                return target;
            } else if (sum > target) {
                k--;
            } else {
                j++;
            }   
        }

    }
    return result;
};

let tests = [];
let solutions = [];

tests.push([[-1,2,1,-4],1]);
solutions.push(2)
tests.push([[0,0,0],1]);
solutions.push(0);

let result = [];
for (let i=0; i<tests.length; i++){
    result = threeSumClosest(tests[i][0],tests[i][1]);
    console.log('Test ' + i + ' ||',result,solutions[i],result==solutions[i]);
}