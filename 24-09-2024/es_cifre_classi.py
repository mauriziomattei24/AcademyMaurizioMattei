import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, classification_report

class MNIST_CIFRE:
    def __init__(self):
        self.model = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

    def load_data(self):
        (self.X_train, self.y_train), (self.X_test, self.y_test) = mnist.load_data()

    def target_handling(self):
        self.y_train = to_categorical(self.y_train, num_classes=10)
        self.y_test = to_categorical(self.y_test, num_classes=10)

    def model_construction(self):

        self.model = Sequential()
        self.model.add(Flatten())
        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dense(10, activation='softmax'))
   
        self.model.compile(optimizer='adam',
                           loss='categorical_crossentropy',
                           metrics=['accuracy'])
        

    def model_fit_predict_visualization(self):
        # train
        self.model.fit(self.X_train, self.y_train,
                       epochs=10,
                       batch_size=32,
                       validation_split=0.1)
        # evaluate
        test_loss, test_accuracy = self.model.evaluate(self.X_test, self.y_test)
        print(f'Perdita sul test set: {test_loss:.4f}')
        print(f'Accuratezza sul test set: {test_accuracy:.4f}')

        # predict
        predictions = self.model.predict(self.X_test)

        # predizioni in etichette
        predicted_classes = np.argmax(predictions, axis=1)
        true_classes = np.argmax(self.y_test, axis=1)

        # Matrice di confusione
        conf_matrix = confusion_matrix(true_classes, predicted_classes)
        plt.figure(figsize=(10, 8))
        sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
        plt.title('Matrice di Confusione')
        plt.xlabel('Predizione')
        plt.ylabel('Vero Valore')
        plt.show()

        # Report di classificazione
        report = classification_report(true_classes, predicted_classes)
        print('Report di Classificazione:')
        print(report)

def main():
    
    mnist_model = MNIST_CIFRE()
    
    mnist_model.load_data()

    mnist_model.target_handling()

    mnist_model.model_construction()

    mnist_model.model_fit_predict_visualization()

main()
