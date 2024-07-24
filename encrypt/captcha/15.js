var r = function () {
    for (var t, e = [], n = 0; n < 256; n++) {
        t = n;
        for (var r = 0; r < 8; r++) t = 1 & t ? 3988292384 ^ t >>> 1 : t >>> 1;
        e[n] = t;
    }
    return e;
}();
module["exports"] = function (t, e, n, i) {
    var o = r,
        a = i + n;
    t ^= -1;
    for (var c = i; c < a; c++) t = t >>> 8 ^ o[255 & (t ^ e[c])];
    return -1 ^ t;
};