import pygame
import pygame_textinput
import string

def evalCalculator(equation):
    if not set(equation).intersection(string.ascii_letters + '{}[]_;\n'):
        return eval(equation)
    else:
        print("illegal character")
        return "none"

def main():
	
	pygame.init()
	pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

	textinput = pygame_textinput.TextInput('','texas_instruments_ti84_series.ttf',64,0,(0,0,0))

	class Equations:
		line = []
		xCor = []
		yCor = []
		textLength = []
		lineSelect = 0
	class Answers:
		line = []
		xCor = []
		yCor = []
		textLength = []
		lineSelect = 0
		
	lineNum = 0
	lineSelect = 0
	
	ReturnValue = ''

	display_surface = pygame.display.set_mode((400, 400 )) 
	font = pygame.font.Font('texas_instruments_ti84_series.ttf', 64)
	
	
	displayWidth = 640
	DisplayHeight = 480
	screen = pygame.display.set_mode((displayWidth,DisplayHeight))
	clock = pygame.time.Clock()
	
	textLineAnswers = font.render('', True, (0,0,0) )
	textLineEquations = font.render('', True, (0,0,0) )
	
	running = True

	while running:
		display_surface.fill((149, 161, 130) )
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					if lineSelect == 0:
						if Answers.lineSelect < len(Answers.line):
							Answers.lineSelect += 1
							lineSelect = 1
					else:
						if Equations.lineSelect < len(Answers.line):
							Equations.lineSelect += 1
							lineSelect = 0
				if event.key == pygame.K_DOWN:
					if lineSelect == 1:
						if Answers.lineSelect > 0:
							Answers.lineSelect -= 1
							lineSelect = 0
					else:
						if Equations.lineSelect > 0:
							Equations.lineSelect -= 1
							lineSelect = 1
				if(event.key == pygame.K_RETURN):
					if lineSelect == 1 and Answers.lineSelect > 0:
						textinput = pygame_textinput.TextInput(textinput.get_text()+str(Answers.line[len(Answers.line) - Answers.lineSelect]),'texas_instruments_ti84_series.ttf',64,0,(0,0,0))
					if lineSelect == 0 and Equations.lineSelect > 0:
						textinput = pygame_textinput.TextInput(textinput.get_text()+str(Equations.line[len(Equations.line) - Equations.lineSelect]),'texas_instruments_ti84_series.ttf',64,0,(0,0,0))
					Equations.lineSelect = 0
					Answers.lineSelect = 0
					lineSelect = 0

					
		if textinput.update(events) and textinput.get_text() != '' and Equations.lineSelect == 0 and Answers.lineSelect == 0:
			Answers.lineSelect = 0
			Equations.line.append(textinput.get_text())
			ReturnValue = textinput.get_text()
			ReturnValue = ReturnValue.replace("^", "**")
			Answers.line.append(evalCalculator(ReturnValue))
			textinput = pygame_textinput.TextInput('','texas_instruments_ti84_series.ttf',64,0,(0,0,0))
			lineNum+=1
			Equations.xCor = [0]*len(Answers.line)
			Equations.yCor = [0]*len(Answers.line)
			Equations.textLength = [0]*len(Answers.line)
			Answers.xCor = [0]*len(Answers.line)
			Answers.yCor = [0]*len(Answers.line)
			Answers.textLength = [0]*len(Answers.line)
			i = 0
			while i < len(Answers.line):
				if lineNum < 3:
					Answers.yCor[i] = 77 + (135 * i)
					Equations.yCor[i] = 12 + (135 * i)
				else:
					Answers.yCor[i] = 77+ (135 * i)  - (lineNum - 3) * 135
					Equations.yCor[i] = 12 + (135 * i) - (lineNum - 3) * 135
				i+=1
		if(Answers.lineSelect > 0):
			if lineSelect == 1:
				pygame.draw.rect(display_surface,(25,86,105),
				(Answers.xCor[len(Answers.line)-Answers.lineSelect]-4,
				Answers.yCor[len(Answers.line)-Answers.lineSelect]-4, 
				Answers.textLength[len(Answers.line)-Answers.lineSelect],65))
		if(Equations.lineSelect > 0):
			if lineSelect == 0:
				pygame.draw.rect(display_surface,(25,86,105),
				(Equations.xCor[len(Equations.line)-Equations.lineSelect]-4,
				Equations.yCor[len(Equations.line)-Equations.lineSelect]-4, 
				Equations.textLength[len(Equations.line)-Equations.lineSelect],65))
				
		i = 0
		while i < len(Answers.line):
			textLineAnswers = font.render(str(Answers.line[i]), True, (0,0,0) )
			textLineAnswers_rect = textLineAnswers.get_rect()	
			textLineAnswers_rect.right = displayWidth - 6
			textLineEquations = font.render(str(Equations.line[i]), True, (0,0,0) )
			textLineEquations_rect = textLineEquations.get_rect()
			textLineEquations_rect.left = displayWidth
			textLineAnswers_rect.y = Answers.yCor[i]
			textLineEquations_rect.y = Equations.yCor[i]
			textLineEquations_rect.left = 10
			display_surface.blit(textLineEquations,textLineEquations_rect)
			display_surface.blit(textLineAnswers,textLineAnswers_rect)
			Answers.textLength[i] = textLineAnswers.get_width()
			Answers.xCor[i] = textLineAnswers_rect.x
			Equations.textLength[i] = textLineEquations.get_width()
			Equations.xCor[i] = textLineEquations_rect.x
			i += 1
	
		
		
			# Blit its surface onto the screen
		if lineNum < 3:
			screen.blit(textinput.get_surface(), (10, 12 + (135 * lineNum)))
		else:
			screen.blit(textinput.get_surface(), (10, 12 + (135 * 3)))
		
		pygame.display.update()
		clock.tick(60)


if __name__=="__main__":
    main()
