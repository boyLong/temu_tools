const zlib = require('./lib/24555');
const i = require('./lib/3')
var x = "keys", f = "indexOf", s = "bind",
        h = "shift", l = "join",
        k = "split", v = "replace", m = "slice",
        _ = "map", b = "toString", p = "parseInt",
        C = "now", g = "handleEvent", S = "fromCharCode",
        w = "substring", y = "userAgent", R = "pow", q = "random",
        O = "serverTime", G = "cookie", P = "addEventListener", Q = "document",
        z = "availHeight", F = "availWidth", J = "screen", K = "port",
        B = "href", L = "location", A = "timestamp", M = "clientY",
        V = "clientX", D = "elementId", j = "length", H = "concat",
        N = "forEach", Z = "push", T = "init", I = "data", U = 0,
        E = void 0, Y = void 0, X = 0, $ = [], tt = function () {
        }, nt = void 0, rt = void 0, et = void 0, ot = void 0, at = void 0, it = void 0
function st(t) {
    if (!t || !t[j])
        return [];
    var n = [];
    return t[N](function (t) {
        var r = i.sc(t[D]);
        n = n[H](i.va(t[V]), i.va(t[M]), i.va(t[A]), i.va(r[j]), r);
    }),
        n;
}

function anti(client,client2,track,location,screen,ServerTime,UpdateServerTime,UpdateFirstServerTime,UserAgent,nano,referrer,pdd_user_id,api_uid,pdd_vds,count,lt_c,gt_c,$) {
    /**
     *    client: {
     *             "elementId": "",
     *              "timestamp": 1627081,
     *              "clientX": 1352,
     *              "clientY": 303
     *             }
     *
     *    track: [
     *     {
     *         "elementId": "",
     *         "timestamp": 1688454,
     *         "clientX": 1317,
     *         "clientY": 918
     *     },
     *     {
     *         "elementId": "",
     *         "timestamp": 1699135,
     *         "clientX": 1909,
     *         "clientY": 229
     *     }
     * ]
     * ServerTime 默认879609302220
   */
    $ = $.map((e)=>{return String.fromCharCode(e)})
    console.log($)
    let vt = {}
    vt["data"] = Object.keys(client).length ? [client] : []
    vt["packN"] = function () {
        let n = {};
        return this[I][j] === 0 ? [] : [][H](i.ek(it ? 1 : 2, this[I]), st(this[I]));
    }
    var _t = {}
    _t["data"] = track,
    _t["maxLength"] = 30,
    _t["packN"] = function() {
          var n = {};
          var e = [];
          if (it) {
              e = this[I]["filter"](function(t) {
                  return t && t[j] > 0;
              });
              for (var o = 0, a = e[j] - 1; a >= 0; a--) {
                  o += e[a][j];
                  var u = o - this["maxLength"];
                  if (u > 0 && (e[a] = e[a][m](u)),
                  u >= 0) {
                      e = e[m](a);
                      break;
                  }
              }
          } else
              e = this[I];
          if (e[j] === 0)
              return [];
          var c = [][H](i.ek(it ? 24 : 25, e));
          return it ? e[N](function(n) {
              c = (c = c[H](i.va(n[j])))[H](st(n));
          }) : c = c[H](st(this[I])),
          c;
      }

    var lt={}
    lt["data"] =  Object.keys(client2).length ? [client2] : []
    lt["maxLength"] = 1, lt["init"] = function() {
        this.c = lt_c

    }

    lt["packN"] = function() {
          var n = {};
          if (this[I][j] === 0)
              return [];
          var e = [][H](i.ek(4, this[I]), st(this[I]));
          return e[H](this.c);
    }
    lt["init"]()

    var pt = {};
    pt.packN = function (){
        // 电脑端空
        return []
    }
    var gt = {}
    gt["init"] = function() {
                  var n = {};
                  var r = n;
                  this[I] = {},
                  this[I][B] = location[B],
                  this[I][K] = location[K]
                  this.c = gt_c


                  console.log(this.c)
                  }
              ,
    gt["packN"] = function() {
              var n = {};
              var e = i.ek(7)
                , o = this[I]
                , a = o.href
                , u = void 0 === a ? "" : a
                , c = o.port
                , W = void 0 === c ? "" : c;
              if (!u && !W)
                  return [][H](e, this.c);
              var x = u[j] > 128 ? u[m](0, 128) : u
                , f = i.sc(x);
              return [][H](e, i.va(f[j]), f, i.va(W[j]), W[j] === 0 ? [] : i.sc(this[I][K]), this.c);
          }
    gt["init"]()
    var wt = {}
    wt["init"] = function() {
      this[I] = {},
      this[I][F] = screen.availWidth,
      this[I][z] = screen.availHeight;
    }
    ,
    wt["packN"] = function() {
      return [][H](i.ek(8), i.va(this[I][F]), i.va(this[I][z]));
    }
    wt["init"]()
    ;
    Rt = {};
    Rt["init"] = function() {
          this[I] = parseInt(Math.random() * (Math.pow(2, 52) + 1)["toString"](), 10)
              + parseInt(Math.random() * (Math.pow(2, 30) + 1)["toString"](), 10) + "-" + (ServerTime || 879609302220);
    },
    Rt["packN"] = function() {
      this[T]()
      return [][H](i.ek(9, this[I]));
    }
    Rt.init()
    var Ot = {};
    Ot["data"] = [],
    Ot["init"] = function() {
      this[I] = [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                null,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0
            ];
    }
    ,
    Ot["packN"] = function() {
        var n = {};

        this[I][18] = 0
        for (var e = 0, o = 0; o < this[I][j]; o++)
          e += this[I][o] << o;
        return [][H](i.ek(10), i.va(e));
    }

    Ot["init"]()
    var Pt = {}
    Pt["init"] = function() {
      this[I] = i["pbc"](location.href ? location.href : "");
      }
      ,
    Pt["packN"] = function() {
        return this[I][b]()[j] ? [][H](i.ek(11), this[I]) : [];
    }
    Pt["init"]()

    var zt = {};
      zt["init"] = function() {
          var n = {};
          var r = n;
          this[I] = "y";
      }
      ,
      zt["packN"] = function() {
          return [][H](i.ek(12, this[I]));
      }
      zt["init"]()

     var Jt = {};
      Jt["init"] = function() {
          var n = {};
          var r = n;
          this[I] = "y" ;
      }
      ,
      Jt["packN"] = function() {
          return [][H](i.ek(13, this[I]));
      }
       Jt["init"]()

    var Bt = {};
    Bt["init"] = function() {
          var n = {};
          const r = n;
          this[I] = Date.now() - UpdateServerTime;

      },

    Bt["packN"] = function() {
          return this[T](),
          [][H](i.ek(14, this[I]));
    }
    Bt["init"]()
    var At = {}
    At["init"] = function() {

      this[I] = UserAgent;
    }
      ,
      At["packN"] = function() {
          return this[I][j] ? [][H](i.ek(15, this[I])) : [];
      }
      At["init"]()


     var Vt = {};
      Vt["init"] = function() {
          var n = {};
          this[I] = {
                    "nano_cookie_fp": nano,
                    "nano_storage_fp": nano
                };
      }
      ,
      Vt["packN"] = function() {
          var t = this
            , r = {};
          var e = r
            , o = []
            , a = {};
          return a["nano_cookie_fp"] = 16,
          a["nano_storage_fp"] = 17,
          Object[x](this[I])[N](function(n) {
              var r = [][H](t[I][n] ? i.ek(a[n], t[I][n]) : []);
              o[Z](r);
          }),
          o;
      }
      Vt["init"]()
      var jt = {};
      jt["init"] = function() {
          var n = {};
          var e = referrer || ""
            , o = e[f]("?");
          this[I] = e[m](0, o > -1 ? o : e[j]);
      },
      jt["packN"] = function() {
          return this[I][j] ? [][H](i.ek(18, this[I])) : [];
      }
      jt["init"]()
    var Nt = {};
     Nt["init"] = function() {
          var n = {};
          this[I] = pdd_user_id || "";
      }
      ,
      Nt["packN"] = function() {
          return this[I][j] ? [][H](i.ek(19, this[I])) : [];
      }
       Nt["init"]()

     var Tt = {};
      Tt["init"] = function() {
          var n = {};
          this[I] = api_uid || "";
      }
      ,
      Tt["packN"] = function() {
          return this[I][j] ? [][H](i.ek(20, this[I])) : [];
      }
      Tt["init"]()
      var Ut = {};
      Ut["data"] = count || 1,
      Ut["packN"] = function() {
          return [][H](i.ek(21, this[I]));
      }
      ;
      var Yt = {}
      Yt["init"] = function(t) {
              this[I] = t;
          }
          ,
      Yt["packN"] = function() {
          return [][H](i.ek(22, this[I]));
      }
      Yt["init"](UpdateFirstServerTime)
      var $t= {}
      $t["init"] = function() {
          var n = {};
          this[I] = pdd_vds || '';
      }
      ,
      $t["packN"] = function() {
          return this[I][j] ? [][H](i.ek(23, this[I])) : [];
      }
      ;
    $t["init"]()

      nn = {};
      nn["init"] = function() {
          var n = {};
          for (var e = [UserAgent["indexOf"](" OPR/") > -1 ? 1 : 0, 'undefined' !== "undefined" ? 1 : 0, false  ? 1 : 0, 0, false ? 1 : 0], a = 0, i = 0; i < e[j]; i++)
              a += e[i] << i;
          this[I] = a;
      }
      ,
      nn["packN"] = function() {
          return [][H](i.ek(26), i.va(this[I]));
      }
      nn.init()
      // if(!$){
      //    if (1){
      //         $ = [183, 185, 118, 34].map((t)=>{return String.fromCharCode(t)})
      //     }else{
      //         $ = ['\x9E', '\x82', '\x11', ',']
      //     }
      // }



      function get_anti(){
          var t, o = "packN";

          var u = (t = [])[H].apply(t, [vt[o](), _t[o](), lt[o](), pt[o](), gt[o](), wt[o](), Rt[o](), Ot[o](), Pt[o](), zt[o](), Jt[o](), Bt[o](), At[o]()].concat(function(t) {
            if (Array.isArray(t)) {
                for (var n = 0, r = Array(t.length); n < t.length; n++)
                    r[n] = t[n];
                return r
            }
            return Array.from(t)
          }(Vt[o]()), [jt[o](), Nt[o](), Tt[o](), Ut[o](), Yt[o](), $t[o](), nn[o]()]))
         for (var c = u[j][b](2)[k](""), W = 0; c[j] < 16; W += 1)
                      c["unshift"]("0");
         c = c[l]("");
         var x = [];


         u[j] === 0 ? x[Z](0, 0) : u[j] > 0 && u[j] <= (1 << 8) - 1 ? x[Z](0, u[j]) : u[j] > (1 << 8) - 1 && x[Z](parseInt(c[w](0, 8), 2), parseInt(c[w](8, 16), 2))
            ,
          u = [][H]([3], [1, 0, 0], x, u);
          var f = zlib["deflate"](u)
            , s = [][_]["call"](f, function(t) {
              return String[S](t);
          });

         return  "0aq" + i["encode"](s[l]("") + $[l](""), i["budget"])



      }

      return get_anti()
}

module.exports = anti
