console.log('starting');

var intToRoman = function(num) {
    let romanNumber = '';
    let remainder =0;
    // Divide by 1000
    romanNumber+='M'.repeat(Math.floor(num/1000));
    remainder=num % 1000
    //Divide by 500
    romanNumber+='D'.repeat(Math.floor(remainder/500));
    remainder=remainder % 500
    //Divide by 100
    Math.floor(remainder/100)>3 ? romanNumber+='CD': romanNumber+='C'.repeat(Math.floor(remainder/100));
    remainder=remainder % 100
    //Divide by 50 
    romanNumber+='L'.repeat(Math.floor(remainder/50));
    remainder=remainder % 50
    // Divide by 10
    Math.floor(remainder/10)>3 ? romanNumber+='XL' : romanNumber+='X'.repeat(Math.floor(remainder/10));
    remainder=remainder % 10
    // Divide by 5
    romanNumber+='V'.repeat(Math.floor(remainder/5));
    remainder=remainder % 5
    // Divide by 1
    remainder >3 ? romanNumber+='IX' : romanNumber+='I'.repeat(remainder);
    return romanNumber;
};

let tests = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    12,
    15,
    36,
    89,
    198,
    3000,
    3999,
    3457
]
let solution = [
    'I',
    'II',
    'III',
    'IV',
    'V',
    'VI',
    'VII',
    'VIII',
    'IX',
    'X',
    'XII',
    'XV',
    'XXXVI',
    'LXXXIX',
    'CXCVIII',
    'MMM',
    'MMMCMXCIX',
    'MMMCDLVII'
]
let result =0;
for(let i=0;i<tests.length;i++){
    result = intToRoman(tests[i]);
    console.log(result,solution[i],result==solution[i]);
}