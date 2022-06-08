def binary_df_cnn_linear(hmm_output_file_name):
    df_tuple=[]
    with open(hmm_output_file_name) as in_file:
        for i in in_file:
            line= i.split()
            file_name= line[0]
            file_names= file_name.split('_')
            name= file_names[2]
            num_of_hit= line[4]
            if int(num_of_hit)==0:
                binary_hit= 0
            else:
                binary_hit= 1
            df_tuple.append((name, binary_hit))
    df= pd.DataFrame(df_tuple, columns= ['class', 'hit'])
    #creates a dataframe so each sequence analysed by hmmscan has either 1 or 0 for hit or not
    count_df=df.groupby(['class']).sum()
    #sum by class, positive hit dataframe
    total_num_seq= len(df_tuple)
    #all seq, positive and negative
    positive_hit_num= count_df['hit'].sum()
    #number of positive overall
    return count_df, positive_hit_num, total_num_seq