from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
Script to login and do stuff in RingZer0 coding challenges
https://ringzer0team.com
Python requests or mechanize doesn't work due to the hidden input field named 'csrf' 
"""

class RingZer0:
	def __init__(self):
		self.driver = webdriver.Firefox()

	def login(self):
		username = "USERNAME"
		password = "PASSWORD"
		#Navigate to url, find username and password element,
		#login with given username and password
		self.driver.get("https://ringzer0team.com/login")
		element = self.driver.find_element_by_name("username")
		element.send_keys(username)
		element = self.driver.find_element_by_name("password")
		element.send_keys(password)
		element.send_keys(Keys.RETURN)

	def doStuff(self):
		#example
		self.driver.get("https://ringzer0team.com/challenges/13")
		element = self.driver.find_element_by_class_name("message")
		print element.text


if __name__ == "__main__":
	#Use Firefox with the Selenium webdriver
	r = RingZer0()
	r.login()
	r.doStuff()