console.log('starting');

var intToRoman = function(num) {
    let romanNumber = '';
    let remainder =0;
    // Divide by 1000
    romanNumber+='M'.repeat(Math.floor(num/1000));
    remainder=num % 1000
    //Divide by 500
    const expr1 = Math.floor(remainder/100);
    switch(true){
        case expr1==9:
            romanNumber += 'CM';
            break;
        case expr1 >4 && expr1<9:
            romanNumber += 'D' + 'C'.repeat(expr1-5);
            break;
        case expr1==4:
            romanNumber += 'CD';
            break;
        case expr1 >0 && expr1<4:
            romanNumber += 'C'.repeat(expr1);
            break;
    }
    remainder =remainder % 100;
    const expr2 = Math.floor(remainder/10);
    switch(true){
        case expr2==9:
            romanNumber += 'XC';
            break;
        case expr2 >4 && expr2<9:
            romanNumber += 'L' + 'X'.repeat(expr2-5);
            break;
        case expr2==4:
            romanNumber += 'XL';
            break;
        case expr2 >0 && expr2<4:
            romanNumber += 'X'.repeat(expr2);
            break;
    }
    remainder = remainder % 10;
    switch(true){
        case remainder==9:
            romanNumber += 'IX';
            break;
        case (remainder >4 && remainder<9):
            romanNumber += 'V' + 'I'.repeat(remainder-5);
            break;
        case remainder==4:
            romanNumber += 'IV';
            break;
        case (remainder >0 && remainder<4):
            romanNumber += 'I'.repeat(remainder);
            break;
    }

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
    console.log(tests[i],result,solution[i],result==solution[i]);
}