function XO(str) {
  var i;
  var xCounter = 0;
  var oCounter = 0;
  for (i = 0; i < str.length; i++) {
    console.log(str[i].toLowerCase())
    if (str[i].toLowerCase() == "x") {
      xCounter++;
    }
    if (str[i].toLowerCase() == "o") {
      oCounter++;
    }
  }
  if (oCounter == xCounter) {
    return true
  }
  else {
    return false
  }
}
