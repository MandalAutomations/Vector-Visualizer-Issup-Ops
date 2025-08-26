# Vector Visualizer

This project visualizes word embeddings in 3D using PCA and Matplotlib. It leverages the Llama model (via Ollama) to generate embeddings for a list of words, then plots them for easy comparison.

## Features

- Generates embeddings for words using a Llama model.
- Reduces embedding dimensions to 3D using PCA.
- Visualizes embeddings in a 3D scatter plot with labels.
- Saves the plot as a high-resolution PNG.

## Requirements

- Python 3.10+
- Ollama server running with a supported Llama model
- `numpy`
- `scikit-learn`
- `matplotlib`

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Ensure your Ollama server is running and accessible (default: `http://ollama:11434`).
2. Add your words to `words.txt`, one per line.
3. Run the main script:
	```bash
	python main.py
	```
4. The output plot will be saved as `3d_plot_small.png`.

## Configuration

- Change the model or host by editing `MODEL` and `OLLAMA_HOST` in `main.py`.

## File Structure

- `main.py`: Main script for generating and plotting embeddings.
- `src/llama.py`: Llama model interface.
- `words.txt`: List of words to visualize.
- `requirements.txt`: Python dependencies.