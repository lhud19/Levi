#Luke Hudspeth modification of CS72 HW5 for use in Levi project
#Using Python Version 3.0
#might need to instsall nltk stemming package


import math
import string
from nltk.stem.snowball import SnowballStemmer
import os



class question_processor():

    def __init__(self, question):

    #parsing in arguments
        self.word_vec_file = "vectors/vectorwords.txt"
        self.question = question

        self.files = os.listdir('vectors/')


    #loading up words into counts structure
        self.word_counts = {}
        with open (self.word_vec_file) as f1:
            for line in f1:
                word = line.lower().split()
                self.word_counts[word[0]] = 0

        self.files.remove("vectorwords.txt")


        #make vectors for each document
        self.doc_vectors = self.document_vectors()











    #function to answer the questions by cosine similary of vectors
    def answer_questions(self):

        #stemmer for stemming
        stemmer = SnowballStemmer("english")


        #removing punctuation
        self.question = self.question.translate(string.punctuation)
        #making words lowercase
        words = self.question.lower().split()
        q_vector = self.word_counts.copy()
        #calculating the vector of the question
        for word in words:

            word_option = stemmer.stem(word)

            if word in self.word_counts:
                q_vector[word] +=1
            elif word_option in self.word_counts:
                q_vector[word_option] +=1


        #calculate cosine similarity to find the most likely function for levi to perform
        best_sim = -5


        for i in range(len(self.doc_vectors)):
            cos_sim = calculate_cosine_similarity(q_vector, self.doc_vectors[i])

            if cos_sim > best_sim:
                best_function = i
                best_sim = cos_sim

        if best_sim == 0:
            return "none"
        else:
            return self.doc_list[best_function]



    # function to calculate vectors for each function
    def document_vectors(self):

        # list that will contain vectors for each document
        doc_vectors = []
        stemmer = SnowballStemmer("english")

        self.doc_list = []
        for doc in self.files:
            self.doc_list.append(doc)

            # copy the dictionary that represents the 12 words we are looking at
            doc_vector = self.word_counts.copy()
            with open("vectors/"+doc) as f:
                for line in f:
                    # removing punctuation
                    line = line.translate(None, string.punctuation)

                    # making words lower case
                    words = line.lower().split()
                    for word in words:
                        word_option = stemmer.stem(word)

                        # count the words we care about
                        if word in self.word_counts:
                            doc_vector[word] += 1
                        elif word_option in self.word_counts:
                            doc_vector[word_option] += 1

            # append that docs vector to the array
            doc_vectors.append(doc_vector)

        return doc_vectors


def calculate_cosine_similarity(A, B):
    keys = A.keys()
    A_v = [0]*len(keys)
    B_v = [0]*len(keys)

    index = 0

    #getting the counts for each vector
    for key in keys:
        A_v[index] = A[key]
        B_v[index] = B[key]
        index +=1


    #formula for cosine similarity
    sum_dot = 0
    sum_a_sqr = 0
    sum_b_sqr = 0
    for i in range(23):
        sum_dot += A_v[i]*B_v[i]
        sum_a_sqr += A_v[i]**2
        sum_b_sqr += B_v[i]**2


    denominator = math.sqrt(sum_a_sqr)*math.sqrt(sum_b_sqr)

    if denominator == 0:
        return 0
    else:
        #return similarity
        return sum_dot/(denominator*1.0)


