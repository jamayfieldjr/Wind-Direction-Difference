def wind_direction_difference(var_1b,var_1f):

    var_f =[]
    var_ra = abs(var_1b-var_1f)

    
    # REFERENCE ANGEL IS OBSERVATION WIND DIRECTION 
     
    #======================================================================    
    # OBSERVATION WIND DIRECTION QUADRANT I 
    #======================================================================
    
    if 0<=var_1b<90:
      
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT I 0 - 
        #======================================================================
        
        if 0<=var_1f<90:
            var_f = var_1f - var_1b
    
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT II absolute difference <=180  
        #======================================================================
        
        elif 90<=var_1f<180 and var_ra<=180:  
            var_f = var_1f - var_1b
    
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT II absolute difference >180  
        #======================================================================

        elif 90<=var_1f<180 and var_ra>180:
            var_rc = var_1b + 360
            var_f = var_1f - var_rc # DO SUBTRACTION

        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT III absolute difference <=180  
        #======================================================================
        
        elif 180<=var_1f<270 and var_ra<=180:
            var_f = var_1f - var_1b
        
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT III absolute difference >180   
        #======================================================================

        elif 180<=var_1f<270 and var_ra>180:
            var_rc = var_1b + 360
            var_f = var_1f - var_rc # DO SUBTRACTION

        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT VI absolute difference <=180   
        #======================================================================
        
        elif 270<=var_1f<=360 and var_ra<=180:
            var_f = var_1f - var_1b
    
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT VI absolute difference >180  
        #======================================================================
          
        elif 270<=var_1f<=360 and var_ra>180:
            var_rc = var_1b + 360
            var_f = var_1f-var_rc # DO SUBTRACTION
            
    #**********************************************************************
    #**********************************************************************
    #**********************************************************************
    
    #======================================================================    
    # OBSERVATION QUADRANT II 90 - 180 
    #======================================================================
    
    elif 90<=var_1b<180:
            
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT I absolute difference <=180  
        #======================================================================

        if 0<=var_1f<90 and var_ra<=180:
            var_f = var_1f - var_1b
          
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT I absolute difference >180 
        #======================================================================
      
        elif 0<=var_1f<90 and var_ra>180:
            var_rc = var_1b+360
            var_f = var_1f-var_rc # DO SUBTRACTION
          
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT II 90 - 180 DEGREES 
        #======================================================================
        
        elif 90<=var_1f<180:
            var_f = var_1f - var_1b
    
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT III absolute difference  
        #======================================================================
        
        elif 180<=var_1f<270 and var_ra<=180:
            var_f = var_1f - var_1b
    
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT III absolute difference >180  
        #======================================================================
      
        elif 180<=var_1f<270 and var_ra>180:
            var_rc = var_1b+360
            var_f = var_1f-var_rc # DO SUBTRACTION

        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT VI absolute difference <=180  
        #======================================================================
        
        elif 270<=var_1f<=360 and var_ra<=180:
            var_f = var_1f - var_1b
          
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT VI absolute difference >180   
        #======================================================================
        
        elif 270<=var_1f<=360 and var_ra>180:
            var_rc = var_1b + 360
            var_f = var_1f - var_rc # DO SUBTRACTION
        
    #**********************************************************************
    #**********************************************************************
    #**********************************************************************

    #======================================================================    
    # OBSERVATION QUADRANT III 180 - 270 
    #======================================================================
    
    elif 180<=var_1b<270:
      
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT I absolute difference <=180 
        #======================================================================
        
        if 0<=var_1f<90 and var_ra<=180:
            var_f = var_1f - var_1b
    
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT I absolute difference >180 
        #======================================================================
        
        elif 0<=var_1f<90 and var_ra>180:
            var_rc = var_1b - 360
            var_f = var_1f - var_rc # DO SUBTRACTION
    
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT II absolute difference <=180  
        #======================================================================
        
        elif 90<=var_1f<180 and var_ra<=180:
            var_f = var_1f - var_1b

        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT II absolute difference >180 
        #======================================================================

        elif 90<=var_1f<180 and var_ra>180:
            var_rc = var_1b + 360
            var_f = var_1f - var_rc # DO SUBTRACTION
    
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT III absolute difference >180  
        #======================================================================
        
        elif 180<=var_1f<270 and var_ra>180:
            var_f = var_1f - var_1b
          
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT III absolute difference <=180  
        #======================================================================
        
        elif 180<=var_1f<270 and var_ra<=180:
            var_f = var_1f - var_1b

        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT VI absolute difference <=180  
        #======================================================================
        
        elif 270<=var_1f<=360 and var_ra<=180:
            var_f = var_1f - var_1b
          
    #======================================================================    
    # FORECAST WIND DIRECTION QUADRANT VI absolute difference >180 
    #======================================================================

        elif 270<=var_1f<=360 and var_ra>180:
            var_rc = var_1b+360
            var_f = var_1f-var_rc # DO SUBTRACTION
    
    #**********************************************************************
    #**********************************************************************
    #********************************************************************** 
    
    #======================================================================    
    # OBSERVATION QUADRANT VI 270 - 360 
    #======================================================================

    elif 270<=var_1b<=360:
                
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT I absolute difference <=180 
        #======================================================================

        if 0<=var_1f<90 and var_ra<=180:
            var_f = var_1f - var_1b
    
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT I absolute difference >180 
        #======================================================================
        
        elif 0<=var_1f<90 and var_ra>180:
            var_rc = var_1b-360
            var_f = var_1f-var_rc # DO SUBTRACTION
    
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT II absolute difference <=180   
        #======================================================================
        
        elif 90<=var_1f<180 and var_ra<=180:
            var_f = var_1f - var_1b

        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT II absolute difference >180  
        #======================================================================
        
        elif 90<=var_1f<180 and var_ra>180:
            var_rc = var_1b-360
            var_f = var_1f-var_rc # DO SUBTRACTION

        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT III absolute difference <180 
        #======================================================================
        
        elif 180<=var_1f<270 and var_ra<=180:
            var_f = var_1f - var_1b
          
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT III absolute difference >180   
        #======================================================================
        
        elif 180<=var_1f<270 and var_ra>180:
            var_rc = var_1b+360
            var_f = var_1f-var_rc # DO SUBTRACTION
          
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT VI absolute difference <=180   
        #======================================================================
         
        elif 270<=var_1f<=360 and var_ra<=180:
            var_f = var_1f - var_1b
          
        #======================================================================    
        # FORECAST WIND DIRECTION QUADRANT VI absolute difference >180 
        #======================================================================

        elif 270<=var_1f<=360 and var_ra>180:
            var_rc = var_1b+360
            var_f = var_1f-var_rc # DO SUBTRACTION

    
    #**********************************************************************
    #**********************************************************************
    #**********************************************************************
    
    print('Observation Wind Direction : ',var_1b)
    print('Forecast Wind Direction : ',var_1f)
    print('Absolute Difference : ',var_ra)
    print('Wind Direction Difference : [ ', var_f,' ]')
    return(var_f)

#print('Wind Direction Difference : ',wind_direction_difference(var_1b,var_1f))
