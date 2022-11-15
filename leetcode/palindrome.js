var isPalindrome = function (string) {
  let start = 0;
  let end = string.length - 1;

  while (end > start) {
    if (string[start++] !== string[end--]) {
      return false;
    }
  }
  return true;
};

console.log(isPalindrome("1234"));
