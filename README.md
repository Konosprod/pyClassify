pyClassify
==========

A small program written in python which tidy directories following a set of rules. Rules are based on the mime type.

How to use ?
------------
pyclassify.py [option]

optional arguments : 
  -h show the help message and exit
  -p print the current ruleset
  -a add couples to the ruleset. Example : -a mime1 dir1 mime2 dir2
  -f specify the file where are stored the rules
  -c specify the directory to clean, if not present on the command line, "." will be cleaned
