'use strict'
var bill = [3, 10, 2, 9]
var k = 1; //index
var b = 7;
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
    console.log(annaBill);
}