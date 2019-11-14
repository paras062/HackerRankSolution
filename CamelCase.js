'use strict'
/**Question - Hacker Rank - Camel Case 
 * URL - https://www.hackerrank.com/challenges/camelcase/problem
* Alice wrote a sequence of words in CamelCase as a string of letters, , having the following properties:
* It is a concatenation of one or more words consisting of English letters.
* All letters in the first word are lowercase.
* For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
* Given , print the number of words in  on a new line.

* For example, s= oneTwoThree . There are 3 words in the string.
 */
/** Test Case */
//var st = "oneTwoThree"; //output - 3
//var st ="saveChangesInTheEditor"; //output - 5
var st = "SaveChangesInTheEditor"; //output - 5
function camelcase(s) {
    var counter = 0;
    for (var i = 0; i < s.length; i++) {
        if (i == 0) {
            if (s.charAt(i) === s.charAt(i).toLowerCase()) {
                counter++;
            }
        }
        if (s.charAt(i) === s.charAt(i).toUpperCase()) {
            counter++;
        }
    }

    return counter;
}

var result = camelcase(st);
console.log(result);