module.exports = function(t, e, n, r) {
    for (var o = 65535 & t | 0, i = t >>> 16 & 65535 | 0, a = 0; 0 !== n; ) {
        n -= a = n > 2e3 ? 2e3 : n;
        do {
            i = i + (o = o + e[r++] | 0) | 0
        } while (--a);
        o %= 65521,
        i %= 65521
    }
    return o | i << 16 | 0
}