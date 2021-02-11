import gensim
import nltk
import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize



# Open file and tokenize sentences
file_docs = []

with open ('demofile.txt') as f:
    tokens = sent_tokenize(f.read())
    for line in tokens:
        file_docs.append(line)
# print("Number of documents:",len(file_docs))



# Tokenize words and create dictionary
gen_docs = [[w.lower() for w in word_tokenize(text)]
            for text in file_docs]

dictionary = gensim.corpora.Dictionary(gen_docs)
# print(dictionary.token2id)
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
# print(corpus)




# TFIDF
# words that occur more frequently across the documents get smaller weights.
tf_idf = gensim.models.TfidfModel(corpus)
# for doc in tf_idf[corpus]:
#     print([[dictionary[id], np.around(freq, decimals=2)] for id, freq in doc])




# Creating similarity measure object
# building the index
sims = gensim.similarities.Similarity('workdir/',tf_idf[corpus],
                                        num_features=len(dictionary))
# print(sims)




# Create Query Document
file2_docs = []

with open ('demofile2.txt') as f:
    tokens = sent_tokenize(f.read())
    for line in tokens:
        file2_docs.append(line)
# print("Number of documents:",len(file2_docs))
for line in file2_docs:
    query_doc = [w.lower() for w in word_tokenize(line)]
    #update an existing dictionary and create bag of words
    query_doc_bow = dictionary.doc2bow(query_doc)

# perform a similarity query against the corpus
query_doc_tf_idf = tf_idf[query_doc_bow]
# print(document_number, document_similarity)
print('Comparing Result:',sims[query_doc_tf_idf])


# Average Similarity(Optional)
import numpy as np

sum_of_sims =(np.sum(sims[query_doc_tf_idf], dtype=np.float32))
print(sum_of_sims)


percentage_of_similarity = round(float((sum_of_sims / len(file_docs)) * 100))
print(f'Average similarity float: {float(sum_of_sims / len(file_docs))}')
print(f'Average similarity percentage: {float(sum_of_sims / len(file_docs)) * 100}')
print(f'Average similarity rounded percentage: {percentage_of_similarity}')
