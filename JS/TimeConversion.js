'use strict'
/** Hacker Rank Problem - Time Conversion (https://www.hackerrank.com/challenges/time-conversion/problem)
 * Given a time in -hour AM/PM format, convert it to military (24-hour) time.
 * Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. 
 * Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
 */
/** Test CASES
 * Input - 07:05:45PM - Output - 19:05:45
 * Input - 12:40:22AM - Output - 00:40:22
 * Input - 06:40:03AM - Output - 06:40:03
 * Input - 12:45:54PM - Output - 12:45:54
 * Input - 04:59:59AM - Output - 04:59:59
 */
var time = "07:05:45PM";

/** Time Conversion Method */
function timeConversion(s) {
    
    var hours = Number(s.match(/^(\d+)/)[1]);
    var minutes = Number(s.match(/:(\d+)/)[1]);
    var seconds = Number(s.match(/:(\d+):(\d+)/)[2]);
    var timeFormat = s.match(/:(\d+):(\d+)(\w+)/)[3];
    var militaryTime = "";

    if (timeFormat === "PM") {
        if (hours < 12) {
            hours = hours + 12;
        }
    }
    else if (timeFormat === "AM") {
        if (hours === 12) {
            hours = 0;
        }
        if (hours < 10) {
            hours = '0' + hours;
        }
    }
        if (minutes < 10) {
            minutes = '0' + minutes;
        }
        if (seconds < 10) {
            seconds = '0' + seconds;
        }
    militaryTime = hours + ':' + minutes + ':' + seconds;
    return militaryTime;
}

var result = timeConversion(time);
console.log(result);