
function a(e){
    return typeof e
}
function n(t){
    return require(`./${t}`)
}
var r = n(12),
    i = n(2),
    o = n(16),
    c = n(9),
    u = n(17),
    f = Object["prototype"].toString,
    x = 0,
    d = -1,
    l = 0,
    h = 8;
 
function v(t) {
    if (!(this instanceof v)) return new v(t);
    this.options = i.assign({
    level: d,
    method: h,
    chunkSize: 16384,
    windowBits: 15,
    memLevel: 8,
    strategy: l,
    to: ""
    }, t || {});
    var e = this["options"];
    e["raw"] && e.windowBits > 0 ? e["windowBits"] = -e["windowBits"] : e["gzip"] && e["windowBits"] > 0 && e["windowBits"] < 16 && (e["windowBits"] += 16), this["err"] = 0, this.msg = "", this.ended = !1, this["chunks"] = [], this["strm"] = new u(), this["strm"]["avail_out"] = 0;
    var n = r["deflateInit2"](this["strm"], e["level"], e.method, e["windowBits"], e.memLevel, e["strategy"]);
    if (n !== x) throw new Error(c[n]);
    if (e["header"] && r["deflateSetHeader"](this["strm"], e["header"]), e.dictionary) {
    var a;
    if (a = "string" == typeof e.dictionary ? o["string2buf"](e["dictionary"]) : f.call(e["dictionary"]) === "[object ArrayBuffer]" ? new Uint8Array(e["dictionary"]) : e["dictionary"], (n = r["deflateSetDictionary"](this.strm, a)) !== x) throw new Error(c[n]);
    this["_dict_set"] = !0;
    }
}
function p(t, e) {
    var n = new v(e);
    if (n["push"](t, !0), n.err) throw n["msg"] || c[n["err"]];
    return n["result"];
}
v["prototype"]["push"] = function (t, e) {
    var n,
    c,
    u = this["strm"],
    d = this["options"]["chunkSize"];
    if (this.ended) return !1;
    c = e === ~~e ? e : !0 === e ? 4 : 0, a(t) === "string" ? u["input"] = o["string2buf"](t) : f["call"](t) === "[object ArrayBuffer]" ? u["input"] = new Uint8Array(t) : u["input"] = t, u.next_in = 0, u.avail_in = u["input"]["length"];
    do {
    if (0 === u["avail_out"] && (u["output"] = new i["Buf8"](d), u["next_out"] = 0, u.avail_out = d), 1 !== (n = r["deflate"](u, c)) && n !== x) return this["onEnd"](n), this["ended"] = !0, !1;
    0 !== u["avail_out"] && (0 !== u["avail_in"] || 4 !== c && 2 !== c) || (this["options"].to === "string" ? this.onData(o["buf2binstring"](i["shrinkBuf"](u.output, u.next_out))) : this["onData"](i["shrinkBuf"](u["output"], u["next_out"])));
    } while ((u.avail_in > 0 || 0 === u.avail_out) && 1 !== n);
    return 4 === c ? (n = r["deflateEnd"](this["strm"]), this["onEnd"](n), this["ended"] = !0, n === x) : 2 !== c || (this["onEnd"](x), u["avail_out"] = 0, !0);
},
v["prototype"]["onData"] = function (t) {
    this["chunks"]["push"](t);
},
v.prototype["onEnd"] = function (t) {
    t === x && ("string" === this["options"].to ? this["result"] = this["chunks"].join("") : this.result = i["flattenChunks"](this["chunks"])), this["chunks"] = [], this["err"] = t, this["msg"] = this["strm"]["msg"];
},
e = {}
e["Deflate"] = v,
e.deflate = p,
e.deflateRaw = function (t, e) {
    return (e = e || {}).raw = !0, p(t, e);
},
e.gzip = function (t, e) {
    return (e = e || {})["gzip"] = !0, p(t, e);
};
module.exports = e