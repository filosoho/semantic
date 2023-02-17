import spacy  

nlp = spacy.load('en_core_web_md')
#nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

word1 = nlp("computer")
word2 = nlp("phone")
word3 = nlp("tablet")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('computer phone tablet banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


#-------------------------------------------------- Additional comments to Compulsory Task 1 -----------------------------------------------------------------------------------
'''The results of the similarity measurements show that "banana" is more similar to "monkey" than it is to "cat", and "cat" is more similar to "monkey" 
than it is to "banana". This may seem counterintuitive, but it makes sense when you consider the fact that both cats and monkeys are animals, while bananas are a type of fruit.

As for an example of my own, one interesting similarity I found using Spacy's word embeddings is that the words "computer", "phone", and "tablet" are highly similar 
to each other. This makes sense because they are all electronic devices that are commonly used for communication and computing. In contrast, the word "banana" 
is less similar to these words, as it belongs to a different semantic category (i.e., it is a type of food).

When running the code with the simpler language model en_core_web_sm, I noticed that the similarity scores were generally lower compared to the medium-sized model en_core_web_md. 
This is because the smaller model has fewer parameters and thus a more limited representation of the language, which can affect the accuracy of the word embeddings. 
However, the code still produced meaningful results, indicating that even a simpler model can be useful for certain natural language processing tasks.

Notes to example.py:
After running the example file with the simpler language model 'en_core_web_sm', I noticed that the output is not as detailed and accurate as when using the larger model 'en_core_web_md'. 
This is because the smaller model has fewer components and does not contain as much linguistic knowledge as the larger model. As a result, the similarity scores for both the complaints 
and recipes are generally lower compared to the output of the larger model.

For instance, when comparing the complaints with each other using 'en_core_web_md', the highest similarity score is 0.836, while the same comparison using 'en_core_web_sm' results in 
the highest similarity score of 0.747. Similarly, when comparing the recipes with each other using 'en_core_web_md', the highest similarity score is 0.871, while the same comparison 
using 'en_core_web_sm' results in the highest similarity score of 0.768.

The comparison between the complaints and recipes using 'en_core_web_sm' also produced lower similarity scores compared to the output of 'en_core_web_md'. 
This is expected since the smaller model has less knowledge and may not be able to accurately capture the nuances in the different domains.
'''