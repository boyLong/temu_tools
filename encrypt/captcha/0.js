
function a(e){
    return typeof e
}

var r, i, o, c, u=function(t) {
    return a(t);
}
c = function() {
    var t, e, n, r, i, o, c, u, f, x, d, l, h = h || (t = Math,
    e = Object["create"] || function() {
        function t() {}
        return function(e) {
            var n;
            return t["prototype"] = e,
            n = new t(),
            t["prototype"] = null,
            n;
        }
        ;
    }(),
    r = (n = {})["lib"] = {},
    i = r["Base"] = {
        extend: function(t) {
            var n = e(this);
            return t && n["mixIn"](t),
            n["hasOwnProperty"]("init") && this["init"] !== n["init"] || (n["init"] = function() {
                n.$super.init["apply"](this, arguments);
            }
            ),
            n["init"]["prototype"] = n,
            n["$super"] = this,
            n;
        },
        create: function() {
            var t = this["extend"]();
            return t["init"]["apply"](t, arguments),
            t;
        },
        init: function() {},
        mixIn: function(t) {
            for (var e in t)
                t["hasOwnProperty"](e) && (this[e] = t[e]);
            t["hasOwnProperty"]("toString") && (this.toString = t["toString"]);
        },
        clone: function() {
            return this["init"]["prototype"]["extend"](this);
        }
    },
    o = r["WordArray"] = i["extend"]({
        init: function(t, e) {
            t = this.words = t || [],
            this["sigBytes"] = null != e ? e : 4 * t["length"];
        },
        toString: function(t) {
            return (t || u).stringify(this);
        },
        concat: function(t) {
            var e = this["words"]
              , n = t["words"]
              , r = this["sigBytes"]
              , i = t["sigBytes"];
            if (this["clamp"](),
            r % 4)
                for (var o = 0; o < i; o++) {
                    var a = n[o >>> 2] >>> 24 - o % 4 * 8 & 255;
                    e[r + o >>> 2] |= a << 24 - (r + o) % 4 * 8;
                }
            else
                for (o = 0; o < i; o += 4)
                    e[r + o >>> 2] = n[o >>> 2];
            return this["sigBytes"] += i,
            this;
        },
        clamp: function() {
            var e = this.words
              , n = this.sigBytes;
            e[n >>> 2] &= 4294967295 << 32 - n % 4 * 8,
            e["length"] = t.ceil(n / 4);
        },
        clone: function() {
            var t = i["clone"].call(this);
            return t["words"] = this["words"]["slice"](0),
            t;
        },
        random: function(e) {
            for (var n, r = [], i = function(e) {
                var n = 987654321;
                return function() {
                    var r = ((n = 36969 * (65535 & n) + (n >> 16) & 4294967295) << 16) + (e = 18e3 * (65535 & e) + (e >> 16) & 4294967295) & 4294967295;
                    return r /= 4294967296,
                    (r += .5) * (t["random"]() > .5 ? 1 : -1);
                }
                ;
            }, a = 0; a < e; a += 4) {
                var c = i(4294967296 * (n || t["random"]()));
                n = 987654071 * c(),
                r["push"](4294967296 * c() | 0);
            }
            return new o["init"](r,e);
        }
    }),
    c = n["enc"] = {},
    u = c["Hex"] = {
        stringify: function(t) {
            for (var e = t["words"], n = t["sigBytes"], r = [], i = 0; i < n; i++) {
                var o = e[i >>> 2] >>> 24 - i % 4 * 8 & 255;
                r["push"]((o >>> 4)["toString"](16)),
                r["push"]((15 & o)["toString"](16));
            }
            return r["join"]("");
        },
        parse: function(t) {
            for (var e = t.length, n = [], r = 0; r < e; r += 2)
                n[r >>> 3] |= parseInt(t["substr"](r, 2), 16) << 24 - r % 8 * 4;
            return new o.init(n,e / 2);
        }
    },
    f = c["Latin1"] = {
        stringify: function(t) {
            for (var e = t.words, n = t.sigBytes, r = [], i = 0; i < n; i++) {
                var o = e[i >>> 2] >>> 24 - i % 4 * 8 & 255;
                r.push(String["fromCharCode"](o));
            }
            return r["join"]("");
        },
        parse: function(t) {
            for (var e = t["length"], n = [], r = 0; r < e; r++)
                n[r >>> 2] |= (255 & t["charCodeAt"](r)) << 24 - r % 4 * 8;
            return new o["init"](n,e);
        }
    },
    x = c["Utf8"] = {
        stringify: function(t) {
            try {
                return decodeURIComponent(escape(f["stringify"](t)));
            } catch (t) {
                throw new Error("Malformed UTF-8 data");
            }
        },
        parse: function(t) {
            return f["parse"](unescape(encodeURIComponent(t)));
        }
    },
    d = r["BufferedBlockAlgorithm"] = i["extend"]({
        reset: function() {
            this["_data"] = new o["init"](),
            this["_nDataBytes"] = 0;
        },
        _append: function(t) {
            a(t) == "string" && (t = x["parse"](t)),
            this["_data"].concat(t),
            this._nDataBytes += t["sigBytes"];
        },
        _process: function(e) {
            var n = this._data
              , r = n.words
              , i = n["sigBytes"]
              , a = this["blockSize"]
              , c = i / (4 * a)
              , u = (c = e ? t["ceil"](c) : t["max"]((0 | c) - this._minBufferSize, 0)) * a
              , f = t.min(4 * u, i);
            if (u) {
                for (var x = 0; x < u; x += a)
                    this["_doProcessBlock"](r, x);
                var d = r["splice"](0, u);
                n["sigBytes"] -= f;
            }
            return new o["init"](d,f);
        },
        clone: function() {
            var t = i["clone"].call(this);
            return t._data = this._data["clone"](),
            t;
        },
        _minBufferSize: 0
    }),
    r["Hasher"] = d["extend"]({
        cfg: i["extend"](),
        init: function(t) {
            this["cfg"] = this["cfg"]["extend"](t),
            this["reset"]();
        },
        reset: function() {
            d["reset"].call(this),
            this["_doReset"]();
        },
        update: function(t) {
            return this["_append"](t),
            this["_process"](),
            this;
        },
        finalize: function(t) {
            return t && this["_append"](t),
            this["_doFinalize"]();
        },
        blockSize: 16,
        _createHelper: function(t) {
            return function(e, n) {
                return new t["init"](n)["finalize"](e);
            }
            ;
        },
        _createHmacHelper: function(t) {
            return function(e, n) {
                return new l["HMAC"]["init"](t,n)["finalize"](e);
            }
            ;
        }
    }),
    l = n["algo"] = {},
    n);
    return h;
}
,
module["exports"] = e = c()
console.log(e)