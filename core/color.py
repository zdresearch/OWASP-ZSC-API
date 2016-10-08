#!/usr/bin/env python
'''
OWASP ZSC
https://www.owasp.org/index.php/OWASP_ZSC_Tool_Project
https://github.com/zscproject/OWASP-ZSC
http://api.z3r0d4y.com/
https://groups.google.com/d/forum/owasp-zsc [ owasp-zsc[at]googlegroups[dot]com ]
'''
#bug fix reported by John Babio in version 1.0.4 johndbabio/[at]/gmail/./com
from core import compatible
os_name = compatible.os_name()


def color(color):
	return ''
