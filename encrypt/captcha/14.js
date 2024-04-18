module["exports"] = function (t, e, n, r) {
    for (var i = 65535 & t | 0, o = t >>> 16 & 65535 | 0, a = 0; 0 !== n;) {
      n -= a = n > 2e3 ? 2e3 : n;
      do {
        o = o + (i = i + e[r++] | 0) | 0;
      } while (--a);
      i %= 65521, o %= 65521;
    }
    return i | o << 16 | 0;
}