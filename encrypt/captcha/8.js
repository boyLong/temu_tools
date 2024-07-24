

function a(e){
    return typeof e
}

var r, i, o, c, u=function(t) {
    return a(t);
}

c = function(t) {
    var e, n, r, i, o, c, u, f, x, d, l, h, v, p, y, m, b, g;
    t["lib"]["Cipher"] || (r = (n = (e = t)["lib"])["Base"],
    i = n["WordArray"],
    o = n["BufferedBlockAlgorithm"],
    (c = e["enc"])["Utf8"],
    u = c["Base64"],
    f = e["algo"]["EvpKDF"],
    x = n.Cipher = o["extend"]({
        cfg: r["extend"](),
        createEncryptor: function(t, e) {
            return this.create(this["_ENC_XFORM_MODE"], t, e);
        },
        createDecryptor: function(t, e) {
            return this["create"](this["_DEC_XFORM_MODE"], t, e);
        },
        init: function(t, e, n) {
            this["cfg"] = this.cfg.extend(n),
            this._xformMode = t,
            this._key = e,
            this["reset"]();
        },
        reset: function() {
            o.reset["call"](this),
            this["_doReset"]();
        },
        process: function(t) {
            return this["_append"](t),
            this["_process"]();
        },
        finalize: function(t) {
            return t && this["_append"](t),
            this["_doFinalize"]();
        },
        keySize: 4,
        ivSize: 4,
        _ENC_XFORM_MODE: 1,
        _DEC_XFORM_MODE: 2,
        _createHelper: function() {
            function t(t) {
                return a(t) == "string" ? g : m;
            }
            return function(e) {
                return {
                    encrypt: function(n, r, i) {
                        return t(r).encrypt(e, n, r, i);
                    },
                    decrypt: function(n, r, i) {
                        return t(r)["decrypt"](e, n, r, i);
                    }
                };
            }
            ;
        }()
    }),
    n["StreamCipher"] = x.extend({
        _doFinalize: function() {
            return this["_process"](!!"flush");
        },
        blockSize: 1
    }),
    d = e["mode"] = {},
    l = n["BlockCipherMode"] = r["extend"]({
        createEncryptor: function(t, e) {
            return this.Encryptor["create"](t, e);
        },
        createDecryptor: function(t, e) {
            return this["Decryptor"].create(t, e);
        },
        init: function(t, e) {
            this._cipher = t,
            this["_iv"] = e;
        }
    }),
    h = d["CBC"] = function() {
        var t = l["extend"]();
        function e(t, e, n) {
            var r = this["_iv"];
            if (r) {
                var i = r;
                this["_iv"] = undefined;
            } else
                i = this["_prevBlock"];
            for (var o = 0; o < n; o++)
                t[e + o] ^= i[o];
        }
        return t["Encryptor"] = t["extend"]({
            processBlock: function(t, n) {
                var r = this["_cipher"]
                  , i = r["blockSize"];
                e["call"](this, t, n, i),
                r["encryptBlock"](t, n),
                this["_prevBlock"] = t["slice"](n, n + i);
            }
        }),
        t["Decryptor"] = t.extend({
            processBlock: function(t, n) {
                var r = this._cipher
                  , i = r.blockSize
                  , o = t["slice"](n, n + i);
                r["decryptBlock"](t, n),
                e["call"](this, t, n, i),
                this["_prevBlock"] = o;
            }
        }),
        t;
    }(),
    v = (e["pad"] = {})["Pkcs7"] = {
        pad: function(t, e) {
            for (var n = 4 * e, r = n - t["sigBytes"] % n, o = r << 24 | r << 16 | r << 8 | r, a = [], c = 0; c < r; c += 4)
                a["push"](o);
            var u = i.create(a, r);
            t["concat"](u);
        },
        unpad: function(t) {
            var e = 255 & t["words"][t.sigBytes - 1 >>> 2];
            t.sigBytes -= e;
        }
    },
    n.BlockCipher = x["extend"]({
        cfg: x["cfg"]["extend"]({
            mode: h,
            padding: v
        }),
        reset: function() {
            x.reset["call"](this);
            var t = this["cfg"]
              , e = t.iv
              , n = t["mode"];
            if (this._xformMode == this["_ENC_XFORM_MODE"])
                var r = n.createEncryptor;
            else
                r = n.createDecryptor,
                this["_minBufferSize"] = 1;
            this._mode && this["_mode"].__creator == r ? this["_mode"]["init"](this, e && e.words) : (this["_mode"] = r["call"](n, this, e && e["words"]),
            this["_mode"]["__creator"] = r);
        },
        _doProcessBlock: function(t, e) {
            this["_mode"].processBlock(t, e);
        },
        _doFinalize: function() {
            var t = this["cfg"]["padding"];
            if (this["_xformMode"] == this["_ENC_XFORM_MODE"]) {
                t["pad"](this["_data"], this["blockSize"]);
                var e = this["_process"](!!"flush");
            } else
                e = this["_process"](!!"flush"),
                t["unpad"](e);
            return e;
        },
        blockSize: 4
    }),
    p = n["CipherParams"] = r["extend"]({
        init: function(t) {
            this["mixIn"](t);
        },
        toString: function(t) {
            return (t || this["formatter"])["stringify"](this);
        }
    }),
    y = (e.format = {})["OpenSSL"] = {
        stringify: function(t) {
            var e = t.ciphertext
              , n = t.salt;
            if (n)
                var r = i["create"]([1398893684, 1701076831])["concat"](n).concat(e);
            else
                r = e;
            return r["toString"](u);
        },
        parse: function(t) {
            var e = u["parse"](t)
              , n = e["words"];
            if (1398893684 == n[0] && 1701076831 == n[1]) {
                var r = i["create"](n["slice"](2, 4));
                n["splice"](0, 4),
                e["sigBytes"] -= 16;
            }
            return p["create"]({
                ciphertext: e,
                salt: r
            });
        }
    },
    m = n["SerializableCipher"] = r.extend({
        cfg: r["extend"]({
            format: y
        }),
        encrypt: function(t, e, n, r) {
            r = this.cfg["extend"](r);
            var i = t["createEncryptor"](n, r)
              , o = i["finalize"](e)
              , a = i.cfg;
            return p.create({
                ciphertext: o,
                key: n,
                iv: a.iv,
                algorithm: t,
                mode: a["mode"],
                padding: a["padding"],
                blockSize: t["blockSize"],
                formatter: r["format"]
            });
        },
        decrypt: function(t, e, n, r) {
            return r = this["cfg"]["extend"](r),
            e = this["_parse"](e, r["format"]),
            t["createDecryptor"](n, r)["finalize"](e["ciphertext"]);
        },
        _parse: function(t, e) {
            return a(t) == "string" ? e["parse"](t, this) : t;
        }
    }),
    b = (e["kdf"] = {})["OpenSSL"] = {
        execute: function(t, e, n, r) {
            r || (r = i.random(8));
            var o = f["create"]({
                keySize: e + n
            })["compute"](t, r)
              , a = i["create"](o["words"]["slice"](e), 4 * n);
            return o.sigBytes = 4 * e,
            p["create"]({
                key: o,
                iv: a,
                salt: r
            });
        }
    },
    g = n.PasswordBasedCipher = m["extend"]({
        cfg: m.cfg.extend({
            kdf: b
        }),
        encrypt: function(t, e, n, r) {
            var i = (r = this.cfg.extend(r))["kdf"]["execute"](n, t["keySize"], t["ivSize"]);
            r.iv = i.iv;
            var o = m["encrypt"]["call"](this, t, e, i.key, r);
            return o["mixIn"](i),
            o;
        },
        decrypt: function(t, e, n, r) {
            r = this.cfg["extend"](r),
            e = this["_parse"](e, r["format"]);
            var i = r["kdf"]["execute"](n, t.keySize, t["ivSize"], e.salt);
            return r.iv = i.iv,
            m["decrypt"]["call"](this, t, e, i["key"], r);
        }
    }));
}
,
module["exports"] = e = c(require("./0"), require("./1"))