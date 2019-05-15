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
	
	textinput = pygame_textinput.TextInput('','texas_instruments_ti84_series.ttf',64)
	
	white = (255, 255, 255) 
	green = (0, 255, 0) 
	blue = (0, 0, 128) 


	numIncrease = 0

	display_surface = pygame.display.set_mode((400, 400 )) 
	font = pygame.font.Font('texas_instruments_ti84_series.ttf', 64)
	
	
	displayWidth = 640
	DisplayHeight = 480
	screen = pygame.display.set_mode((displayWidth,DisplayHeight))
	clock = pygame.time.Clock()
	
	text = font.render('', True, (0,0,0) )
	
	running = True
	
	while running:
		display_surface.fill(white) 
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				exit()
				
		if textinput.update(events):
			print(textinput.get_text())
			text = font.render(str(evalCalculator(textinput.get_text())), True, (0,0,0) )
			
		text_rect = text.get_rect()	
		text_rect.right = displayWidth
		text_rect.bottom = 10 + (64 *2)
		
		display_surface.blit(text,text_rect) 
		
			# Blit its surface onto the screen
		screen.blit(textinput.get_surface(), (10, 10))
		
		pygame.display.update()  
		clock.tick(60)
if __name__=="__main__":
    main()
