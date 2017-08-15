##
## OPIERDALACZ EKRANIKU MICRO DOT PHAT
##                (c)P1X
##

import time
import random
import microdotphat as dot


logo_time = 10
delay_time = 0
delay_time_max = 400

loading = ['P',
	   'P1',
	   'P1X',
	   'P1X_',
	   'P1X__',
	   'P1X___',
	   '_LOAD_']
msg = '      - -=<<+<   P 1 X   >+>>=- -      visit ---> HTTP://P1X.IN   - -=<+>=- -  Inde Games  - -=<+>=- -  Source Code  - -=<+>=- -  Pixel Art  - -=<+>=- -  GODOT ENGiNE  - -=<+>=- -  PiCO-8  - -=<+>=- -     '


dot.clear()
dot.set_rotate180(True)

for str in loading:
	dot.write_string(str, kerning=False)
	dot.show()
	time.sleep(0.2)

dot.clear()
dot.write_string(msg)
dot.show()

while True:
    dot.scroll()
    dot.show()
	
