# Ollama Embedding Issue Ops

Automation isn't just for builds and deployments anymore, lets build something fun with it. In this project, we'll explore how to turn GitHub Issues into a creative workflow using Issue Ops. We'll leverage Ollama to generate text embeddings, visualize them as vector images, and automatically display these images in the issue itself.

## What we need
To follow along, start with the Ollama Devcontainer GitHub template, which comes pre-configured with Python and Ollama.
You'll just need to add the following Python libraries to your requirements.txt file:
```
scikit-learn
numpy
matplotlib
```
This will set up your environment for embedding text and visualizing vector images.

## Running Issue Ops
Go to this GitHub repo. Select "Issues" on the top horizonal nav bar. Once the issues dashboard pops up select the green "New issues" button in the upper right corner. Insert any title you want to the title bar and insert words or phrases that you want to in the issue body. 

Once an issue is created or edited, a GitHub workflow runs in the background. This workflow extracts the words and phrases from the issue body and then executes the main.py script in the repository. The Python script embeds each word, plots them on a graph using Matplotlib, and outputs the result as a .png file.

## Generating Word Vectors — main.py
The main engine of this project is the main.py. The script connects to an Ollama model (nomic-embed-text:v1.5) to generate embeddings. These embeddings allow us to understand how words relate to one another in a mathematical space.

### Setting Up Environment 
Running this in a devcontainer using .devcontainer/devcontainer.jsonwith the docker compose .devcontainer/docker-compose.ymlfile will create an Ollama server that can be accessed from “” and a python workspace to work in.

### Environment Variables:
OLLAMA_HOST: The URL to the Ollama server. When running inside the devcontainer, an Ollama server will be available at:http://ollama:11434
MODEL: The model used to embed text.Currently set to: "nomic-embed-text:v1.5". Other available models can be found in the Ollama Library.

### Loading Inputs 
Running this outside of the workflow we will need to create a words.txt to add out words/phrases. These need to be in new lines and have a “- “ prefix.
Example:
```
- king
- queen
- princess
- prince
```

### Whats main.py Does 
#### Generating embeddings 
Each word is sent to the Ollama model, which returns a high-dimensional embedding vector. Think of this as a fingerprint of the word’s meaning, with hundreds of numbers encoding semantic context.

#### Dimensionality reduction with PCA 
Since these embeddings are too large to visualize directly, the script applies Principal Component Analysis (PCA). PCA compresses the data down to three dimensions while preserving as much of the structure as possible. This makes it possible to plot the relationships in a 3D space.

#### Plotting in 3D 
Using matplotlib, the script creates a 3D scatter plot. Each point represents a word, and its location reflects semantic similarity—words with closer meanings appear closer together. Labels are added with coordinates for clarity, and the visualization is saved as a high-resolution PNG file.

## Issue Ops Workflow— issue-ops.yml
### Workflow Name & Trigger
Name: Run Vector Image Create
Trigger: It runs when a GitHub issue is opened or edited (on: issues: types: [opened, edited]).
This means anytime someone creates or modifies an issue, this workflow will automatically kick off.

### Important Steps of Workflow

#### Save Issue Body to File 
Takes the text from the issue body and writes it into a file called words.txt. This will be the input for the Python script.

#### Run Script & Generate Image
Runs the main.py script and save the image created to the img folder.

#### Commit Image Back to Repo
Commit and pushes the image created by main.py.

#### Comment on the Issue
uses peter-evans/create-or-update-comment@v3 to post a comment on the original issue with the image embedded.

## Conclusion
This project shows how automation can be used not just for routine DevOps tasks, but also for creative and exploratory workflows. By combining GitHub Issue Ops, Ollama embeddings, and visualization with Python, we’ve built a system that transforms plain text into meaningful, interactive images. Each issue becomes more than just a record of words it becomes a visual map of relationships and meaning.

The best part is that everything runs automatically in the background. Contributors simply open or edit an issue, and the workflow takes care of embedding, plotting, and posting the visualization back into the conversation. It’s a fun example of how we can blend AI, automation, and collaboration platforms like GitHub to make everyday tools more engaging.

Whether you want to explore semantic relationships between words, experiment with embeddings, or just add some creative flair to your GitHub projects, this pattern can serve as a starting point for countless other ideas. Automation doesn’t have to be boring it can be powerful, educational, and even fun.
