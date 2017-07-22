// TLDR:  Oi, Barnes.  We'll miss ya.  Here's a grimy RNG in your honor.
//        node oi.js or paste the below into your favorite browser's JS console.
// DEFCON CHALLENGE:  Break this!
 
function millis()         { return Date.now(); }
function flip_coin()      { n=0; then = millis()+1; while(millis()<=then) { n=!n; } return n; }
function get_fair_bit()   { while(1) { a=flip_coin(); if(a!=flip_coin()) { return(a); } } }
function get_random_byte(){ n=0; bits=8; while(bits--){ n<<=1; n|=get_fair_bit(); } return n; }
 
report_console = function() { while(1) { console.log(get_random_byte()); }}
report_console();
 
 
//Oi 1.0:  The 'Obviously Incorrect' Random Number Generator
//         (so go break it!)
//   From: Dan Kaminsky
// Greetz: Barnaby Jack -- there's a pile of awesome reasons to name this
//         Oi, but this one's for you.
//   Date:  1-Aug-2013
//   Idea:
//       A man with one clock knows what time it is.
//       A man with two clocks is never sure.
//       Or:  Anyone who thinks computers are deterministic
//       systems has never tried to write realtime code :)
//
//       In 2011, Nadia Heninger et al found that at least 1 of 200 RSA
//       keys on the Internet were crackable due to random number generators,
//       and that generally those RNGs lived on embedded devices.
//
//       Can we do better?
//
//       In the real world, when we need to make a random choice, we don't
//       go out and buy a hunk of radioactive material and stick a
//       Geiger counter next to it.  We just flip a coin.  Coin flipping
//       ultimately is just measuring a slow system (how many seconds
//       does it take for a coin to rise and fall) against a fast system
//       (how many spins, or bit flips, a coin can complete before it
//       lands).
//
//       That can be done in code.  Lets compare janky millisecond timers
//       (1000 cycles/sec AT BEST) to CPUs themselves (millions to
//       billions of cycles/sec).  And, lets just get one bit, heads
//       or tails.
//
//       Interrupts ain't cycle accurate.
//
//       Oi, like Dakarand and Matt Blaze's Truerand before it, might very
//       well not work. But, you know, this is four lines of JavaScript,
//       The Language That Must Never Be Allowed To Do Cryptography
//       Ever Because Ew.  So here's a Defcon challenge, in honor of our
//       fallen friend.  Lets break this!
//
//       Pick any hardware, pick any language.  Even be an
//       active attacker, doing pesky things to available CPU.
//       If you can influence a bit, greater than chance, you
//       win!  I'm sure this fails _somewhere_.
//
//       This isn't a production version of Oi, by any means.  I'm
//       only doing simple Von Neumann debiasing (throwing away
//       any two 'coin flips' that return the same value). I'm not
//       scrambling the output with even a basic hash, allowing
//       an active attacker some access to the direct bitstream.
//       And there's no PRNG, so speed is actually too slow for
//       lots of production uses.  5 seconds in IE6 for 128 bits
//       is too much, for instance.
//
//       But, I wanna give attackers a fighting chance here.  And the
//       more an attack falls to a fifth line of code, the more
//       obvious it is that our threat models perhaps need adjusting.
//
//       This'll definitely fail to a cycle accurate emulator, but
//       anything else is fair game.
//
//Execution:  node oi.js, or paste into a JS console in your favorite
//            browser.
//Note:  You may need a "nicer" emitter of bytes.  Do this.
//report_console = function() { console.log(get_random_byte()); setTimeout(report_console, 0); }
 
 
===
Output from ent (unlike diehard/dieharder, ent doesn't emit bad results on small bitstreams):
 
$ ent rand_js.bin
Entropy = 7.999967 bits per byte.
 
Optimum compression would reduce the size
of this 7006068 byte file by 0 percent.
 
Chi square distribution for 7006068 samples is 316.67, and randomly
would exceed this value 0.50 percent of the times.
 
Arithmetic mean value of data bytes is 127.5564 (127.5 = random).
Monte Carlo value for Pi is 3.139320943 (error 0.07 percent).
Serial correlation coefficient is -0.000659 (totally uncorrelated = 0.0).
 
===
Simple packer:
 
#!/usr/bin/python
 
import sys
import struct
 
 
for line in open(sys.argv[1], "r").xreadlines():
  n=struct.pack("B", int(line.rstrip()))
  sys.stdout.write(n)
