**Project Overview**

The AI Website Assistant is a Streamlit-based application designed to assist users in finding job opportunities. Utilizing the power of Pinecone and HuggingFace, this tool searches for relevant job listings based on user input and presents the most pertinent results.

**Features**

- Easy-to-use interface for inputting search queries.
- Secure entry for HuggingFace and Pinecone API keys.
- Capability to push and fetch data to and from Pinecone.
- Dynamic search result display based on user-defined criteria.

**Prerequisites**

Before running the AI Website Assistant, ensure you have:

- A Pinecone account and a corresponding API key.
- A HuggingFace account with an API key.

**Installation**

Clone the repository
First, clone the repository to your local machine using Git:

git clone https://github.com/Bvcott21/ai-website-assistant.git
cd ai-website-assistant

Install dependencies
Make sure you have Python installed on your system. Then, install the required packages using:

pip install -r requirements.txt

**Configuration**

To interact with Pinecone and HuggingFace services, you need to have valid API keys. These keys are entered via the application's sidebar.

**Running the Application**

Launch the application by running the following command in your terminal:

python -m streamlit run app.py

**Usage**

After launching, follow these steps:

- Enter your HuggingFace and Pinecone API keys in the sidebar.
- Optionally, click "Load data to Pinecone" if you're setting up for the first time or updating the dataset.
- In the main interface, type your query in the "How can I help?" input box.
- Adjust the slider to select the number of results you wish to receive.
- Click "Search" to display job listings relevant to your query.

**Important Files**

_**app.py:**_ The main application script.

_**utils.py:**_ Contains utility functions for data processing and interaction with Pinecone and HuggingFace APIs.

_**constants.py:**_ Defines constants used across the application, such as API endpoints and environment configurations.

**Creating a Pinecone Instance**

It is essential to have a Pinecone instance created and properly configured before using the AI Website Assistant. Refer to the Pinecone documentation for guidance on setting up an instance and obtaining your API key.
