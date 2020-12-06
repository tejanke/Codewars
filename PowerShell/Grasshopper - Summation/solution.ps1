function Summation([int] $n) {
  $count = 0
  for ($i = 1; $i -le $n; $i++) {
    $count += $i
  }
  return $count
}
