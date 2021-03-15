# rolling_average.py
def ra(tr,window=8,u=True):
    '''
    Rolling average
    
    Useage: rolling_avg(j,t)
    
    Inputs: window = window. 8 is the default.
            t = rolling value (temperature) to be averaged.
            u = boolean 'True' or 'False' on or off.
    
    Output: ta = temp average
    This function was written by Ed Ivory
    '''
    
    t_list = []
    while len(t_list) < window:
        t_list.append(tr)
        ta = round(sum(t_list) / len(t_list),3)
    
        if len(t_list) == window:
            t_list.pop(0)
            #t_list.pop(0)
            #t_list.append(ta)
            return ta
        else:
            pass
        return ta

