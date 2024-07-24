var r = require("./24236.js")
    , o = 0
    , i = 1;
function a(t) {
    for (var e = t.length; --e >= 0; )
        t[e] = 0
}
var u = 0
    , s = 29
    , c = 256
    , l = c + 1 + s
    , f = 30
    , p = 19
    , d = 2 * l + 1
    , h = 15
    , v = 16
    , g = 7
    , y = 256
    , m = 16
    , b = 17
    , w = 18
    , _ = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 0]
    , x = [0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13]
    , S = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 7]
    , E = [16, 17, 18, 0, 8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15]
    , O = new Array(2 * (l + 2));
a(O);
var k = new Array(2 * f);
a(k);
var P = new Array(512);
a(P);
var A = new Array(256);
a(A);
var T = new Array(s);
a(T);
var j, C, R, L = new Array(f);
function N(t, e, n, r, o) {
    this.static_tree = t,
    this.extra_bits = e,
    this.extra_base = n,
    this.elems = r,
    this.max_length = o,
    this.has_stree = t && t.length
}
function I(t, e) {
    this.dyn_tree = t,
    this.max_code = 0,
    this.stat_desc = e
}
function M(t) {
    return t < 256 ? P[t] : P[256 + (t >>> 7)]
}
function D(t, e) {
    t.pending_buf[t.pending++] = 255 & e,
    t.pending_buf[t.pending++] = e >>> 8 & 255
}
function B(t, e, n) {
    t.bi_valid > v - n ? (t.bi_buf |= e << t.bi_valid & 65535,
    D(t, t.bi_buf),
    t.bi_buf = e >> v - t.bi_valid,
    t.bi_valid += n - v) : (t.bi_buf |= e << t.bi_valid & 65535,
    t.bi_valid += n)
}
function U(t, e, n) {
    B(t, n[2 * e], n[2 * e + 1])
}
function F(t, e) {
    var n = 0;
    do {
        n |= 1 & t,
        t >>>= 1,
        n <<= 1
    } while (--e > 0);
    return n >>> 1
}
function z(t, e, n) {
    var r, o, i = new Array(h + 1), a = 0;
    for (r = 1; r <= h; r++)
        i[r] = a = a + n[r - 1] << 1;
    for (o = 0; o <= e; o++) {
        var u = t[2 * o + 1];
        0 !== u && (t[2 * o] = F(i[u]++, u))
    }
}
function V(t) {
    var e;
    for (e = 0; e < l; e++)
        t.dyn_ltree[2 * e] = 0;
    for (e = 0; e < f; e++)
        t.dyn_dtree[2 * e] = 0;
    for (e = 0; e < p; e++)
        t.bl_tree[2 * e] = 0;
    t.dyn_ltree[2 * y] = 1,
    t.opt_len = t.static_len = 0,
    t.last_lit = t.matches = 0
}
function $(t) {
    t.bi_valid > 8 ? D(t, t.bi_buf) : t.bi_valid > 0 && (t.pending_buf[t.pending++] = t.bi_buf),
    t.bi_buf = 0,
    t.bi_valid = 0
}
function H(t, e, n, r) {
    var o = 2 * e
        , i = 2 * n;
    return t[o] < t[i] || t[o] === t[i] && r[e] <= r[n]
}
function Z(t, e, n) {
    for (var r = t.heap[n], o = n << 1; o <= t.heap_len && (o < t.heap_len && H(e, t.heap[o + 1], t.heap[o], t.depth) && o++,
    !H(e, r, t.heap[o], t.depth)); )
        t.heap[n] = t.heap[o],
        n = o,
        o <<= 1;
    t.heap[n] = r
}
function W(t, e, n) {
    var r, o, i, a, u = 0;
    if (0 !== t.last_lit)
        do {
            r = t.pending_buf[t.d_buf + 2 * u] << 8 | t.pending_buf[t.d_buf + 2 * u + 1],
            o = t.pending_buf[t.l_buf + u],
            u++,
            0 === r ? U(t, o, e) : (U(t, (i = A[o]) + c + 1, e),
            0 !== (a = _[i]) && B(t, o -= T[i], a),
            U(t, i = M(--r), n),
            0 !== (a = x[i]) && B(t, r -= L[i], a))
        } while (u < t.last_lit);
    U(t, y, e)
}
function q(t, e) {
    var n, r, o, i = e.dyn_tree, a = e.stat_desc.static_tree, u = e.stat_desc.has_stree, s = e.stat_desc.elems, c = -1;
    for (t.heap_len = 0,
    t.heap_max = d,
    n = 0; n < s; n++)
        0 !== i[2 * n] ? (t.heap[++t.heap_len] = c = n,
        t.depth[n] = 0) : i[2 * n + 1] = 0;
    for (; t.heap_len < 2; )
        i[2 * (o = t.heap[++t.heap_len] = c < 2 ? ++c : 0)] = 1,
        t.depth[o] = 0,
        t.opt_len--,
        u && (t.static_len -= a[2 * o + 1]);
    for (e.max_code = c,
    n = t.heap_len >> 1; n >= 1; n--)
        Z(t, i, n);
    o = s;
    do {
        n = t.heap[1],
        t.heap[1] = t.heap[t.heap_len--],
        Z(t, i, 1),
        r = t.heap[1],
        t.heap[--t.heap_max] = n,
        t.heap[--t.heap_max] = r,
        i[2 * o] = i[2 * n] + i[2 * r],
        t.depth[o] = (t.depth[n] >= t.depth[r] ? t.depth[n] : t.depth[r]) + 1,
        i[2 * n + 1] = i[2 * r + 1] = o,
        t.heap[1] = o++,
        Z(t, i, 1)
    } while (t.heap_len >= 2);
    t.heap[--t.heap_max] = t.heap[1],
    function(t, e) {
        var n, r, o, i, a, u, s = e.dyn_tree, c = e.max_code, l = e.stat_desc.static_tree, f = e.stat_desc.has_stree, p = e.stat_desc.extra_bits, v = e.stat_desc.extra_base, g = e.stat_desc.max_length, y = 0;
        for (i = 0; i <= h; i++)
            t.bl_count[i] = 0;
        for (s[2 * t.heap[t.heap_max] + 1] = 0,
        n = t.heap_max + 1; n < d; n++)
            (i = s[2 * s[2 * (r = t.heap[n]) + 1] + 1] + 1) > g && (i = g,
            y++),
            s[2 * r + 1] = i,
            r > c || (t.bl_count[i]++,
            a = 0,
            r >= v && (a = p[r - v]),
            u = s[2 * r],
            t.opt_len += u * (i + a),
            f && (t.static_len += u * (l[2 * r + 1] + a)));
        if (0 !== y) {
            do {
                for (i = g - 1; 0 === t.bl_count[i]; )
                    i--;
                t.bl_count[i]--,
                t.bl_count[i + 1] += 2,
                t.bl_count[g]--,
                y -= 2
            } while (y > 0);
            for (i = g; 0 !== i; i--)
                for (r = t.bl_count[i]; 0 !== r; )
                    (o = t.heap[--n]) > c || (s[2 * o + 1] !== i && (t.opt_len += (i - s[2 * o + 1]) * s[2 * o],
                    s[2 * o + 1] = i),
                    r--)
        }
    }(t, e),
    z(i, c, t.bl_count)
}
function K(t, e, n) {
    var r, o, i = -1, a = e[1], u = 0, s = 7, c = 4;
    for (0 === a && (s = 138,
    c = 3),
    e[2 * (n + 1) + 1] = 65535,
    r = 0; r <= n; r++)
        o = a,
        a = e[2 * (r + 1) + 1],
        ++u < s && o === a || (u < c ? t.bl_tree[2 * o] += u : 0 !== o ? (o !== i && t.bl_tree[2 * o]++,
        t.bl_tree[2 * m]++) : u <= 10 ? t.bl_tree[2 * b]++ : t.bl_tree[2 * w]++,
        u = 0,
        i = o,
        0 === a ? (s = 138,
        c = 3) : o === a ? (s = 6,
        c = 3) : (s = 7,
        c = 4))
}
function Y(t, e, n) {
    var r, o, i = -1, a = e[1], u = 0, s = 7, c = 4;
    for (0 === a && (s = 138,
    c = 3),
    r = 0; r <= n; r++)
        if (o = a,
        a = e[2 * (r + 1) + 1],
        !(++u < s && o === a)) {
            if (u < c)
                do {
                    U(t, o, t.bl_tree)
                } while (0 != --u);
            else
                0 !== o ? (o !== i && (U(t, o, t.bl_tree),
                u--),
                U(t, m, t.bl_tree),
                B(t, u - 3, 2)) : u <= 10 ? (U(t, b, t.bl_tree),
                B(t, u - 3, 3)) : (U(t, w, t.bl_tree),
                B(t, u - 11, 7));
            u = 0,
            i = o,
            0 === a ? (s = 138,
            c = 3) : o === a ? (s = 6,
            c = 3) : (s = 7,
            c = 4)
        }
}
a(L);
var G = !1;
function X(t, e, n, o) {
    B(t, (u << 1) + (o ? 1 : 0), 3),
    function(t, e, n, o) {
        $(t),
        o && (D(t, n),
        D(t, ~n)),
        r.arraySet(t.pending_buf, t.window, e, n, t.pending),
        t.pending += n
    }(t, e, n, !0)
}
e._tr_init = function(t) {
    G || (!function() {
        var t, e, n, r, o, i = new Array(h + 1);
        for (n = 0,
        r = 0; r < s - 1; r++)
            for (T[r] = n,
            t = 0; t < 1 << _[r]; t++)
                A[n++] = r;
        for (A[n - 1] = r,
        o = 0,
        r = 0; r < 16; r++)
            for (L[r] = o,
            t = 0; t < 1 << x[r]; t++)
                P[o++] = r;
        for (o >>= 7; r < f; r++)
            for (L[r] = o << 7,
            t = 0; t < 1 << x[r] - 7; t++)
                P[256 + o++] = r;
        for (e = 0; e <= h; e++)
            i[e] = 0;
        for (t = 0; t <= 143; )
            O[2 * t + 1] = 8,
            t++,
            i[8]++;
        for (; t <= 255; )
            O[2 * t + 1] = 9,
            t++,
            i[9]++;
        for (; t <= 279; )
            O[2 * t + 1] = 7,
            t++,
            i[7]++;
        for (; t <= 287; )
            O[2 * t + 1] = 8,
            t++,
            i[8]++;
        for (z(O, l + 1, i),
        t = 0; t < f; t++)
            k[2 * t + 1] = 5,
            k[2 * t] = F(t, 5);
        j = new N(O,_,c + 1,l,h),
        C = new N(k,x,0,f,h),
        R = new N(new Array(0),S,0,p,g)
    }(),
    G = !0),
    t.l_desc = new I(t.dyn_ltree,j),
    t.d_desc = new I(t.dyn_dtree,C),
    t.bl_desc = new I(t.bl_tree,R),
    t.bi_buf = 0,
    t.bi_valid = 0,
    V(t)
}
,
e._tr_stored_block = X,
e._tr_flush_block = function(t, e, n, r) {
    var a, u, s = 0;
    t.level > 0 ? (2 === t.strm.data_type && (t.strm.data_type = function(t) {
        var e, n = 4093624447;
        for (e = 0; e <= 31; e++,
        n >>>= 1)
            if (1 & n && 0 !== t.dyn_ltree[2 * e])
                return o;
        if (0 !== t.dyn_ltree[18] || 0 !== t.dyn_ltree[20] || 0 !== t.dyn_ltree[26])
            return i;
        for (e = 32; e < c; e++)
            if (0 !== t.dyn_ltree[2 * e])
                return i;
        return o
    }(t)),
    q(t, t.l_desc),
    q(t, t.d_desc),
    s = function(t) {
        var e;
        for (K(t, t.dyn_ltree, t.l_desc.max_code),
        K(t, t.dyn_dtree, t.d_desc.max_code),
        q(t, t.bl_desc),
        e = p - 1; e >= 3 && 0 === t.bl_tree[2 * E[e] + 1]; e--)
            ;
        return t.opt_len += 3 * (e + 1) + 5 + 5 + 4,
        e
    }(t),
    a = t.opt_len + 3 + 7 >>> 3,
    (u = t.static_len + 3 + 7 >>> 3) <= a && (a = u)) : a = u = n + 5,
    n + 4 <= a && -1 !== e ? X(t, e, n, r) : 4 === t.strategy || u === a ? (B(t, 2 + (r ? 1 : 0), 3),
    W(t, O, k)) : (B(t, 4 + (r ? 1 : 0), 3),
    function(t, e, n, r) {
        var o;
        for (B(t, e - 257, 5),
        B(t, n - 1, 5),
        B(t, r - 4, 4),
        o = 0; o < r; o++)
            B(t, t.bl_tree[2 * E[o] + 1], 3);
        Y(t, t.dyn_ltree, e - 1),
        Y(t, t.dyn_dtree, n - 1)
    }(t, t.l_desc.max_code + 1, t.d_desc.max_code + 1, s + 1),
    W(t, t.dyn_ltree, t.dyn_dtree)),
    V(t),
    r && $(t)
}
,
e._tr_tally = function(t, e, n) {
    return t.pending_buf[t.d_buf + 2 * t.last_lit] = e >>> 8 & 255,
    t.pending_buf[t.d_buf + 2 * t.last_lit + 1] = 255 & e,
    t.pending_buf[t.l_buf + t.last_lit] = 255 & n,
    t.last_lit++,
    0 === e ? t.dyn_ltree[2 * n]++ : (t.matches++,
    e--,
    t.dyn_ltree[2 * (A[n] + c + 1)]++,
    t.dyn_dtree[2 * M(e)]++),
    t.last_lit === t.lit_bufsize - 1
}
,
e._tr_align = function(t) {
    B(t, 2, 3),
    U(t, y, O),
    function(t) {
        16 === t.bi_valid ? (D(t, t.bi_buf),
        t.bi_buf = 0,
        t.bi_valid = 0) : t.bi_valid >= 8 && (t.pending_buf[t.pending++] = 255 & t.bi_buf,
        t.bi_buf >>= 8,
        t.bi_valid -= 8)
    }(t)
}
console.log(e)
module.exports = e