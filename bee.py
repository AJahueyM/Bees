import keyboard
import time
import re

f = open("bee.txt", "r")

bee_lines = f.readlines()

time.sleep(3)

for line in bee_lines:
	words = line.split()
	for word in words:
		#print(word)
		keyboard.write(" {}".format(word.lower()), delay=0.01)
		keyboard.press_and_release("enter")
		time.sleep(0.1)
