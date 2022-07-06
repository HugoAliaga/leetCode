console.log('start');

var fourSum = function(nums, target) {
    if(nums.length<4) return [];

    nums.sort((a,b)=>a-b);
    result = [];
    let sum=0;
    for (let i=0; i<nums.length-3; i++){
        if(nums[i]==nums[i-1]) continue;
        for (let j=i+1;j<nums.length-2;j++){
            let k=j+1;
            let l=nums.length-1;
            while(k<l && l<nums.length){
                sum = nums[i] + nums[j] + nums[k] + nums[l];
                if(sum==target){
                    result.push([nums[i],nums[j],nums[k],nums[l]]);
                    while (nums[l]==nums[l-1]) l--;
                    while (nums[k]==nums[k+1]) k++;
                    k++;
                    l--;
                } else if (sum>target) {
                    l--;
                } else {
                    k++;
                }
            }
            while (nums[j]==nums[j+1]) j++;
        }
        while (nums[i]==nums[i+1]) i++;
    }

    return result;
    
};

let tests = [];
let solutions = [];

/* tests.push([[1,0,-1,0,-2,2],0]);
solutions.push([[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]);

tests.push([[2,2,2,2,2],8]);
solutions.push([2,2,2,2]); */

tests.push([[-3,-2,-1,0,0,1,2,3],0]);
solutions.push([[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]);

let result ='';
for (let i=0; i<tests.length; i++){
    result = fourSum(tests[i][0],tests[i][1]);
    console.log('Test ' + i,'||',result,solutions[i]);
}