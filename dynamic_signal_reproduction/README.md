# Dynamic Signal Reproduction

## Run:
run 'dynamic signal generation.vi'.
Data is entered as a .csv that does not contain any line breaks. Within the VI, select "X file data" and navigate to the file you wish to reproduce. Within the VI, you have the option to select synthesis by using the NI 9260 in cDAQ slot 7 or the NI 9263 in cDAQ slot 8. You must also specify the synthesis rate. Scaling ratio is number which multiply your signal with to get the signal in volts. (So if your signal is already in volts, enter this value as one). If left as zero by default, the VI will scale the data to match the output range of the synthesis card. 