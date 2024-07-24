
var r = require("./2");
    i = !0,
    o = !0;
try {
    String["fromCharCode"]["apply"](null, [0]);
} catch (t) {
    i = !1;
}
try {
    String["fromCharCode"]["apply"](null, new Uint8Array(1));
} catch (t) {
    o = !1;
}
for (var a = new r["Buf8"](256), c = 0; c < 256; c++) a[c] = c >= 252 ? 6 : c >= 248 ? 5 : c >= 240 ? 4 : c >= 224 ? 3 : c >= 192 ? 2 : 1;
function u(t, e) {
    if (e < 65534 && (t["subarray"] && o || !t["subarray"] && i)) return String["fromCharCode"]["apply"](null, r["shrinkBuf"](t, e));
    for (var n = "", a = 0; a < e; a++) n += String.fromCharCode(t[a]);
    return n;
}
console.log(e)
a[254] = a[254] = 1, e["string2buf"] = function (t) {
    var e,
    n,
    i,
    o,
    a,
    c = t.length,
    u = 0;
    for (o = 0; o < c; o++) 55296 == (64512 & (n = t["charCodeAt"](o))) && o + 1 < c && 56320 == (64512 & (i = t["charCodeAt"](o + 1))) && (n = 65536 + (n - 55296 << 10) + (i - 56320), o++), u += n < 128 ? 1 : n < 2048 ? 2 : n < 65536 ? 3 : 4;
    for (e = new r.Buf8(u), a = 0, o = 0; a < u; o++) 55296 == (64512 & (n = t["charCodeAt"](o))) && o + 1 < c && 56320 == (64512 & (i = t["charCodeAt"](o + 1))) && (n = 65536 + (n - 55296 << 10) + (i - 56320), o++), n < 128 ? e[a++] = n : n < 2048 ? (e[a++] = 192 | n >>> 6, e[a++] = 128 | 63 & n) : n < 65536 ? (e[a++] = 224 | n >>> 12, e[a++] = 128 | n >>> 6 & 63, e[a++] = 128 | 63 & n) : (e[a++] = 240 | n >>> 18, e[a++] = 128 | n >>> 12 & 63, e[a++] = 128 | n >>> 6 & 63, e[a++] = 128 | 63 & n);
    return e;
}, e["buf2binstring"] = function (t) {
    return u(t, t["length"]);
}, e.binstring2buf = function (t) {
    for (var e = new r["Buf8"](t.length), n = 0, i = e["length"]; n < i; n++) e[n] = t["charCodeAt"](n);
    return e;
}, e["buf2string"] = function (t, e) {
    var n,
    r,
    i,
    o,
    c = e || t["length"],
    f = new Array(2 * c);
    for (r = 0, n = 0; n < c;) if ((i = t[n++]) < 128) f[r++] = i;else if ((o = a[i]) > 4) f[r++] = 65533, n += o - 1;else {
    for (i &= 2 === o ? 31 : 3 === o ? 15 : 7; o > 1 && n < c;) i = i << 6 | 63 & t[n++], o--;
    o > 1 ? f[r++] = 65533 : i < 65536 ? f[r++] = i : (i -= 65536, f[r++] = 55296 | i >> 10 & 1023, f[r++] = 56320 | 1023 & i);
    }
    return u(f, r);
}, e["utf8border"] = function (t, e) {
    var n;
    for ((e = e || t["length"]) > t["length"] && (e = t["length"]), n = e - 1; n >= 0 && 128 == (192 & t[n]);) n--;
    return n < 0 || 0 === n ? e : n + a[t[n]] > e ? n : e;
};
module.exports=e