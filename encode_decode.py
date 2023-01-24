#base64 printable sytax ları encode edebiliyor. Bu yüzden öncelikle stringi ascii
# formatında encode etmek gerekiyor. Daha sonra stringi base64 formatında encode ediyoruz
# Tekrardan bu stringi yazdırabilmek için ascii formatında decode edilmesi gerekiyor!

import base64
import os
import time

class encodeDecode():
	def __init__(self):
		pass

	def convert(self):
		while True:
			os.system('clear')
			self.user_string = input("Please enter that you want convert string: ")
			self.encode_decode = input("You want the (encode/decode): ")

			if self.encode_decode == "encode":
				self.byte_to_ascii = self.user_string.encode('ascii')
				self.ascii_to_base64 = base64.b64encode(self.byte_to_ascii)
				self.b64_to_ascii = self.ascii_to_base64.decode('ascii')
				print("Base64 Encode: " + self.b64_to_ascii)
				time.sleep(5)
			elif self.encode_decode == "decode":
				self.base64_decode = self.user_string.encode('ascii')
				self.base64_to_ascii = base64.b64decode(self.base64_decode)
				self.ascii_to_byte = self.base64_to_ascii.decode('ascii')
				print("Base64 Decode: " + self.ascii_to_byte)
				time.sleep(5)
				


my_instance = encodeDecode()
my_instance.convert()