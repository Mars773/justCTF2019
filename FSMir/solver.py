#!/usr/bin/env python
import binascii

def convert_from_file():
	f = open('./data.txt', 'r')
	binlist = []
	bindic1 = {}
	bindic2 = {}
	binary = f.readline()
	while binary:
		binlist.append(binary)
		binlist = binary.split(" ")
		binlist[2] = binlist[2].rstrip('\n')
		bindic1.update([(str(binlist[0]),binlist[2])])
		bindic2.update([(str(binlist[0]),binlist[1])])
		binary = f.readline()

	keylist = []
	valuelist = []
	fkey = '111011'
	xor2 = ''
	while fkey:
		fkey = find_key(bindic1, fkey)
		xor2 = find_xor(bindic2, fkey)
		keylist.append(fkey)
		valuelist.append(xor2)
	
	return keylist, valuelist
	
def find_key(bindic1, start):
	for key, value in bindic1.items():
		if value == start:
			return key

def find_xor(bindic2, first):
	for key2, value2 in bindic2.items():
		if key2 == first:
			return value2

def convert_from_input():
	all_string = []
	xor1list,xor2list = convert_from_file()
	for num in range(0,len(xor1list)-1):
		b1 = int(str(xor1list[num]),2)
		b2 = int(str(xor2list[num]),2)
		binary = bin(b1 ^ b2)
		if binary == 'q':
			break
		binnumber = 0
		test = ""
		binnumber = int(str(binary), 2)
		hexnumber = hex(binnumber)
		if binnumber > 31 and binnumber < 127:
			test = binascii.unhexlify('%x' % binnumber)
			all_string.append(str(test)[2])
			all_string.reverse()
			all_string = [''.join([i for i in all_string])]
			print(''.join(all_string))
	

def main():
		print("Start:")
		convert_from_input()		
		

if __name__ == '__main__':
	main()
