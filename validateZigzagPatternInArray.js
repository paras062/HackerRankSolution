'use strict'
/* Questions:
* Validate if the given array is in zigzag pattern or not.
*/

/* Test cases */
//var arr = [1, 7, 10, 0, -5000, 2500];
//var arr = [-1111, -1, 0, -1, 5000, -2500];
//var arr = [-1111, -1, -2, -1, -5000, -2500];
var arr = [0, 1, 0, 1]
//var arr = [0, 1, -2, -1, -5, 'A', 1];
/* ---------- CODE ---------- */
var lvl = 0;
var zigzag = false;

function checkLvl(x) {
    if (x > 1 || x < -1) {
        return true;
    }
    else {
        return false;
    }
}
for (var i = 0; i < arr.length; i++) {
    if (Number.isInteger(arr[i])) { //Check if element of an array is number.
        if (arr[i] > arr[i + 1]) {
            lvl++;
            if (checkLvl(lvl)) {
                zigzag = false;
                break;
            }
            zigzag = true;
        } else if (arr[i] < arr[i + 1]) {
            lvl--;
            if (checkLvl(lvl)) {
                zigzag = false;
                break;
            }
            zigzag = true;
        } else if (arr[i] === arr[i + 1]) {
            zigzag = false;
            break;
        }
    } else {
        zigzag = false;
        break;
    }
}
console.log(zigzag);