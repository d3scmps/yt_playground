import pandas as pd
import numpy as np
# cette fonction va nous permettre de créer la suite de matrice

def mat_adj_vid(mat_prec, vid_ids):
    """
        mat_prec : DataFrame?
        vid_ids : set
    """
    try:
        n,m = mat_prec.shape
        #vid_ids info
        colomn_name = list(vid_ids)
        row_name = list(vid_ids)
        nw_shape = len(vid_ids)
        mat = np.ones((nw_shape, nw_shape), dtype = int)
        new_mat = pd.DataFrame(mat,columns = colomn_name, index = row_name)
        # ----- prepare merge
        old_rows_index = []
        old_clm = mat_prec.columns
        # old one
        for name in colomn_name:
            if name not in old_clm :
                old_rows_index.append(name)
        mat_zeros1 = np.zeros((len(old_rows_index),len(old_clm)))
        df2 = pd.DataFrame(mat_zeros1, columns = old_clm, index = old_rows_index)
        old_df = pd.concat([mat_prec,df2])
        del mat_prec
        for x in old_rows_index:
            old_df[x] = [0 for i in range(len(old_df.index))]
        # new one
        new_rows_index = []
        for name in old_clm:
            if name not in colomn_name:
                new_rows_index.append(name)
        mat_zeros2 = np.zeros((len(new_rows_index),len(new_mat)))
        df3 = pd.DataFrame(mat_zeros2, columns = colomn_name, index = new_rows_index)
        new_df = pd.concat([new_mat,df3])
        del new_mat
        for x in new_rows_index:
            new_df[x] = [0 for i in range(len(new_df.index))]
        # --- merging
        
        return new_df + old_df
    except AttributeError: 
        row_name = list(vid_ids)
        nw_shape = len(vid_ids)
        mat = np.ones((nw_shape, nw_shape), dtype = int)
        new_mat = pd.DataFrame(mat,columns = row_name, index = row_name)
        return new_mat

    #mat_prec_res = np.pad(mat_prec,(0,nw_shape - n))

if __name__ == '__main__':
    mat2 = np.ones((4,4))
    mat1 = np.ones((1,1))
    l = {'a', 'j', 'd'}
    A  = mat_adj_vid('',l)
    df5 = pd.DataFrame(mat2, columns = ['e','a','c','b'], index = ['e','a','c','b'])
    df = mat_adj_vid(A, {'a','z','f'})
    print(df)

