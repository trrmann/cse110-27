#!/usr/bin/bash.exe
if [[ -d /c/Users/Public/OneDrive/Documents/Projects/BYU-I/cse110-27/profile.d ]];
then
  PROFILE_SHELLS=`ls /c/Users/Public/OneDrive/Documents/Projects/BYU-I/cse110-27/profile.d/*.sh 2>/dev/null|wc -l`
  if [[ ${PROFILE_SHELLS} == "" ]];
  then
    echo > /dev/null
  elif [[ ${PROFILE_SHELLS} -gt 0 ]];
  then
    for cse110_27ProfileFile in `ls /c/Users/Public/OneDrive/Documents/Projects/BYU-I/cse110-27/profile.d/*.sh`
    do
      source ${cse110_27ProfileFile};
    done;
  fi
fi