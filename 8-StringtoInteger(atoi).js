console.log('starting');

var myAtoi = function(s) {
    s = s.replace(/^[ ]+|[ ]+$/g,'','');
    let signS='';
    if(s[0]=='-' || s[0]=='+') {
        signS = s[0];
        s= s.replace(s[0],'');
    };
    let regexp = new RegExp("[^0-9]","g");
    s=s.split(regexp)[0]
    if(!'1234567890'.includes(s[0])) return 0;
    s=signS+s;
    s=parseInt(s);
    if(!s) return 0;
    s=Math.max(-(2**31),Math.min(s,2**31-1));
    return s;
};

console.log('result',myAtoi('+1'),'1');
console.log('result',myAtoi('  +745.645-1.a asd fasd f'),'745');
console.log('result',myAtoi('  -745645-1.a asd fasd f'),'-745645');
console.log('result',myAtoi('-745645-1.a asd fasd f'),'-745645');
console.log('result',myAtoi('sdf-745645-1.a asd fasd f'),'0');
console.log('result',myAtoi('45  -745645-1.a asd fasd f'),'45');
console.log('result',myAtoi('  -745645'),'-745645');
console.log('result',myAtoi('  -745645-'),'-745645');
console.log('result',myAtoi('a'),'0');
console.log('result',myAtoi('3'),'3');
console.log('result',myAtoi('1a'),'1');
console.log('result',myAtoi('  -745.645-1.a asd fasd f'),'-745');


