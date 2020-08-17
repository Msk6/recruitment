def main():
	#write your code here
	skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
	print ("Welcome to the special recruitment program, please answer the following questions: ")
	name = input("What's your name? ")
	age = int(input("How old are you? "))
	experience = int(input("How many years of experience do you have? "))
	cv = {
		"name": name , 
		"age": age , 
		"experience": experience , 
		"skills": [] 
	}
	for i in skills:
		index = skills.index(i)+1
		print ("%d. %s" % (index, i))
	first_skill = int(input("Choose a skill from above by entering its number: "))
	cv["skills"].append(skills[first_skill-1])
	second_skill = int(input("Choose another skill from above by entering its number: "))
	cv["skills"].append(skills[second_skill-1])

	if  40 > cv["age"] > 25 and cv["experience"] > 5 and skills[5] in cv["skills"]:
		print ("Congrats you are accepted")
	else:
		print ("Sorry you are rejected")  
	

	
#[skills[first_skill-1], skills[second_skill-1]]

'''
 Kale Salad
 30
 6

Skills:
1. Python
2. C++
3. Javascript
4. Juggling
5. Running
6. Eating

 1
 6
You have been accepted, Kale Salad.
'''

if __name__ == '__main__':
	main()