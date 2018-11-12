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

function regexVar(s) {
    // let re = /^([aeiou])\w+([aeiou])$/i;
    let re = /^([aeiou])\w+\1$/i;
    // let re = /^[aeiou]$/i;
    return re.test(s)
}

console.log(regexVar('abca')== true)
console.log(regexVar('ab') == false)
console.log(regexVar('ba') == false)
console.log(regexVar('abab') == false)


function reverseString(s) {
    try {
     return s.split('').reverse().join('')
    }
    catch(e) {
        // console.log(e.message);
        // console.log(s)
        return 'caught'
    }
}

console.log(reverseString('abc') == 'cba')
console.log(reverseString(123) == 'caught')
console.log(reverseString('') == '')

function isPalindrome(x) {
    
    if (x < 0) {
        return false
    }
    
    if (x < 10) {
        return true
    }
    
    let a = x
    let rev = 0
    while (a) {
        let pop = a % 10;
        rev = rev*10 + pop;
        a = Math.floor(a /10);
    }
    
    return rev == x
}

console.log(isPalindrome(123) == false)
console.log(isPalindrome(121) == true)

var removeDuplicates = function(nums) {
    
    if (nums.length <= 0) {
        return nums
    }
    
    let j = 0
    
    for (i=0; i < nums.length; i ++) {
        if (nums[i] != nums[j]) {
            j ++
            nums[j] = nums[i];
        }
        
    } 
    nums = nums.slice(0, j+1)
    return nums

};

// console.log(removeDuplicates([]) == [])
// console.log(removeDuplicates([1]) == [1])
// console.log(removeDuplicates([1, 1, 3]) == [1, 3])