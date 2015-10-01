#!/bin/bash

iconv -f EUC-JIS-2004 kanjidic.gz > kanjidic-utf8.txt
cp kanjd212.gz kanjd212.txt
recode EUC-JP..UTF-8 kanjd212.txt
cat kanjd212.txt >> kanjidic-utf8.txt
rm kanjd212.txt