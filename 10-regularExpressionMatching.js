console.log('starting');

const isMatch = (string, pattern) => {
    // early return when pattern is empty
    if (!pattern) {
		// returns true when string and pattern are empty
		// returns false when string contains chars with empty pattern
        return !string;
    }
    
	// check if the current char of the string and pattern match when the string has chars
    const hasFirstCharMatch = Boolean(string) && (pattern[0] === '.' || pattern[0] === string[0]);

    // track when the next character * is next in line in the pattern
    if (pattern[1] === '*') {
        // if next pattern match (after *) is fine with current string, then proceed with it (s, p+2).  That's because the current pattern may be skipped.
        // otherwise check hasFirstCharMatch. That's because if we want to proceed with the current pattern, we must be sure that the current pattern char matches the char
		// If hasFirstCharMatch is true, then do the recursion with next char and current pattern (s+1, p).  That's because current char matches the pattern char. 
        return (
            isMatch(string, pattern.slice(2)) || 
            (hasFirstCharMatch && isMatch(string.slice(1), pattern))
        );
    }
    
    // now we know for sure that we need to do 2 simple actions
	// check the current pattern and string chars
	// if so, then can proceed with next string and pattern chars (s+1, p+1)
    return hasFirstCharMatch ? isMatch(string.slice(1), pattern.slice(1)) : false;
};

var isMatch1 = function (s,p) {
    let pIndex = 0;
    let sIndex = 0;
    let pPre = '';
    while(s.length>0 || p.length>0){
        if (s[s.length-1] == p[p.length-1]) {
            s=s.substring(0,s.length-1);
            p=p.substring(0,p.length-1);
        } else if ((s[0] == p[0] || p[0]=='.') && s.length) {
            s=s.substring(1,s.length);
            if(p[1]!='*'){
                p=p.substring(1,p.length);
            } 
        } else if (s[0]!=p[0] && p[1]=='*') {
            p=p.substring(2,p.length);
        } else if (p[0]=='.') {
            p=p.substring(1,p.length);
        } else { 
            return false;
        }
    }
    return true;
};

function runTests (testArray){
    for (let i=0;i<testArray.length;i++){
        console.log('test '+ i,testArray[i].slice(0,2),testArray[i][2],isMatch(testArray[i][0],testArray[i][1]));
    }
}

let testArray = [["ab",".*..*",true],["ab",".*..",true],["aaa","ab*a",false],["aaa","a*a",true],["ab",".*",true],["ab",".*c",false],["aaaab","c*a*b",true],["aab","c*a*b",true],["aaferefe","a.*",true],["aaferefe","a.b*",false],["aa","a*",true]]
runTests(testArray);