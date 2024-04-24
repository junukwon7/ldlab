# Installing Xilinx ISE 14.7 on a Silicon Mac

*I wrote a brief manual to make the VM work for someone like me who owns an arm mac, using QEMU(UTM) x86 emulation. Make & Spike also works, and I was able to solve Task 1 on UTM. The performance is great but may depend on the host machine.*

## Preview
![CleanShot 2024-04-24 at 15 43 25@2x](https://github.com/junukwon7/ldlab/assets/48399106/2dbf0c56-4cb1-41e0-9835-423459c1d87c)
![CleanShot 2024-04-24 at 15 44 00@2x](https://github.com/junukwon7/ldlab/assets/48399106/8e02d86d-3688-4f69-8ae4-a40ccfa61e3e)


## Perquisites

1. UTM ([link](https://mac.getutm.app/))
2. QEMU tools, install using brew with the command: `brew install qemu`
3. Download the [Xilinx ISE Webpack for Windows](https://www.xilinx.com/member/forms/download/xef.html?filename=Xilinx_ISE_14.7_Win10_14.7_VM_0213_1.zip)
4. Unzip the file, then locate `ova/14.7_VM.ova` (you might have noticed, the install package is literally a VM)

## Prepare

1. Unarchive the ova file. `tar -xvf 14.7_VM.ova.`
2. You will have `14.7_VM-disk001.vmdk`, which is a virtual disk. It should be much bigger than the original ova file.
3. Convert the image with the command: `qemu-img convert -O qcow2 14.7_VM-disk001.vmdk data.qcow2`

## Making the VM

1. Use UTM to make a emulation VM. Click on the plus icon and select emulate.
2. Select other and click “Skip ISO boot”
3. Modify the CPU & Memory. I’m using 8 and 16 each, but you may change it depending on the host machine configuration. I recommend at least 4cpu, 8gb.
4. The disk size can be just 1GB. It will be later switched to the `qcow2` file we made earlier.
5. No shared settings
6. Right-click the created VM and click “Show in Finder”. Then right-click the `.utm` file and click “Show Package Contents”
7. In `./Data`, there should be a `(Some Filename).qcow2` file. Copy the exact name, then delete it.
8. Copy-paste the `data.qcow2` file we made earlier while preparing, then change the name to the text you copied. It’s basically swapping the actual disk.

*Now, the VM is basically set, but yet unusable due to lack of performance.*

## Extra Settings for Performance

1. In System, set CPU to “qemu64"
2. In System, enable “Force Multicore”
3. In System, enable “Balloon Device” and "RNG Device"
4. In QEMU, **disable** “UEFI Device”
5. In Display, change the Display card to `virtio-vga-gl (GPU supported)`, or `Spice QXL GPU (primary, ...)`. The former yields better performance while the latter provides better resolution for retina displays.
6. In Drives, change the interface to `virtio` which allows better performance
7. Note that, the boot process takes a while.
8. Also be aware of the "pause" feature. Using `Spice QXL`, you can now pause VMs and resume whenever you want.

## What you can do with this

1. You can run test benches, use iMPACT, capture waveforms, just everything we learnt from LDLAB. Every functionalities of the Xilinx ISE 14.7 should work, *theoretically*.
2. If you want to program FPGAs, you can by passing-through the USB connection directly into the VM.
3. RHEL is an old OS. Nothing is supported. You may install Firefox ESR, but I suggest just using Safari from the Host OS. Setting up Spice allows you to share the clipboard.
4. As I remember, I had to do some licensing (from AMD Xilinx) to use those tools. As far as I know this licensing problem isn't exclusive for macs, but for all individual users. The licensing is free via Xilinx but it took some time to figure it out. (like keygen and copy-paste)
