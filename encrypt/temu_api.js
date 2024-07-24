const express = require("express")
const encode = require('./lib/3.js');
var bodyParser = require("body-parser")

const captcha_encrypt = require("./captcha/captcha_encrypt");

var a4 = require("./a4")
var anti = require("./anti")
const app = express()
const port = 8980
// const nano_gen = require("./nano")
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json({limit: '10mb',extended: true}));
app.use(express.json())

app.post('/anti', async (req, res) => {
    // console.log(req.body)
    var client = req.body.client
    var client2 = req.body.client2 || {}
    var track = req.body.track
    var location = req.body.location
    var screen = req.body.screen
    var ServerTime = req.body.ServerTime
    var UpdateServerTime = req.body.UpdateServerTime
    var UpdateFirstServerTime = req.body.UpdateFirstServerTime || + new Date();
    var UserAgent = req.body.UserAgent
    var nano = req.body.nano
    var referrer = req.body.referrer
    var pdd_user_id = req.body.pdd_user_id
    var api_uid = req.body.api_uid
    var pdd_vds = req.body.pdd_vds
    var count = req.body.count
    var lt_c = req.body.lt_c
    var gt_c = req.body.gt_c
    var $ = req.body._
    try{

        var result = anti(client,client2,track,location,screen,ServerTime,UpdateServerTime,UpdateFirstServerTime,UserAgent,nano,referrer,pdd_user_id,api_uid,pdd_vds,count,lt_c,gt_c,$)
        res.json({"code":0,"msg":"成功",'data':result})
    }catch {
        res.json({"code":-1,"msg":"失败",'data':""})
    }
})

app.post('/device', async (req, res) => {
    var hi = req.body.device
    // try {
    res.json({
        "code": 0, "msg": "成功", 'data': a4({}, hi)
    })
    // } catch {
    //      res.json({
    //                 "code": -1, "msg": "失败", 'data': ""
    //         })
    // }
})


app.get('/nano', async (req, res) => {
    u = function (t, n, r) {
        if ("string" != typeof t)
            throw new Error("The string parameter must be a string.");
        if (t.length < 1)
            throw new Error("The string parameter must be 1 character or longer.");
        if ("number" != typeof n)
            throw new Error("The length parameter must be a number.");
        if ("string" != typeof r && r)
            throw new Error("The character parameter must be a string.");
        var e = -1;
        for (n -= t.length, r || 0 === r || (r = " "); ++e < n; ) t += r;
        return t;
    };
    i = function (t) {
        t = t || 21;
        for (var n = ""; 0 < t--; )
            n += "_~varfunctio0125634789bdegjhklmpqswxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"[
                (64 * Math.random()) | 0
            ];
        return n;
    };
    function p() {
        var t =
                arguments.length > 0 && void 0 !== arguments[0]
                    ? arguments[0]
                    : Date["now"](),
            r = {};
        var o = String(t)["slice"](0, 10),
            c = i(),
            d =
                (o + "_" + c)["split"]("")["reduce"](function (t, r) {
                    return t + r["charCodeAt"](0);
                }, 0) % 1e3,
            s = u(String(d), 3, "0");
        return encode["encode"]("" + o + s)["replace"](/=/g, "") + "_" + c;
    }

    try {
        res.json({"code":0,"msg":"成功",'data': p()})
    }catch {
        res.json({"code": -1,"msg":"失败",'data': -1})
    }
})


app.post("/captcha_encrypt",async (req,res)=>{
    try{
        var data = captcha_encrypt(req.body.data,req.body.init)
        res.json({
            "data": data,
            "ok":true
        })
    }catch{
        res.json({
            "data": "",
            "ok": false
        })
    }
}
)

app.post("/crc32",async (req,res)=>{

    var data = encode.crc32(req.body.data,)
    try {
        res.json({
            "data": data,
            "ok":true
        })
     }catch {
            res.json({
                "data": "",
                "ok": false
            })
        }
    }
)


app.listen(port, "0.0.0.0", async () => {
 console.log(`Example app listening at http://0.0.0.0:${port}`)
})
