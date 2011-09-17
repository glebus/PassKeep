import hashlib
import time
import sys

class PassKeep:
	__password = ""
	__length = 10
	url = ""
	time = ""

	def getMd5(self, b):
		b = str(b)
		m = hashlib.md5()
		m.update(b)
		return m.hexdigest()

	def __init__(self):
		self.__password = self.getMd5(self.__password)
		self.time = self.getMd5(time.time())

	def setUrl(self, url):
		self.url = self.getMd5(url)
		return self.url
		
	def setPasswd(self, passwd):
		self.__password = self.getMd5(passwd)
		return self.__password

	def decrypt(self):
		password = self.__password
		url = self.url
		time = self.time
		a = self.getMd5(password + url)
		#b = self.getMd5(url + time)
		#c = self.getMd5(time + password)
		#d1 = self.getMd5(a + b + c)
		#d2 = self.getMd5(d1)
		#d3 = self.getMd5(d2)
		#result = d1 + d2 + d3
		result = a
		return result[:self.__length]

p = PassKeep()
passwd = raw_input("Enter passwd \n")
p.setPasswd(passwd)
url = raw_input("Enter url, like www.example.com \n")
p.setUrl(url)
print p.decrypt()
sys.exit(0)
