'use strict'
/* Questions:
* Validate if the given array is in zigzag pattern or not.
*/

/* Test cases */
//var arr = [1, 7, 10, 0, -5000, 2500];                 //output - false
//var arr = [-1111, -1, 0, -1, 5000, -2500];            //output - false
//var arr = [-1111, -1, -2, -1, -5000, -2500];          //output - true
//var arr = [0, 1, 0, 1];                               //output - true
//var arr = [0, 1, 0, -1, 0];                           //output - false
//var arr = [0, 1, -2, -1, -5, 'A', 1];                 //output - false
var arr = [-10, -1, -5, 0, -1, -3];                     //output - false
/* ---------- CODE ---------- */
var lvl = 0;
var zigzag = false;
var flag = "";
var up = false;
var down = false;

for (var i = 0; i < arr.length; i++) {
    if (Number.isInteger(arr[i])) { //Check if element of an array is number.
        if (arr[i] < arr[i + 1]) {
            if (i > 0) {
                zigzag = (up && flag === 'U') ? false : true;
                if (!zigzag) {
                    break;
                }
                //expanded fomr of above logic
                // if (up && flag === 'U') {
                //     zigzag = false;
                //     break;
                // }
                // else {
                //     zigzag = true;
                // }
            }
            up = true;
            flag = 'U';
            down = false;
        } else if (arr[i] > arr[i + 1]) {
            if (i > 0) {
                zigzag = (down && flag === 'D') ? false : true;
                if (!zigzag) {
                    break;
                }
                //expanded fomr of above logic
                // if (down && flag === 'D') {
                //     zigzag = false;
                //     break;
                // }
                // else {
                //     zigzag = true;
                // }
            }
            down = true;
            flag = 'D'
            up = false;
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