import numpy as np

def cleaning(matrix, index):
    if index==1:
     rows = 1
     prev_mean =0
     columns_tocut = 0
   
     mean_all = np.mean(matrix[rows,:])
     dev_all = np.std(matrix[rows,:])
   
     for columns in range(0,50, 10):  
       local_mean = np.mean(matrix[rows,columns:columns+10])
       if (local_mean < mean_all - 1*dev_all):
         continue
       else:
         columns_tocut = columns
         break
     matrix = matrix[:,columns_tocut:]
   
     mean_all = np.mean(matrix[rows,:])
     dev_all = np.std(matrix[rows,:])

     values = matrix.shape[1]   
     for columns in range(0,50, 10): 
       local_mean =  np.mean(matrix[rows,values-((columns+1)):values-(columns)])
       if (local_mean < mean_all - 2*dev_all):
         continue
       else:
         columns_tocut = columns
         break
     matrix = matrix[:,:values-(columns_tocut)]
    
    elif index==2:
        columns_tocutR = 0
        columns_tocutL = 0

        total_integral = np.trapz(matrix[1,:])
        for columns in range(0,200, 10):
            integral = np.trapz(matrix[1,:columns])
            if integral/total_integral > 0.1:
                columns_tocutR = columns
                break
            else:
                continue
        columns = matrix.shape[1]   
        for column in range(0,200, 10):
            integral = np.trapz(matrix[1, columns-column:])
            if integral/total_integral > 0.1:
                columns_tocutL = column
                break
            else:
                continue

        matrix = matrix[:,columns_tocutR:columns-columns_tocutL]
        
        
            
    
    return matrix