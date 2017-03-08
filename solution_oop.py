class System(object):
	def _init(self,ref_type=None,yr_joined=2017):
		self.referral_type = ref_type
		self.year_joined = yr_joined
		if self.referral_type != 'Code Blue':
			 self.referral_type = 'Consult'

class Referral(System): #demonstrates class referral inheriting from class system - inheritance
	__file = 0  #demonstrates private variable that can only be accessed with class- Encapsulation

	def admit(self):
		print("assign room 10 and admit")

	def set_file_num(self,num):
		self.__file = num

	def get_file_num(self):
		return self.__file

class Emergency(System):
	__file = 0

	def admit(self):
		print("assign room 2 and admit")

	def set_file_num(self,num):
	    self.__file=num

	def get_file_num(self):
	 	return self.__file
def system_admit(any_system): # demonstrating polymorphism via a function
	return any_system.admit()




