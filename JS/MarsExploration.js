'use strict'
/** Question - Mars Exploration (https://www.hackerrank.com/challenges/mars-exploration/problem)
 * Sami's spaceship crashed on Mars! She sends a series of SOS messages to Earth for help.
 * Letters in some of the SOS messages are altered by cosmic radiation during transmission.
 * Given the signal received by Earth as a string, s , determine how many letters of Sami's 
 * SOS have been changed by radiation.
 * For example, Earth receives SOSTOT. Sami's original message was SOSSOS.
 * Two of the message characters were changed in transit.
 */

//var msg ='SOSSOSSOS'; //output - 0
var msg = 'SOSSPSSQSSOR'; //output - 3
//var msg ='SOSSOT'; //output - 1
//var msg = 'SOSOOSOSOSOSOSSOSOSOSOSOSOS'  //output - 12
var total_msg = (msg.length) / 3;
function sosMessage(s) {
    var counter = 0;
    var subString = 'SOS';
    for (var i = 0; i < s.length; i++) {
        if (s.charAt(i) !== subString.charAt(i % 3)) {
            counter++;
        }
    }

    return counter;
}
var result = sosMessage(msg);
console.log(result);
