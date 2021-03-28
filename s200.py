import requests
import sys
from os import system                                                                               
arg1 = sys.argv[1]
arg2 = sys.argv[2]


with open(arg1,'rt') as fin:
    for i in fin:    
        i = i.strip()
        r = requests.get(i+str('wp-login.php'))
        if r.status_code == 200 or r.status_code == 302:
            print ('200 ok = ',r.url)
            with open(arg2,'wt') as fout:
                print('200 =',r.url)
                fout.write(r.url)
        else:
            print('404 = ',r.url)   
