# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def Main():
    import pygame
    import csv
    import random
    import pandas as pd
    import os

    BASE_DIR = os.path.dirname(__file__)
    gamer_answers_path = os.path.join(BASE_DIR, 'data', 'gamer_answers.csv')
    correct_answers_path = os.path.join(BASE_DIR, 'data', 'correct_answers.csv')
    correct_data_path = os.path.join(BASE_DIR, 'data', 'correct_data.csv')
    gamer_data_path = os.path.join(BASE_DIR, 'data', 'gamer_data.csv')
    tile_path = os.path.join(BASE_DIR, 'assets', 'tiles')
    map_img_path = os.path.join(BASE_DIR, 'assets', 'AllegiantMap.png')
    calc_img_path = os.path.join(BASE_DIR, 'assets', 'calc_img.png')
    again_img_path = os.path.join(BASE_DIR, 'assets', 'again_img.png')
    blank_img_path = os.path.join(BASE_DIR, 'assets', 'blank_img.png')
    airplane_img_path = os.path.join(BASE_DIR, 'assets', 'helper_circle.png')


   
    #button class with click
    class Button():
    	def __init__(self,x, y, image, scale):
    		width = image.get_width()
    		height = image.get_height()
    		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    		self.rect = self.image.get_rect()
    		self.rect.topleft = (x, y)
    		self.clicked = False

    	def draw(self, surface):
    		action = False

    		#get mouse position
    		pos = pygame.mouse.get_pos()

    		#check mouseover and clicked conditions
    		if self.rect.collidepoint(pos):
    			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
    				action = True
    				self.clicked = True

    		if pygame.mouse.get_pressed()[0] == 0:
    			self.clicked = False

    		#draw button
    		surface.blit(self.image, (self.rect.x, self.rect.y))

    		return action
        
    #button class without click
    class Button123():
        def __init__(self,x, y, image, scale):
        	width = image.get_width()
        	height = image.get_height()
        	self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        	self.rect = self.image.get_rect()
        	self.rect.topleft = (x, y)
        	self.clicked = False

        def draw(self, surface):
        	action = False

        	#draw button
        	surface.blit(self.image, (self.rect.x, self.rect.y))

        	return action
    
    pygame.init()
    
    #game window
    SCREEN_WIDTH=920
    SCREEN_HEIGHT=620
    LOWER_MARGIN=100
    SIDE_MARGIN=300
    
    screen=pygame.display.set_mode((SCREEN_WIDTH+SIDE_MARGIN, SCREEN_HEIGHT+LOWER_MARGIN))
    pygame.display.set_caption('MapGame')
    
    #define game veriables
    TILE_SIZE=25
    TILE_TYPES=123
    tile_dict = {}
    airport_dict = {}
    
    current_tile = 0
    dict_item = 0
    score = 0
    has_ran = False
    has_calculated = False
    game_dict = {}
    incorrect_list = []
    gamer_data = []
    gamer_answers=[]
    z=[]

    q=5 #number of questions
    m=0
    n=m+q
    
    #Load correct data
    correct_data_pd = pd.read_csv(correct_data_path, header = None)
    #create correct data list
    correct_data = []
    for row in range(620):
        correct_data_row = []
        for column in range(920):
            r = correct_data_pd.iloc[row][column]
            correct_data_row.append(r)
        correct_data.append(correct_data_row)
    
    #load images
    themap_img=pygame.image.load(map_img_path).convert_alpha()
    themap_img = pygame.transform.scale(themap_img, (1910/2, 1235/2))
    calc_img = pygame.image.load(calc_img_path).convert_alpha()
    again_img = pygame.image.load(again_img_path).convert_alpha()
    
    #helper box load
    helperbox_img = pygame.image.load(airplane_img_path).convert_alpha()
    helperbox_img=pygame.transform.scale(helperbox_img,(TILE_SIZE,TILE_SIZE))
    
    #store tiles in a list
    img_list=[]
    for x in range(TILE_TYPES):
        img=pygame.image.load(f'{tile_path}/{x}.png').convert_alpha()
        img=pygame.transform.scale(img,(TILE_SIZE,TILE_SIZE))
        img_list.append(img)
    blank_img=pygame.image.load(blank_img_path).convert_alpha()
    blank_img=pygame.transform.scale(blank_img,(TILE_SIZE,TILE_SIZE))
        
    #create a random shuffle list for the dictionary
    s_list = []
    for s in range(TILE_TYPES):
        s_list.append(s)
        random.shuffle(s_list)
    random.shuffle(s_list)
    
    #define colors and font
    GRAY=(128, 128,128)
    RED=(200,25,25)
    font = pygame.font.SysFont('Futura', 30)
    
    #create empty data list
    for row in range(620):
        r = [-1]*920
        gamer_data.append(r)
    
    #create function for drawing background
    def draw_bg():
        screen.fill(GRAY)
        screen.blit(themap_img, (3,3))
    
    #function for drawing the gamer's answers:
    def draw_gamer_airports():
        for y, row in enumerate(gamer_data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    screen.blit(img_list[tile],(x, y))
      
    #function for outputting text onto the screen
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))
        
    #function that shows airplane when hovering over dots
    def helper_box():
        if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
            if correct_data[y][x] >= 0:
                screen.blit(helperbox_img,(x, y))
    
    #create "Calculate Score" and "Try Again" buttons
    calc_button = Button(SCREEN_WIDTH//8, SCREEN_HEIGHT + LOWER_MARGIN - 85, calc_img, 0.1)
    again_button = Button(SCREEN_WIDTH//1.5, SCREEN_HEIGHT + LOWER_MARGIN - 85, again_img, 0.1)
    
    #make a tile dictionary (that has all airports)
    for i in range(len(img_list)):
        tile_located = Button123(SCREEN_WIDTH+200, 75, img_list[i], 2)
        tile_dict.update({s_list[i]: [tile_located, i]})
    blank_tile = Button123(SCREEN_WIDTH+200, 75, blank_img, 2)
    
    #make a game dictionary in a random sequence
    def game_dictionary(m,n):
        for i in range(m,n,1):
            game_dict[i]=tile_dict[i]
            z.append(game_dict[i][1])
        game_dict[n] = [blank_tile, 'blank']  
    game_dictionary(m,n)
    
    #make an airport dictionary ex {0:BLI,...}
    airport_string = 'BLIPDXEUGMFROAKSCKFATMRYSMXLAXSNAPSPSANRNOLASPHXIWAGEGPSCGPIGTFMSOBZNBIL\
BOIIDAPVUGJTDENELPEYWSATAUSLRDMFEHOUMOTGFKBISFARRAPFSDOMAGRIICTTULOKCSTCMSPDSMCIDMLIMCI\
SGFXNALITSHVMSYATWRFDMDWPIABMISPIBLVTVCGRRFNTSBNTOLFWAINDEVVSDFVPSBNAMEMPIEBGRPBGPSM\
BOSPVDROCSYRALBIAGELMSWFABEEWRCAKMDTPITDAYLCKHGRBWICVGCKBIADHTSROARICORFLEXTRIGSOSRQ\
TYSAVLUSACHAGSPMYRCHSSAVJAXSFBMLBPBIFLLPGD'
    for i in range(TILE_TYPES):
        airport_dict.update({i:airport_string[:3]})
        airport_string = airport_string[3:]
    
    #make a play_again list with the rest of the airports:
    num_sets=int(TILE_TYPES/q)
    play_list=[]
    for i in range(num_sets):
        play_list.append([m+q*i,n+q*i,False])
    play_set=0
    
    ###WHILE LOOP STARTS HERE###
    ############################
    
    run = True
    while run:
        draw_bg()
        draw_gamer_airports()
        draw_text(f'Score: {score} out of {q}', font, RED, SCREEN_WIDTH//3, SCREEN_HEIGHT + LOWER_MARGIN - 90)
        
        
        #try the game again
        if again_button.draw(screen) and play_set!=num_sets-1:
            if play_list[play_set][2]==True:
                play_set+=1
                m=play_list[play_set][0]
                n=play_list[play_set][1]
                game_dict={}
                z=[]
                game_dictionary(m,n)
                current_tile = 0
                dict_item = m
                score = 0
                has_ran = False
                has_calculated = False
                incorrect_list = []
                gamer_data = []
                for row in range(620):
                    r = [-1]*920
                    gamer_data.append(r)
                gamer_answers=[]
                
        
        #the play has started so set it to True
        play_list[play_set][2]=True
        
        #add new tiles to the screen
        #get mouse position  
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
       
        #run the helper box
        helper_box()
        
        #display the tile (airport code on the right hand sode)
        game_dict[dict_item][0].draw(screen)
            
        #check that the coordinates are within the tile area
        if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT and has_ran == False:
            if dict_item != n :
                #update tile value if clicked
                if pygame.mouse.get_pressed()[0]==1 and correct_data[y][x] >= 0:
                    if gamer_data[y][x] == -1:
                        current_tile = game_dict[dict_item][1]
                        gamer_data[y][x] = current_tile
                        gamer_answers.append([y,x,current_tile])
                        dict_item +=1
            else:
                has_ran = True             
        #save, load and calculate data
        if calc_button.draw(screen) and dict_item == n and has_ran == True and has_calculated == False:
            # with open('C:/Users/Kamila/OneDrive/Desktop/Project0/map_game/gamer_answers.csv', 'w', newline='') as csvfile:
            #     writer = csv.writer(csvfile, delimiter = ',')
            #     for row in gamer_answers:
            #         writer.writerow(row)
            with open(answers_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter = ',')
                for row in gamer_answers:
                    writer.writerow(row)
            # gamer_answers_pd = pd.read_csv('C:/Users/Kamila/OneDrive/Desktop/Project0/map_game/gamer_answers.csv', header=None, names = ['y','x','z'])
            # correct_answers_pd = pd.read_csv('C:/Users/Kamila/OneDrive/Desktop/Project0/map_game/correct_answers.csv', header=None, names = ['y','x','z'])
            gamer_answers_pd = pd.read_csv(answers_path, header=None, names=['y', 'x', 'z'])
            correct_answers_pd = pd.read_csv(correct_path, header=None, names=['y', 'x', 'z'])
            for i in range(q):    
                if (correct_answers_pd.loc[correct_answers_pd['z']==z[i], 'y'].item()-6) < gamer_answers_pd['y'].iloc[i]\
                    and (correct_answers_pd.loc[correct_answers_pd['z']==z[i], 'y'].item()+6) > gamer_answers_pd['y'].iloc[i]\
                    and (correct_answers_pd.loc[correct_answers_pd['z']==z[i], 'x'].item()-6) < gamer_answers_pd['x'].iloc[i]\
                   and (correct_answers_pd.loc[correct_answers_pd['z']==z[i], 'x'].item()+6) > gamer_answers_pd['x'].iloc[i]:
                    score+=1
                else:
                    incorrect_list.append(z[i])
            incorrect_txt=" ".join(airport_dict[i] for i in incorrect_list)
            has_calculated = True
        
        #load txt with incorrect answers
        if has_calculated == True:
            draw_text("Incorrect: "+incorrect_txt, font, RED, SCREEN_WIDTH//15, SCREEN_HEIGHT + LOWER_MARGIN - 40)
        
        #highlight the selected tile
        pygame.draw.rect(screen, RED, game_dict[dict_item][0].rect, 3)
        
        #close the game with an "x" button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        pygame.display.update()
    pygame.quit()
Main()

            
  






