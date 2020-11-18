function Get-SumOfPositive($NumberArray)
{
    $Result = 0
    foreach ($Num in $NumberArray) {
        if ($Num -gt 0) {
            $Result += $Num
        }
    }
    return $Result
}
