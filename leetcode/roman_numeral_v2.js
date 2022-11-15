var romanToInt = function (s) {
  var dict = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  var answer = 0,
    prev = 0,
    current = 0;

  for (let i = s.length - 1; i >= 0; i--) {
    current = dict[s[i]];
    if (current < prev) {
      answer -= current;
    } else {
      answer += current;
    }
    prev = current;
  }
  return answer;
};

console.log(romanToInt("MCMXCIV"));
console.log(romanToInt("LVIII"));
console.log(romanToInt("III"));
