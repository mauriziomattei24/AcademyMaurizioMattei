# Classe Testing

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix


class testing:

    def __init__(self, X_test, y_test, model):

        self.model=model
        self.test_loss, self.test_accuracy = self.model.evaluate(X_test, y_test)

    
    def predictions(self, X_test, y_test):

        predictions = self.model.predict(X_test)

        # Converte le probabilità nelle classi predette dal modello
        predicted_classes = np.argmax(predictions, axis=1)
        for index in range(len(predicted_classes)):
            if predicted_classes[index] >= 9:
                predicted_classes[index] +=1

        # Estrae le etichette di classe corrette dal test set
        true_classes = np.argmax(y_test, axis=1)
        for index in range(len(true_classes)):
            if true_classes[index] >= 9:
                true_classes[index] +=1

        return predicted_classes, true_classes


    def confusionmatrix(self, true_classes, predicted_classes):
        
        # Matrice di confusione
        conf_matrix = confusion_matrix(true_classes, predicted_classes)

        # Visualizzazione della matrice di confusione
        plt.figure(figsize=(10,8))
        sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
        plt.title('Matrice di Confusione')
        plt.xlabel('Predizione')
        plt.ylabel('Vero Valore')
        plt.show()