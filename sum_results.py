import os
import subprocess
import pandas as pd
os.system('echo summing up neuripp results')

os.chdir('/rds/general/user/ytt16/home/NeuRiPP/out_dir/antismash_prodigal')
f=[]
for (dirpath, dirnames, filenames) in os.walk('/rds/general/user/ytt16/home/NeuRiPP/out_dir/antismash_prodigal'):
	f.extend(filenames)
	break

df = pd.DataFrame(columns= ['file_name','num_seqs'])
for i in f:
    print(i)
    wc_output= subprocess.check_output(["wc", "-l", i])
    num_lines = int(wc_output.split()[0])
    n= int(num_lines/2)
    df = df.append({'file_name':i,'num_seqs': n}, ignore_index= True)

df.to_csv('/rds/general/user/ytt16/home/NeuRiPP_paper/seq_count_df.csv', index=False)