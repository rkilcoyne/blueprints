#!/bin/bash
REPO_URL="{{ YUM_REPO_URL }}"
export PATH=/usr/bin:/sbin
dnf-3 config-manager --add-repo $REPO_URL