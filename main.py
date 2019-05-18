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
	
	white = (255, 255, 255) 
	green = (0, 255, 0) 
	blue = (0, 0, 128) 

	lineEquations = []
	lineAnswers = []
	lineNum = 0
	
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
				
		if textinput.update(events) and textinput.get_text() != '':
			lineEquations.append(textinput.get_text())
			print(lineEquations)
			ReturnValue = textinput.get_text()
			ReturnValue = ReturnValue.replace("^", "**")
			lineAnswers.append(evalCalculator(ReturnValue))
			print(lineAnswers)
			textinput = pygame_textinput.TextInput('','texas_instruments_ti84_series.ttf',64,0,(0,0,0))
			lineNum += 1
			print(lineNum)
		i = 0
		while i < len(lineAnswers):
			textLineAnswers = font.render(str(lineAnswers[i]), True, (0,0,0) )
			textLineAnswers_rect = textLineAnswers.get_rect()	
			textLineAnswers_rect.right = displayWidth
			textLineEquations = font.render(str(lineEquations[i]), True, (0,0,0) )
			textLineEquations_rect = textLineEquations.get_rect()
			if lineNum < 3:
				textLineAnswers_rect.bottom = 138 + (130 * i)
				textLineEquations_rect.bottom = 74 + (130 * i)
			else:
				textLineAnswers_rect.bottom = 138 + (130 * i)  - (lineNum - 3) * 130
				textLineEquations_rect.bottom = 74 + (130 * i) - (lineNum - 3) * 130
			textLineEquations_rect.left = 10
			display_surface.blit(textLineEquations,textLineEquations_rect) 
			display_surface.blit(textLineAnswers,textLineAnswers_rect) 
			i += 1
		text_width = textLineAnswers.get_width()
		pygame.draw.rect(display_surface,blue,(200,150, text_width,50))
		
		
			# Blit its surface onto the screen
		if lineNum < 3:
			screen.blit(textinput.get_surface(), (10, 10 + (130 * lineNum)))
		else:
			screen.blit(textinput.get_surface(), (10, 10 + (130 * 3)))
		
		pygame.display.update()  
		clock.tick(60)
if __name__=="__main__":
    main()
