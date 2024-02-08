# Graphika

Graphika is a user-friendly one-page interface that simplifies the process of integrating Hugging Face Language Models (LLM) with Neo4j by converting natural language input into Neo4j Cypher Queries. This library aims to provide a smooth learning curve for individuals who want to start using Neo4j's Cypher language for querying their graphs.

## Features

- **Model Selection:** Choose from a variety of pre-trained language models available on Hugging Face.
  
- **API Integration:** Input your Hugging Face API key directly in the web interface for seamless model access.

- **Text Transformation:** Effortlessly convert natural language input into Neo4j Cypher Queries.

## Getting Started

Follow these steps to get started with Graphika:

1. Clone the repository:
    ```bash
    git clone https://github.com/elmondhir/Graphika-v1.0.git
    cd Graphika
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the Hugging Face API key:
    - Obtain your Hugging Face API key from [Hugging Face](https://huggingface.co/).
     
4. Start the application with the following command, where you can set the API key directly in the web interface:
    ```bash
    python -B manage.py runserver
    ```

4. Open your browser and go to [http://localhost:8000](http://localhost:8000) to access the Graphika interface.

## OR Running with Docker

To run Graphika using Docker, make sure Docker is installed on your machine. If not, you can download and install Docker from the [official Docker website](https://www.docker.com/get-started).

Follow these steps:

1. Build the Docker image:
    ```bash
    docker-compose build
    ```

2. Start the application:
    ```bash
    docker-compose up
    ```

3. Open your browser and go to [http://localhost:8000](http://localhost:8000) to access the Graphika interface.

## Usage

1. Choose an LLM model from the available options.

2. Enter your Hugging Face API key in the designated input field on the web page.

3. Input your natural language text that you want to transform into a Neo4j Cypher Query.

4. Click the "Submit" button to generate the Cypher Query.

5. Copy the generated Cypher Query and use it in your Neo4j database.

## Screenshots

### Chose the model, enter the HF API and press submit
![Alt text](screenshot.png?raw=true "Title")

## Contributing

We welcome contributions! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.