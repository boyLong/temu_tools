

var r, o = require("./24236.js"), i = require("./10342.js"), a = require("./66069.js"), u = require("./2869.js"), s = require("./48898.js"), c = 0, l = 4, f = 0, p = -2, d = -1, h = 4, v = 2, g = 8, y = 9, m = 286, b = 30, w = 19, _ = 2 * m + 1, x = 15, S = 3, E = 258, O = E + S + 1, k = 42, P = 103, A = 113, T = 666, j = 1, C = 2, R = 3, L = 4;
function N(t, e) {
    return t.msg = s[e],
    e
}
function I(t) {
    return (t << 1) - (t > 4 ? 9 : 0)
}
function M(t) {
    for (var e = t.length; --e >= 0; )
        t[e] = 0
}
function D(t) {
    var e = t.state
        , n = e.pending;
    n > t.avail_out && (n = t.avail_out),
    0 !== n && (o.arraySet(t.output, e.pending_buf, e.pending_out, n, t.next_out),
    t.next_out += n,
    e.pending_out += n,
    t.total_out += n,
    t.avail_out -= n,
    e.pending -= n,
    0 === e.pending && (e.pending_out = 0))
}
function B(t, e) {
    i._tr_flush_block(t, t.block_start >= 0 ? t.block_start : -1, t.strstart - t.block_start, e),
    t.block_start = t.strstart,
    D(t.strm)
}
function U(t, e) {
    t.pending_buf[t.pending++] = e
}
function F(t, e) {
    t.pending_buf[t.pending++] = e >>> 8 & 255,
    t.pending_buf[t.pending++] = 255 & e
}
function z(t, e) {
    var n, r, o = t.max_chain_length, i = t.strstart, a = t.prev_length, u = t.nice_match, s = t.strstart > t.w_size - O ? t.strstart - (t.w_size - O) : 0, c = t.window, l = t.w_mask, f = t.prev, p = t.strstart + E, d = c[i + a - 1], h = c[i + a];
    t.prev_length >= t.good_match && (o >>= 2),
    u > t.lookahead && (u = t.lookahead);
    do {
        if (c[(n = e) + a] === h && c[n + a - 1] === d && c[n] === c[i] && c[++n] === c[i + 1]) {
            i += 2,
            n++;
            do {} while (c[++i] === c[++n] && c[++i] === c[++n] && c[++i] === c[++n] && c[++i] === c[++n] && c[++i] === c[++n] && c[++i] === c[++n] && c[++i] === c[++n] && c[++i] === c[++n] && i < p);
            if (r = E - (p - i),
            i = p - E,
            r > a) {
                if (t.match_start = e,
                a = r,
                r >= u)
                    break;
                d = c[i + a - 1],
                h = c[i + a]
            }
        }
    } while ((e = f[e & l]) > s && 0 != --o);
    return a <= t.lookahead ? a : t.lookahead
}
function V(t) {
    var e, n, r, i, s, c, l, f, p, d, h = t.w_size;
    do {
        if (i = t.window_size - t.lookahead - t.strstart,
        t.strstart >= h + (h - O)) {
            o.arraySet(t.window, t.window, h, h, 0),
            t.match_start -= h,
            t.strstart -= h,
            t.block_start -= h,
            e = n = t.hash_size;
            do {
                r = t.head[--e],
                t.head[e] = r >= h ? r - h : 0
            } while (--n);
            e = n = h;
            do {
                r = t.prev[--e],
                t.prev[e] = r >= h ? r - h : 0
            } while (--n);
            i += h
        }
        if (0 === t.strm.avail_in)
            break;
        if (c = t.strm,
        l = t.window,
        f = t.strstart + t.lookahead,
        p = i,
        d = void 0,
        (d = c.avail_in) > p && (d = p),
        n = 0 === d ? 0 : (c.avail_in -= d,
        o.arraySet(l, c.input, c.next_in, d, f),
        1 === c.state.wrap ? c.adler = a(c.adler, l, d, f) : 2 === c.state.wrap && (c.adler = u(c.adler, l, d, f)),
        c.next_in += d,
        c.total_in += d,
        d),
        t.lookahead += n,
        t.lookahead + t.insert >= S)
            for (s = t.strstart - t.insert,
            t.ins_h = t.window[s],
            t.ins_h = (t.ins_h << t.hash_shift ^ t.window[s + 1]) & t.hash_mask; t.insert && (t.ins_h = (t.ins_h << t.hash_shift ^ t.window[s + S - 1]) & t.hash_mask,
            t.prev[s & t.w_mask] = t.head[t.ins_h],
            t.head[t.ins_h] = s,
            s++,
            t.insert--,
            !(t.lookahead + t.insert < S)); )
                ;
    } while (t.lookahead < O && 0 !== t.strm.avail_in)
}
function $(t, e) {
    for (var n, r; ; ) {
        if (t.lookahead < O) {
            if (V(t),
            t.lookahead < O && e === c)
                return j;
            if (0 === t.lookahead)
                break
        }
        if (n = 0,
        t.lookahead >= S && (t.ins_h = (t.ins_h << t.hash_shift ^ t.window[t.strstart + S - 1]) & t.hash_mask,
        n = t.prev[t.strstart & t.w_mask] = t.head[t.ins_h],
        t.head[t.ins_h] = t.strstart),
        0 !== n && t.strstart - n <= t.w_size - O && (t.match_length = z(t, n)),
        t.match_length >= S)
            if (r = i._tr_tally(t, t.strstart - t.match_start, t.match_length - S),
            t.lookahead -= t.match_length,
            t.match_length <= t.max_lazy_match && t.lookahead >= S) {
                t.match_length--;
                do {
                    t.strstart++,
                    t.ins_h = (t.ins_h << t.hash_shift ^ t.window[t.strstart + S - 1]) & t.hash_mask,
                    n = t.prev[t.strstart & t.w_mask] = t.head[t.ins_h],
                    t.head[t.ins_h] = t.strstart
                } while (0 != --t.match_length);
                t.strstart++
            } else
                t.strstart += t.match_length,
                t.match_length = 0,
                t.ins_h = t.window[t.strstart],
                t.ins_h = (t.ins_h << t.hash_shift ^ t.window[t.strstart + 1]) & t.hash_mask;
        else
            r = i._tr_tally(t, 0, t.window[t.strstart]),
            t.lookahead--,
            t.strstart++;
        if (r && (B(t, !1),
        0 === t.strm.avail_out))
            return j
    }
    return t.insert = t.strstart < S - 1 ? t.strstart : S - 1,
    e === l ? (B(t, !0),
    0 === t.strm.avail_out ? R : L) : t.last_lit && (B(t, !1),
    0 === t.strm.avail_out) ? j : C
}
function H(t, e) {
    for (var n, r, o; ; ) {
        if (t.lookahead < O) {
            if (V(t),
            t.lookahead < O && e === c)
                return j;
            if (0 === t.lookahead)
                break
        }
        if (n = 0,
        t.lookahead >= S && (t.ins_h = (t.ins_h << t.hash_shift ^ t.window[t.strstart + S - 1]) & t.hash_mask,
        n = t.prev[t.strstart & t.w_mask] = t.head[t.ins_h],
        t.head[t.ins_h] = t.strstart),
        t.prev_length = t.match_length,
        t.prev_match = t.match_start,
        t.match_length = S - 1,
        0 !== n && t.prev_length < t.max_lazy_match && t.strstart - n <= t.w_size - O && (t.match_length = z(t, n),
        t.match_length <= 5 && (1 === t.strategy || t.match_length === S && t.strstart - t.match_start > 4096) && (t.match_length = S - 1)),
        t.prev_length >= S && t.match_length <= t.prev_length) {
            o = t.strstart + t.lookahead - S,
            r = i._tr_tally(t, t.strstart - 1 - t.prev_match, t.prev_length - S),
            t.lookahead -= t.prev_length - 1,
            t.prev_length -= 2;
            do {
                ++t.strstart <= o && (t.ins_h = (t.ins_h << t.hash_shift ^ t.window[t.strstart + S - 1]) & t.hash_mask,
                n = t.prev[t.strstart & t.w_mask] = t.head[t.ins_h],
                t.head[t.ins_h] = t.strstart)
            } while (0 != --t.prev_length);
            if (t.match_available = 0,
            t.match_length = S - 1,
            t.strstart++,
            r && (B(t, !1),
            0 === t.strm.avail_out))
                return j
        } else if (t.match_available) {
            if ((r = i._tr_tally(t, 0, t.window[t.strstart - 1])) && B(t, !1),
            t.strstart++,
            t.lookahead--,
            0 === t.strm.avail_out)
                return j
        } else
            t.match_available = 1,
            t.strstart++,
            t.lookahead--
    }
    return t.match_available && (r = i._tr_tally(t, 0, t.window[t.strstart - 1]),
    t.match_available = 0),
    t.insert = t.strstart < S - 1 ? t.strstart : S - 1,
    e === l ? (B(t, !0),
    0 === t.strm.avail_out ? R : L) : t.last_lit && (B(t, !1),
    0 === t.strm.avail_out) ? j : C
}
function Z(t, e, n, r, o) {
    this.good_length = t,
    this.max_lazy = e,
    this.nice_length = n,
    this.max_chain = r,
    this.func = o
}
function W() {
    this.strm = null,
    this.status = 0,
    this.pending_buf = null,
    this.pending_buf_size = 0,
    this.pending_out = 0,
    this.pending = 0,
    this.wrap = 0,
    this.gzhead = null,
    this.gzindex = 0,
    this.method = g,
    this.last_flush = -1,
    this.w_size = 0,
    this.w_bits = 0,
    this.w_mask = 0,
    this.window = null,
    this.window_size = 0,
    this.prev = null,
    this.head = null,
    this.ins_h = 0,
    this.hash_size = 0,
    this.hash_bits = 0,
    this.hash_mask = 0,
    this.hash_shift = 0,
    this.block_start = 0,
    this.match_length = 0,
    this.prev_match = 0,
    this.match_available = 0,
    this.strstart = 0,
    this.match_start = 0,
    this.lookahead = 0,
    this.prev_length = 0,
    this.max_chain_length = 0,
    this.max_lazy_match = 0,
    this.level = 0,
    this.strategy = 0,
    this.good_match = 0,
    this.nice_match = 0,
    this.dyn_ltree = new o.Buf16(2 * _),
    this.dyn_dtree = new o.Buf16(2 * (2 * b + 1)),
    this.bl_tree = new o.Buf16(2 * (2 * w + 1)),
    M(this.dyn_ltree),
    M(this.dyn_dtree),
    M(this.bl_tree),
    this.l_desc = null,
    this.d_desc = null,
    this.bl_desc = null,
    this.bl_count = new o.Buf16(x + 1),
    this.heap = new o.Buf16(2 * m + 1),
    M(this.heap),
    this.heap_len = 0,
    this.heap_max = 0,
    this.depth = new o.Buf16(2 * m + 1),
    M(this.depth),
    this.l_buf = 0,
    this.lit_bufsize = 0,
    this.last_lit = 0,
    this.d_buf = 0,
    this.opt_len = 0,
    this.static_len = 0,
    this.matches = 0,
    this.insert = 0,
    this.bi_buf = 0,
    this.bi_valid = 0
}
function q(t) {
    var e;
    return t && t.state ? (t.total_in = t.total_out = 0,
    t.data_type = v,
    (e = t.state).pending = 0,
    e.pending_out = 0,
    e.wrap < 0 && (e.wrap = -e.wrap),
    e.status = e.wrap ? k : A,
    t.adler = 2 === e.wrap ? 0 : 1,
    e.last_flush = c,
    i._tr_init(e),
    f) : N(t, p)
}
function K(t) {
    var e, n = q(t);
    return n === f && ((e = t.state).window_size = 2 * e.w_size,
    M(e.head),
    e.max_lazy_match = r[e.level].max_lazy,
    e.good_match = r[e.level].good_length,
    e.nice_match = r[e.level].nice_length,
    e.max_chain_length = r[e.level].max_chain,
    e.strstart = 0,
    e.block_start = 0,
    e.lookahead = 0,
    e.insert = 0,
    e.match_length = e.prev_length = S - 1,
    e.match_available = 0,
    e.ins_h = 0),
    n
}
function Y(t, e, n, r, i, a) {
    if (!t)
        return p;
    var u = 1;
    if (e === d && (e = 6),
    r < 0 ? (u = 0,
    r = -r) : r > 15 && (u = 2,
    r -= 16),
    i < 1 || i > y || n !== g || r < 8 || r > 15 || e < 0 || e > 9 || a < 0 || a > h)
        return N(t, p);
    8 === r && (r = 9);
    var s = new W;
    return t.state = s,
    s.strm = t,
    s.wrap = u,
    s.gzhead = null,
    s.w_bits = r,
    s.w_size = 1 << s.w_bits,
    s.w_mask = s.w_size - 1,
    s.hash_bits = i + 7,
    s.hash_size = 1 << s.hash_bits,
    s.hash_mask = s.hash_size - 1,
    s.hash_shift = ~~((s.hash_bits + S - 1) / S),
    s.window = new o.Buf8(2 * s.w_size),
    s.head = new o.Buf16(s.hash_size),
    s.prev = new o.Buf16(s.w_size),
    s.lit_bufsize = 1 << i + 6,
    s.pending_buf_size = 4 * s.lit_bufsize,
    s.pending_buf = new o.Buf8(s.pending_buf_size),
    s.d_buf = 1 * s.lit_bufsize,
    s.l_buf = 3 * s.lit_bufsize,
    s.level = e,
    s.strategy = a,
    s.method = n,
    K(t)
}
r = [new Z(0,0,0,0,(function(t, e) {
    var n = 65535;
    for (n > t.pending_buf_size - 5 && (n = t.pending_buf_size - 5); ; ) {
        if (t.lookahead <= 1) {
            if (V(t),
            0 === t.lookahead && e === c)
                return j;
            if (0 === t.lookahead)
                break
        }
        t.strstart += t.lookahead,
        t.lookahead = 0;
        var r = t.block_start + n;
        if ((0 === t.strstart || t.strstart >= r) && (t.lookahead = t.strstart - r,
        t.strstart = r,
        B(t, !1),
        0 === t.strm.avail_out))
            return j;
        if (t.strstart - t.block_start >= t.w_size - O && (B(t, !1),
        0 === t.strm.avail_out))
            return j
    }
    return t.insert = 0,
    e === l ? (B(t, !0),
    0 === t.strm.avail_out ? R : L) : (t.strstart > t.block_start && (B(t, !1),
    t.strm.avail_out),
    j)
}
)), new Z(4,4,8,4,$), new Z(4,5,16,8,$), new Z(4,6,32,32,$), new Z(4,4,16,16,H), new Z(8,16,32,32,H), new Z(8,16,128,128,H), new Z(8,32,128,256,H), new Z(32,128,258,1024,H), new Z(32,258,258,4096,H)],
e.deflateInit = function(t, e) {
    return Y(t, e, g, 15, 8, 0)
}
,
e.deflateInit2 = Y,
e.deflateReset = K,
e.deflateResetKeep = q,
e.deflateSetHeader = function(t, e) {
    return t && t.state ? 2 !== t.state.wrap ? p : (t.state.gzhead = e,
    f) : p
}
,
e.deflate = function(t, e) {
    var n, o, a, s;
    if (!t || !t.state || e > 5 || e < 0)
        return t ? N(t, p) : p;
    if (o = t.state,
    !t.output || !t.input && 0 !== t.avail_in || o.status === T && e !== l)
        return N(t, 0 === t.avail_out ? -5 : p);
    if (o.strm = t,
    n = o.last_flush,
    o.last_flush = e,
    o.status === k)
        if (2 === o.wrap)
            t.adler = 0,
            U(o, 31),
            U(o, 139),
            U(o, 8),
            o.gzhead ? (U(o, (o.gzhead.text ? 1 : 0) + (o.gzhead.hcrc ? 2 : 0) + (o.gzhead.extra ? 4 : 0) + (o.gzhead.name ? 8 : 0) + (o.gzhead.comment ? 16 : 0)),
            U(o, 255 & o.gzhead.time),
            U(o, o.gzhead.time >> 8 & 255),
            U(o, o.gzhead.time >> 16 & 255),
            U(o, o.gzhead.time >> 24 & 255),
            U(o, 9 === o.level ? 2 : o.strategy >= 2 || o.level < 2 ? 4 : 0),
            U(o, 255 & o.gzhead.os),
            o.gzhead.extra && o.gzhead.extra.length && (U(o, 255 & o.gzhead.extra.length),
            U(o, o.gzhead.extra.length >> 8 & 255)),
            o.gzhead.hcrc && (t.adler = u(t.adler, o.pending_buf, o.pending, 0)),
            o.gzindex = 0,
            o.status = 69) : (U(o, 0),
            U(o, 0),
            U(o, 0),
            U(o, 0),
            U(o, 0),
            U(o, 9 === o.level ? 2 : o.strategy >= 2 || o.level < 2 ? 4 : 0),
            U(o, 3),
            o.status = A);
        else {
            var d = g + (o.w_bits - 8 << 4) << 8;
            d |= (o.strategy >= 2 || o.level < 2 ? 0 : o.level < 6 ? 1 : 6 === o.level ? 2 : 3) << 6,
            0 !== o.strstart && (d |= 32),
            d += 31 - d % 31,
            o.status = A,
            F(o, d),
            0 !== o.strstart && (F(o, t.adler >>> 16),
            F(o, 65535 & t.adler)),
            t.adler = 1
        }
    if (69 === o.status)
        if (o.gzhead.extra) {
            for (a = o.pending; o.gzindex < (65535 & o.gzhead.extra.length) && (o.pending !== o.pending_buf_size || (o.gzhead.hcrc && o.pending > a && (t.adler = u(t.adler, o.pending_buf, o.pending - a, a)),
            D(t),
            a = o.pending,
            o.pending !== o.pending_buf_size)); )
                U(o, 255 & o.gzhead.extra[o.gzindex]),
                o.gzindex++;
            o.gzhead.hcrc && o.pending > a && (t.adler = u(t.adler, o.pending_buf, o.pending - a, a)),
            o.gzindex === o.gzhead.extra.length && (o.gzindex = 0,
            o.status = 73)
        } else
            o.status = 73;
    if (73 === o.status)
        if (o.gzhead.name) {
            a = o.pending;
            do {
                if (o.pending === o.pending_buf_size && (o.gzhead.hcrc && o.pending > a && (t.adler = u(t.adler, o.pending_buf, o.pending - a, a)),
                D(t),
                a = o.pending,
                o.pending === o.pending_buf_size)) {
                    s = 1;
                    break
                }
                s = o.gzindex < o.gzhead.name.length ? 255 & o.gzhead.name.charCodeAt(o.gzindex++) : 0,
                U(o, s)
            } while (0 !== s);
            o.gzhead.hcrc && o.pending > a && (t.adler = u(t.adler, o.pending_buf, o.pending - a, a)),
            0 === s && (o.gzindex = 0,
            o.status = 91)
        } else
            o.status = 91;
    if (91 === o.status)
        if (o.gzhead.comment) {
            a = o.pending;
            do {
                if (o.pending === o.pending_buf_size && (o.gzhead.hcrc && o.pending > a && (t.adler = u(t.adler, o.pending_buf, o.pending - a, a)),
                D(t),
                a = o.pending,
                o.pending === o.pending_buf_size)) {
                    s = 1;
                    break
                }
                s = o.gzindex < o.gzhead.comment.length ? 255 & o.gzhead.comment.charCodeAt(o.gzindex++) : 0,
                U(o, s)
            } while (0 !== s);
            o.gzhead.hcrc && o.pending > a && (t.adler = u(t.adler, o.pending_buf, o.pending - a, a)),
            0 === s && (o.status = P)
        } else
            o.status = P;
    if (o.status === P && (o.gzhead.hcrc ? (o.pending + 2 > o.pending_buf_size && D(t),
    o.pending + 2 <= o.pending_buf_size && (U(o, 255 & t.adler),
    U(o, t.adler >> 8 & 255),
    t.adler = 0,
    o.status = A)) : o.status = A),
    0 !== o.pending) {
        if (D(t),
        0 === t.avail_out)
            return o.last_flush = -1,
            f
    } else if (0 === t.avail_in && I(e) <= I(n) && e !== l)
        return N(t, -5);
    if (o.status === T && 0 !== t.avail_in)
        return N(t, -5);
    if (0 !== t.avail_in || 0 !== o.lookahead || e !== c && o.status !== T) {
        var h = 2 === o.strategy ? function(t, e) {
            for (var n; ; ) {
                if (0 === t.lookahead && (V(t),
                0 === t.lookahead)) {
                    if (e === c)
                        return j;
                    break
                }
                if (t.match_length = 0,
                n = i._tr_tally(t, 0, t.window[t.strstart]),
                t.lookahead--,
                t.strstart++,
                n && (B(t, !1),
                0 === t.strm.avail_out))
                    return j
            }
            return t.insert = 0,
            e === l ? (B(t, !0),
            0 === t.strm.avail_out ? R : L) : t.last_lit && (B(t, !1),
            0 === t.strm.avail_out) ? j : C
        }(o, e) : 3 === o.strategy ? function(t, e) {
            for (var n, r, o, a, u = t.window; ; ) {
                if (t.lookahead <= E) {
                    if (V(t),
                    t.lookahead <= E && e === c)
                        return j;
                    if (0 === t.lookahead)
                        break
                }
                if (t.match_length = 0,
                t.lookahead >= S && t.strstart > 0 && (r = u[o = t.strstart - 1]) === u[++o] && r === u[++o] && r === u[++o]) {
                    a = t.strstart + E;
                    do {} while (r === u[++o] && r === u[++o] && r === u[++o] && r === u[++o] && r === u[++o] && r === u[++o] && r === u[++o] && r === u[++o] && o < a);
                    t.match_length = E - (a - o),
                    t.match_length > t.lookahead && (t.match_length = t.lookahead)
                }
                if (t.match_length >= S ? (n = i._tr_tally(t, 1, t.match_length - S),
                t.lookahead -= t.match_length,
                t.strstart += t.match_length,
                t.match_length = 0) : (n = i._tr_tally(t, 0, t.window[t.strstart]),
                t.lookahead--,
                t.strstart++),
                n && (B(t, !1),
                0 === t.strm.avail_out))
                    return j
            }
            return t.insert = 0,
            e === l ? (B(t, !0),
            0 === t.strm.avail_out ? R : L) : t.last_lit && (B(t, !1),
            0 === t.strm.avail_out) ? j : C
        }(o, e) : r[o.level].func(o, e);
        if (h !== R && h !== L || (o.status = T),
        h === j || h === R)
            return 0 === t.avail_out && (o.last_flush = -1),
            f;
        if (h === C && (1 === e ? i._tr_align(o) : 5 !== e && (i._tr_stored_block(o, 0, 0, !1),
        3 === e && (M(o.head),
        0 === o.lookahead && (o.strstart = 0,
        o.block_start = 0,
        o.insert = 0))),
        D(t),
        0 === t.avail_out))
            return o.last_flush = -1,
            f
    }
    return e !== l ? f : o.wrap <= 0 ? 1 : (2 === o.wrap ? (U(o, 255 & t.adler),
    U(o, t.adler >> 8 & 255),
    U(o, t.adler >> 16 & 255),
    U(o, t.adler >> 24 & 255),
    U(o, 255 & t.total_in),
    U(o, t.total_in >> 8 & 255),
    U(o, t.total_in >> 16 & 255),
    U(o, t.total_in >> 24 & 255)) : (F(o, t.adler >>> 16),
    F(o, 65535 & t.adler)),
    D(t),
    o.wrap > 0 && (o.wrap = -o.wrap),
    0 !== o.pending ? f : 1)
}
,
e.deflateEnd = function(t) {
    var e;
    return t && t.state ? (e = t.state.status) !== k && 69 !== e && 73 !== e && 91 !== e && e !== P && e !== A && e !== T ? N(t, p) : (t.state = null,
    e === A ? N(t, -3) : f) : p
}
,
e.deflateSetDictionary = function(t, e) {
    var n, r, i, u, s, c, l, d, h = e.length;
    if (!t || !t.state)
        return p;
    if (2 === (u = (n = t.state).wrap) || 1 === u && n.status !== k || n.lookahead)
        return p;
    for (1 === u && (t.adler = a(t.adler, e, h, 0)),
    n.wrap = 0,
    h >= n.w_size && (0 === u && (M(n.head),
    n.strstart = 0,
    n.block_start = 0,
    n.insert = 0),
    d = new o.Buf8(n.w_size),
    o.arraySet(d, e, h - n.w_size, n.w_size, 0),
    e = d,
    h = n.w_size),
    s = t.avail_in,
    c = t.next_in,
    l = t.input,
    t.avail_in = h,
    t.next_in = 0,
    t.input = e,
    V(n); n.lookahead >= S; ) {
        r = n.strstart,
        i = n.lookahead - (S - 1);
        do {
            n.ins_h = (n.ins_h << n.hash_shift ^ n.window[r + S - 1]) & n.hash_mask,
            n.prev[r & n.w_mask] = n.head[n.ins_h],
            n.head[n.ins_h] = r,
            r++
        } while (--i);
        n.strstart = r,
        n.lookahead = S - 1,
        V(n)
    }
    return n.strstart += n.lookahead,
    n.block_start = n.strstart,
    n.insert = n.lookahead,
    n.lookahead = 0,
    n.match_length = n.prev_length = S - 1,
    n.match_available = 0,
    t.next_in = c,
    t.input = l,
    t.avail_in = s,
    n.wrap = u,
    f
}
,
e.deflateInfo = "pako deflate (from Nodeca project)"
module.exports = e