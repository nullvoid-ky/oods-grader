class TorKham:

	def __init__(self):
		self.words = []

	def restart(self):
		self.words = []
		 ### Enter Your Code Here ###
		return "game restarted"

	def play(self, word):
		 ### Enter Your Code Here ###
		a = str(self.words[-1:])[-4:-2].upper()
		b = word[:2].upper()
		if a != b and len(self.words)>0:
			return f"'{word}' -> game over"
		self.words.append(word)
		return f"'{word}' -> {self.words}"




torkham = TorKham()

print("*** TorKham HanSaa ***")
S = input("Enter Input : ").split(',')
for command in S:
	if ' ' in command:
		k, v = command.split(' ')
	else:
		k = command
	if k == 'R':
		print(torkham.restart())
	elif k == 'P':
		print(torkham.play(v))
	elif k == 'X' :
		exit()
	else:
		print(f"'{k} {v}' is Invalid Input !!!")
		exit()




 ### Enter Your Code Here ###