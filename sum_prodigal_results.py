import os
import subprocess
import pandas as pd


os.chdir('/rds/general/user/ytt16/home/Prodigal/Prodigal/antismash_BGCs_prodigal')
f=[]
for (dirpath, dirnames, filenames) in os.walk('/rds/general/user/ytt16/home/Prodigal/Prodigal/antismash_BGCs_prodigal'):
	f.extend(filenames)
	break
#only want to include faa files    
faa_files=[]
for i in f:
    if i.split('.')[-1] == 'faa':
        faa_files.append(i)



df = pd.DataFrame(columns= ['file_name','num_seqs'])
for i in faa_files:
    wc_output= subprocess.check_output(["wc", "-l", i])
    num_lines = int(wc_output.split()[0])
    n= int(num_lines/2)
    df = df.append({'file_name':i,'num_seqs': n}, ignore_index= True)

df.to_csv('/rds/general/user/ytt16/home/NeuRiPP_paper/prodigal_results.csv', index=False)