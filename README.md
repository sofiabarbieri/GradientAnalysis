# GradientAnalysis
***
- lineprofile.ijm: ImaageJ macro to extract the intensity profile in the embryo, given a manually drawn line ROI, for a list of input images with two channels (DIC+fluorescence)
Run in Fiji/ImageJ. Output: directory ./Results with list of txt output files with the intesity profile per image 
***
- main_func_single.py: takes as input the ImageJ output txt files, parse the data, clean them (for border effect), and finally fits the data with a linear function to extrapolate the linear coefficient, as indicator of the gradient. It calls the *_module.py files.
``` 
python main_func_single.py -d input_directory -o output_directory
```
For each input file, it created a folder with name in which separate images of the intensity profiles for each timeframe before and post correction, along with the linear fit are contained.
It provides moreover a log file with the extrapolated gradient as a function of time.
