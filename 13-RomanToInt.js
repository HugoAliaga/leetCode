console.log('start');

mapRoman = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}
var romanToInt = function(s) {
    let integer = 0;
    let thisVal = 0;
    for (let i=0;i<s.length;i++){
        thisVal = mapRoman[s[i]];
        if(i<s.length-1){
            nextVal = mapRoman[s[i+1]]
            if(thisVal>=nextVal){
                integer+=thisVal;
            } else {
                integer += nextVal - thisVal;
                i++
            }
        } else {
            integer += thisVal;
        }
    }
    return integer;
};

testCases = [];
solutions=[];

testCases.push('MCCXXXIV');
solutions.push(1234);

let result = '';
for (let i=0; i < testCases.length; i++){
    result = romanToInt(testCases[i]);
    console.log('Test '+ i, result, solutions[i] , solutions[i]==result);
}