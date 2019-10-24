'use strict'
/*
* Question: https://www.hackerrank.com/challenges/bon-appetit/problem
* Anna and Brian are sharing a meal at a restuarant and they agree to split the bill equally. 
* Brian wants to order something that Anna is allergic to though, and they agree that 
* Anna won't pay for that item. Brian gets the check and calculates Anna's portion. 
* You must determine if his calculation is correct.
*/
/**
 * Test Case:
 * array = [3, 10, 2, 9]
 * k= 1
 * b =12
 */
var bill = [3, 10, 2, 9]
var k = 1; //index, item Anna refused to eat
var b = 7; // money Brian charged Anna
var bActual = 0;
var brianBill = 0;
var annaBill = 0;
bill.splice(k, 1);
for (var i = 0; i < bill.length; i++) {
    brianBill = brianBill + bill[i];
}
bActual = brianBill / 2;
if (b === bActual) {
    console.log("Bon Appetit")
}
else {
    //Amount Refund to Anna
    annaBill = b - bActual;
    console.log(annaBill)
}