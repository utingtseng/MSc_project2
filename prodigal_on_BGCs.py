import os

os.system('echo start running prodigal on antismash BGCs')


f=[]
for (dirpath, dirnames, filenames) in os.walk('/rds/general/user/ytt16/home/Prodigal/Prodigal/antismash_BGCs_seq'):
	f.extend(filenames)
	break

os.chdir('/rds/general/user/ytt16/home/Prodigal/Prodigal')


for i in f:
    name_split = i.rsplit('.fasta',1)
    name = (name_split[0])
    command= './prodigal -i /rds/general/user/ytt16/home/Prodigal/Prodigal/antismash_BGCs_seq/%s -o antismash_BGCs_prodigal/%s.genes -a antismash_BGCs_prodigal/%s.proteins.faa -p meta'%(i,name,name)
    os.system('%s'%str(command))