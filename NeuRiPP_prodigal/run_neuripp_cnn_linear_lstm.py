import os
os.system('echo start running neuripp on prodigal short seqs')

os.chdir('/rds/general/user/ytt16/home/NeuRiPP')
f=[]
for (dirpath, dirnames, filenames) in os.walk('/rds/general/user/ytt16/home/Prodigal/Prodigal/antismash_BGCs_seq'):
	f.extend(filenames)
	break

name_list=[]
for i in f:
    name_split = i.rsplit('.fasta',1)
    name = (name_split[0])
    name_list.append(name)

command_list=[]
for i in name_list:
	command = 'python classify.py -m cnn-linear-lstm -w /rds/general/user/ytt16/home/NeuRiPP/weights/cnn_linear_lstm.hdf5 -outdir /rds/general/user/ytt16/home/NeuRiPP/out_dir/antismash_prodigal -outname cnn_linear_lstm_%s --keep_negatives -i /rds/general/user/ytt16/home/Prodigal/Prodigal/antismash_BGCs_prodigal/%s.proteins.faa'%(i,i)
	command_list.append(command)

for i in command_list:
	os.system('%s'%str(i))