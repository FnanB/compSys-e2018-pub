# Exercises for 24/9-2018

Author: Michael Kirkedal Thomsen <kirkedal@acm.org>

These exercises will:
* Recap basic instructions
* Translation of C to assembler

## Understanding translations
  * 3.13 (BOH p 240)
  * 3.14 (BOH p 241)
  * 3.18 (BOH p 249)
  * 3.23 (BOH p 258)
  * 3.24 (BOH p 260)

## Decompilation
Rewrite the following program to C

```
p:
        jmp     .L5
.L3:
        addq    %rsi, %rdx
        addq    $8, %rdi
        movq    %rdx, -8(%rdi)
.L5:
        movq    (%rdi), %rdx
        testq   %rdx, %rdx
        jg      .L3
        movq    %rdi, %rax
        sarq    $3, %rax
        ret
```

## Recap Boolean arithmetic and logic circuits
Look at your exercises from Monday 10/09.
