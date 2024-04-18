
"use strict";
var r = require("./30405.js")
    , o =require("./24236.js")
    , i = require("./29373.js")
    , a = require("./48898.js")
    , u = require("./62292.js")
    , s = Object.prototype.toString
    , c = 0
    , l = -1
    , f = 0
    , p = 8;
e = {}
function d(t) {
    if (!(this instanceof d))
        return new d(t);
    this.options = o.assign({
        level: l,
        method: p,
        chunkSize: 16384,
        windowBits: 15,
        memLevel: 8,
        strategy: f,
        to: ""
    }, t || {});
    var e = this.options;
    e.raw && e.windowBits > 0 ? e.windowBits = -e.windowBits : e.gzip && e.windowBits > 0 && e.windowBits < 16 && (e.windowBits += 16),
    this.err = 0,
    this.msg = "",
    this.ended = !1,
    this.chunks = [],
    this.strm = new u,
    this.strm.avail_out = 0;
    var n = r.deflateInit2(this.strm, e.level, e.method, e.windowBits, e.memLevel, e.strategy);
    if (n !== c)
        throw new Error(a[n]);
    if (e.header && r.deflateSetHeader(this.strm, e.header),
    e.dictionary) {
        var h;
        if (h = "string" == typeof e.dictionary ? i.string2buf(e.dictionary) : "[object ArrayBuffer]" === s.call(e.dictionary) ? new Uint8Array(e.dictionary) : e.dictionary,
        (n = r.deflateSetDictionary(this.strm, h)) !== c)
            throw new Error(a[n]);
        this._dict_set = !0
    }
}
function h(t, e) {
    var n = new d(e);
    if (n.push(t, !0),
    n.err)
        throw n.msg || a[n.err];
    return n.result
}
d.prototype.push = function(t, e) {
    var n, a, u = this.strm, l = this.options.chunkSize;
    if (this.ended)
        return !1;
    a = e === ~~e ? e : !0 === e ? 4 : 0,
    "string" == typeof t ? u.input = i.string2buf(t) : "[object ArrayBuffer]" === s.call(t) ? u.input = new Uint8Array(t) : u.input = t,
    u.next_in = 0,
    u.avail_in = u.input.length;
    do {
        if (0 === u.avail_out && (u.output = new o.Buf8(l),
        u.next_out = 0,
        u.avail_out = l),
        1 !== (n = r.deflate(u, a)) && n !== c)
            return this.onEnd(n),
            this.ended = !0,
            !1;
        0 !== u.avail_out && (0 !== u.avail_in || 4 !== a && 2 !== a) || ("string" === this.options.to ? this.onData(i.buf2binstring(o.shrinkBuf(u.output, u.next_out))) : this.onData(o.shrinkBuf(u.output, u.next_out)))
    } while ((u.avail_in > 0 || 0 === u.avail_out) && 1 !== n);
    return 4 === a ? (n = r.deflateEnd(this.strm),
    this.onEnd(n),
    this.ended = !0,
    n === c) : 2 !== a || (this.onEnd(c),
    u.avail_out = 0,
    !0)
}
,
d.prototype.onData = function(t) {
    this.chunks.push(t)
}
,
d.prototype.onEnd = function(t) {
    t === c && ("string" === this.options.to ? this.result = this.chunks.join("") : this.result = o.flattenChunks(this.chunks)),
    this.chunks = [],
    this.err = t,
    this.msg = this.strm.msg
}
,
e.Deflate = d,
e.deflate = h,
e.deflateRaw = function(t, e) {
    return (e = e || {}).raw = !0,
    h(t, e)
}
,
e.gzip = function(t, e) {
    return (e = e || {}).gzip = !0,
    h(t, e)
}
module.exports = e

console.log(e.deflate("").toString())