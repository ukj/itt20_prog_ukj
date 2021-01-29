__author__='Uku-Kaarel Jõesaar, ITT20'
# 23.01.2021
# Ülesanne 10'
import os, re
ipaadressid_fail='yl_10.txt'
ipaadressid_lines =  []
if os.path.isfile(ipaadressid_fail):
    ipaadressid_fail_o = open(ipaadressid_fail, 'r')
    ipaadressid_lines = ipaadressid_fail_o.read().splitlines()
    print(f"Nimekiri loeti failist", ipaadressid_fail)
    ipaadressid_fail_o.close()

def print_pealkiri(pealkiri):
    print (f"\n\t{pealkiri}\n\t",end='')
    i=0
    while i < len(pealkiri):
        print('-',sep='',end='')
        i += 1
    print()

print_pealkiri('IP Aadressid')
for line in ipaadressid_lines:
    
    # https://stackoverflow.com/questions/11264005/using-a-regex-to-match-ip-addresses-in-python
    #              250-255|200-249|0-9|0-000-199.                250-255|200-249|0-000-199
    if re.match('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', line):
        print(line)

print_pealkiri('Paroolid')
for line in ipaadressid_lines:
    if re.search('[A-Z]+', line) and re.search('[a-z]+', line) and re.search('[0-9]+', line):
        print(line)
