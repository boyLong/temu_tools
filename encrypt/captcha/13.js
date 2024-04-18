var r = require("./2");
function i(t) {
    for (var e = t["length"]; --e >= 0; )
        t[e] = 0;
}
var o = 256
  , a = o + 1 + 29
  , c = 30
  , u = 19
  , f = 2 * a + 1
  , x = 15
  , d = 16
  , l = 256
  , h = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 0]
  , v = [0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13]
  , p = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 7]
  , y = [16, 17, 18, 0, 8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15]
  , m = new Array(2 * (a + 2));
i(m);
var b = new Array(60);
i(b);
var g = new Array(512);
i(g);
var w = new Array(256);
i(w);
var _ = new Array(29);
i(_);
var S, k, E, O = new Array(c);
function I(t, e, n, r, i) {
    this["static_tree"] = t,
    this.extra_bits = e,
    this["extra_base"] = n,
    this["elems"] = r,
    this["max_length"] = i,
    this["has_stree"] = t && t.length;
}
function P(t, e) {
    this.dyn_tree = t,
    this["max_code"] = 0,
    this["stat_desc"] = e;
}
function R(t) {
    return t < 256 ? g[t] : g[256 + (t >>> 7)];
}
function B(t, e) {
    t.pending_buf[t["pending"]++] = 255 & e,
    t["pending_buf"][t.pending++] = e >>> 8 & 255;
}
function T(t, e, n) {
    t["bi_valid"] > d - n ? (t.bi_buf |= e << t["bi_valid"] & 65535,
    B(t, t["bi_buf"]),
    t["bi_buf"] = e >> d - t["bi_valid"],
    t["bi_valid"] += n - d) : (t.bi_buf |= e << t["bi_valid"] & 65535,
    t["bi_valid"] += n);
}
function C(t, e, n) {
    T(t, n[2 * e], n[2 * e + 1]);
}
function z(t, e) {
    var n = 0;
    do {
        n |= 1 & t,
        t >>>= 1,
        n <<= 1;
    } while (--e > 0);
    return n >>> 1;
}
function A(t, e, n) {
    var r, i, o = new Array(x + 1), a = 0;
    for (r = 1; r <= x; r++)
        o[r] = a = a + n[r - 1] << 1;
    for (i = 0; i <= e; i++) {
        var c = t[2 * i + 1];
        0 !== c && (t[2 * i] = z(o[c]++, c));
    }
}
function j(t) {
    var e;
    for (e = 0; e < a; e++)
        t["dyn_ltree"][2 * e] = 0;
    for (e = 0; e < c; e++)
        t["dyn_dtree"][2 * e] = 0;
    for (e = 0; e < u; e++)
        t["bl_tree"][2 * e] = 0;
    t.dyn_ltree[2 * l] = 1,
    t["opt_len"] = t["static_len"] = 0,
    t.last_lit = t["matches"] = 0;
}
function F(t) {
    t["bi_valid"] > 8 ? B(t, t.bi_buf) : t.bi_valid > 0 && (t.pending_buf[t["pending"]++] = t["bi_buf"]),
    t.bi_buf = 0,
    t["bi_valid"] = 0;
}
function M(t, e, n, r) {
    var i = 2 * e
      , o = 2 * n;
    return t[i] < t[o] || t[i] === t[o] && r[e] <= r[n];
}
function D(t, e, n) {
    for (var r = t["heap"][n], i = n << 1; i <= t.heap_len && (i < t["heap_len"] && M(e, t["heap"][i + 1], t["heap"][i], t["depth"]) && i++,
    !M(e, r, t["heap"][i], t.depth)); )
        t["heap"][n] = t["heap"][i],
        n = i,
        i <<= 1;
    t["heap"][n] = r;
}
function L(t, e, n) {
    var r, i, a, c, u = 0;
    if (0 !== t.last_lit)
        do {
            r = t.pending_buf[t["d_buf"] + 2 * u] << 8 | t["pending_buf"][t["d_buf"] + 2 * u + 1],
            i = t["pending_buf"][t.l_buf + u],
            u++,
            0 === r ? C(t, i, e) : (C(t, (a = w[i]) + o + 1, e),
            0 !== (c = h[a]) && T(t, i -= _[a], c),
            C(t, a = R(--r), n),
            0 !== (c = v[a]) && T(t, r -= O[a], c));
        } while (u < t["last_lit"]);
    C(t, l, e);
}
function Z(t, e) {
    var n, r, i, o = e["dyn_tree"], a = e["stat_desc"]["static_tree"], c = e["stat_desc"]["has_stree"], u = e["stat_desc"]["elems"], d = -1;
    for (t["heap_len"] = 0,
    t.heap_max = f,
    n = 0; n < u; n++)
        0 !== o[2 * n] ? (t.heap[++t["heap_len"]] = d = n,
        t["depth"][n] = 0) : o[2 * n + 1] = 0;
    for (; t["heap_len"] < 2; )
        o[2 * (i = t["heap"][++t["heap_len"]] = d < 2 ? ++d : 0)] = 1,
        t["depth"][i] = 0,
        t.opt_len--,
        c && (t["static_len"] -= a[2 * i + 1]);
    for (e["max_code"] = d,
    n = t.heap_len >> 1; n >= 1; n--)
        D(t, o, n);
    i = u;
    do {
        n = t.heap[1],
        t["heap"][1] = t.heap[t["heap_len"]--],
        D(t, o, 1),
        r = t.heap[1],
        t.heap[--t["heap_max"]] = n,
        t.heap[--t.heap_max] = r,
        o[2 * i] = o[2 * n] + o[2 * r],
        t["depth"][i] = (t["depth"][n] >= t["depth"][r] ? t["depth"][n] : t.depth[r]) + 1,
        o[2 * n + 1] = o[2 * r + 1] = i,
        t["heap"][1] = i++,
        D(t, o, 1);
    } while (t["heap_len"] >= 2);
    t["heap"][--t["heap_max"]] = t.heap[1],
    function(t, e) {
        var n, r, i, o, a, c, u = e["dyn_tree"], d = e["max_code"], l = e["stat_desc"]["static_tree"], h = e.stat_desc.has_stree, v = e["stat_desc"]["extra_bits"], p = e["stat_desc"]["extra_base"], y = e["stat_desc"]["max_length"], m = 0;
        for (o = 0; o <= x; o++)
            t["bl_count"][o] = 0;
        for (u[2 * t["heap"][t["heap_max"]] + 1] = 0,
        n = t.heap_max + 1; n < f; n++)
            (o = u[2 * u[2 * (r = t["heap"][n]) + 1] + 1] + 1) > y && (o = y,
            m++),
            u[2 * r + 1] = o,
            r > d || (t.bl_count[o]++,
            a = 0,
            r >= p && (a = v[r - p]),
            c = u[2 * r],
            t["opt_len"] += c * (o + a),
            h && (t["static_len"] += c * (l[2 * r + 1] + a)));
        if (0 !== m) {
            do {
                for (o = y - 1; 0 === t.bl_count[o]; )
                    o--;
                t["bl_count"][o]--,
                t.bl_count[o + 1] += 2,
                t["bl_count"][y]--,
                m -= 2;
            } while (m > 0);
            for (o = y; 0 !== o; o--)
                for (r = t["bl_count"][o]; 0 !== r; )
                    (i = t["heap"][--n]) > d || (u[2 * i + 1] !== o && (t["opt_len"] += (o - u[2 * i + 1]) * u[2 * i],
                    u[2 * i + 1] = o),
                    r--);
        }
    }(t, e),
    A(o, d, t["bl_count"]);
}
function N(t, e, n) {
    var r, i, o = -1, a = e[1], c = 0, u = 7, f = 4;
    for (0 === a && (u = 138,
    f = 3),
    e[2 * (n + 1) + 1] = 65535,
    r = 0; r <= n; r++)
        i = a,
        a = e[2 * (r + 1) + 1],
        ++c < u && i === a || (c < f ? t.bl_tree[2 * i] += c : 0 !== i ? (i !== o && t["bl_tree"][2 * i]++,
        t["bl_tree"][32]++) : c <= 10 ? t.bl_tree[34]++ : t["bl_tree"][36]++,
        c = 0,
        o = i,
        0 === a ? (u = 138,
        f = 3) : i === a ? (u = 6,
        f = 3) : (u = 7,
        f = 4));
}
function U(t, e, n) {
    var r, i, o = -1, a = e[1], c = 0, u = 7, f = 4;
    for (0 === a && (u = 138,
    f = 3),
    r = 0; r <= n; r++)
        if (i = a,
        a = e[2 * (r + 1) + 1],
        !(++c < u && i === a)) {
            if (c < f)
                do {
                    C(t, i, t["bl_tree"]);
                } while (0 != --c);
            else
                0 !== i ? (i !== o && (C(t, i, t["bl_tree"]),
                c--),
                C(t, 16, t["bl_tree"]),
                T(t, c - 3, 2)) : c <= 10 ? (C(t, 17, t.bl_tree),
                T(t, c - 3, 3)) : (C(t, 18, t["bl_tree"]),
                T(t, c - 11, 7));
            c = 0,
            o = i,
            0 === a ? (u = 138,
            f = 3) : i === a ? (u = 6,
            f = 3) : (u = 7,
            f = 4);
        }
}
i(O);
var V = !1;
function H(t, e, n, i) {
    var o, a, c;
    T(t, 0 + (i ? 1 : 0), 3),
    a = e,
    c = n,
    F(o = t),
    B(o, c),
    B(o, ~c),
    r["arraySet"](o["pending_buf"], o["window"], a, c, o.pending),
    o.pending += c;
}
e["_tr_init"] = function(t) {
    V || (function() {
        var t, e, n, r, i, f = new Array(x + 1);
        for (n = 0,
        r = 0; r < 28; r++)
            for (_[r] = n,
            t = 0; t < 1 << h[r]; t++)
                w[n++] = r;
        for (w[n - 1] = r,
        i = 0,
        r = 0; r < 16; r++)
            for (O[r] = i,
            t = 0; t < 1 << v[r]; t++)
                g[i++] = r;
        for (i >>= 7; r < c; r++)
            for (O[r] = i << 7,
            t = 0; t < 1 << v[r] - 7; t++)
                g[256 + i++] = r;
        for (e = 0; e <= x; e++)
            f[e] = 0;
        for (t = 0; t <= 143; )
            m[2 * t + 1] = 8,
            t++,
            f[8]++;
        for (; t <= 255; )
            m[2 * t + 1] = 9,
            t++,
            f[9]++;
        for (; t <= 279; )
            m[2 * t + 1] = 7,
            t++,
            f[7]++;
        for (; t <= 287; )
            m[2 * t + 1] = 8,
            t++,
            f[8]++;
        for (A(m, a + 1, f),
        t = 0; t < c; t++)
            b[2 * t + 1] = 5,
            b[2 * t] = z(t, 5);
        S = new I(m,h,o + 1,a,x),
        k = new I(b,v,0,c,x),
        E = new I(new Array(0),p,0,u,7);
    }(),
    V = !0),
    t["l_desc"] = new P(t["dyn_ltree"],S),
    t["d_desc"] = new P(t["dyn_dtree"],k),
    t["bl_desc"] = new P(t.bl_tree,E),
    t["bi_buf"] = 0,
    t["bi_valid"] = 0,
    j(t);
}
,
e["_tr_stored_block"] = H,
e["_tr_flush_block"] = function(t, e, n, r) {
    var i, a, c = 0;
    t["level"] > 0 ? (2 === t["strm"]["data_type"] && (t["strm"]["data_type"] = function(t) {
        var e, n = 4093624447;
        for (e = 0; e <= 31; e++,
        n >>>= 1)
            if (1 & n && 0 !== t["dyn_ltree"][2 * e])
                return 0;
        if (0 !== t["dyn_ltree"][18] || 0 !== t.dyn_ltree[20] || 0 !== t.dyn_ltree[26])
            return 1;
        for (e = 32; e < o; e++)
            if (0 !== t["dyn_ltree"][2 * e])
                return 1;
        return 0;
    }(t)),
    Z(t, t["l_desc"]),
    Z(t, t["d_desc"]),
    c = function(t) {
        var e;
        for (N(t, t["dyn_ltree"], t["l_desc"].max_code),
        N(t, t.dyn_dtree, t["d_desc"].max_code),
        Z(t, t["bl_desc"]),
        e = u - 1; e >= 3 && 0 === t["bl_tree"][2 * y[e] + 1]; e--)
            ;
        return t["opt_len"] += 3 * (e + 1) + 5 + 5 + 4,
        e;
    }(t),
    i = t["opt_len"] + 3 + 7 >>> 3,
    (a = t["static_len"] + 3 + 7 >>> 3) <= i && (i = a)) : i = a = n + 5,
    n + 4 <= i && -1 !== e ? H(t, e, n, r) : 4 === t.strategy || a === i ? (T(t, 2 + (r ? 1 : 0), 3),
    L(t, m, b)) : (T(t, 4 + (r ? 1 : 0), 3),
    function(t, e, n, r) {
        var i;
        for (T(t, e - 257, 5),
        T(t, n - 1, 5),
        T(t, r - 4, 4),
        i = 0; i < r; i++)
            T(t, t["bl_tree"][2 * y[i] + 1], 3);
        U(t, t["dyn_ltree"], e - 1),
        U(t, t["dyn_dtree"], n - 1);
    }(t, t.l_desc.max_code + 1, t["d_desc"]["max_code"] + 1, c + 1),
    L(t, t.dyn_ltree, t["dyn_dtree"])),
    j(t),
    r && F(t);
}
,
e["_tr_tally"] = function(t, e, n) {
    return t["pending_buf"][t["d_buf"] + 2 * t["last_lit"]] = e >>> 8 & 255,
    t["pending_buf"][t.d_buf + 2 * t["last_lit"] + 1] = 255 & e,
    t["pending_buf"][t["l_buf"] + t.last_lit] = 255 & n,
    t["last_lit"]++,
    0 === e ? t["dyn_ltree"][2 * n]++ : (t["matches"]++,
    e--,
    t["dyn_ltree"][2 * (w[n] + o + 1)]++,
    t.dyn_dtree[2 * R(e)]++),
    t["last_lit"] === t["lit_bufsize"] - 1;
}
,
e._tr_align = function(t) {
    var e;
    T(t, 2, 3),
    C(t, l, m),
    16 === (e = t)["bi_valid"] ? (B(e, e["bi_buf"]),
    e["bi_buf"] = 0,
    e.bi_valid = 0) : e["bi_valid"] >= 8 && (e["pending_buf"][e.pending++] = 255 & e["bi_buf"],
    e["bi_buf"] >>= 8,
    e.bi_valid -= 8);
}
;
module.exports = e
