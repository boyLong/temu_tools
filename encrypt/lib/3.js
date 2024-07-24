
 crc32 = function(t) {
    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : 0;
    t = function(t) {
        for (var n = "", r = 0; r < t.length; r++) {
            var e = t.charCodeAt(r);
            e < 128 ? n += String.fromCharCode(e) : e < 2048 ? n += String.fromCharCode(192 | e >> 6) + String.fromCharCode(128 | 63 & e) : e < 55296 || e >= 57344 ? n += String.fromCharCode(224 | e >> 12) + String.fromCharCode(128 | e >> 6 & 63) + String.fromCharCode(128 | 63 & e) : (e = 65536 + ((1023 & e) << 10 | 1023 & t.charCodeAt(++r)),
            n += String.fromCharCode(240 | e >> 18) + String.fromCharCode(128 | e >> 12 & 63) + String.fromCharCode(128 | e >> 6 & 63) + String.fromCharCode(128 | 63 & e))
        }
        return n
    }(t),
    n ^= -1;
    for (var r = 0; r < t.length; r++)
        n = n >>> 8 ^ e[255 & (n ^ t.charCodeAt(r))];
    return (-1 ^ n) >>> 0
}
            ;
var e = function() {
    for (var t = [], n = void 0, r = 0; r < 256; r++) {
        n = r;
        for (var e = 0; e < 8; e++)
            n = 1 & n ? 3988292384 ^ n >>> 1 : n >>> 1;
        t[r] = n
    }
    return t
}()
i = crc32
var o=function(t) {
    return typeof t
},
a=function(t, n, r) {
    var e = ["", " ", "  ", "   ", "    ", "     ", "      ", "       ", "        ", "         "]
    if ((n -= (t += "").length) <= 0)
        return t;
    if (r || 0 === r || (r = " "),
    " " == (r += "") && n < 10)
        return e[n] + t;
    for (var o = ""; 1 & n && (o += r),
    n >>= 1; )
        r += r;
    return o + t
},W = "join", d = "ceil", x = "split", f = "replace", s = "slice", h = "map", l = "unshift", k = "toString", v = "parseInt", m = "substring", _ = "charCodeAt", b = "length", p = "concat", C = "push", g = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"[x](""), S = {
      "+": "-",
      "/": "_",
      "=": ""
}, y = parseInt;
R = {
      crc32 : crc32,
      base64: function(t) {
          var r = {};
          for (var o = void 0, a = void 0, i = void 0, u = "", W = t[b], d = 0, x = y(W / 3) * 3; d < x; )
              o = t[d++],
              a = t[d++],
              i = t[d++],
              u += g[o >>> 2] + g[(o << 4 | a >>> 4) & 63] + g[(a << 2 | i >>> 6) & 63] + g[i & 63];
          var f = W - x;
          return f === 1 ? (o = t[d],
          u += g[o >>> 2] + g[o << 4 & 63] + "==") : f === 2 && (o = t[d++],
          a = t[d],
          u += g[o >>> 2] + g[(o << 4 | a >>> 4) & 63] + g[a << 2 & 63] + "="),
          w(u);
      },
      charCode: function(t) {
          var r = {};
          for (var o = [], a = 0, i = 0; i < t[b]; i += 1) {
              var u = t[_](i);
              u >= 0 && u <= 127 ? (o[C](u),
              a += 1) : 128 <= 80 && u <= 2047 ? (a += 2,
              o[C](192 | 31 & u >> 6),
              o[C](128 | 63 & u)) : (u >= 2048 && u <= 55295 || u >= 57344 && u <= 65535) && (a += 3,
              o[C](224 | 15 & u >> 12),
              o[C](128 | 63 & u >> 6),
              o[C](128 | 63 & u));
          }
          for (var W = 0; W < o[b]; W += 1)
              o[W] &= 255;
          return a <= 255 ? [0, a][p](o) : [a >> 8, a & 255][p](o);
      },
      es: function(t) {
          t || (t = "");
          var r = t[m](0, 255)
            , e = []
            , o = R["charCode"](r)[s](2);
          return e[C](o[b]),
          e[p](o);
      },
      en: function(t) {
          var r = {};
          t || (t = 0);
          var o = y(t)
            , a = [];
          o > 0 ? a[C](0) : a[C](1);
          for (var i = Math["abs"](o)[k](2)[x](""), u = 0; i[b] % 8 !== 0; u += 1)
              i[l]("0");
          i = i[W]("");
          for (var f = Math[d](i[b] / 8), s = 0; s < f; s += 1) {
              var h = i[m](s * 8, (s + 1) * 8);
              a[C](y(h, 2));
          }
          var v = a[b];
          return a[l](v),
          a;
      },
      sc: function(t) {
          var r = {};
          t || (t = "");
          var e = t[b] > 255 ? t[m](0, 255) : t;
          return R["charCode"](e)[s](2);
      },
      nc: function(t) {
          var r = {};
          t || (t = 0);
          var o = Math["abs"](y(t))[k](2)
            , i = Math[d](o[b] / 8);
          o = a(o, i * 8, "0");
          for (var u = [], W = 0; W < i; W += 1) {
              var x = o[m](W * 8, (W + 1) * 8);
              u[C](y(x, 2));
          }

          return u;
      },
      va: function(t) {
          var r = {};
          t || (t = 0);
          for (var o = Math["abs"](y(t)), i = o[k](2), u = [], W = (i = a(i, Math[d](i[b] / 7) * 7, "0"))[b]; W >= 0; W -= 7) {
              var x = i[m](W - 7, W);
              if ((o & -128) === 0) {
                  u[C]("0" + x);
                  break;
              }
              u[C]("1" + x),
              o = o >>> 7;
          }
          return u[h](function(t) {
              return y(t, 2);
          });
      },
      ek: function(t) {
          var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : ""
            , e = {};
          if (!t)
              return [];
          var u = []
            , W = 0;
          n !== "" && (Object["prototype"][k]["call"](n) === "[object Array]" && (W = n[b]),
          (void 0 === n ? "undefined" : o(n)) === "string" && (W = (u = R.sc(n))[b]),
          (void 0 === n ? "undefined" : o(n)) === "number" && (W = (u = R.nc(n))[b]));
          var d = Math["abs"](t)[k](2)
            , x = "";
          x = W > 0 && W <= 7 ? d + a(W[k](2), 3, "0") : d + "000";
          var f = [y(x[s](Math["max"](x[b] - 8, 0)), 2)];
          return W > 7 ? f[p](R.va(W), u) : f[p](u);
      },
      ecl: function(t) {
          var r = {};
          for (var o = [], a = t[k](2)[x](""), i = 0; a[b] < 16; i += 1)
              a[l](0);
          return a = a[W](""),
          o[C](y(a[m](0, 8), 2), y(a[m](8, 16), 2)),
          o;
      },
      pbc: function() {
          var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : ""
            , r = {};
          var o = []
            , a = R.nc(crc32(t[f](/\s/g, "")));
          if (a[b] < 4)
              for (var u = 0; u < 4 - a[b]; u++)
                  o[C](0);
          return o[p](a);
      },
      gos: function(t, n) {
          var e = {};
          var a = Object["keys"](t)[h](function(n) {
              return n === "data" || n === "c" ? "" : n + ":" + t[n][k]() + ",";
          })[W]("");
          return "const " + n + "={" + a + "}";
      },
      budget: function(t, n) {
          var e = {};
          return t === 64 ? 64 : t === 63 ? n : t >= n ? t + 1 : t;
      },
      encode: function(t, n) {
          var e = {};
          for (var a, i, u, W, x = {
              "_bÇ": t,
              _bK: 0,
              _bf: function() {
                  return t[_](x["_bK"]++);
              }
          }, s = {
              "_ê": [],
              "_bÌ": -1,
              "_á": function(t) {
                  s["_bÌ"]++,
                  s["_ê"][s["_bÌ"]] = t;
              },
              "_bÝ": function() {
                  return _bÝ["_bÌ"]--,
                  _bÝ["_bÌ"] < 0 && (_bÝ["_bÌ"] = 0),
                  _bÝ["_ê"][_bÝ["_bÌ"]];
              }
          }, h = "", l = "9240gsB6PftGXnlQTw_pdvz7EekDmuAWCVZ5UF-MSK1IHOchoaxqYyj8Jb3LrNiR", k = 0; k < l[b]; k++)
              s["_á"](l["charAt"](k));
          s["_á"]("=");
          var v = (void 0 === n ? "undefined" : o(n)) !== "undefined" ? Math["floor"](Math["random"]() * 64) : -1;
          for (k = 0; k < t[b]; k = x["_bK"])
              for (var m = "9|2|5|3|0|7|1|4|6|10|8"["split"]("|"), p = 0; ; ) {
                  switch (m[p++]) {
                  case "0":
                      i = (s["_ê"][s["_bÌ"] - 2] & 3) << 4 | s["_ê"][s["_bÌ"] - 1] >> 4;
                      continue;
                  case "1":
                      W = s["_ê"][s["_bÌ"]] & 63;
                      continue;
                  case "2":
                      s["_á"](x["_bf"]());
                      continue;
                  case "3":
                      a = s["_ê"][s["_bÌ"] - 2] >> 2;
                      continue;
                  case "4":
                      isNaN(s["_ê"][s["_bÌ"] - 1]) ? u = W = 64 : isNaN(s["_ê"][s["_bÌ"]]) && (W = 64);
                      continue;
                  case "5":
                      s["_á"](x["_bf"]());
                      continue;
                  case "6":
                      (void 0 === n ? "undefined" : o(n)) !== "undefined" && (a = n(a, v),
                      i = n(i, v),
                      u = n(u, v),
                      W = n(W, v));
                      continue;
                  case "7":
                      u = (s["_ê"][s["_bÌ"] - 1] & 15) << 2 | s["_ê"][s["_bÌ"]] >> 6;
                      continue;
                  case "8":
                      h = h + s["_ê"][a] + s["_ê"][i] + s["_ê"][u] + s["_ê"][W];
                      continue;
                  case "9":
                      s["_á"](x["_bf"]());
                      continue;
                  case "10":
                      s["_bÌ"] -= 3;
                      continue;
                  }
                  break;
              }
          return h[f](/=/g, "") + (l[v] || "");
      }
  }


module["exports"] = R;
console.log(R.ek('1',123))