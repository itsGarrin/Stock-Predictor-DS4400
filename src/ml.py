# Define a function to calculate the log probability of a sentence given a speaker
import numpy as np
import pandas as pd


def log_prob(sentence, speaker):
    # Calculate the log probability of the sentence given the speaker
    log_prob = np.log(prior_prob[speaker])
    for word in sentence.split():
        if word in word_prob.columns:
            log_prob += np.log(word_prob.loc[speaker, word])
    return log_prob


# Define a function to predict the speaker of a sentence
def predict_speaker(sentence):
    # Calculate the log probability of the sentence given Trump
    log_prob_trump = log_prob(sentence, 'trump')
    # Calculate the log probability of the sentence given Obama
    log_prob_obama = log_prob(sentence, 'obama')
    # Return 1 if the sentence is more likely to be spoken by Trump, 0 otherwise
    if log_prob_trump > log_prob_obama:
        return '1'
    else:
        return '0'


# Define a function to calculate the metrics of the classifier
def calculate_metrics(df):
    tp = len(df[(df['speaker'] == 'trump') & (df['prediction'] == '1')])
    tn = len(df[(df['speaker'] == 'obama') & (df['prediction'] == '0')])
    fp = len(df[(df['speaker'] == 'obama') & (df['prediction'] == '1')])
    fn = len(df[(df['speaker'] == 'trump') & (df['prediction'] == '0')])

    # Calculate the accuracy
    accuracy = (tp + tn) / (tp + tn + fp + fn + 1e-10)

    # Calculate the sensitivity
    sensitivity = tp / (tp + fn + 1e-10)

    # Calculate the specificity
    specificity = tn / (tn + fp + 1e-10)

    # Calculate the precision
    precision = tp / (tp + fp + 1e-10)

    # Calculate the F1 score
    f1_score = 2 * (precision * sensitivity) / (precision + sensitivity + 1e-10)

    return accuracy, sensitivity, specificity, precision, f1_score


def word_vector(words, word_list, use_frequency=False):
    """ Convert a list of words to a vector by comparing with words in word_list
    words: A list of words which we convert to a vector
    word_list: The chosen words against which we compare
    use_frequency: if False, vector components are 1/0, else n = # of occurrences
    """

    word_list = sorted(list(set(word_list)))

    if use_frequency:
        count = Counter(words)
        return [count[w] for w in word_list]
    else:
        return [int(w in words) for w in word_list]


# Define a function to calculate the Euclidean distance between two sentences
def euclidean_distance(sentence1, sentence2):
    # Convert the sentences to vectors
    vector1 = word_vector(sentence1, top_word_subset['word'])
    vector2 = word_vector(sentence2, top_word_subset['word'])
    # Calculate the Euclidean distance between the vectors
    distance = np.linalg.norm(np.array(vector1) - np.array(vector2))
    return distance


# Define a function to calculate k-NN
def knn(sentence, k, df_train):
    # Calculate the Euclidean distance between the sentence and each sentence in the dataset
    df_train['distance'] = df_train['text'].apply(lambda x: euclidean_distance(sentence, x))
    # Sort the dataset by distance
    df_sorted = df_train.sort_values(by='distance', ascending=True)
    # Select the top k sentences
    df_knn = df_sorted.head(k)

    # Calculate the probability of the sentence being spoken by Trump
    prob_trump = len(df_knn[df_knn['speaker'] == 'trump']) / k
    # Calculate the probability of the sentence being spoken by Obama
    prob_obama = len(df_knn[df_knn['speaker'] == 'obama']) / k

    # Return 1 if the sentence is more likely to be spoken by Trump, 0 if the sentence is more likely to be spoken by Obama
    if prob_trump > prob_obama:
        return '1'
    else:
        return '0'


# Define a function to perform n-fold cross validation on the k-NN classifier
def cross_validation(n, k):
    # Calculate the size of each fold
    fold_size = int(len(df2) / n)
    # Initialize a DataFrame to store the metrics of each fold
    df_metrics = pd.DataFrame(columns=['accuracy', 'sensitivity', 'specificity', 'precision', 'f1'])

    # Perform n-fold cross validation
    for i in range(n):
        # Select the training set
        df_train = pd.concat([df2.iloc[:i * fold_size], df2.iloc[(i + 1) * fold_size:]]).reset_index(drop=True)
        # Select the test set
        df_test = df2.iloc[i * fold_size:(i + 1) * fold_size].reset_index(drop=True)
        # Calculate the predicted speaker for each sentence in the test set
        df_test['prediction'] = df_test['text'].apply(lambda x: knn(x, k, df_train))
        # Calculate the metrics of the classifier
        accuracy, sensitivity, specificity, precision, f1 = calculate_metrics(df_test)
        # Append the metrics to the DataFrame
        df_metrics.loc[i] = [accuracy, sensitivity, specificity, precision, f1]
    # Calculate the average metrics across all folds
    df_metrics.loc['mean'] = df_metrics.mean()
    return df_metrics
