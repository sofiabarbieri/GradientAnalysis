#!/usr/bin/python
import sys, getopt
import numpy as np

from scipy import optimize
import os
import matplotlib.pyplot as plt

import plotter_module as plotter_module
import cleaning_module 


class eloG:
    def __init__(self, filename):
        self.log_open(filename)
        self.name = filename
    def log_open(self, name):
        self.file = open(name,"w+")
    def log_open_append(self):
        self.file = open(self.name,"a+")
    def writeLine(self, string):
        self.file.write(string)
        self.file.write("\n")
    def writeListRow(self, lista):
        for item in lista:
            self.file.write(str(item)) 
            self.file.write("\t")
        self.file.write("\n")
    def writeListCol(self, lista):
        for item in lista:
            self.file.write(str(item)) 
            self.file.write("\n")

    def closeFile(self):
        self.file.close()
        
def readfiletomatrix(inputfile):
     lines = [line.rstrip('\n') for line in open(inputfile)]
     vec_lines = [line.split('\t') for line in lines]
     matrix = np.array(vec_lines)
     matrix = np.delete(matrix, matrix.shape[1]-1, axis=1)
     matrix = np.asfarray(matrix,float)
     return matrix
     
def main(argv):
   indir = ''
   outdir = ''
   list_files = []
   list_files_red = []

   list_filename_only = []
   

    
    ## LEGGERE FILES  
   try:
      opts, args = getopt.getopt(argv,"hd:o:",["dir=","outdir="])
   except getopt.GetoptError:
      print 'test.py -d <input dir> -o <ouput dir> '
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -d <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-d", "--dir"):
         indir = arg
      elif opt in ("-o", "--outdir"):
         outdir = arg
         
   if (indir == ''  or outdir == ''):
        exit()
   curr_dir =  os.path.dirname(os.path.realpath(__file__))

    
#check if the outpt dir exists, if not create
   if not os.path.exists(outdir):
        os.makedirs(outdir)
   
   print outdir   
   #create log file
   log_file = eloG(outdir+"/log.txt")     
   log_file.writeLine("Starting working on: ")
   log_file.writeLine(indir)
   log_file.writeLine(outdir)

    
   for filename in os.listdir(indir):
     print filename
     if filename.endswith(".txt"): 
       log_file.writeLine("File " + (os.path.join(indir, filename) + " Has been found"))


       list_files.append(os.path.join(indir, filename))
       list_filename_only.append(filename.split(".txt")[0])


     else:
       continue
    
   for counter, inputfile in enumerate(list_files):
   
        log_file.writeLine("Analyzing " + inputfile )
        
        matrix = readfiletomatrix(inputfile)
        
        #create the outputdir

        outdir_loop = os.path.join(outdir, list_filename_only[counter])
        if not os.path.exists(outdir_loop):
            os.makedirs(outdir_loop)
        log_file.writeLine("Creating " + outdir_loop)
        
        x = np.arange(len(matrix[0]))
        t = np.arange(matrix.shape[0])

        plotter_module.plotter(matrix, 0, x, False, "Int_I_X_precorr " , outdir_loop)        
        
        matrix = cleaning_module.cleaning(matrix, 1)
        
        x = np.arange(len(matrix[0]))
        t = np.arange(matrix.shape[0])


        plotter_module.plotter(matrix, 0, x, False, "Int_I_X_corr " , outdir_loop)
        

        list_fit_green = plotter_module.plotter_Fit(matrix, 0,x, True, "Int_I_X_fit" , outdir_loop)

        log_file_k = eloG(outdir_loop+"/log_fit_k.txt")     
        log_file_k.writeListCol(list_fit_green)
   
        log_file.writeLine("fit results saved to: " + outdir_loop+"/log_fit_k.txt")
        log_file_k.closeFile()
  
        fit_outcom = plt.figure(5)
        plt.clf()
        plt.plot(t, list_fit_green, marker='', linewidth=1, alpha=0.9, label="" )

        plt.xlabel('t(units)',fontsize=16)
        plt.ylabel('parameter from fit',fontsize=16)
        plt.savefig(os.path.join(outdir_loop, "Fit_parameter"))
        fit_outcom.show()
   log_file.closeFile()



if __name__ == "__main__":
   main(sys.argv[1:])       