

const zlib = require('./lib/24555.js');
const encode = require('./lib/3.js');



function vt (e, n, r) {
    if ((n -= (e += "").length) <= 0)
        return e;
    r || 0 === r || (r = " ");
    if (" " === (r += "") && n < 10)
        return t[n] + e;
    var o = "";
    for (; 1 & n && (o += r),
    n >>= 1; )
        r += r;
    return o + e
  }
gt =  [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "+",
    "/"
]
Et = {
    "+": "-",
    "/": "_",
    "=": ""
}
var Ne = {
    pako: function(e) {
        return zlib["deflate"](e);
    },
    base64: function(e) {
        for (var t, n, r, o = "", i = e.length, a = 0, u = 3 * parseInt(i / 3); a < u; )
            t = e[a++],
            n = e[a++],
            r = e[a++],
            o += gt[t >>> 2] + gt[63 & (t << 4 | n >>> 4)] + gt[63 & (n << 2 | r >>> 6)] + gt[63 & r];
        var c = i - u;
        return 1 === c ? (t = e[a],
        o += gt[t >>> 2] + gt[t << 4 & 63] + "==") : 2 === c && (t = e[a++],
        n = e[a],
        o += gt[t >>> 2] + gt[63 & (t << 4 | n >>> 4)] + gt[n << 2 & 63] + "="),
        o["replace"](/[+\/=]/g, function(e) {
            return Et[e];
        });
    },
    charCode: function(e) {
        for (var n = [], r = 0, o = 0; o < e["length"]; o += 1) {
            var i = e["charCodeAt"](o);
            i >= 0 && i <= 127 ? (n["push"](i),
            r += 1) : (i >= 2048 && i <= 55295 || i >= 57344 && i <= 65535) && (r += 3,
            n["push"](224 | 15 & i >> 12),
            n.push(128 | 63 & i >> 6),
            n.push(128 | 63 & i));
        }
        for (var a = 0; a < n["length"]; a += 1)
            n[a] &= 255;
        return r <= 255 ? [0, r]["concat"](n) : [r >> 8, 255 & r].concat(n);
    },
    es: function(e) {

        e || (e = "undefined");
        var n = []
          , r = this["charCode"](e)["slice"](2)
          , o = this["enn"](r["length"]);
        return n = n.concat(this["enn"](241), o, r);
    },
    en1: function(e) {

        e || (e = 0);
        var n = parseInt(e);
        return []["concat"](this.enn(239), this["enn"](n));
    },
    en: function(e) {

        e || (e = 0);
        var n = parseInt(e)
          , r = [];
        n > 0 ? r["push"](0) : r.push(1);
        for (var o = Math["abs"](n).toString(2)["split"](""), i = 0; o["length"] % 8 != 0; i++)
            o["unshift"]("0");
        o = o["join"]("");
        for (var a = Math["ceil"](o.length / 8), u = 0; u < a; u++) {
            var c = o["substring"](8 * u, 8 * (u + 1));
            r["push"](parseInt(c, 2));
        }
        return r["unshift"](r["length"]),
        r;
    },
    sc: function(e) {
        return e || (e = ""),
        this["charCode"](e).slice(2);
    },
    nc: function(e) {

        e || (e = 0);
        var n = Math["abs"](parseInt(e))["toString"](2)
          , r = Math.ceil(n["length"] / 8);
        n = vt(n, 8 * r, "0");
        for (var o = [], i = 0; i < r; i++) {
            var a = n.substring(8 * i, 8 * (i + 1));
            o["push"](parseInt(a, 2));
        }
        return o;
    },
    enn: function(e) {a

        e || (e = 0);
        for (var n = parseInt(e), r = n << 1 ^ n >> 31, o = r["toString"](2), i = [], a = (o = vt(o, 7 * Math["ceil"](o.length / 7), "0")).length; a >= 0; a -= 7) {
            var u = o["substring"](a - 7, a);
            if (0 == (-128 & r)) {
                i["push"]("0" + u);
                break;
            }
            i["push"]("1" + u),
            r >>>= 7;
        }
        return i["map"](function(e) {
            return parseInt(e, 2);
        });
    },
    ecl: function(e) {
        for (var n = [], r = e["toString"](2).split(""), o = 0; r["length"] < 16; o += 1)
            r["unshift"](0);
        return r = r["join"](""),
        n.push(parseInt(r["substring"](0, 8), 2), parseInt(r["substring"](8, 16), 2)),
        n;
    },
    pes: function(e) {

        return zlib["deflate"](e, {
            to: "string"
        });
    }
};
function un(){
    return JSON.stringify({
        "chrome": "true",
        "cef": "udf",
        "miniblink": "udf",
        "navigator": "udf",
        "electron": "udf",
        "unknowChrome": {
            "runtime": "true",
            "brands": "false",
            "version": "false",
            "webviewName": "false",
            "wke": "false",
            "ua": "false",
            "_process": "false",
            "_prompt": "false"
        }
    })
}

function Ei(e,hi) {
    var t, n, r, o, i, a, u, c, x, s, f, l, d, v, h, p, m, g, E, S, b, y, _, T, w, C, O, A, R, M, I, N, D, H, B, P, k, X, F, L, U, j, G, W, Z, J, V, K, z, Y, q, $, Q, ee, te, ne, re, oe, ie, ae, ue, ce, xe, se, fe, le, de, ve, he, pe, me, ge, Ee, Se, be, ye, _e, Te, we, Ce, Oe, Ae, Re, Me, Ie, Ne, He = (e || {}).callback;
    var Pe = (
    c = (u = e || {}).collectEvent,
    x = u.isInterval,
    s = void 0 !== x && x,
    f = hi.rawData,
    l = void 0 === f ? {} : f,
    d = hi.localIp,
    v = void 0 === d ? "undefined" : d,
    h = hi.version,
    p = void 0 === h ? "2.4.5" : h,
    m = hi.app,
    g = void 0 === m ? "h5Market" : m,
    E = hi.FKGJ,
    S = void 0 === E ? "undefined" : E,
    b = hi.uid,
    y = void 0 === b ? "undefined" : b,
    _ = hi.moveData,
    T = void 0 === _ ? [] : _,
    w = hi.clickData,
    C = void 0 === w ? [] : w,
    O = hi.inputData,
    A = void 0 === O ? [] : O,
    R = hi.blurData,
    M = void 0 === R ? [] : R,
    I = hi.pasteData,
    N = void 0 === I ? "0" : I,
    D = hi.hasSensor,
    H = hi.isFront,
    B = hi.webGLInfos,
    P = hi.windowSize,
    k = hi.winSelenium,
    X = hi.chromium,
    F = hi.headlessByProperties,
    L = hi.languages,
    U = hi.consoleLied,
    j = hi.chromeExtensionScripts,
    G = hi.extensionImgs,
    W = hi.hookFuncs,
    Z = hi.frontReferer,
    J = hi.elements,
    V = void 0 === J ? {} : J,
    K = hi.clientIp,
    z = void 0 === K ? void 0 : K,
    Y = hi.outterJs,
    q = void 0 === Y ? JSON["stringify"]({}) : Y,
    $ = hi.cssFeatures,
    Q = hi.webglFt,
    ee = hi.performanceTime,
    te = hi.emptyEvalLength,
    ne = hi.errorFF,
    re = hi.headerCache,
    oe = hi.fonts,
    ie = hi.h5Features,
    ae = String(Date.now()),
    ue = []["concat"](St.es("isInterval"), St.es(String(!!s)),
        St.es("rawData"), St.es(JSON.stringify(l)),
        St.es("localIp"), St.es(v),
        St.es("reportTimestamp"),
        St.es(ae), St.es("version"),
        St.es(p), St.es("app"), St.es(g), St.es("FKGJ"), St.es(S), St.es("uid"), St.es(y), St.es("hasCdc"), St.es("false"), St.es("electronCef"), St.es(un()), St.es("frontReferer"), St.es(Z)),
    ce = c ? [].concat(St.es("moveData"), St.es(JSON.stringify(T)), St.es("clickData"), St.es(JSON.stringify(C)), St.es("inputData"), St.es(JSON.stringify(A)), St.es("blurData"), St.es(JSON["stringify"](M)), St.es("pasteData"), St.es(N)) : [],
    xe = D ? [].concat(St.es("hasSensor"), St.es(D)) : [],
    se = H ? []["concat"](St.es("isFront"), St.es(H)) : [],
    fe = B ? []["concat"](St.es("webGLInfos"), St.es(B)) : [],
    le = P ? [].concat(St.es("windowSize"), St.es(P)) : [],
    de = X ? []["concat"](St.es("chromium"), St.es(X)) : [],
    ve = F ? [].concat(St.es("headlessByProperties"), St.es(F)) : [],
    he = k ? []["concat"](St.es("winSelenium"), St.es(k)) : [],
    pe = L ? [].concat(St.es("languages"), St.es(L)) : [],
    me = U ? [].concat(St.es("consoleLied"), St.es(U)) : [],
    ge = j ? []["concat"](St.es("injectScripts"), St.es(j)) : [],
    Ee = G ? []["concat"](St.es("extensionImgs"), St.es(G)) : [],
    Se = W ? [].concat(St.es("hookFuncs"), St.es(W)) : [],
    be = V ? [].concat(St.es("elements"), St.es(JSON["stringify"](V))) : [],
    ye = z ? [].concat(St.es("frontClientIp"), St.es(z)) : [],
    _e = q ? [].concat(St.es("outterJs"), St.es(q)) : [],
    Te = $ ? []["concat"](St.es("cssFeatures"), St.es($)) : [],
    we = Q ? []["concat"](St.es("webglFt"), St.es(Q)) : [],
    Ce = ee ? []["concat"](St.es("performanceTime"), St.es(ee)) : [],
    Oe = te ? []["concat"](St.es("emptyEvalLength"), St.es(te)) : [],
    Ae = ne ? []["concat"](St.es("errorFF"), St.es(ne)) : [],
    Re = re ? []["concat"](St.es("headerCache"), St.es(re)) : [],
    Me = oe ? []["concat"](St.es("fonts"), St.es(oe)) : [],
    Ie = ie ? [].concat(St.es("h5Features"), St.es(ie)) : [],
    Ne = ue.concat(ce, xe, se, fe, le, de, ve, he, pe, me, ge, Ee, Se, be, ye, _e, Te, we, Ce, Oe, Ae, Re, Me, Ie),
    {
        timeStamp: ae,
        result: "0a" + St["base64"](St.pako(Ne))
    })
    return Pe
}

function Yi(t, Vi) {
    var e;
    var n;
    var r;
    var o;
    var i;
    var a;
    var u;
    var c;
    var x;
    var s;
    var f;
    var l;
    var d;
    var v;
    var h;
    var p;
    var m;
    var g;
    var E;
    var b;
    var y;
    var S;
    var _;
    var A;
    var w;
    var T;
    var O;
    var C;
    var R;
    var M;
    var I;
    var N;
    var D;
    var H;
    var B;
    var P;
    var k;
    var X;
    var F;
    var L;
    var j;
    var U;
    var G;
    var W;
    var J;
    var V;
    var K;
    var z;
    var q;
    var Y;
    var Z;
    var Q;
    var $;
    var tt;
    var et;
    var nt;
    var rt;
    var ot;
    var it;
    var at;
    var ut;
    var ct;
    var xt;
    var st;
    var ft;
    var lt;
    var dt;
    var vt;
    var ht;
    var pt;
    var mt;
    var gt;
    var Et;
    var bt;
    var yt;
    var St;
    var _t;
    var At;
    var wt;
    var Tt;
    var Ot;
    var Ct;
    var Rt;
    var Mt;
    var It;
    var Nt;
    return (c = (u = t || {})["collectEvent"],
    x = u["isInterval"],
    s = void 0 !== x && x,
    f = Vi["rawData"],
    l = void 0 === f ? {} : f,
    d = Vi["localIp"],
    v = void 0 === d ? "undefined" : d,
    h = Vi["version"],
    p = void 0 === h ? '2.4.7' : h,
    m = Vi["app"],
    g = void 0 === m ? "h5Market" : m,
    E = Vi["FKGJ"],
    b = void 0 === E ? "undefined" : E,
    y = Vi["uid"],
    S = void 0 === y ? "undefined" : y,
    _ = Vi["moveData"],
    A = void 0 === _ ? [] : _,
    w = Vi["clickData"],
    T = void 0 === w ? [] : w,
    O = Vi["inputData"],
    C = void 0 === O ? [] : O,
    R = Vi["blurData"],
    M = void 0 === R ? [] : R,
    I = Vi["pasteData"],
    N = void 0 === I ? "0" : I,
    D = Vi["hasSensor"],
    H = Vi["isFront"],
    B = Vi["webGLInfos"],
    P = Vi["windowSize"],
    k = Vi["winSelenium"],
    X = Vi["chromium"],
    F = Vi["headlessByProperties"],
    L = Vi["languages"],
    j = Vi["consoleLied"],
    U = Vi["chromeExtensionScripts"],
    G = Vi["extensionImgs"],
    W = Vi["hookFuncs"],
    J = Vi["frontReferer"],
    V = Vi["elements"],
    K = void 0 === V ? {} : V,
    z = Vi["clientIp"],
    q = void 0 === z ? void 0 : z,
    Y = Vi["outterJs"],
    Z = void 0 === Y ? JSON["stringify"]({}) : Y,
    Q = Vi["cssFeatures"],
    $ = Vi["webglFt"],
    tt = Vi["performanceTime"],
    et = Vi["emptyEvalLength"],
    nt = Vi["errorFF"],
    rt = Vi["headerCache"],
    ot = Vi["fonts"],
    it = Vi["h5Features"],
    at = String(Date["now"]()),
    ut = []["concat"](Ne["es"]("isInterval"), Ne["es"](String(!!s)), Ne["es"]("rawData"), Ne["es"](JSON["stringify"](l)), Ne["es"]("localIp"), Ne["es"](v), Ne["es"]("reportTimestamp"), Ne["es"](at), Ne["es"]("version"), Ne["es"](p), Ne["es"]("app"), Ne["es"](g), Ne["es"]("FKGJ"), Ne["es"](b), Ne["es"]("uid"), Ne["es"](S), Ne["es"]("hasCdc"), Ne["es"]('false'), Ne["es"]("electronCef"), Ne["es"](un()), Ne["es"]("frontReferer"), Ne["es"](J)),
    ct = c ? []["concat"](Ne["es"]("moveData"), Ne["es"](JSON["stringify"](A)), Ne["es"]("clickData"), Ne["es"](JSON["stringify"](T)), Ne["es"]("inputData"), Ne["es"](JSON["stringify"](C)), Ne["es"]("blurData"), Ne["es"](JSON["stringify"](M)), Ne["es"]("pasteData"), Ne["es"](N)) : [],
    xt = D ? []["concat"](Ne["es"]("hasSensor"), Ne["es"](D)) : [],
    st = H ? []["concat"](Ne["es"]("isFront"), Ne["es"](H)) : [],
    ft = B ? []["concat"](Ne["es"]("webGLInfos"), Ne["es"](B)) : [],
    lt = P ? []["concat"](Ne["es"]("windowSize"), Ne["es"](P)) : [],
    dt = X ? []["concat"](Ne["es"]("chromium"), Ne["es"](X)) : [],
    vt = F ? []["concat"](Ne["es"]("headlessByProperties"), Ne["es"](F)) : [],
    ht = k ? []["concat"](Ne["es"]("winSelenium"), Ne["es"](k)) : [],
    pt = L ? []["concat"](Ne["es"]("languages"), Ne["es"](L)) : [],
    mt = j ? []["concat"](Ne["es"]("consoleLied"), Ne["es"](j)) : [],
    gt = U ? []["concat"](Ne["es"]("injectScripts"), Ne["es"](U)) : [],
    Et = G ? []["concat"](Ne["es"]("extensionImgs"), Ne["es"](G)) : [],
    bt = W ? []["concat"](Ne["es"]("hookFuncs"), Ne["es"](W)) : [],
    yt = K ? []["concat"](Ne["es"]("elements"), Ne["es"](JSON["stringify"](K))) : [],
    St = q ? []["concat"](Ne["es"]("frontClientIp"), Ne["es"](q)) : [],
    _t = Z ? []["concat"](Ne["es"]("outterJs"), Ne["es"](Z)) : [],
    At = Q ? []["concat"](Ne["es"]("cssFeatures"), Ne["es"](Q)) : [],
    wt = $ ? []["concat"](Ne["es"]("webglFt"), Ne["es"]($)) : [],
    Tt = tt ? []["concat"](Ne["es"]("performanceTime"), Ne["es"](tt)) : [],
    Ot = et ? []["concat"](Ne["es"]("emptyEvalLength"), Ne["es"](et)) : [],
    Ct = nt ? []["concat"](Ne["es"]("errorFF"), Ne["es"](nt)) : [],
    Rt = rt ? []["concat"](Ne["es"]("headerCache"), Ne["es"](rt)) : [],
    Mt = ot ? []["concat"](Ne["es"]("fonts"), Ne["es"](ot)) : [],
    It = it ? []["concat"](Ne["es"]("h5Features"), Ne["es"](it)) : [],
    Nt = ut["concat"](ct, xt, st, ft, lt, dt, vt, ht, pt, mt, gt, Et, bt, yt, St, _t, At, wt, Tt, Ot, Ct, Rt, Mt, It),
    {
        "timeStamp": at,
        "result": "0a" + Ne["base64"](Ne["pako"](Nt))
    }) || {};

}
function _i(e,Ei) {
    var t;
    var n;
    var r;
    var o;
    var i;
    var a;
    var u;
    var c;
    var x;
    var s;
    var f;
    var l;
    var d;
    var v;
    var h;
    var p;
    var m;
    var g;
    var E;
    var b;
    var S;
    var y;
    var _;
    var A;
    var T;
    var w;
    var O;
    var C;
    var R;
    var M;
    var I;
    var N;
    var D;
    var H;
    var P;
    var B;
    var k;
    var X;
    var L;
    var F;
    var j;
    var U;
    var G;
    var W;
    var J;
    var V;
    var K;
    var z;
    var Y;
    var q;
    var Z;
    var $;
    var Q;
    var ee;
    var te;
    var ne;
    var re;
    var oe;
    var ie;
    var ae;
    var ue;
    var ce;
    var xe;
    var se;
    var fe;
    var le;
    var de;
    var ve;
    var he;
    var pe;
    var me;
    var ge;
    var Ee;
    var be;
    var Se;
    var ye;
    var _e;
    var Ae;
    var Te;
    var we;
    var Oe;
    var Ce;
    var Re;
    var Me;
    var Ie;
    var Ne;
    return (c = (u = e || {})["collectEvent"],
    x = u["isInterval"],
    s = void 0 !== x && x,
    f = Ei["rawData"],
    l = void 0 === f ? {} : f,
    d = Ei["localIp"],
    v = void 0 === d ? "undefined" : d,
    h = Ei["version"],
    p = void 0 === h ? "2.4.5" : h,
    m = Ei["app"],
    g = void 0 === m ? "h5Market" : m,
    E = Ei["FKGJ"],
    b = void 0 === E ? "undefined" : E,
    S = Ei["uid"],
    y = void 0 === S ? "undefined" : S,
    _ = Ei["moveData"],
    A = void 0 === _ ? [] : _,
    T = Ei["clickData"],
    w = void 0 === T ? [] : T,
    O = Ei["inputData"],
    C = void 0 === O ? [] : O,
    R = Ei["blurData"],
    M = void 0 === R ? [] : R,
    I = Ei["pasteData"],
    N = void 0 === I ? "0" : I,
    D = Ei["hasSensor"],
    H = Ei["isFront"],
    P = Ei["webGLInfos"],
    B = Ei["windowSize"],
    k = Ei["winSelenium"],
    X = Ei["chromium"],
    L = Ei["headlessByProperties"],
    F = Ei["languages"],
    j = Ei["consoleLied"],
    U = Ei["chromeExtensionScripts"],
    G = Ei["extensionImgs"],
    W = Ei["hookFuncs"],
    J = Ei["frontReferer"],
    V = Ei["elements"],
    K = void 0 === V ? {} : V,
    z = Ei["clientIp"],
    Y = void 0 === z ? void 0 : z,
    q = Ei["outterJs"],
    Z = void 0 === q ? JSON["stringify"]({}) : q,
    $ = Ei["cssFeatures"],
    Q = Ei["webglFt"],
    ee = Ei["performanceTime"],
    te = Ei["emptyEvalLength"],
    ne = Ei["errorFF"],
    re = Ei["headerCache"],
    oe = Ei["fonts"],
    ie = Ei["h5Features"],
    ae = String(Date["now"]()),
    ue = []["concat"](bt["es"]("isInterval"), bt["es"](String(!!s)), bt["es"]("rawData"), bt["es"](JSON["stringify"](l)), bt["es"]("localIp"), bt["es"](v), bt["es"]("reportTimestamp"), bt["es"](ae), bt["es"]("version"), bt["es"](p), bt["es"]("app"), bt["es"](g), bt["es"]("FKGJ"), bt["es"](b), bt["es"]("uid"), bt["es"](y), bt["es"]("hasCdc"), bt["es"]('false'), bt["es"]("electronCef"), bt["es"](un()), bt["es"]("frontReferer"), bt["es"](J)),
    ce = c ? []["concat"](bt["es"]("moveData"), bt["es"](JSON["stringify"](A)), bt["es"]("clickData"), bt["es"](JSON["stringify"](w)), bt["es"]("inputData"), bt["es"](JSON["stringify"](C)), bt["es"]("blurData"), bt["es"](JSON["stringify"](M)), bt["es"]("pasteData"), bt["es"](N)) : [],
    xe = D ? []["concat"](bt["es"]("hasSensor"), bt["es"](D)) : [],
    se = H ? []["concat"](bt["es"]("isFront"), bt["es"](H)) : [],
    fe = P ? []["concat"](bt["es"]("webGLInfos"), bt["es"](P)) : [],
    le = B ? []["concat"](bt["es"]("windowSize"), bt["es"](B)) : [],
    de = X ? []["concat"](bt["es"]("chromium"), bt["es"](X)) : [],
    ve = L ? []["concat"](bt["es"]("headlessByProperties"), bt["es"](L)) : [],
    he = k ? []["concat"](bt["es"]("winSelenium"), bt["es"](k)) : [],
    pe = F ? []["concat"](bt["es"]("languages"), bt["es"](F)) : [],
    me = j ? []["concat"](bt["es"]("consoleLied"), bt["es"](j)) : [],
    ge = U ? []["concat"](bt["es"]("injectScripts"), bt["es"](U)) : [],
    Ee = G ? []["concat"](bt["es"]("extensionImgs"), bt["es"](G)) : [],
    be = W ? []["concat"](bt["es"]("hookFuncs"), bt["es"](W)) : [],
    Se = K ? []["concat"](bt["es"]("elements"), bt["es"](JSON["stringify"](K))) : [],
    ye = Y ? []["concat"](bt["es"]("frontClientIp"), bt["es"](Y)) : [],
    _e = Z ? []["concat"](bt["es"]("outterJs"), bt["es"](Z)) : [],
    Ae = $ ? []["concat"](bt["es"]("cssFeatures"), bt["es"]($)) : [],
    Te = Q ? []["concat"](bt["es"]("webglFt"), bt["es"](Q)) : [],
    we = ee ? []["concat"](bt["es"]("performanceTime"), bt["es"](ee)) : [],
    Oe = te ? []["concat"](bt["es"]("emptyEvalLength"), bt["es"](te)) : [],
    Ce = ne ? []["concat"](bt["es"]("errorFF"), bt["es"](ne)) : [],
    Re = re ? []["concat"](bt["es"]("headerCache"), bt["es"](re)) : [],
    Me = oe ? []["concat"](bt["es"]("fonts"), bt["es"](oe)) : [],
    Ie = ie ? []["concat"](bt["es"]("h5Features"), bt["es"](ie)) : [],
    Ne = ue["concat"](ce, xe, se, fe, le, de, ve, he, pe, me, ge, Ee, be, Se, ye, _e, Ae, Te, we, Oe, Ce, Re, Me, Ie),
    {
        "timeStamp": ae,
        "result": "0a" + bt["base64"](bt["pako"](Ne))
    }) || {};

}

module.exports = Yi;
