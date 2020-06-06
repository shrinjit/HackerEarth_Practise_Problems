class Answerforremovalvowels(object):
	def   removal_of_vowels(self,string):
		string=string.lower()   ## converting it into the lower the string
		string=string.replace("a","")
		string=string.replace("e","")
		string=string.replace("i","")
		string=string.replace("o","")
		string=string.replace("u","")
		return string





ob1=Answerforremovalvowels()
user_input_string=input("enter the string to remove the vowels ----->>>>")
print(f'the input given by u is , {user_input_string}')

print(ob1.removal_of_vowels(user_input_string))