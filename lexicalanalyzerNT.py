#!/usr/bin/python
#Author: Nathan Thompson
import string

letterunder = list(string.ascii_lowercase) + list(string.ascii_uppercase) # makes a list of letters & underscore
digits = list(string.digits) # makes a list of digits
terminalstate = [1,2,4,5,7,8,10,11,13,14,15,16,17,18,19,20,21,22,25,31,37,39,40,42] # list of states that are terminal


state = 0

endstate = False
characters = [] 
s = "" # temporary string to hold characters that make up identifiers, etc.
i = 0 # initialize iteration for while loop

f = open('lexicalinput.txt', 'r')
while True: # the following loop reads characters from input file and buffers them into the character list
    ch=f.read(1)
    if not ch: break
    characters.append(ch)
	

f.close()

while i < len(characters): # iterates through character list

	

	
	if endstate == True:

		i = temp # if an endstate was previously encountered, i is set back to the iteration that was not part of the string : ex. if encountered x; then i will be set back to ;
		#otherwise the loop would skip ;
		endstate = False

	char = characters[i]

	
	if state == 0: 

		if char.isspace() == True: 
			state = 0
		

		elif char == ';':
			state = 2;
			print("Token: [", char,"] is a semicolon.")

		elif char == '!':
			state = 3;
			
			s += char
		elif char =='<':
			state = 6;
			s += char
			
		elif char =='>':
			state = 9;
			s += char

		elif char == '=':
			state = 12;
			s += char
			
		elif char == '+':
			state = 15;
			print("Token: [", char,"] is an addition sign.")

		elif char == '-':
			state = 16;
			print("Token: [", char,"] is a negative sign.")

		elif char == '/':
			state = 17;
			print("Token: [", char,"] is a division sign.")

		elif char == '*':
			state = 18;
			print("Token: [", char,"] is a multiplication sign.")

		elif char == '(':
			state = 19;
			print("Token: [", char,"] is a left parenthesis.")

		elif char == ')':
			state = 20;
			print("Token: [", char,"] is a right parenthesis.")

		elif char == '{':
			state = 21;
			print("Token: [", char,"] is a left curly bracket.")

		elif char == '}':
			state = 22;
			print("Token: [", char,"] is a right curly bracket.")

		elif char == 'i':
			state = 23
			s += char
	

		elif char == 'w':
			state = 26
			s += char

		elif char == 'p':
			state = 32
			s += char

		elif char in letterunder:
			state = 38
			s += char

		elif char in digits:
			state = 41
			s += char

	elif state == 3:

		

		if char == '=':
			state = 4
			s += char
			print("Token: [",s,"] is a comparison operator.")

		else:
			state = 40;
			print("Error")

		temp = i
	
	elif state == 6:

		

		if char == '=':
			state = 7
			s += char
			print("Token: [", s,"] is a comparison operator.")


		else:
			state = 8
			print("Token: [", s,"] is a less than sign")

			temp = i

	elif state == 9:

		

		if char == '=':
			state = 10
			s += char
			print("Token: [", s,"] is a comparison operator.")

		else:
			state = 11

			print("Token: [", s,"] is a greater than sign.")

	elif state == 12:


		if char == '=':
			state = 13
			s += char
			print("Token: [", s,"] is a comparison operator.")
		else: 
			state = 14
			print("Token: [", s,"] is an assignment operator.")
			endstate = True
			temp = i
			

	elif state == 23:

		if char == 'f':
			state = 24
			s += char

		elif char in letterunder:
			state = 38
			s += char
			temp = i
			endstate = True

	elif state == 24:

		if char in letterunder:
			state = 38
			s += char
		else:
			state = 25
			
			print("Token: [", s,"] is an if statement.")
			temp = i
			endstate = True

	elif state == 26:

		if char == 'h':
			s += char
			state = 27

		elif char in letterunder:
			s += char
			state == 38
			temp = i
			enstate = True

	elif state == 27:

		if char == 'i':
			state = 28
			s += char

		elif char in letterunder:
			state == 38
			s += char
			temp = i
			endstate = True

	elif state == 28:

		if char == 'l':
			state = 29
			s += char
			

		elif char in letterunder:
			state = 38
			
			s += char
			temp = i
			endstate = True

	elif state == 29:

		if char == 'e':
			state = 30
			s += char

		elif char in letterunder:
			state = 38
			s += char
			temp = i
			endstate = True

	elif state == 30:

		if char in letterunder:
			state = 38
			s += char
		else:
			state = 31
			
			print("Token: [", s,"] is a while statement.")
			temp = i
			endstate = True
		
		
			
			

	elif state == 32:

		if char == 'r':
			state = 33
			s += char
		elif char in letterunder:
			state = 38
			temp = i
			s += char
			endstate = True
	elif state == 33:
	
		if char == 'i':
			state = 34
			s += char
		elif char in letterunder:
			state = 38
			temp = i
			s += char
			endstate = True


	elif state == 34:

		if char == 'n':
			state = 35
			s += char

		elif char in letterunder:
			state = 38
			s += char
			temp = i
			endstate = True

	elif state == 35:

		if char == 't':
			state = 36
			s += char
		elif char in letterunder:
			state = 38
			s += char
			temp = i
			endstate = True
	elif state == 36:

		if char in letterunder:
			state = 38
			
			
			state = 0

		else:
			print("Token: [", s,"] is a print statement.")
			state = 37
		
			temp = i
			endstate = True

	elif state == 38:

		if char in letterunder:
			state = 38
			s += char
		else:
			state = 39
			
			print("Token: [", s,"] is an identifier.")
			temp = i
			endstate = True
			


	elif state == 40:
		print("ERROR")
		temp = i
		endstate = True
		

	elif state == 41:
		if char in digits:
			state = 41
			s += char
		elif char in letterunder:
			state = 40
		else:
			
			state = 42
			print("Token: [", s,"] is an integer value.")
			temp = i
			endstate = True
			
	if state in terminalstate: # if terminal state then the state is reset to 0 and the string buffer s is cleared
			
		state = 0
		s = ""
	if endstate != True: # advance interation for while loop if endstate not occured
		i += 1 



print("----------END OF SCRIPT----------");
