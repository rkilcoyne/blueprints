#!/bin/bash
setenforce permissive
sed -i 's/enforcing/permissive/g' /etc/selinux/config /etc/selinux/config