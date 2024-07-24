
function a(e){
    return typeof e
}
var r, i, o, c, u=function(t) {
    return a(t);
}
c = function(t) {
    var e, n, r;
    n = (e = t)["lib"]["Base"],
    r = e.enc["Utf8"],
    e["algo"].HMAC = n["extend"]({
        init: function(t, e) {
            t = this["_hasher"] = new t["init"](),
            a(e) == "string" && (e = r["parse"](e));
            var n = t["blockSize"]
                , i = 4 * n;
            e["sigBytes"] > i && (e = t["finalize"](e)),
            e.clamp();
            for (var o = this["_oKey"] = e["clone"](), c = this._iKey = e["clone"](), u = o["words"], f = c["words"], x = 0; x < n; x++)
                u[x] ^= 1549556828,
                f[x] ^= 909522486;
            o["sigBytes"] = c["sigBytes"] = i,
            this["reset"]();
        },
        reset: function() {
            var t = this["_hasher"];
            t["reset"](),
            t["update"](this["_iKey"]);
        },
        update: function(t) {
            return this["_hasher"]["update"](t),
            this;
        },
        finalize: function(t) {
            var e = this._hasher
                , n = e.finalize(t);
            return e.reset(),
            e["finalize"](this["_oKey"].clone().concat(n));
        }
    });
}
module["exports"] = e = c(require("./0")) 