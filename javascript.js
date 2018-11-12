function vowelsAndConsonants(s) {
    let cons = '';
    // let vowels = ['a'
    let re = /^[aeiou]$/i;

    let i
    for (i = 0; i < s.length; i ++) {

        if (re.test(s[i])) {
            console.log(s[i]);
        }
        else {
            cons += s[i]
        }
    }
    let j
    for (j = 0; j < cons.length; j ++) {
        console.log(cons[j]);
    }
}

// console.log(vowelsAndConsonants('javascriptloops'))

function regexVar(s) {
    // let re = /^([aeiou])\w+([aeiou])$/i;
    let re = /^([aeiou])\w+\1$/i;
    // let re = /^[aeiou]$/i;
    return re.test(s)
}

console.log(regexVar('abca'))
console.log(regexVar('ab'))
console.log(regexVar('ba'))
console.log(regexVar('abab'))