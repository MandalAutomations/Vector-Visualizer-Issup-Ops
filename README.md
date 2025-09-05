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
