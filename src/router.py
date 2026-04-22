from sentence_transformers import SentenceTransformer  #converts text → numerical vectors (embeddings)
import faiss                                            # fast similarity search between vectors
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")   #pretrained model that converts sentences into 384-dimensional vectors

personas = {
    "bot_a": "AI and crypto will solve everything. Optimistic about Elon Musk and space.",
    "bot_b": "Tech is destroying society. Critical of AI and capitalism.",
    "bot_c": "Focused on markets, trading, ROI, finance."
}

bot_ids = list(personas.keys())   #Separate Keys and Values  stores-->bots name
persona_texts = list(personas.values())  #Stores all persona descriptions (text)

embeddings = model.encode(persona_texts)  #Converts all persona texts → vectors   3 bots, each with 384 numbers)

dimension = embeddings.shape[1]  #Create FAISS Index
index = faiss.IndexFlatL2(dimension) #Creates FAISS index using L2 distance (Euclidean distance)
index.add(np.array(embeddings))   #Adds all persona vectors into FAISS


def route_post_to_bots(post_content, threshold=1.5):  #threshold → max allowed distance
    post_embedding = model.encode([post_content])     #Converts input post into vector
    D, I = index.search(np.array(post_embedding), k=3)   #D → distances (how close vectors are)   ,,I → indices of closest bots

    selected = []    #Empty list to store matching bots
    print("\n FAISS ROUTING")

    for idx, dist in zip(I[0], D[0]):  #idx → index of bot, dist->distance score
        bot_id = bot_ids[idx]    #Get actual bot name from index
        print(f"{bot_id} distance: {dist:.3f}")  #Print similarity score

        if dist < threshold:   #If distance is small enough → bot is relevant
            selected.append(bot_id)

    print("Selected Bots:", selected)
    return selected