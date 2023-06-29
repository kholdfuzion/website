Title: Gold007
Date: 05.15.2017 17:51
Category: Retro Dev
Tags: n64, dev, retro, goldeneye, 007, reversing, hacking

Been working on reversing Goldeneye 007 on N64 to a recompilable disassembly. So far I have gotten the framework in place to rebuild/recompress the rom, and have been keeping the rom fully recompilable as I continue to reverse the binary. I've been decompiling a few functions at a time. That got annoying quickly, so in looking for a better way, I found queueRAM's awesome [sm64tools](https://github.com/queueRAM/sm64tools/). I've been making a config for that and have almost of the functions disassembled in one go. So once I have that spitting out all the code and data, that disassembly will become the new basis for renaming and macroing. Also it support's gcc so I can use that to link.
