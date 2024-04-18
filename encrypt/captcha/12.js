
function n(t){
    return require(`./${t}`)
}

var r,
    i = n(2),
    o = n(13),
    a = n(14),
    c = n(15),
    u = n(9),
    f = 0,
    x = 4,
    d = 0,
    l = -2,
    h = 2,
    v = 8,
    p = 3,
    y = 258,
    m = y + p + 1,
    b = 42,
    g = 103,
    w = 113,
    _ = 666,
    S = 1,
    k = 2,
    E = 3,
    O = 4;
function I(t, e) {
    return t.msg = u[e], e;
}
function P(t) {
    return (t << 1) - (t > 4 ? 9 : 0);
}
function R(t) {
    for (var e = t["length"]; --e >= 0;) t[e] = 0;
}
function B(t) {
    var e = t["state"],
    n = e["pending"];
    n > t["avail_out"] && (n = t["avail_out"]), 0 !== n && (i["arraySet"](t.output, e.pending_buf, e["pending_out"], n, t["next_out"]), t["next_out"] += n, e["pending_out"] += n, t["total_out"] += n, t["avail_out"] -= n, e["pending"] -= n, 0 === e["pending"] && (e["pending_out"] = 0));
}
function T(t, e) {
    o["_tr_flush_block"](t, t.block_start >= 0 ? t.block_start : -1, t["strstart"] - t["block_start"], e), t["block_start"] = t["strstart"], B(t["strm"]);
}
function C(t, e) {
    t["pending_buf"][t["pending"]++] = e;
}
function z(t, e) {
    t["pending_buf"][t["pending"]++] = e >>> 8 & 255, t.pending_buf[t["pending"]++] = 255 & e;
}
function A(t, e) {
    var n,
    r,
    i = t["max_chain_length"],
    o = t.strstart,
    a = t["prev_length"],
    c = t["nice_match"],
    u = t["strstart"] > t["w_size"] - m ? t["strstart"] - (t["w_size"] - m) : 0,
    f = t.window,
    x = t["w_mask"],
    d = t.prev,
    l = t["strstart"] + y,
    h = f[o + a - 1],
    v = f[o + a];
    t["prev_length"] >= t["good_match"] && (i >>= 2), c > t["lookahead"] && (c = t["lookahead"]);
    do {
    if (f[(n = e) + a] === v && f[n + a - 1] === h && f[n] === f[o] && f[++n] === f[o + 1]) {
        o += 2, n++;
        do {} while (f[++o] === f[++n] && f[++o] === f[++n] && f[++o] === f[++n] && f[++o] === f[++n] && f[++o] === f[++n] && f[++o] === f[++n] && f[++o] === f[++n] && f[++o] === f[++n] && o < l);
        if (r = y - (l - o), o = l - y, r > a) {
        if (t["match_start"] = e, a = r, r >= c) break;
        h = f[o + a - 1], v = f[o + a];
        }
    }
    } while ((e = d[e & x]) > u && 0 != --i);
    return a <= t["lookahead"] ? a : t["lookahead"];
}
function j(t) {
    var e,
    n,
    r,
    o,
    u,
    f,
    x,
    d,
    l,
    h,
    v = t.w_size;
    do {
    if (o = t["window_size"] - t.lookahead - t["strstart"], t.strstart >= v + (v - m)) {
        i.arraySet(t["window"], t["window"], v, v, 0), t["match_start"] -= v, t["strstart"] -= v, t.block_start -= v, e = n = t["hash_size"];
        do {
        r = t["head"][--e], t["head"][e] = r >= v ? r - v : 0;
        } while (--n);
        e = n = v;
        do {
        r = t.prev[--e], t["prev"][e] = r >= v ? r - v : 0;
        } while (--n);
        o += v;
    }
    if (0 === t.strm["avail_in"]) break;
    if (f = t.strm, x = t.window, d = t.strstart + t.lookahead, l = o, h = void 0, (h = f["avail_in"]) > l && (h = l), n = 0 === h ? 0 : (f["avail_in"] -= h, i["arraySet"](x, f["input"], f["next_in"], h, d), 1 === f["state"]["wrap"] ? f.adler = a(f["adler"], x, h, d) : 2 === f["state"]["wrap"] && (f["adler"] = c(f["adler"], x, h, d)), f["next_in"] += h, f.total_in += h, h), t["lookahead"] += n, t["lookahead"] + t["insert"] >= p) for (u = t["strstart"] - t.insert, t["ins_h"] = t["window"][u], t["ins_h"] = (t.ins_h << t["hash_shift"] ^ t["window"][u + 1]) & t.hash_mask; t["insert"] && (t["ins_h"] = (t.ins_h << t["hash_shift"] ^ t["window"][u + p - 1]) & t["hash_mask"], t["prev"][u & t["w_mask"]] = t["head"][t["ins_h"]], t["head"][t["ins_h"]] = u, u++, t["insert"]--, !(t.lookahead + t["insert"] < p)););
    } while (t.lookahead < m && 0 !== t["strm"]["avail_in"]);
}
function F(t, e) {
    for (var n, r;;) {
    if (t.lookahead < m) {
        if (j(t), t.lookahead < m && e === f) return S;
        if (0 === t["lookahead"]) break;
    }
    if (n = 0, t.lookahead >= p && (t.ins_h = (t["ins_h"] << t.hash_shift ^ t.window[t["strstart"] + p - 1]) & t.hash_mask, n = t["prev"][t["strstart"] & t["w_mask"]] = t["head"][t["ins_h"]], t["head"][t.ins_h] = t["strstart"]), 0 !== n && t["strstart"] - n <= t["w_size"] - m && (t.match_length = A(t, n)), t["match_length"] >= p) {
        if (r = o["_tr_tally"](t, t.strstart - t.match_start, t["match_length"] - p), t["lookahead"] -= t["match_length"], t["match_length"] <= t["max_lazy_match"] && t["lookahead"] >= p) {
        t.match_length--;
        do {
            t.strstart++, t.ins_h = (t["ins_h"] << t["hash_shift"] ^ t["window"][t["strstart"] + p - 1]) & t.hash_mask, n = t.prev[t["strstart"] & t.w_mask] = t["head"][t["ins_h"]], t["head"][t["ins_h"]] = t["strstart"];
        } while (0 != --t["match_length"]);
        t["strstart"]++;
        } else t["strstart"] += t.match_length, t["match_length"] = 0, t.ins_h = t["window"][t.strstart], t.ins_h = (t["ins_h"] << t["hash_shift"] ^ t["window"][t["strstart"] + 1]) & t["hash_mask"];
    } else r = o["_tr_tally"](t, 0, t["window"][t["strstart"]]), t["lookahead"]--, t["strstart"]++;
    if (r && (T(t, !1), 0 === t["strm"].avail_out)) return S;
    }
    return t.insert = t["strstart"] < p - 1 ? t["strstart"] : p - 1, e === x ? (T(t, !0), 0 === t["strm"]["avail_out"] ? E : O) : t["last_lit"] && (T(t, !1), 0 === t.strm["avail_out"]) ? S : k;
}
function M(t, e) {
    for (var n, r, i;;) {
    if (t["lookahead"] < m) {
        if (j(t), t.lookahead < m && e === f) return S;
        if (0 === t["lookahead"]) break;
    }
    if (n = 0, t["lookahead"] >= p && (t.ins_h = (t["ins_h"] << t.hash_shift ^ t["window"][t.strstart + p - 1]) & t["hash_mask"], n = t["prev"][t["strstart"] & t["w_mask"]] = t["head"][t["ins_h"]], t.head[t.ins_h] = t["strstart"]), t["prev_length"] = t.match_length, t["prev_match"] = t["match_start"], t.match_length = p - 1, 0 !== n && t["prev_length"] < t["max_lazy_match"] && t["strstart"] - n <= t["w_size"] - m && (t["match_length"] = A(t, n), t["match_length"] <= 5 && (1 === t["strategy"] || t["match_length"] === p && t["strstart"] - t["match_start"] > 4096) && (t.match_length = p - 1)), t.prev_length >= p && t["match_length"] <= t["prev_length"]) {
        i = t["strstart"] + t.lookahead - p, r = o["_tr_tally"](t, t["strstart"] - 1 - t["prev_match"], t["prev_length"] - p), t["lookahead"] -= t["prev_length"] - 1, t.prev_length -= 2;
        do {
        ++t.strstart <= i && (t["ins_h"] = (t.ins_h << t["hash_shift"] ^ t["window"][t["strstart"] + p - 1]) & t["hash_mask"], n = t.prev[t["strstart"] & t["w_mask"]] = t.head[t.ins_h], t.head[t.ins_h] = t["strstart"]);
        } while (0 != --t["prev_length"]);
        if (t.match_available = 0, t["match_length"] = p - 1, t["strstart"]++, r && (T(t, !1), 0 === t["strm"]["avail_out"])) return S;
    } else if (t["match_available"]) {
        if ((r = o._tr_tally(t, 0, t["window"][t["strstart"] - 1])) && T(t, !1), t["strstart"]++, t["lookahead"]--, 0 === t["strm"].avail_out) return S;
    } else t["match_available"] = 1, t.strstart++, t.lookahead--;
    }
    return t["match_available"] && (r = o["_tr_tally"](t, 0, t.window[t["strstart"] - 1]), t.match_available = 0), t.insert = t["strstart"] < p - 1 ? t["strstart"] : p - 1, e === x ? (T(t, !0), 0 === t.strm["avail_out"] ? E : O) : t["last_lit"] && (T(t, !1), 0 === t["strm"].avail_out) ? S : k;
}
function D(t, e, n, r, i) {
    this.good_length = t, this["max_lazy"] = e, this["nice_length"] = n, this["max_chain"] = r, this["func"] = i;
}
function L(t) {
    var e;
    return t && t.state ? (t["total_in"] = t["total_out"] = 0, t["data_type"] = h, (e = t["state"]).pending = 0, e["pending_out"] = 0, e.wrap < 0 && (e["wrap"] = -e.wrap), e["status"] = e["wrap"] ? b : w, t.adler = 2 === e["wrap"] ? 0 : 1, e.last_flush = f, o["_tr_init"](e), d) : I(t, l);
}
function Z(t) {
    var e,
    n = L(t);
    return n === d && ((e = t["state"]).window_size = 2 * e.w_size, R(e["head"]), e.max_lazy_match = r[e["level"]].max_lazy, e.good_match = r[e["level"]]["good_length"], e["nice_match"] = r[e["level"]]["nice_length"], e["max_chain_length"] = r[e["level"]].max_chain, e["strstart"] = 0, e["block_start"] = 0, e["lookahead"] = 0, e.insert = 0, e.match_length = e["prev_length"] = p - 1, e.match_available = 0, e["ins_h"] = 0), n;
}
function N(t, e, n, r, o, a) {
    if (!t) return l;
    var c = 1;
    if (-1 === e && (e = 6), r < 0 ? (c = 0, r = -r) : r > 15 && (c = 2, r -= 16), o < 1 || o > 9 || n !== v || r < 8 || r > 15 || e < 0 || e > 9 || a < 0 || a > 4) return I(t, l);
    8 === r && (r = 9);
    var u = new function () {
    this["strm"] = null, this.status = 0, this["pending_buf"] = null, this["pending_buf_size"] = 0, this["pending_out"] = 0, this["pending"] = 0, this.wrap = 0, this.gzhead = null, this["gzindex"] = 0, this["method"] = v, this["last_flush"] = -1, this["w_size"] = 0, this["w_bits"] = 0, this.w_mask = 0, this["window"] = null, this.window_size = 0, this["prev"] = null, this["head"] = null, this["ins_h"] = 0, this["hash_size"] = 0, this["hash_bits"] = 0, this["hash_mask"] = 0, this["hash_shift"] = 0, this["block_start"] = 0, this["match_length"] = 0, this["prev_match"] = 0, this["match_available"] = 0, this["strstart"] = 0, this["match_start"] = 0, this.lookahead = 0, this["prev_length"] = 0, this["max_chain_length"] = 0, this.max_lazy_match = 0, this["level"] = 0, this.strategy = 0, this["good_match"] = 0, this["nice_match"] = 0, this["dyn_ltree"] = new i["Buf16"](1146), this["dyn_dtree"] = new i.Buf16(122), this["bl_tree"] = new i["Buf16"](78), R(this.dyn_ltree), R(this["dyn_dtree"]), R(this["bl_tree"]), this["l_desc"] = null, this["d_desc"] = null, this.bl_desc = null, this.bl_count = new i.Buf16(16), this["heap"] = new i.Buf16(573), R(this["heap"]), this["heap_len"] = 0, this["heap_max"] = 0, this["depth"] = new i.Buf16(573), R(this.depth), this.l_buf = 0, this["lit_bufsize"] = 0, this["last_lit"] = 0, this.d_buf = 0, this["opt_len"] = 0, this["static_len"] = 0, this["matches"] = 0, this["insert"] = 0, this["bi_buf"] = 0, this.bi_valid = 0;
    }();
    return t["state"] = u, u["strm"] = t, u.wrap = c, u.gzhead = null, u["w_bits"] = r, u["w_size"] = 1 << u["w_bits"], u["w_mask"] = u["w_size"] - 1, u["hash_bits"] = o + 7, u["hash_size"] = 1 << u["hash_bits"], u["hash_mask"] = u["hash_size"] - 1, u.hash_shift = ~~((u["hash_bits"] + p - 1) / p), u["window"] = new i["Buf8"](2 * u["w_size"]), u["head"] = new i.Buf16(u["hash_size"]), u["prev"] = new i["Buf16"](u["w_size"]), u["lit_bufsize"] = 1 << o + 6, u.pending_buf_size = 4 * u["lit_bufsize"], u["pending_buf"] = new i["Buf8"](u.pending_buf_size), u.d_buf = 1 * u["lit_bufsize"], u["l_buf"] = 3 * u["lit_bufsize"], u.level = e, u["strategy"] = a, u["method"] = n, Z(t);
}
e = {}
r = [new D(0, 0, 0, 0, function (t, e) {
    var n = 65535;
    for (n > t.pending_buf_size - 5 && (n = t.pending_buf_size - 5);;) {
    if (t["lookahead"] <= 1) {
        if (j(t), 0 === t["lookahead"] && e === f) return S;
        if (0 === t.lookahead) break;
    }
    t["strstart"] += t["lookahead"], t.lookahead = 0;
    var r = t["block_start"] + n;
    if ((0 === t["strstart"] || t["strstart"] >= r) && (t["lookahead"] = t["strstart"] - r, t["strstart"] = r, T(t, !1), 0 === t["strm"]["avail_out"])) return S;
    if (t["strstart"] - t["block_start"] >= t["w_size"] - m && (T(t, !1), 0 === t["strm"]["avail_out"])) return S;
    }
    return t.insert = 0, e === x ? (T(t, !0), 0 === t["strm"]["avail_out"] ? E : O) : (t.strstart > t.block_start && (T(t, !1), t["strm"].avail_out), S);
}), new D(4, 4, 8, 4, F), new D(4, 5, 16, 8, F), new D(4, 6, 32, 32, F), new D(4, 4, 16, 16, M), new D(8, 16, 32, 32, M), new D(8, 16, 128, 128, M), new D(8, 32, 128, 256, M), new D(32, 128, 258, 1024, M),
 new D(32, 258, 258, 4096, M)],

e["deflateInit"] = function (t, e) {
    return N(t, e, v, 15, 8, 0);
}, 
e["deflateInit2"] = N, e["deflateReset"] = Z, e.deflateResetKeep = L, e.deflateSetHeader = function (t, e) {
    return t && t["state"] ? 2 !== t["state"]["wrap"] ? l : (t["state"].gzhead = e, d) : l;
}, e["deflate"] = function (t, e) {
    var n, i, a, u;
    if (!t || !t["state"] || e > 5 || e < 0) return t ? I(t, l) : l;
    if (i = t["state"], !t["output"] || !t["input"] && 0 !== t["avail_in"] || i["status"] === _ && e !== x) return I(t, 0 === t.avail_out ? -5 : l);
    if (i["strm"] = t, n = i["last_flush"], i["last_flush"] = e, i["status"] === b) if (2 === i.wrap) t["adler"] = 0, C(i, 31), C(i, 139), C(i, 8), i["gzhead"] ? (C(i, (i["gzhead"].text ? 1 : 0) + (i["gzhead"]["hcrc"] ? 2 : 0) + (i["gzhead"]["extra"] ? 4 : 0) + (i["gzhead"]["name"] ? 8 : 0) + (i["gzhead"]["comment"] ? 16 : 0)), C(i, 255 & i["gzhead"].time), C(i, i["gzhead"]["time"] >> 8 & 255), C(i, i["gzhead"]["time"] >> 16 & 255), C(i, i.gzhead["time"] >> 24 & 255), C(i, 9 === i["level"] ? 2 : i["strategy"] >= 2 || i["level"] < 2 ? 4 : 0), C(i, 255 & i.gzhead.os), i["gzhead"]["extra"] && i.gzhead.extra["length"] && (C(i, 255 & i["gzhead"].extra["length"]), C(i, i["gzhead"]["extra"]["length"] >> 8 & 255)), i["gzhead"].hcrc && (t["adler"] = c(t["adler"], i["pending_buf"], i.pending, 0)), i["gzindex"] = 0, i["status"] = 69) : (C(i, 0), C(i, 0), C(i, 0), C(i, 0), C(i, 0), C(i, 9 === i["level"] ? 2 : i["strategy"] >= 2 || i["level"] < 2 ? 4 : 0), C(i, 3), i["status"] = w);else {
    var h = v + (i["w_bits"] - 8 << 4) << 8;
    h |= (i["strategy"] >= 2 || i.level < 2 ? 0 : i["level"] < 6 ? 1 : 6 === i.level ? 2 : 3) << 6, 0 !== i["strstart"] && (h |= 32), h += 31 - h % 31, i["status"] = w, z(i, h), 0 !== i["strstart"] && (z(i, t["adler"] >>> 16), z(i, 65535 & t["adler"])), t["adler"] = 1;
    }
    if (69 === i.status) if (i["gzhead"]["extra"]) {
    for (a = i["pending"]; i["gzindex"] < (65535 & i["gzhead"].extra["length"]) && (i["pending"] !== i.pending_buf_size || (i["gzhead"].hcrc && i.pending > a && (t["adler"] = c(t["adler"], i["pending_buf"], i["pending"] - a, a)), B(t), a = i.pending, i.pending !== i["pending_buf_size"]));) C(i, 255 & i["gzhead"].extra[i["gzindex"]]), i["gzindex"]++;
    i["gzhead"].hcrc && i.pending > a && (t["adler"] = c(t["adler"], i["pending_buf"], i["pending"] - a, a)), i["gzindex"] === i["gzhead"]["extra"]["length"] && (i["gzindex"] = 0, i["status"] = 73);
    } else i.status = 73;
    if (73 === i.status) if (i["gzhead"]["name"]) {
    a = i["pending"];
    do {
        if (i["pending"] === i.pending_buf_size && (i["gzhead"]["hcrc"] && i["pending"] > a && (t["adler"] = c(t["adler"], i.pending_buf, i["pending"] - a, a)), B(t), a = i.pending, i.pending === i.pending_buf_size)) {
        u = 1;
        break;
        }
        u = i.gzindex < i["gzhead"]["name"].length ? 255 & i.gzhead["name"]["charCodeAt"](i["gzindex"]++) : 0, C(i, u);
    } while (0 !== u);
    i["gzhead"]["hcrc"] && i.pending > a && (t.adler = c(t["adler"], i["pending_buf"], i["pending"] - a, a)), 0 === u && (i.gzindex = 0, i.status = 91);
    } else i.status = 91;
    if (91 === i.status) if (i["gzhead"]["comment"]) {
    a = i["pending"];
    do {
        if (i["pending"] === i.pending_buf_size && (i.gzhead["hcrc"] && i.pending > a && (t.adler = c(t["adler"], i["pending_buf"], i["pending"] - a, a)), B(t), a = i["pending"], i["pending"] === i["pending_buf_size"])) {
        u = 1;
        break;
        }
        u = i["gzindex"] < i["gzhead"]["comment"]["length"] ? 255 & i["gzhead"]["comment"]["charCodeAt"](i["gzindex"]++) : 0, C(i, u);
    } while (0 !== u);
    i.gzhead.hcrc && i["pending"] > a && (t["adler"] = c(t["adler"], i["pending_buf"], i["pending"] - a, a)), 0 === u && (i["status"] = g);
    } else i["status"] = g;
    if (i["status"] === g && (i["gzhead"]["hcrc"] ? (i.pending + 2 > i["pending_buf_size"] && B(t), i["pending"] + 2 <= i.pending_buf_size && (C(i, 255 & t["adler"]), C(i, t["adler"] >> 8 & 255), t["adler"] = 0, i["status"] = w)) : i["status"] = w), 0 !== i["pending"]) {
    if (B(t), 0 === t.avail_out) return i["last_flush"] = -1, d;
    } else if (0 === t.avail_in && P(e) <= P(n) && e !== x) return I(t, -5);
    if (i["status"] === _ && 0 !== t["avail_in"]) return I(t, -5);
    if (0 !== t["avail_in"] || 0 !== i["lookahead"] || e !== f && i["status"] !== _) {
    var m = 2 === i["strategy"] ? function (t, e) {
        for (var n;;) {
        if (0 === t["lookahead"] && (j(t), 0 === t.lookahead)) {
            if (e === f) return S;
            break;
        }
        if (t["match_length"] = 0, n = o._tr_tally(t, 0, t["window"][t["strstart"]]), t["lookahead"]--, t["strstart"]++, n && (T(t, !1), 0 === t["strm"]["avail_out"])) return S;
        }
        return t["insert"] = 0, e === x ? (T(t, !0), 0 === t["strm"]["avail_out"] ? E : O) : t["last_lit"] && (T(t, !1), 0 === t["strm"]["avail_out"]) ? S : k;
    }(i, e) : 3 === i["strategy"] ? function (t, e) {
        for (var n, r, i, a, c = t["window"];;) {
        if (t["lookahead"] <= y) {
            if (j(t), t["lookahead"] <= y && e === f) return S;
            if (0 === t["lookahead"]) break;
        }
        if (t.match_length = 0, t.lookahead >= p && t["strstart"] > 0 && (r = c[i = t["strstart"] - 1]) === c[++i] && r === c[++i] && r === c[++i]) {
            a = t["strstart"] + y;
            do {} while (r === c[++i] && r === c[++i] && r === c[++i] && r === c[++i] && r === c[++i] && r === c[++i] && r === c[++i] && r === c[++i] && i < a);
            t.match_length = y - (a - i), t.match_length > t.lookahead && (t["match_length"] = t["lookahead"]);
        }
        if (t["match_length"] >= p ? (n = o["_tr_tally"](t, 1, t["match_length"] - p), t.lookahead -= t.match_length, t["strstart"] += t["match_length"], t.match_length = 0) : (n = o._tr_tally(t, 0, t.window[t["strstart"]]), t["lookahead"]--, t["strstart"]++), n && (T(t, !1), 0 === t["strm"]["avail_out"])) return S;
        }
        return t.insert = 0, e === x ? (T(t, !0), 0 === t["strm"]["avail_out"] ? E : O) : t["last_lit"] && (T(t, !1), 0 === t.strm["avail_out"]) ? S : k;
    }(i, e) : r[i["level"]]["func"](i, e);
    if (m !== E && m !== O || (i.status = _), m === S || m === E) return 0 === t["avail_out"] && (i.last_flush = -1), d;
    if (m === k && (1 === e ? o["_tr_align"](i) : 5 !== e && (o["_tr_stored_block"](i, 0, 0, !1), 3 === e && (R(i["head"]), 0 === i["lookahead"] && (i["strstart"] = 0, i["block_start"] = 0, i.insert = 0))), B(t), 0 === t["avail_out"])) return i.last_flush = -1, d;
    }
    return e !== x ? d : i["wrap"] <= 0 ? 1 : (2 === i.wrap ? (C(i, 255 & t["adler"]), C(i, t["adler"] >> 8 & 255), C(i, t["adler"] >> 16 & 255), C(i, t.adler >> 24 & 255), C(i, 255 & t.total_in), C(i, t["total_in"] >> 8 & 255), C(i, t["total_in"] >> 16 & 255), C(i, t["total_in"] >> 24 & 255)) : (z(i, t.adler >>> 16), z(i, 65535 & t.adler)), B(t), i["wrap"] > 0 && (i.wrap = -i["wrap"]), 0 !== i["pending"] ? d : 1);
}, e["deflateEnd"] = function (t) {
    var e;
    return t && t["state"] ? (e = t["state"]["status"]) !== b && 69 !== e && 73 !== e && 91 !== e && e !== g && e !== w && e !== _ ? I(t, l) : (t["state"] = null, e === w ? I(t, -3) : d) : l;
}, e.deflateSetDictionary = function (t, e) {
    var n,
    r,
    o,
    c,
    u,
    f,
    x,
    h,
    v = e["length"];
    if (!t || !t["state"]) return l;
    if (2 === (c = (n = t["state"])["wrap"]) || 1 === c && n.status !== b || n["lookahead"]) return l;
    for (1 === c && (t["adler"] = a(t.adler, e, v, 0)), n.wrap = 0, v >= n["w_size"] && (0 === c && (R(n.head), n["strstart"] = 0, n["block_start"] = 0, n["insert"] = 0), h = new i["Buf8"](n.w_size), i["arraySet"](h, e, v - n["w_size"], n["w_size"], 0), e = h, v = n["w_size"]), u = t["avail_in"], f = t.next_in, x = t["input"], t["avail_in"] = v, t["next_in"] = 0, t["input"] = e, j(n); n.lookahead >= p;) {
    r = n.strstart, o = n["lookahead"] - (p - 1);
    do {
        n["ins_h"] = (n["ins_h"] << n.hash_shift ^ n.window[r + p - 1]) & n["hash_mask"], n["prev"][r & n["w_mask"]] = n["head"][n["ins_h"]], n["head"][n["ins_h"]] = r, r++;
    } while (--o);
    n["strstart"] = r, n.lookahead = p - 1, j(n);
    }
    return n["strstart"] += n["lookahead"], n["block_start"] = n.strstart, n["insert"] = n["lookahead"], n["lookahead"] = 0, n["match_length"] = n["prev_length"] = p - 1, n["match_available"] = 0, t.next_in = f, t["input"] = x, t["avail_in"] = u, n["wrap"] = c, d;
}, e["deflateInfo"] = "pako deflate (from Nodeca project)";

module.exports = e