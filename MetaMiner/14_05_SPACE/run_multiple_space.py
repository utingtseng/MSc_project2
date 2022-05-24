import os

os.system('echo start running multiple sequences')
os.chdir('/rds/general/user/ytt16/home/MetaMiner/NPDtools-2.5.0-Linux/bin')
os.system('pwd')

raw_list= '''Bacillus_anthracis_Ames.fasta                    a.IF7SW-P3_S6_R1_001.fastq.gz.contigs.fasta
Bacillus_thuringiensis_ATCC_10792.fasta          a.IIF1SW-P1_S17_R1_001.fastq.gz.contigs.fasta
IF3SW-P1_S19_R1_001.contigs.fasta                a.IIF2SW-P5_S16_R1_001.fastq.gz.contigs.fasta
IF5SW-P1_S18_R1_001.contigs.fasta                a.IIF6SW-P2-RA_S11_R1_001.contigs.fasta
ISSFR_3F.pacbio.fasta                            a.IIF6SW-P2_S7_R1_001.fastq.gz.contigs.fasta
JEM2.pacbio.fasta                                a.IIF6SW-P3_S8_R1_001.fastq.gz.contigs.fasta
S1R2T1.miseq.fasta                               a.IIF8SW-P1_S9_R1_001.contigs.fasta
S1R3J1.miseq.fasta                               a.IIF8SW-P2-RA_S14_R1_001.contigs.fasta
a.IF4SW-P1_S1_R1_001.fastq.gz.contigs.fasta      a.IIF8SW-P2_S10_R1_001.contigs.fasta
a.IF6SW-P2_S2_R1_001.fastq.gz.contigs.fasta      if2sw_b1.fasta
a.IF6SW-P3A-RA_S5_R1_001.fastq.gz.contigs.fasta  if2sw_p2.fasta
a.IF6SW-P3A_S3_R1_001.fastq.gz.contigs.fasta'''
my_list= raw_list.split()
#my_list is a list of file names in the fasta/space directory

command_list=[]
for i in my_list:
    dir_nlist= i.split('.')
    if len(dir_nlist)>3:
        dir_name= dir_nlist[0]+'.'+dir_nlist[1]
    elif len(dir_nlist)<=3:
        dir_name= dir_nlist[0]
    command = '''python metaminer.py /rds/general/user/ytt16/home/MetaMiner/data/msms/space -s /rds/general/user/ytt16/home/MetaMiner/data/fasta/space/%s -o /rds/general/user/ytt16/home/MetaMiner/results/space/14_05_22_seq_%s'''%(i,dir_name)
    command_list.append(command)


for i in command_list:
	os.system('%s' %str(i))

os.system('echo processed all sequences')