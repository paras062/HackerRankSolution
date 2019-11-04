'use strict'
/** Questions: Hacker Rank Drawing Books Problem - https://www.hackerrank.com/challenges/drawing-book/problem
 * Brie’s Drawing teacher asks her class to open their books to a page number. Brie can either start turning pages from 
 * the front of the book or from the back of the book. She always turns pages one at a time. When she opens the book, 
 * page  is always on the right side:
 * 
 * When she flips page , she sees pages  and . Each page except the last page will always be printed on both sides. 
 * The last page may only be printed on the front, given the length of the book. If the book is  pages long, and she 
 * wants to turn to page , what is the minimum number of pages she will turn? She can start at the beginning or the 
 * end of the book.
 * Given  and , find and print the minimum number of pages Brie must turn in order to arrive at page .
 */
function solve(n, p) {
    function stripDecimal(x) {
        return x | 0; //Using Bitwise Operator
    }
    var fromFront = p;
    var fromBack = n;
    if (n % 2 == 0) {
        fromBack = n + 1;
    }
    var answer = Math.min(fromFront / 2, (fromBack - p) / 2);
    return stripDecimal(answer);

}
var n = 5; //total pages number in book
var p = 4; //page to open
var result = solve(n, p);
console.log(result);