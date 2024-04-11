# AI Fundamentals: Building AI Solutions with Python

This repository is designed to provide you with a foundation in the basic building blocks of creating AI solutions using Python. 


## Getting Started

#### 1. Clone the repository

```bash
git clone https://github.com/daveebbelaar/ai-fundamentals.git
```

#### 2. Create a Python environment

Python 3.6 or higher using `venv` or `conda`. Using `venv`:

``` bash
cd ai-fundamentals
python3 -m venv env
source env/bin/activate
```

Using `conda`:
``` bash
cd ai-fundamentals
conda create -n ai-fundamentals python=3.10
conda activate ai-fundamentals
```

#### 3. Install the required dependencies
``` bash
pip install -r requirements.txt
```

#### 4. Set up the keys in a .env file

First, create a `.env` file in the root directory of the project. Inside the file, add your OpenAI API key:

```makefile
OPENAI_API_KEY="your_api_key_here"
```

Save the file and close it. In your Python script or Jupyter notebook, load the `.env` file using the following code:
```python
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
```

By using the right naming convention for the environment variable, you don't have to manually store the key in a separate variable and pass it to the function. The library or package that requires the API key will automatically recognize the `OPENAI_API_KEY` environment variable and use its value.

When needed, you can access the `OPENAI_API_KEY` as an environment variable:
```python
import os
api_key = os.environ['OPENAI_API_KEY']
```

## Tutorials

For video tutorials on how to use the LangChain library and run experiments, visit the YouTube channel: [youtube.com/@daveebbelaar](https://www.youtube.com/channel/UCn8ujwUInbJkBhffxqAPBVQ?sub_confirmation=1)