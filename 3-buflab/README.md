## level 0

直接溢出，改`retaddr`



## level 1

鉴于32位系统函数是从栈上取参数，所以直接把`cookie`放在栈上的合适位置，作为`fizz()`的参数即可



## level 2

这里要修改bss段上的一个值：

1. `getbuf()`是精心设计的，每次读入的字符串都在同一个地址，用gdb调一下就能发现了，于是栈地址就泄露了
2. 在栈上合适位置放一段命令，修改并返回`test()`
3. 溢出，控制`retaddr`返回到shellcode的位置即可



## level 3

这里要修改返回值，与level2思路差不多：

1. 同样，在栈上合适位置放一段命令，修改返回值（即`eax`）并返回到`test()`

2. 取巧的方法是`retaddr`直接覆盖为正确输出的地址，但题意显然不是要我们这么做

3. 如果`retaddr`覆盖为紧接在`getbuf()`后面的那一行的话，由于后面还要调用一些函数，所以要保证栈帧不被破坏，也即溢出时，要在`ebp`的位置覆盖正确的`ebp`值，否则就会segfault

   但由于栈地址没有随机化（在这题中），用gdb调一下就能得到ebp的值

#### **注：**

我看网上有些教程中的shellcode是这样的

```
push $0x08048e50        # set return address
push $0x55682fb0        # restore ebp
mov $0x23a81b97,%eax    # return value (cookie)
leave
ret
```

1. `ebp`不需要再恢复了，只要在溢出的时候保护好栈上存的ebp的值，就没问题了，这是多此一举

2. 这段并没有改动栈帧，没有动`esp`，不能用`leave`，

   因为`leave`相当于`mov %ebp,%esp`和`pop %ebp`，这里用了反而破坏了栈帧

   要么在之前加一句`mov %esp,%ebp`，要么`leave`改成`pop %ebp`



## level 4

这里栈是随机化了，但是给了一段0x208的空白可写区域，就可以尝试`nop sled`，即在shellcode前放许多`\x90`，只要retaddr落在这段区域内，就成功了。

还有一点是`ebp`也得换种方法恢复，显然`esp`是没有被破坏的，所以可以通过`esp`算出`ebp`，这段放在shellcode里即可。