var n = "undefined" != typeof Uint8Array && "undefined" != typeof Uint16Array && "undefined" != typeof Int32Array;
function r(t, e) {
    return Object.prototype.hasOwnProperty.call(t, e)
}
e = {}
e.assign = function(t) {
    for (var e = Array.prototype.slice.call(arguments, 1); e.length; ) {
        var n = e.shift();
        if (n) {
            if ("object" != typeof n)
                throw new TypeError(n + "must be non-object");
            for (var o in n)
                r(n, o) && (t[o] = n[o])
        }
    }
    return t
}
,
e.shrinkBuf = function(t, e) {
    return t.length === e ? t : t.subarray ? t.subarray(0, e) : (t.length = e,
    t)
}
;
var o = {
    arraySet: function(t, e, n, r, o) {
        if (e.subarray && t.subarray)
            t.set(e.subarray(n, n + r), o);
        else
            for (var i = 0; i < r; i++)
                t[o + i] = e[n + i]
    },
    flattenChunks: function(t) {
        var e, n, r, o, i, a;
        for (r = 0,
        e = 0,
        n = t.length; e < n; e++)
            r += t[e].length;
        for (a = new Uint8Array(r),
        o = 0,
        e = 0,
        n = t.length; e < n; e++)
            i = t[e],
            a.set(i, o),
            o += i.length;
        return a
    }
}
    , i = {
    arraySet: function(t, e, n, r, o) {
        for (var i = 0; i < r; i++)
            t[o + i] = e[n + i]
    },
    flattenChunks: function(t) {
        return [].concat.apply([], t)
    }
};
e.setTyped = function(t) {
    t ? (e.Buf8 = Uint8Array,
    e.Buf16 = Uint16Array,
    e.Buf32 = Int32Array,
    e.assign(e, o)) : (e.Buf8 = Array,
    e.Buf16 = Array,
    e.Buf32 = Array,
    e.assign(e, i))
}
,
e.setTyped(n)
module.exports = e
