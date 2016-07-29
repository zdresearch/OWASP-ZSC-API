#!/usr/bin/python
'''
OWASP ZSC | ZCR Shellcoder

ZeroDay Cyber Research
Z3r0D4y.Com
Ali Razmjoo
'''
import cgi,os,sys,string
import cgitb; cgitb.enable()
import sys
import os
from core.update import _update
from lib.shell_storm_api.grab import _search_shellcode
from lib.shell_storm_api.grab import _download_shellcode
from lib.shell_storm_api.grab import _grab_all
from core.obfuscate import obf_code
from core.encode import encode_process
from core.opcoder import op
from core.file_out import file_output
exec (compile(
    open(
        str(os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')) +
        '/core/commands.py', "rb").read(), str(os.path.dirname(os.path.abspath(
            __file__)).replace('\\', '/')) + '/core/commands.py', 'exec'))
exec (compile(
	open(
		str(os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')) +
		'/core/start.py', "rb").read(), str(os.path.dirname(os.path.abspath(
			__file__)).replace('\\', '/')) + '/core/start.py', 'exec'))
print 'Content-type: text/html\nAPI-SERVER: ZERODAY CYBER RESEARCH\nAdmin: Ali@Z3r0d4y.Com\n'
form = cgi.FieldStorage()
api = form.getvalue("api_name")
if api == None:
        print '''Hello, Please Visit <a href="https://github.com/zscproject/OWASP-ZSC/wiki">WIKI</a> to know about this API server.<br>
Please report problems to Admin, Thank you.<br>
<a href="mailto:ali[dot]razmjoo[at]owasp[dot]org">Ali Razmjoo</a>'''

elif api == 'zsc':
	mypayload = form.getvalue("payload")
	myinput = form.getvalue("input")
	asm_code = form.getvalue("asm_code")
	if mypayload != None and myinput != None:
		payloads = _show_payloads(commands,True)
		if len(payloads) is 0:
			print 'no payload found!'
			sys.exit(0)
			
		if len(mypayload.rsplit('/')) is 2:	
			if mypayload in _show_payloads(commands,True):
				filename = myinput
				language = mypayload.rsplit('/')[0]
				encode = mypayload.rsplit('/')[1]
				try:
					content = myinput
				except:
					warn('sorry, cann\'t find file\n')
					sys.exit(0)
				info('Obfuscated Code is:\n\n' + obf_code(language, encode, filename, content,True) +
							 '\n\n')
		if len(mypayload.rsplit('/')) is 3:
			os = mypayload.rsplit('/')[0]
			func = mypayload.rsplit('/')[1]
			encode = mypayload.rsplit('/')[2]
			encode_tmp = mypayload.rsplit('/')[2][:3]
			data = myinput.rsplit('~~~')
			payload_tmp = os+'/'+func+'/'+encode_tmp
			payload_flag = False
			for _ in _show_payloads(commands,True):
				if payload_tmp in _:
					payload_flag = True
			if payload_flag is True:
				run = getattr(
					__import__('lib.generator.%s.%s' % (os, func),
							   fromlist=['run']),
					'run')
				shellcode = run(data)
				try:
					asm_code = int(asm_code)
				except:
					asm_code = 'nop'
				if asm_code == 1:
					info('Generated shellcode(Assembly) is:\n\n' +encode_process(encode, shellcode, os, func)+
							 '\n\n')
				else:
					info('Generated shellcode is:\n\n' +op(encode_process(encode, shellcode, os, func),os) +
							 '\n\n')	
	elif mypayload == 'show_all':
		limit = form.getvalue("limit")
		if limit is not None:
			for _ in _show_payloads(commands,True):
				if limit in _:
					print '[+]',_
		if limit is None:
			_show_payloads(commands,False)
		sys.exit(0)
	else:
		print '''please be sure you send all required fields!'''
		sys.exit(0)
else:
	print '''api not found!'''
	sys.exit(0)

