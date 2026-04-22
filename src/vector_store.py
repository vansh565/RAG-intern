import faiss                           #  a library used for fast similarity search on vectors.
import numpy as np                     #  used for handling arrays and numerical data
from embeddings import get_embedding   #  function that converts text → vector (embedding).
from personas import personas          #  bot personas (likely a dictionary with descriptions).

class FAISSVectorStore:                # Defines a class that manages: storing vectors , searching similar vectors
    def __init__(self):                 # Constructor (Initialization)
        self.dimension = 384  # MiniLM embedding size -> Sets vector size to 384

        self.index = faiss.IndexFlatL2(self.dimension)   #Creates a FAISS index using:L2 distance (Euclidean distance),Used to compare similarity between vectors


        self.bot_ids = []           #Stores bot names
        self.vectors = []           #Stores vector representations of personas

        self._build_index()         # convert personas into vectors,store them in FAISS

    def _build_index(self):         # internal function to prepare  vector database
        print("Building FAISS index")

        for bot, data in personas.items():  #Loop through each persona,bot name,persona details
            vec = get_embedding(data["description"])   #Convert persona description → vector
            vec = np.array(vec, dtype="float32")   #Convert vector into NumPy array, FAISS requires float32 format

            self.vectors.append(vec)   #Store vector in list
            self.bot_ids.append(bot)   #Store corresponding bot ID

        self.index.add(np.array(self.vectors))   #Add all vectors to FAISS index

    def search(self, query, k=3):       #Searches for top k similar bots for a given query
        q_vec = get_embedding(query)    #Convert input text → vector
        q_vec = np.array([q_vec], dtype="float32")   #Convert into proper shape (2D array)

        distances, indices = self.index.search(q_vec, k)  #Faiss returns->distances → similarity scores,indices->positions of closest vectors

        results = []   #Create empty list to store results
        for i, idx in enumerate(indices[0]):
            results.append((self.bot_ids[idx], float(distances[0][i])))

        return results