library('Metrics')
library('randomForest')
library('ggplot2')
library('ggthemes')
library('dplyr')
file="/Users/deeps/Desktop/Quora-Question-Classifier/PHASE 2/dataset_sel.csv"
data1 = read.csv(file,header=FALSE, sep = ",")
head(data1)
str(data1)
summary(data1)
set.seed(100)
train <- sample(nrow(data1), 0.7*nrow(data1), replace = FALSE)
TrainSet <- data1[train,]
ValidSet <- data1[-train,]
summary(TrainSet)
summary(ValidSet)
model1 <- randomForest(V1 ~ ., data = TrainSet, importance = TRUE)
model1
model2 <- randomForest(V1 ~ ., data = TrainSet, ntree = 500, mtry = 1, importance = TRUE)
model2
predTrain <- predict(model2, TrainSet, type = "class")
table(predTrain,TrainSet$V1)
sort(importance(model2)[,1],decreasing = TRUE)
