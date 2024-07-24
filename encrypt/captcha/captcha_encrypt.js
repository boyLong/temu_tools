const d = require("./11"); 
const get_aes_key = require("./get_aes_key"); 
const aes = require("./10")
const c  = require("./3")

function captcha_encrypt(data,init){

    function p(e, t, n) {
        return t && n ? aes.encrypt(e, c["parse"](t), {
            iv: c.parse(n)
        })["toString"]() : e;
    }
    var ase_key = get_aes_key(init)
    return p(d.gzip(JSON["stringify"](data), {
        "to": "string"
    }), ase_key.aes_key, ase_key.aes_iv);
  
}

module.exports = captcha_encrypt
a = get_aes_key({"serverTime":"1703502393945","salt":"a13029a25"})
console.log(a)