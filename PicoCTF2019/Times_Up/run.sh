#!/bin/bash
coproc /problems/time-s-up_2_af1f9d8c14e16bcbe591af8b63f7e286/times-up
read LINE <&${COPROC[0]}
echo $(echo ${LINE:11} | bc) >&${COPROC[1]}
cat <&${COPROC[0]}