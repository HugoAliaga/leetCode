console.log('Starting code')
var twoSum = function(nums, target) {
    let seen = [];
    for(let i in nums){
        console.log(i);
        let required = target - nums[i];
        if(seen.includes(required)){
            return [seen.indexOf(required),i];
        } else {
            seen.push(nums[i]);
        }
    }
};

const result = twoSum([3,3],6);
console.log('result',result);
