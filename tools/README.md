# Tools

Throughout the course we will use C as programming language, so it is important that you have access to a compiler on your machine. For this we recommend GCC (https://gcc.gnu.org/), which is also the compiler we will use check correctness of your implementations. For what we are to use, there should be no difference between the later versions, but need not to install the latest GCC 8.2. We will also from second week use GDB, so you can just as well also install this. See also below for some specifics for your operating system.

We will also later during the course use a simulation tool that might (or might not) course problems on non-Linux machines. We will at this time release a VM image that you can use in case of problems. See more about running the image further below.

## Roll Your Own Toolchain
If you prefer to not have to deal with the VirtualBox, most parts can run on your local machine. See OS specific pages

  * [Linux tools](linux.md)
  * [OS X tools](osx.md)
  * [Windows tools](windows.md)

## VirtualBox
We will create a VirtualBox image with most the tools you will need pre-installed. During the course we will further provide you with installations scripts and an updated images for new tools. First image will be published later this week.

For this you will need to install Virtual box: https://www.virtualbox.org/wiki/Downloads

### Virtualisation Technology
For efficiently running the VM you need to have enabled Intel Virtualisation Technology (Intel VT) or AMD-Virtualisation (AMD-V), depending on your processor provider. It you get the error 

```
VT-x is disabled in the BIOS for all CPU modes (VERR_VMX_MSR_ALL_VMX_DISABLED)
```

or similar, you need to enter your BIOS setup and update this. This is very architecture specific, so you need to search how to solve this.

