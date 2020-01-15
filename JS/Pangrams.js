'use strict'
/**
 * Hacker Rank Question - Pangrams (https://www.hackerrank.com/challenges/pangrams/problem)
 * Roy wanted to increase his typing speed for programming contests. His friend suggested that he type the sentence "The quick brown fox jumps over the lazy dog" repeatedly. This sentence is known as a pangram because it contains every letter of the alphabet.
 * After typing the sentence several times, Roy became bored with it so he started to look for other pangrams.
 * Given a sentence, determine whether it is a pangram. Ignore case.
 */

//var s = "We promptly judged antique ivory buckles for the next prize";  // panagram
//var s = "We promptly judged antique ivory buckles for the prize";  //output - not panagram
var s="qmExzBIJmdELxyOFWv LOCmefk TwPhargKSPEqSxzveiun";  //output - panagram

function pangrams(s) {
    s = s.replace(/ /g, '').toLowerCase();
    var uniq1 = "";

    for (var i = 0; i < s.length; i++) {
        if (uniq1.indexOf(s.charAt(i)) == -1) {
            uniq1 += s[i];
        }
    }

    if (uniq1.length === 26) {
        return "pangram";
    } else {
        return "not pangram";
    }
}

var result = pangrams(s);
console.log(result);

