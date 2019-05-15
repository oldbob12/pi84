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

	display_surface = pygame.display.set_mode((400, 400 )) 
	font = pygame.font.Font('texas_instruments_ti84_series.ttf', 64)
	
	
	displayWidth = 640
	DisplayHeight = 480
	screen = pygame.display.set_mode((displayWidth,DisplayHeight))
	clock = pygame.time.Clock()
	
	text = font.render('', True, (0,0,0) )
	
	running = True
	
	while running:
		display_surface.fill((149, 161, 128) ) 
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				exit()
				
		if textinput.update(events):
			lineEquations.append(textinput.get_text())
			print(lineEquations)
			lineAnswers.append(evalCalculator(textinput.get_text()))
			print(lineAnswers)
			textinput = pygame_textinput.TextInput('','texas_instruments_ti84_series.ttf',64,0,(0,0,0))
			lineNum += 1
			
		i = 0
		while i < len(lineAnswers):
			text = font.render(str(lineAnswers[i]), True, (0,0,0) )
			text_rect = text.get_rect()	
			text_rect.right = displayWidth
			text_rect.bottom = 138 + (128 * i)
			display_surface.blit(text,text_rect) 
			i += 1
		i = 0
		while i < len(lineEquations):
			text = font.render(str(lineEquations[i]), True, (0,0,0) )
			text_rect = text.get_rect()	
			text_rect.bottom = 74 + (128 * i)
			text_rect.left = 10
			display_surface.blit(text,text_rect) 
			i += 1
			
			
		
			# Blit its surface onto the screen
		screen.blit(textinput.get_surface(), (10, 10 + (128 * lineNum)))
		
		pygame.display.update()  
		clock.tick(60)
if __name__=="__main__":
    main()
