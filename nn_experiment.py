# Import prerequisites
import tensorflow as tf
from openpyxl import load_workbook

# Load in data - MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize data
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# Keep track of tests while running
test_number = 1

# Create neural network function
def create_NN(name, hidden_layers, neurons_per_hl):
    # Define model and input layer
    # Uses Sequential model because of its relative simplicity
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
    
    # Create hidden layers
    while hidden_layers > 0:
        # relu activation over sigmoid 
        model.add(tf.keras.layers.Dense(neurons_per_hl, activation='relu'))
        hidden_layers -= 1

    # Add output layer
    # Softmax due to classification problem
    model.add(tf.keras.layers.Dense(10, activation='softmax'))

    # Compile and train model
    # Original experiment used Adam optimizer, now using SGD because the data is simple and I want to keep the models as simple as possible
    # Using sparse categorical crossentropy because of classification problem
    model.compile(optimizer='sgd', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=2)

    # Save metrics
    test_loss, test_accuracy = model.evaluate(x_test, y_test)
    
    # Display metrics
    print("Loss: " + test_loss)
    print("Accuracy: " + test_accuracy)
    
    # Load in Excel file
    wb = load_workbook('results_v2.xlsx')
    file = wb.active

    # Add data to Excel file and save
    file.append([name, test_accuracy, test_loss])
    wb.save(filename='results_v2.xlsx')
    
    # Display test number to estimate time remaining
    print("Test number: " + test_number)
    test_number += 1

# Function calls on create_nn but for each number of hidden layers
def generator(name, neurons_per_hl):
    hidden_layers = 1

    while hidden_layers <= 5:
        name_and_number = name + " with " + str(hidden_layers) + " layers"
        create_NN(name_and_number, hidden_layers, neurons_per_hl)
        hidden_layers += 1

# Call on create_nn for no hidden layers since no need to test 5 times
create_NN('No Hidden Layer', 0, 0)

# Call on generator for each desired test
# Note: Very inefficient way of doing this - like this because of the large amount of editing throughout the experimentation design process
generator('One Nueron Per Layer', 1)
generator('2 Neurons per Layer', 2)
generator('3 Neurons per Layer', 3)
generator('4 Neurons per Layer', 4)
generator('5 Neurons per Layer', 5)
generator('10 Neurons Per Layer', 10)
generator('20 Neurons Per Layer', 20)
generator('30 Neurons Per Layer', 30)
generator('40 Neurons Per Layer', 40)
generator('50 Neurons Per Layer', 50)
generator('60 Neurons Per Layer', 60)
generator('70 Neurons Per Layer', 70)
generator('80 Neurons Per Layer', 80)
generator('90 Neurons Per Layer', 90)
generator('100 Neurons', 100)
generator('200 Neurons', 200)
generator('300 Neurons', 300)
generator('400 Neurons', 400) # hypothesis - with two layers
generator('500 Neurons', 500)
generator('1000 Neurons', 1000)
generator('5000 Neurons', 5000)
generator('10k Neurons', 10000)
