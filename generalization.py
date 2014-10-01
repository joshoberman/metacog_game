<<<<<<< HEAD
from psychopy import visual, core, event
from os import listdir, path, mkdir
from itertools import product, permutations
from random import shuffle



SUBJECT = raw_input("Subject Number: ")
def checkData(SUBJECT):
    if path.exists("Subject %s/Generalization"%SUBJECT):
        answer = raw_input("Data already exists for Subject %s, would you like to erase the data and continue? Y/N: "%SUBJECT)
        if answer == "N":
            SUBJECT = raw_input ("Subject Number:")
            return checkData(SUBJECT)
        elif answer == "Y":
            pass
        else:
            checkData(SUBJECT)
checkData(SUBJECT)
"""make directory for subject if it doesn't already exist"""
if not path.exists("Subject %s/Generalization"%SUBJECT):
	mkdir("Subject %s/Generalization"%SUBJECT)

win = visual.Window(monitor="testMonitor", units="deg", fullscr=True, allowGUI=False)

intro = visual.TextStim(win, text="You will be presented with a series of aliens, please use buttons '1' and '2' to categorize the aliens as either 'Friendly' or 'Enemy'", wrapWidth=20)

question = visual.TextStim(win, text="Was this alien a friend or Enemy?", color='Black', pos=(0,4), wrapWidth=20)
answer = visual.TextStim(win, text="1								2", color='Black', pos=(0,-2), wrapWidth=20)
reminder = visual.TextStim(win,text="  Friend 							  Enemy", color='Black', pos=(0,0),wrapWidth=20) 


confidenceQuestion = visual.TextStim(win, text="How confident are you in your judgment", color = 'Black', pos = (0,4), wrapWidth=20)
confidenceResponse = visual.TextStim(win, text="1			2	 		3			4			5", color='Black', pos=(0,-4), wrapWidth=20)
confidenceReminder = visual.TextStim(win, text="Not at all Confident 					 Very Confident", color = 'Black', pos=(0,0), wrapWidth=40)

fixation = visual.TextStim(win,text="+", pos=(0,0))
fixation.size = 2


eachEnemy = 4  #total number of times they see each enemy
enemyATypes = listdir("Images/Enemies/EnemyA")
enemyA = ["Images/Enemies/EnemyA/{0}".format(i) for i in enemyATypes if not i.startswith('.')]
enemyA = [visual.SimpleImageStim(win, A, pos=(0,0), name=A[-7:-4]) for A in enemyA]
enemyBTypes = listdir("Images/Enemies/EnemyB")
enemyB = ["Images/Enemies/EnemyB/{0}".format(i) for i in enemyBTypes if not i.startswith('.')]
enemyB = [visual.SimpleImageStim(win, B, pos=(0,0), name=B[-7:-4]) for B in enemyB]
enemies = enemyA*eachEnemy+enemyB*eachEnemy
shuffle(enemies)
shuffle(enemies)

confidenceRatings=[]
alienResponses= []

familiarityRankings = open("Subject %s/Generalization/responses.txt"%SUBJECT, "w")

newPair = False
aliens = False
response = False
start = True
confidence = False

while True:

	if start:
		intro.draw()
		win.flip()
		if len(event.waitKeys())>0:
			start = False
			newPair = True

	if newPair:
		fixation.draw()
		win.flip()
		core.wait(1.5)
		image = enemies.pop()
		alien = image
		alienType = alien.name
		newPair = False
		aliens = True

	elif aliens and not response and not newPair:
		alien.draw()
		win.flip()
		core.wait(2)
		response = True
		aliens = False

	elif response and not newPair and not aliens:
		question.draw()
		answer.draw()
		reminder.draw()
		win.flip()

		responseKeys = event.waitKeys(keyList=['1','2'])
		if len(responseKeys)>0:
			alienResponse = (alienType, responseKeys.pop())
			alienResponses.append(str(alienResponse))
			"""if len(enemyCombinations)==0:
				for response in responses:
					familiarityRankings.write("%s \n"%response)
				break"""
			confidence = True
			response = False
		event.clearEvents()

	elif confidence and not response and not aliens:
		confidenceReminder.draw()
		confidenceQuestion.draw()
		confidenceResponse.draw()
		win.flip()
		responseKeys = event.waitKeys(keyList=['1','2','3','4','5'])
		if len(responseKeys)>0:
			confidenceRating = (responseKeys.pop())
			confidenceRatings.append(str(confidenceRating))
			if len(enemies)==0:
				break
			confidence = False
			newPair = True
		event.clearEvents()


#cleanup

for response,rating in zip(alienResponses,confidenceRatings):
	familiarityRankings.write(response+", "+rating+'\n')
familiarityRankings.close()
win.close()
=======
from psychopy import visual, core, event
from os import listdir, path, mkdir
from itertools import product, permutations
from random import shuffle



SUBJECT = raw_input("Subject Number: ")
def checkData(SUBJECT):
    if path.exists("Subject %s/Generalization"%SUBJECT):
        answer = raw_input("Data already exists for Subject %s, would you like to erase the data and continue? Y/N: "%SUBJECT)
        if answer == "N":
            SUBJECT = raw_input ("Subject Number:")
            return checkData(SUBJECT)
        elif answer == "Y":
            pass
        else:
            checkData(SUBJECT)
checkData(SUBJECT)
"""make directory for subject if it doesn't already exist"""
if not path.exists("Subject %s/Generalization"%SUBJECT):
	mkdir("Subject %s/Generalization"%SUBJECT)

win = visual.Window(monitor="testMonitor", units="deg", fullscr=True, allowGUI=False)

intro = visual.TextStim(win, text="You will be presented with a series of aliens, please use buttons '1' and '2' to categorize the aliens as either 'Friendly' or 'Enemy'", wrapWidth=20)

question = visual.TextStim(win, text="Was this alien a friend or Enemy?", color='Black', pos=(0,4), wrapWidth=20)
answer = visual.TextStim(win, text="1								2", color='Black', pos=(0,-2), wrapWidth=20)
reminder = visual.TextStim(win,text="  Friend 							  Enemy", color='Black', pos=(0,0),wrapWidth=20) 


confidenceQuestion = visual.TextStim(win, text="How confident are you in your judgment", color = 'Black', pos = (0,4), wrapWidth=20)
confidenceResponse = visual.TextStim(win, text="1			2	 		3			4			5", color='Black', pos=(0,-4), wrapWidth=20)
confidenceReminder = visual.TextStim(win, text="Not at all Confident 					 Very Confident", color = 'Black', pos=(0,0), wrapWidth=40)

fixation = visual.TextStim(win,text="+", pos=(0,0))
fixation.size = 2


eachEnemy = 4  #total number of times they see each enemy
enemyATypes = listdir("Images/Enemies/EnemyA")
enemyA = ["Images/Enemies/EnemyA/{0}".format(i) for i in enemyATypes if not i.startswith('.')]
enemyA = [visual.SimpleImageStim(win, A, pos=(0,0), name=A[-7:-4]) for A in enemyA]
enemyBTypes = listdir("Images/Enemies/EnemyB")
enemyB = ["Images/Enemies/EnemyB/{0}".format(i) for i in enemyBTypes if not i.startswith('.')]
enemyB = [visual.SimpleImageStim(win, B, pos=(0,0), name=B[-7:-4]) for B in enemyB]
enemies = enemyA+enemyB
shuffle(enemies)
shuffle(enemies)

confidenceRatings=[]
alienResponses= []

familiarityRankings = open("Subject %s/Generalization/responses.txt"%SUBJECT, "w")

newPair = False
aliens = False
response = False
start = True
confidence = False

while True:

	if start:
		intro.draw()
		win.flip()
		if len(event.waitKeys())>0:
			start = False
			newPair = True

	if newPair:
		fixation.draw()
		win.flip()
		core.wait(1.5)
		image = enemies.pop()
		alien = image
		alienType = alien.name
		newPair = False
		aliens = True

	elif aliens and not response and not newPair:
		alien.draw()
		win.flip()
		core.wait(2)
		response = True
		aliens = False

	elif response and not newPair and not aliens:
		question.draw()
		answer.draw()
		reminder.draw()
		win.flip()

		responseKeys = event.waitKeys(keyList=['1','2'])
		if len(responseKeys)>0:
			alienResponse = (alienType, responseKeys.pop())
			alienResponses.append(str(alienResponse))
			"""if len(enemyCombinations)==0:
				for response in responses:
					familiarityRankings.write("%s \n"%response)
				break"""
			confidence = True
			response = False
		event.clearEvents()

	elif confidence and not response and not aliens:
		confidenceReminder.draw()
		confidenceQuestion.draw()
		confidenceResponse.draw()
		win.flip()
		responseKeys = event.waitKeys(keyList=['1','2','3','4','5'])
		if len(responseKeys)>0:
			confidenceRating = (responseKeys.pop())
			confidenceRatings.append(str(confidenceRating))
			if len(enemies)==0:
				break
			confidence = False
			newPair = True
		event.clearEvents()


#cleanup

for response,rating in zip(alienResponses,confidenceRatings):
	familiarityRankings.write(response+", "+rating+'\n')
familiarityRankings.close()
win.close()
>>>>>>> 926bc0538fcf5630958a3f1c79ad5755b1ad54e9
core.quit()