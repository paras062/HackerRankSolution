'use strict';
        //var s = [1, 2, 1, 3, 2];
        // var s = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1];
        // var d = 18;
        // var m = 7;

        var s = [4];
        var d = 4;
        var m = 1;
        var result = 0;
        for (var i = 0; i < s.length - m + 1; i++) {
            var sum = 0;
            for (var j = 0; j < m; j++) {
                sum = sum + s[i + j]
            }
            if (sum === d) {
                result++;
            }
        }

        console.log(result);