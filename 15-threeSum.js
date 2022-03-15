console.log('start');

var threeSum = function(nums) {
    if(nums.length<3) return [];
    nums.sort((a, b) => a - b)
    let solutions = [];
    let sum =0;
    let newArray = [];
    let i=0; 
    let j = i+1;
    let k = nums.length-1;
    for(let i =0; i<nums.length-2; i++){
        if(nums[i]==nums[i-1]) continue;
        j=i+1;
        k= nums.length-1;
        while(k>j){
            sum=nums[i]+nums[j]+nums[k];
            if(sum==0){
                solutions.push([nums[i],nums[j],nums[k]]);
                while(nums[k]==nums[k-1]){
                    k--;
                }
                while(nums[j]==nums[j+1]){
                    j++;
                }
                j++;
                k--;
            } else if(sum>0){
                k--;
            } else {
                j++;
            }
        }
    }
    return solutions;
};

let tests = [];
let solutions = [];

tests.push([-1,0,1,2,-1,-4,-2,-3,3,0,4]);
solutions.push([[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]);

tests.push([1,-1,-1,0]);
solutions.push([[-1,0,1]]);

tests.push([-2,0,0,2,2]);
solutions.push([[-2,0,2]]);

tests.push([-2,0,1,1,2]);
solutions.push([[-2,0,2],[-2,1,1]]);

tests.push([-1,0,1,2,-1,-4]);
solutions.push([[-1,-1,2],[-1,0,1]]);

tests.push([0,0,0]);
solutions.push([0,0,0]);

tests.push([0,0,0,0]);
solutions.push([0,0,0]);

let result = [];
for (let i=0; i<tests.length; i++){
    result = threeSum(tests[i]);
    console.log('Test ' + i,result,solutions[i],result==solutions[i]);
}