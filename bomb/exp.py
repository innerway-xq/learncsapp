#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 xiangq <xiangq@ubuntu>
#
# Distributed under terms of the MIT license.


from pwn import *
context.log_level = 'debug'
context.arch = 'amd64'
r = process("./bomb")


r.recvuntil('!')
r.sendline("Border relations with Canada have never been better.")
r.sendline("1 2 4 8 16 32")
r.sendline("0 207")
r.sendline("7 0 DrEvil")
r.sendline("\x69\x6f\x6e\x65\x66\x67")
r.sendline("4 3 2 1 6 5")
r.recvuntil("...")
r.sendline(str(0x14))
r.interactive()
