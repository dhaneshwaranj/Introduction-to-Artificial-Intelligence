import Testing

accuracies = []
for i in range(5):
    nnet, testAccuracy = Testing.testPenData()
    accuracies.append(testAccuracy)

print "Testing on Pen Data \n"
print "Maximum Accuracy: ", max(accuracies)
print "Average Accuracy: ", Testing.average(accuracies)
print "Standard Deviation: ", Testing.stDeviation(accuracies)


accuracies = []
for i in range(5):
    nnet, testAccuracy = Testing.testCarData()
    accuracies.append(testAccuracy)

print "Testing on Car Data \n"
print "Maximum Accuracy: ", max(accuracies)
print "Average Accuracy: ", Testing.average(accuracies)
print "Standard Deviation: ", Testing.stDeviation(accuracies)
