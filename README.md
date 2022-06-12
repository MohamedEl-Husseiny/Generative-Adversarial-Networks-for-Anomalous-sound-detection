# Generative-Adversarial-Networks-for-Anomalous-sound-detection
 Packages needed:
 1. torch 
 2. tqdm
 3. numpy
 4. librosa
 5. matplotlib
 6. scikit-learn
 
 
 Steps to run the code:
 1. Download the development dataset  
 2. The dataset consists of 7 machines, decompress the data for the machine you want to train. The dataset file for each machine consists of 3 folders train , source test and target test
 3. Create a folder and put the 3 folders (train , source test and target test) in it.
 4. Take a copy of the .py file "Featureextraction" and paste in each folder (train , source test and target test)    
 5. run the command "python Featureextraction.py"
 6. To train the model run the command "python train.py --dataset name of machine trained for example (fan0) --dataroot (path to dataset folder) --niter 300 --batchsize 16 --id (is the section number)
 7. To test the trained mode run the command "python train.py --dataset (name used when training) --dataroot (path to dataset folder) --load_weights --batchsize 16 --id (section number)
 8. The results will appear in the terminal the first value is the AUC of testing on source test and the second value is the AUC of testing on target test. 
