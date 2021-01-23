function UnluckyDays([int] $year) {
    $result = 0
    for ($month = 1; $month -le 12; $month++) {
      if ((get-date -year $year -month $month -day 13).dayofweek -eq "Friday") {
        $result += 1
      }
    }
    return $result
  }