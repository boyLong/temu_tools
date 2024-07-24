function oe(e, t) {
    var r = Object.keys(e);
    if (Object.getOwnPropertySymbols) {
        var n = Object.getOwnPropertySymbols(e);
        t && (n = n.filter((function(t) {
            return Object.getOwnPropertyDescriptor(e, t).enumerable
        }
        ))),
        r.push.apply(r, n)
    }
    return r
}
function o(e, t, n) {
    return t in e ? Object.defineProperty(e, t, {
        value: n,
        enumerable: !0,
        configurable: !0,
        writable: !0
    }) : e[t] = n,
    e
}
// o={}
var ce = "bN3%cH2$H1@*jCo$"
, le = "gl3-w^dN)3#h6E1%";
function se(e) {
    var t = e.serverTime
      , r = e.salt;
    var s = function d(e) {
        for (var t = 1; t < arguments.length; t++) {
            var r = null != arguments[t] ? arguments[t] : {};
            t % 2 ? oe(Object(r), !0).forEach((function(t) {
                o(e, t, r[t])
            }
            )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(r)) : oe(Object(r)).forEach((function(t) {
                Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(r, t))
            }
            ))
        }
        return e
    }({
        server_time: t
    }, function(e) {
        var t = {
            aes_key: ce,
            aes_iv: le
        };
        if (!e || 9 !== e.length)
            return t;
        var r = e.slice(0, 1)
          , n = e.slice(1)
          , i = n.slice(0, 4)
          , a = n.slice(4)
          , o = a.split("")
          , c = (["a", "b"].includes(r) ? ce : le).slice(0, 8)
          , l = ["a", "b"].includes(r) ? "aes_key" : "aes_iv"
          , s = "";
        switch (r) {
        case "a":
        case "c":
            t[l] = c + n;
            break;
        case "b":
        case "d":
            for (var u = 0; u < 4; u++)
                s += o[i[u]];
            t[l] = c + s + a
        }
        return t
    }(r) || {})
    return s
}
module.exports = se
