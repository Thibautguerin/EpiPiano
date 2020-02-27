#!/usr/bin/python3

from include import *
from clic import *
from verif_format import *
from parameter import *
from create import *
from delete import *
from play import *

def Choose_song_mode(window, validate_song, detect):
	window.blit(select, (706, 90))
	window.blit(create, (1100, 750))

	global global_x_song

	mouse_pos = pygame.mouse.get_pos()
	if (mouse_pos[0] >= 37 and mouse_pos[0] <= 107 and mouse_pos[1] >= 336 and mouse_pos[1] <= 432 and global_x_song < 0):
		window.blit(arrow_l_c, (37, 336))
		window.blit(arrow_r, (1813, 336))
		window.blit(start, (152, 792))
		window.blit(delete, (620, 792))
		if (pygame.mouse.get_pressed()[0]):
			wait_mouse_up()
			global_x_song = global_x_song + 1
	elif (mouse_pos[0] >= 1813 and mouse_pos[0] <= 1883 and mouse_pos[1] >= 336 and mouse_pos[1] <= 432 and len(validate_song) > 1 + abs(global_x_song)):
		window.blit(arrow_l, (37, 336))
		window.blit(arrow_r_c, (1813, 336))
		window.blit(start, (152, 792))
		window.blit(delete, (620, 792))
		if (pygame.mouse.get_pressed()[0]):
			wait_mouse_up()
			global_x_song = global_x_song - 1
	elif (mouse_pos[0] >= 152 and mouse_pos[0] <= 589 and mouse_pos[1] >= 792 and mouse_pos[1] <= 943 and len(validate_song) != 0):
		window.blit(arrow_l, (37, 336))
		window.blit(arrow_r, (1813, 336))
		window.blit(start_c, (152, 792))
		window.blit(delete, (620, 792))
		if (pygame.mouse.get_pressed()[0]):
			wait_mouse_up()
			play_the_song(window, validate_song[abs(global_x_song)], detect)
	elif (mouse_pos[0] >= 1176 and mouse_pos[0] <= 1759 and mouse_pos[1] >= 872 and mouse_pos[1] <= 940):
		window.blit(arrow_l, (37, 336))
		window.blit(arrow_r, (1813, 336))
		pygame.draw.rect(window, (150, 150, 150), (1176, 872, 583, 68))
		window.blit(start, (152, 792))
		window.blit(delete, (620, 792))
		if (pygame.mouse.get_pressed()[0]):
			wait_mouse_up()
			input_text(window, detect)
	elif (mouse_pos[0] >= 620 and mouse_pos[0] <= 1057 and mouse_pos[1] >= 792 and mouse_pos[1] <= 943 and len(validate_song) != 0):
		window.blit(arrow_l, (37, 336))
		window.blit(arrow_r, (1813, 336))
		window.blit(start, (152, 792))
		window.blit(delete_c, (620, 792))
		if (pygame.mouse.get_pressed()[0]):
			wait_mouse_up()
			delete_the_song(window, validate_song[abs(global_x_song)])
	else:
		window.blit(arrow_l, (37, 336))
		window.blit(arrow_r, (1813, 336))
		window.blit(start, (152, 792))
		window.blit(delete, (620, 792))
	pygame.display.update()

def start_game(window, i):
	global global_x_song
	songs = os.listdir("./song/")

	detect = midi.Input(int(i), 0)
	
	i = 0
	myfont = pygame.font.SysFont("monospace", 28, True)

	while (1):
		pygame.draw.rect(window, back_color, (0, 0, 1920, 1080))
		songs = os.listdir("./song/")
		x = 736 + global_x_song * 592
		validate_song = []
		while (i != len(songs)):
			if (os.path.exists("./song/" + songs[i])):
				if (os.path.isfile("./song/" + songs[i])):
					parsing = verif_format("./song/" + songs[i])
					if (parsing != False):
						validate_song.append(songs[i])
						window.blit(song, (x, 120))
						name = myfont.render(songs[i], 1, (255,0,0))
						window.blit(name, (x + 448 / 2 - name.get_rect().width / 2, 330))
						nb_notes = myfont.render("Notes: " + str(len(parsing)), 1, (255,0,0))
						window.blit(nb_notes, (x + 448 / 2 - nb_notes.get_rect().width / 2, 370))
						x = x + 592
			i = i + 1
		Choose_song_mode(window, validate_song, detect)
		for event in pygame.event.get():
			if (event.type == QUIT):
				return (2)
			if (event.type == KEYDOWN):
				if (event.key == K_ESCAPE):
					return (1)
				if (event.key == K_LEFT):
					if (global_x_song < 0):
						window.blit(arrow_l_c, (37, 336))
						pygame.display.update()
						global_x_song = global_x_song + 1
						wait_key_up()
				if (event.key == K_RIGHT):
					if (len(validate_song) > 1 + abs(global_x_song)):
						window.blit(arrow_r_c, (1813, 336))
						pygame.display.update()
						global_x_song = global_x_song - 1
						wait_key_up()
				if (event.key == K_RETURN and len(validate_song) != 0):
					window.blit(start_c, (152, 792))
					pygame.display.update()
					wait_key_up()
					play_the_song(window, validate_song[abs(global_x_song)], detect)
				if (event.key == K_DELETE and len(validate_song) != 0):
					window.blit(delete_c, (620, 792))
					pygame.display.update()
					wait_key_up()
					delete_the_song(window, validate_song[abs(global_x_song)])
				if (event.key == K_f):
					pygame.display.toggle_fullscreen()
		i = 0
		clockFps.tick(maxFps)

def choose_input(window):
	pygame.draw.rect(window, back_color, (0, 0, 1920, 1080))
	window.blit(input_choice, (510, 150))
	window.blit(input_tab, (431, 350))
	
	y1_button = 419
	y2_button = 498
	y = 443
	myfont = pygame.font.SysFont("monospace", 25, True)

	mouse_pos = pygame.mouse.get_pos()
	for i in range(midi.get_count()):
		if (i % 2 != 0):
			if (mouse_pos[0] >= 528 and mouse_pos[0] <= 1391 and mouse_pos[1] >= y1_button and mouse_pos[1] <= y2_button):
				window.blit(myfont.render(str(midi.get_device_info(i)), 1, (255,0,0)), (550, y))
				if (pygame.mouse.get_pressed()[0]):
					wait_mouse_up()
					return (start_game(window, i))
			else:
				window.blit(myfont.render(str(midi.get_device_info(i)), 1, (33,33,33)), (550, y))
			y = y + 112
			y1_button = y1_button + 112
			y2_button = y2_button + 112
	pygame.display.update()
	return (0)

def play_start(window):
	running = 0

	while (running == 0):
		midi.init()
		running = choose_input(window)
		midi.quit()
		for event in pygame.event.get():
			if (event.type == QUIT):
				return (False)
			if (event.type == KEYDOWN):
				if (event.key == K_ESCAPE):
					return (True)
				if (event.key == K_f):
					pygame.display.toggle_fullscreen()
		clockFps.tick(maxFps)
	if (running == 1):
		return (True)
	else:
		return (False)

def menu(window):
	pygame.draw.rect(window, back_color, (0, 0, 1920, 1080))
	window.blit(title, (495, 130))

	mouse_pos = pygame.mouse.get_pos()
	if (mouse_pos[0] >= 679 and mouse_pos[0] <= 1242 and mouse_pos[1] >= 450 and mouse_pos[1] <= 557):
		window.blit(play_c, (679, 450))
		window.blit(parameters, (679, 620))
		if (pygame.mouse.get_pressed()[0]):
			wait_mouse_up()
			return (play_start(window))
	elif (mouse_pos[0] >= 679 and mouse_pos[0] <= 1242 and mouse_pos[1] >= 620 and mouse_pos[1] <= 727):
		window.blit(play, (679, 450))
		window.blit(parameters_c, (679, 620))
		if (pygame.mouse.get_pressed()[0]):
			wait_mouse_up()
			return (parameters_start(window))
	else:
		window.blit(play, (679, 450))
		window.blit(parameters, (679, 620))
	pygame.display.update()
	return (True)