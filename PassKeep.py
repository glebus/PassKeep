#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from getpass import getpass
import re
import hashlib

class PassKeep(object):
	"""Generate password from personal key and site name.

		Usage:
			p = PassKeep()
			# Set password length
			p.length = 8

			# Request password
			p.passphrase = getpass("Enter passphrase: ")
			# Request site domain
			p.site = raw_input("Enter site domain (like www.example.com): ")

			# Show result
			print p
	"""

	def getMD5(self, s):
		md5 = hashlib.md5()
		md5.update(str(s))
		return md5.hexdigest()

	def __init__(self):
		self.length = 12
		self._site = ""
		self._passphrase = ""
		self._pass = ""
		self.__site_hash = ""
		self.__passphrase_hash = ""

	@property
	def site(self):
		return self._site
	@site.setter
	def site(self, v):
		# TODO: Check for sitedomain "*.[a-zA-Z0-9-_].\d{2,3}"
		self._site = v
		self.__sitehash = self.getMD5(v)
		return self.__sitehash

	@property
	def passphrase(self):
		return self._passphrase
	@passphrase.setter
	def passphrase(self, v):
		self.__passphrase_hash = self.getMD5(v)
		return self._passphrase

	def __str__(self):
		if self.__passphrase_hash is "":
			raise NameError("Not found `passphrase` variable")
		if self.__site_hash is "":
			raise NameError("Not found `site` variable")
		# concat and gen hash
		result = self.getMD5(self.__passphrase_hash + self.__site_hash)
		passwd_candidate = result[:self.length]
		# Magic. Don't touch it!'
		if (len(re.findall(r'([0-9]+)', passwd_candidate)[0]) + 3 < len(passwd_candidate)): #Не менее трёх букв
			return passwd_candidate
		else: # Need fix numbers in password
			result = ""
			count = 0
			sum = 1
			for symbol in passwd_candidate:   #Получаем по одному символы и проверяем.
				if (sum < 4):   #Если мы уже замени три цифры на буквы, то остальное просто добавляем.
					try:   #Если символ не приводиться к int, то он str (кэп).
						int_symbol = int(symbol)
						if (count%2 != 0):   #Будем преобразовывать только нечётные по счету цифры.
							result += chr(122 - int_symbol) #Заменим цифру на букву, которая находиться под тем же порядковым номером с конца алфавита, что б никто не догадался!
							sum += 1
							count += 1
						else:   #Если четная, то пусть не меняется.
							result += symbol
							count += 1
					except:   #Если он str то мы его просто добавляем к результату.
						result += symbol
						count += 1
				else:
					result += symbol
					count += 1
			return result


if __name__ == "__main__":
	# create object
	p = PassKeep()

	p.length = 15
	# Request password
	p.passphrase = getpass("Enter passphrase: ")
	# Request site domain
	p.site = raw_input("Enter site domain (like www.example.com): ")

	# Show result
	print "Password from site '%s' is: %s" % (p.site, p)
	sys.exit(0)


# vim: set noet fenc=utf-8 ff=unix sts=0 sw=4 ts=4 :
