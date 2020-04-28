import Testing
import NeuralNet

for numPerceptrons in range(0, 41, 5):
    accuracies = []
    for i in range(5):
        nnet, testAccuracy = NeuralNet.buildNeuralNet(examples=Testing.penData,
                                                      maxItr=200,
                                                      hiddenLayerList=[numPerceptrons])
        accuracies.append(testAccuracy)

    print "Testing on Pen Data with ", numPerceptrons, " Perceptrons. \n"
    print "Maximum Accuracy: ", max(accuracies)
    print "Average Accuracy: ", Testing.average(accuracies)
    print "Standard Deviation: ", Testing.stDeviation(accuracies)


for numPerceptrons in range(0, 41, 5):
    accuracies = []
    for i in range(5):
        nnet, testAccuracy = NeuralNet.buildNeuralNet(examples=Testing.carData,
                                                      maxItr=200,
                                                      hiddenLayerList=[numPerceptrons])
        accuracies.append(testAccuracy)

    print "Testing on Car Data ", numPerceptrons, " Perceptrons. \n"
    print "Maximum Accuracy: ", max(accuracies)
    print "Average Accuracy: ", Testing.average(accuracies)
    print "Standard Deviation: ", Testing.stDeviation(accuracies)