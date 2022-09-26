#!/usr/bin/bash.exe
CALLED=$0
#echo $CALLED
STATUS=`git status | grep "nothing to commit" | wc -l`
if [[ ${STATUS} -eq 0 ]];
then
  git commit -a -m "deployed"
  git push
  git pull
fi
exit 0