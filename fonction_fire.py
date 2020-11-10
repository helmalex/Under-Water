def fire(target_x, target_y):
    """Specification of the function:
    Parameter:
    ----------
    target_x : the position on the axe x of the cursor of the player (0-4) (int)
    target_y : the position on the axe y of the cursor of the player (0-4) (int)
    
    Note:
    -----------
    The function will verify if the cursor and a submarine are in the same axe (x and y), if yes the submarine will lose one 
    point of life"""
    
    for a in range(1, nb_submarines + 1):
      if target_x == submarine[a]["x"] and target_y == submarine[a]["y"] and submarine[a]["life"] > 0:
        submarine[a]["life"] -= 1
        
        microbit.display.set_pixel(submarine[a]["x"], submarine[a]["y"], 9)
        microbit.sleep(2500)
        microbit.display.clear
        #light up at the position of the submarine to show that he is touch
          
        if submarine[a]["life"] == 0:
          nb_sub -= 1
          #verif if the submarine is destroy or not
   
          microbit.display.set_pixel(submarine[a]["x"], submarine[a]["y"], 9)
          microbit.sleep(500)
          microbit.display.clear
          microbit.display.set_pixel(submarine[a]["x"], submarine[a]["y"], 9)
          microbit.sleep(500)
          microbit.display.clear
          microbit.display.set_pixel(submarine[a]["x"], submarine[a]["y"], 9)
          microbit.sleep(500)
          microbit.display.clear
          #flash when a submarine is destroy in his position
