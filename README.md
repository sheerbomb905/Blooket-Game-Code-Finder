# Working blooket game finder

**Not recommended to self host as this takes up a LOT of resources (if you think you can make this more optimized, please open a PR!)**

### If you just want to get game codes to troll people, [join our discord](https://discord.gg/36sgQJ3pcH)! 
*you can also find some really good, working hacks in the discord*
  
This is a blooket game finder that works right now! There are many older version of this but blooket changed the api url. I was able to intercept a request using devtools and get the url!    
   
**In case you are intrested, the api url is `https://fb.blooket.com/c/firebase/id?id=` where you put your 6 dight game code after `id=`**  

To use the finder, just run main.py! You can edit the number of threads used to find codes in main.py! I find that over 50 threads the codes per second is similar. On replit (where I run this), I am using 25 threads with `2 vCPU` (hacker plan default).      

This is not the fastest finder, but it is very simple! *~7 codes per minute using 25 threads*

*I am working on a game flooder!*