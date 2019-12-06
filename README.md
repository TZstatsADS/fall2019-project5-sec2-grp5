# ADS Project 5: 

Term: Fall 2018

+ Team group5
+ Projec title: Implementation of CNN in Emotion Recognition
+ Team members
	+ team member Xudong Guo
	+ team member Yanyan Liu
	+ team member Hang Hu
	+ team member Nan Yang
	+ team member Sixuan Li
+ Project summary: The purpose of this project is using CNN models to recognize facial expression, we used fer2013 dataset from kaggle https://www.kaggle.com/deadskull7/fer2013. The dataset contains 34034 unique photos with clearly-defined labels of 7 different emotions.

+ Transfer Learning

	Three modified CNN models: VGG19, Mobilenet, Resnet were applied to our datasets, there training accuracy and testing accuracy were collected to make comparison.

![](https://github.com/TZstatsADS/fall2019-proj5-sec2--proj5-grp5/blob/master/figs/transfer%20learning.jpg)

+ Improved Model

	We also build an improved model based on all three models above, the new model performance is better than previous models.
Training time drops from around 450s to 360s for each epoch. Validation loss drops from 1.3889 to 1.2041 and validation accuracy enhances from 45.12% to 54.08%.

![](https://github.com/TZstatsADS/fall2019-proj5-sec2--proj5-grp5/blob/master/figs/improved%20model.png)
	
**Contribution statement**: 
1. Xudong Guo: Trained and tuned MobileNet, ResNet transfer learning models and the Improved Model, generated report
2. Yanyan Liu: Trained and tuned VGG19 transfer learning model and the Improved Model, developed pixel decoding algorithm
3. Hang Hu:
4. Nan Yang:
5. Sixuan Li:

Following [suggestions](http://nicercode.github.io/blog/2013-04-05-projects/) by [RICH FITZJOHN](http://nicercode.github.io/about/#Team) (@richfitz). This folder is orgarnized as follows.

```
proj/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

Please see each subfolder for a README file.
