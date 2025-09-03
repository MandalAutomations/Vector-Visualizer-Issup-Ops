#!/usr/bin/env python
import os
from src.llama import llama
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://ollama:11434")
MODEL = "nomic-embed-text:v1.5" # Find available models here https://ollama.com/library

def plot_embeddings_3d(embeddings_3d, labels):

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    for i, label in enumerate(labels):
        x, y, z = embeddings_3d[i]
        text= f"{label} ({x:.2f}, {y:.2f}, {z:.2f})"
        ax.scatter(x, y, z, label=label)
        ax.text(x, y, z, text, fontsize=10)

    ax.set_title("3D Visualization of Similar Words Embeddings")
    ax.legend(loc='center left', bbox_to_anchor=(1.05, 0.5), title="Words")  # Adjust position
    plt.tight_layout()
    plt.savefig("3d_plot_small.png", dpi=1000, bbox_inches='tight')
    
if __name__ == "__main__":
    llama = llama(OLLAMA_HOST, MODEL)
    
    texts = open("words.txt", "r").read().splitlines()
    text_split = [text.replace("-", "") for text in texts]

    embeddings = []
    for text in text_split:  
        embedding = llama.create_embedding(text.strip())
        if embedding is not None:
            embeddings.append(embedding)

    embeddings = np.array(embeddings)
    embeddings = np.array(embeddings)

    pca = PCA(n_components=3)
    embeddings_3d = pca.fit_transform(embeddings)

    plot_embeddings_3d(embeddings_3d, text_split)
