library(caret)
library(RWeka)

file="/Users/deeps/Desktop/QUORA/dataset.csv"
data1 = read.csv(file,header=FALSE, sep = ",")
colnames(data1)<-c("Label","CC","EX","JJS","MD","PRP","PRP$")
TrainData <- data1[2:601,2:7]
TrainClasses <- as.character(data1[2:601,1])
jripFit <- train(TrainData, TrainClasses,method = "JRip")
plot(jripFit)
m<-summary(jripFit)

library(rpart.plot)
head(data1)
set.seed(3033)
intrain <- createDataPartition(y = data1$Label, p= 0.7, list = FALSE)
training <- data1[intrain,]
testing <- data1[-intrain,]
dim(training); 
dim(testing);
anyNA(data1)
summary(data1)
trctrl <- trainControl(method = "repeatedcv", number = 10, repeats = 3)
set.seed(3333)
dtree_fit <- train(TrainData, TrainClasses, method = "rpart",parms = list(split = "information"))
prp(dtree_fit$finalModel, box.palette = "Reds", tweak = 1.2)

