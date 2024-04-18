var e = function() {
    for (var t, e = [], n = 0; n < 256; n++) {
        t = n;
        for (var r = 0; r < 8; r++)
            t = 1 & t ? 3988292384 ^ t >>> 1 : t >>> 1;
        e[n] = t
    }
    return e
}();

module.exports = function(t, n, r, o) {
    var i = e
      , a = o + r;
    t ^= -1;
    for (var u = o; u < a; u++)
        t = t >>> 8 ^ i[255 & (t ^ n[u])];
    return -1 ^ t
}