#!/bin/bash

$(dirname "$0")/DevelopmentSetupScripts/SetupHooks.sh
## Add ssh commit reference
git remote -v |grep sshupstream > /dev/null 2>&1
if [[ $? -ne 0 ]] ;then
    git remote add sshupstream git@github.com:InsightSoftwareConsortium/SimpleITK-Notebook-Answers.git
fi
