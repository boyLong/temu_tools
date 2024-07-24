
function a(e){
    return typeof e
}

var r, i, o, c, u=function(t) {
    return a(t);
}
c = function(t) {
    var e, n, r, i, o, a;
    return n = (e = t)["lib"],
    r = n["WordArray"],
    i = n["Hasher"],
    o = [],
    a = e["algo"].SHA1 = i["extend"]({
        _doReset: function() {
            this["_hash"] = new r["init"]([1732584193, 4023233417, 2562383102, 271733878, 3285377520]);
        },
        _doProcessBlock: function(t, e) {
            for (var n = this["_hash"]["words"], r = n[0], i = n[1], a = n[2], c = n[3], u = n[4], f = 0; f < 80; f++) {
                if (f < 16)
                    o[f] = 0 | t[e + f];
                else {
                    var x = o[f - 3] ^ o[f - 8] ^ o[f - 14] ^ o[f - 16];
                    o[f] = x << 1 | x >>> 31;
                }
                var d = (r << 5 | r >>> 27) + u + o[f];
                d += f < 20 ? 1518500249 + (i & a | ~i & c) : f < 40 ? 1859775393 + (i ^ a ^ c) : f < 60 ? (i & a | i & c | a & c) - 1894007588 : (i ^ a ^ c) - 899497514,
                u = c,
                c = a,
                a = i << 30 | i >>> 2,
                i = r,
                r = d;
            }
            n[0] = n[0] + r | 0,
            n[1] = n[1] + i | 0,
            n[2] = n[2] + a | 0,
            n[3] = n[3] + c | 0,
            n[4] = n[4] + u | 0;
        },
        _doFinalize: function() {
            var t = this["_data"]
                , e = t["words"]
                , n = 8 * this._nDataBytes
                , r = 8 * t.sigBytes;
            return e[r >>> 5] |= 128 << 24 - r % 32,
            e[14 + (r + 64 >>> 9 << 4)] = Math["floor"](n / 4294967296),
            e[15 + (r + 64 >>> 9 << 4)] = n,
            t["sigBytes"] = 4 * e["length"],
            this._process(),
            this["_hash"];
        },
        clone: function() {
            var t = i["clone"]["call"](this);
            return t["_hash"] = this._hash.clone(),
            t;
        }
    }),
    e.SHA1 = i._createHelper(a),
    e["HmacSHA1"] = i["_createHmacHelper"](a),
    t["SHA1"];
}
module.exports = e = c(require("./0"))
