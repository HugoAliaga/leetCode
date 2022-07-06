console.log('start');

var longestCommonPrefix = function(strs) {
    let prefix = '';
    let currentLetter ='';
    for(i=0;i<strs[0].length;i++){
        currentLetter = strs[0][i];
        for (j=0; j<strs.length;j++){
            if(strs[j][i]!=currentLetter){
                return prefix;
            }
        }
        prefix += currentLetter;
    }
    return prefix;
};

let tests = [];
let solutions = [];

tests.push(['florida','flatter','fluorish']);
solutions.push('fl');

let result = '';
for (let i=0; i<tests.length; i++){
    result = longestCommonPrefix(tests[i]);
    console.log('Test ' + i,result,solutions[i],result==solutions[i]);
}