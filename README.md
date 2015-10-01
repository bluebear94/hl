## hl

a kanji highlighter

I wanted to see how many hyōgai kanji I was using in CY character names for the lulz, so I whipped up a .txt to .html converter.

### How to Run

To generate kanjidic-utf8.txt:

    ./conv.sh

To generate kls.txt:

    python3 cn.py

To generate an HTML file:

    python3 hl.py < in.txt > out.html

### Licenses

KANJIDIC/KANJD212 files by ERDG under [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/). As a consequence, kanjidic-utf8.txt, which includes data from both files, and kls.txt, are under the same license.