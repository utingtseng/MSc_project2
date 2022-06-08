import os
os.system('echo running hmmscan')

os.chdir('/rds/general/user/ytt16/home/TIGRFAM_HMM/hmm_pressed')
f=[]
for (dirpath, dirnames, filenames) in os.walk('/rds/general/user/ytt16/home/NeuRiPP/out_dir/antismash_prodigal/cnn_parallel'):
	f.extend(filenames)
	break

name_list=[]
for i in f:
    name_split = i.rsplit('.fa',1)
    name = (name_split[0])
    name_list.append(name)

command_list=[]
output_filenames= []
for i in name_list:
	command = 'hmmscan -o /rds/general/user/ytt16/home/TIGRFAM_HMM/out_dir/%s_hmmscanned cat_all.hmm /rds/general/user/ytt16/home/NeuRiPP/out_dir/antismash_prodigal/cnn_parallel/%s.fa'%(i,i)
	command_list.append(command)
	output_filename= '%s_hmmscanned'%str(i)
	output_filenames.append(output_filename)

for i in command_list:
	os.system('%s'%str(i))
	os.system('echo finished one file')

os.chdir('/rds/general/user/ytt16/home/TIGRFAM_HMM/out_dir')

for i in output_filenames:
	grep_command= 'grep \'Domain search space  (domZ):\' %s > %s_overthreshold_count.txt'%(i, i)
	os.system('%s'%str(grep_command)