'user strict'
/**
 * Question - https://www.hackerrank.com/challenges/counting-valleys/problem
 * Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like 
 * topography. During his last hike he took exactly  steps. For every step he took, he noted if it was an 
 * uphill, , or a downhill,  step. Gary's hikes start and end at sea level and each step up or down represents a  
 * unit change in altitude. We define the following terms:
 */
/**
 * Test Case
 * var s = ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U'];
 * var s = ['D', 'D', 'U', 'U', 'U', 'U', 'D', 'D'];
 */
var s = ['D', 'D', 'U', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'D'];
var lvl = 0; //sea level
var v = 0; //valley
var step = "";
for (var i = 0; i < s.length; i++) {
    if (s[i] == 'D') {
        lvl--;
    } else if (s[i] == 'U') {
        lvl++;
    }
    step = s[i];
    if (lvl === 0 && step === 'U') {
        v++;
    }
}
console.log(v);