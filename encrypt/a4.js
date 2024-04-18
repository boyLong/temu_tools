

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
var St = {
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
    p = void 0 === h ? "2.3.6" : h,
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
    ue = []["concat"](St.es("isInterval"), St.es(String(!!s)), St.es("rawData"), St.es(JSON.stringify(l)), St.es("localIp"), St.es(v), St.es("reportTimestamp"), St.es(ae), St.es("version"), St.es(p), St.es("app"), St.es(g), St.es("FKGJ"), St.es(S), St.es("uid"), St.es(y), St.es("hasCdc"), St.es("false"), St.es("electronCef"), St.es(un()), St.es("frontReferer"), St.es(Z)),
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


module.exports = Ei;
