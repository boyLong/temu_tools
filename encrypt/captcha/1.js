
function a(e){
    return typeof e
}

var r, i, o, c, u=function(t) {
    return a(t);
}
c = function(t) {
    var e, n, r, i, o, a, c;
    return r = (n = (e = t).lib)["Base"],
    i = n["WordArray"],
    a = (o = e.algo).MD5,
    c = o["EvpKDF"] = r["extend"]({
        cfg: r["extend"]({
            keySize: 4,
            hasher: a,
            iterations: 1
        }),
        init: function(t) {
            this["cfg"] = this["cfg"]["extend"](t);
        },
        compute: function(t, e) {
            for (var n = this["cfg"], r = n.hasher.create(), o = i["create"](), a = o["words"], c = n.keySize, u = n["iterations"]; a["length"] < c; ) {
                f && r["update"](f);
                var f = r["update"](t)["finalize"](e);
                r["reset"]();
                for (var x = 1; x < u; x++)
                    f = r["finalize"](f),
                    r.reset();
                o["concat"](f);
            }
            return o.sigBytes = 4 * c,
            o;
        }
    }),
    e["EvpKDF"] = function(t, e, n) {
        return c["create"](n)["compute"](t, e);
    }
    ,
    t.EvpKDF;
}

module.exports = e = c(require("./0"), require("./6"), require("./7")) 