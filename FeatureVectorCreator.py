#FeatureVectorCreator.py

#import statements
import cv2
import os

#Begin the HOG class
class H_O_G:
    #constructor
    def __init__(self, directory):
        self.currentDirectory = directory
        self.positiveSampleImages = 0
        self.negativeSampleImages = 0
        os.chdir(directory)
        print(os.getcwd())
    
    #Helper function to compute the feature vector for each image
    def ImageHOGComputer(self, img, hog):
        tmpImg = cv2.imread(img)
        featureVector = hog.compute(tmpImg)
        return featureVector
    
    #Computes the feature vector for each image in a directory and saves it to a CSV file
    def FeatureVectorCreator(self):
        images = 0;
        hog = cv2.HOGDescriptor()
        DS = open("PositiveImages.csv", 'a')
        for files in os.listdir(os.getcwd()):
            if files.endswith(".jpeg"):
                tmpstr = ""
                tmp = self.ImageHOGComputer(files, hog)
                images = images + 1
                for i in tmp:
                    tmpstr = tmpstr + str(i[0]) + ","
                tmpstr = tmpstr + "1" + "\n"    
                print(tmpstr)
                DS.write(tmpstr)
        DS.close()
        print("The amount of images processed: " + str(images) + "\n")
    
    #Displays the options for the user
    def DisplayOptions(self):
        print("=============================================================================================")
        print("HOGModule for use in extracting feature vectors into a CSV file")
        print("----Options----")
        print("1. Create feature vectors from samples in directory")
        print("2. Exit")

#Main function
if __name__ == '__main__': 
    inputDir = raw_input("Enter the name of the directory where the files are located for HOG Training:\n")
    HOGClass = H_O_G(inputDir)
    end = False
    HOGClass.DisplayOptions()
    while(not end):
        inputCommand = raw_input("Ready for command: ")
        if(inputCommand == "1"):
            HOGClass.FeatureVectorCreator()
        elif(inputCommand == "2"):
            end = True
        else:
            print("Not a valid command. Try Again...")
        HOGClass.DisplayOptions()
    print("Ending program...")
else:
    print 'HOGModule is being imported from another module.'

