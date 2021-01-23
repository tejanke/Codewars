#!/bin/bash
printerError() {
  PASS=[abcdefghijklm]
  ERROR=0
  TOTAL=0
  for i in $(seq 1 ${#1})
  do
    if [[ ${1:i-1:1} =~ $PASS ]]
    then
      ((ERROR=ERROR+0))
    else
      ((ERROR=ERROR+1))
    fi
    ((TOTAL=TOTAL+1))
  done
  echo $ERROR/$TOTAL
}
printerError $1