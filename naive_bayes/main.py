import csv
import math
import random


# Veri setinin yüklenmesi
def loadCsv(filename):
    lines = csv.reader(open('C:/Users/eymen/Desktop/pima-indians-diabetes.csv'))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset


# Veri setini train,test ayrımı
def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]


# Her sınıf kendi içerisinde değerlendirilir. Sınıfları birbirinden ayırdık.
def seperateByClass(dataset):
    seperated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in seperated):
            seperated[vector[-1]] = []
        seperated[vector[-1]].append(vector)
    return seperated


# Ortalama
def mean(numbers):
    return sum(numbers) / float(len(numbers))


# Standart Sapma
def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1)
    return math.sqrt(variance)


# Tüm featurelar için Ortalama ve Standart sapma
def summarize(dataset):
    summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries


# Sınıflarda aynı işlemlerin yapılması
def summerizeByClass(dataset):
    seperated = seperateByClass(dataset)
    summaries = {}
    for classValue, instances in seperated.items():
        summaries[classValue] = summarize(instances)
    return summaries


# Normal Dağılımı hesaplama
def calculateProbability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent


#  Sınıf Değeri için olasılıklar
def calculateClassProbabilities(summaries, inputVector):
    probabilities = {}
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = inputVector[i]
            probabilities[classValue] *= calculateProbability(x, mean, stdev)
        return probabilities


# Tahminler
def predict(summaries, inputVector):
    probabilities = calculateClassProbabilities(summaries, inputVector)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.items():
        if bestLabel is None or probability > bestProb:
            bestProb = property
            bestLabel = classValue
    return bestLabel


# Test verisinde tahminlerin yapılması
def getPredictions(summaries, testSize):
    predictions = []
    for i in range(len(testSize)):
        result = predict(summaries, testSize[i])
        predictions.append(result)
    return predictions


# Başarı testi
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0


def main():
    filename = 'pima-indians-diabetes.csv'
    splitRatio = 0.67
    dataset = loadCsv(filename)
    # print(dataset)
    trainingSet, testSet = splitDataset(dataset, splitRatio)
    print('Split {0} row into train = {1} and test {2} rows'.format(len(dataset), len(trainingSet), len(testSet)))
    # prepare model
    summaries = summerizeByClass(trainingSet)
    # test model
    predictions = getPredictions(summaries, testSet)
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy %{0}'.format(accuracy))


main()
