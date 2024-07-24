function a(e){
    return typeof e
}
var r = function (t) {
    return typeof t;
    },
    i = "undefined" != typeof Uint8Array && ("undefined" == typeof Uint16Array ? "undefined" : a(Uint16Array)) !== "undefined" && "undefined" != typeof Int32Array;
    e = {}
    e["assign"] = function (t) {
    for (var e, n, i = Array["prototype"]["slice"].call(arguments, 1); i["length"];) {
    var o = i["shift"]();
    if (o) {
        if ((a(o) === "undefined" ? "undefined" : r(o)) !== "object") throw new TypeError(o + "must be non-object");
        for (var c in o) e = o, n = c, Object["prototype"]["hasOwnProperty"]["call"](e, n) && (t[c] = o[c]);
    }
    }
    return t;
}, e["shrinkBuf"] = function (t, e) {
    return t["length"] === e ? t : t["subarray"] ? t.subarray(0, e) : (t.length = e, t);
};
var o = {
    arraySet: function (t, e, n, r, i) {
        if (e["subarray"] && t.subarray) t["set"](e["subarray"](n, n + r), i);else for (var o = 0; o < r; o++) t[i + o] = e[n + o];
    },
    flattenChunks: function (t) {
        var e, n, r, i, o, a;
        for (r = 0, e = 0, n = t["length"]; e < n; e++) r += t[e].length;
        for (a = new Uint8Array(r), i = 0, e = 0, n = t["length"]; e < n; e++) o = t[e], a["set"](o, i), i += o.length;
        return a;
    }
    },
    c = {
    arraySet: function (t, e, n, r, i) {
        for (var o = 0; o < r; o++) t[i + o] = e[n + o];
    },
    flattenChunks: function (t) {
        return []["concat"]["apply"]([], t);
    }
    };
e["setTyped"] = function (t) {
    t ? (e["Buf8"] = Uint8Array, e["Buf16"] = Uint16Array, e.Buf32 = Int32Array, e["assign"](e, o)) : (e["Buf8"] = Array, e["Buf16"] = Array, e["Buf32"] = Array, e["assign"](e, c));
}, e["setTyped"](i);

module.exports = e