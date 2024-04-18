"use strict";
var r = require("./24236.js")
    , o = !0
    , i = !0;
try {
    String.fromCharCode.apply(null, [0])
} catch (t) {
    o = !1
}
try {
    String.fromCharCode.apply(null, new Uint8Array(1))
} catch (t) {
    i = !1
}
for (var a = new r.Buf8(256), u = 0; u < 256; u++)
    a[u] = u >= 252 ? 6 : u >= 248 ? 5 : u >= 240 ? 4 : u >= 224 ? 3 : u >= 192 ? 2 : 1;
function s(t, e) {
    if (e < 65534 && (t.subarray && i || !t.subarray && o))
        return String.fromCharCode.apply(null, r.shrinkBuf(t, e));
    for (var n = "", a = 0; a < e; a++)
        n += String.fromCharCode(t[a]);
    return n
}
a[254] = a[254] = 1,
e.string2buf = function(t) {
    var e, n, o, i, a, u = t.length, s = 0;
    for (i = 0; i < u; i++)
        55296 == (64512 & (n = t.charCodeAt(i))) && i + 1 < u && 56320 == (64512 & (o = t.charCodeAt(i + 1))) && (n = 65536 + (n - 55296 << 10) + (o - 56320),
        i++),
        s += n < 128 ? 1 : n < 2048 ? 2 : n < 65536 ? 3 : 4;
    for (e = new r.Buf8(s),
    a = 0,
    i = 0; a < s; i++)
        55296 == (64512 & (n = t.charCodeAt(i))) && i + 1 < u && 56320 == (64512 & (o = t.charCodeAt(i + 1))) && (n = 65536 + (n - 55296 << 10) + (o - 56320),
        i++),
        n < 128 ? e[a++] = n : n < 2048 ? (e[a++] = 192 | n >>> 6,
        e[a++] = 128 | 63 & n) : n < 65536 ? (e[a++] = 224 | n >>> 12,
        e[a++] = 128 | n >>> 6 & 63,
        e[a++] = 128 | 63 & n) : (e[a++] = 240 | n >>> 18,
        e[a++] = 128 | n >>> 12 & 63,
        e[a++] = 128 | n >>> 6 & 63,
        e[a++] = 128 | 63 & n);
    return e
}
,
e.buf2binstring = function(t) {
    return s(t, t.length)
}
,
e.binstring2buf = function(t) {
    for (var e = new r.Buf8(t.length), n = 0, o = e.length; n < o; n++)
        e[n] = t.charCodeAt(n);
    return e
}
,
e.buf2string = function(t, e) {
    var n, r, o, i, u = e || t.length, c = new Array(2 * u);
    for (r = 0,
    n = 0; n < u; )
        if ((o = t[n++]) < 128)
            c[r++] = o;
        else if ((i = a[o]) > 4)
            c[r++] = 65533,
            n += i - 1;
        else {
            for (o &= 2 === i ? 31 : 3 === i ? 15 : 7; i > 1 && n < u; )
                o = o << 6 | 63 & t[n++],
                i--;
            i > 1 ? c[r++] = 65533 : o < 65536 ? c[r++] = o : (o -= 65536,
            c[r++] = 55296 | o >> 10 & 1023,
            c[r++] = 56320 | 1023 & o)
        }
    return s(c, r)
}
,
e.utf8border = function(t, e) {
    var n;
    for ((e = e || t.length) > t.length && (e = t.length),
    n = e - 1; n >= 0 && 128 == (192 & t[n]); )
        n--;
    return n < 0 || 0 === n ? e : n + a[t[n]] > e ? n : e
}
module.exports = e