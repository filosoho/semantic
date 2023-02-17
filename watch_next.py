# Import the spacy library to perform natural language processing.
import spacy

# Load the pre-trained English language model.
nlp = spacy.load("en_core_web_md")

# Define a function to find the most similar movie to a given movie description.
def find_similar_movie(description):
    
    # Open the 'movies.txt' file and read in each line as a separate string.
    with open("movies.txt") as f:
        lines = f.readlines()
    
    # Set an initial maximum similarity score and a variable to hold the title of the most similar movie.
    max_sim = -1
    similar_movie = None
    
    # Loop through each line in the 'movies.txt' file.
    for line in lines:
        
        # Split the line into separate title and description strings.
        title, desc = line.split(" :")
        
        # Process the given movie description and the description of the current movie in the loop.
        doc1 = nlp(description)
        doc2 = nlp(desc)
        
        # Calculate the similarity score between the two processed descriptions.
        sim = doc1.similarity(doc2)
        
        # If the similarity score is higher than the current maximum similarity score, update the maximum similarity score
        # and the title of the most similar movie.
        if sim > max_sim:
            max_sim = sim
            similar_movie = title.strip()
            
    # Return the title of the most similar movie.
    return similar_movie

# Define a movie description to find the most similar movie to.
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Call the 'find_similar_movie' function with the given movie description and store the returned movie title.
similar_movie = find_similar_movie(description)

# Print the title of the most similar movie to the given movie description.
print("The most similar movie to 'Planet Hulk' is:", similar_movie)