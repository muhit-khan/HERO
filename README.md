# HERO Voice Assistant

HERO - The AI power Voice Assistant is a Python-based project that allows you to ask daily life queries that uses speech recognition and synthesis, respectively. Additionally, it leverages the `bardapi` module, developed by [dsdanielpark](https://github.com/dsdanielpark), for retrieving answers using Google BARD AI to user queries.

## Prerequisites

To run HERO, you need to have the following dependencies installed:

- Python 3.10 or higher
- `speech_recognition` library
- `pyttsx3` library
- `bardapi` module
- `pyaudio` library

You can install the required dependencies by running the following command:
    `pip install -r requirements.txt`

Make sure you have a working microphone connected to your computer for voice input.

## Installation

1. Clone the repository:
    `git clone https://github.com/your-username/hero-voice-assistant.git`
    `cd hero-voice-assistant`

2. Install the dependencies:
    `pip install -r requirements.txt`

3. Set up the Bard API key:

To use the `bardapi` module, you need to obtain an unofficial API key from [Bard](https://bard.google.com/) and set it as an environment variable:
    `export _BARD_API_KEY="your-api-key"`

Alternatively, you can set the API key directly in the code:

```python
import os
os.environ['_BARD_API_KEY'] = "your-api-key" 
```

## Usage
Run the following command to start the HERO voice assistant:
    `python main.py`
Once the program starts, HERO will greet you and listen for your commands. You can interact with HERO by speaking your queries or commands. It will process your input using speech recognition and provide responses using speech synthesis.

To exit the voice assistant, say "exit" or wait for the termination command prompt.

## Credits
* The bardapi module used in this project is developed by [dsdanielpark](https://gitgub.com/dsdanielpark). 
* [Google BARD AI](https://bard.google.com)

## Contribution
Contributions to the HERO Voice Assistant project are welcome! If you have any ideas, bug reports, or feature requests, please open an issue or submit a pull request on the GitHub repository. Let's make HERO even better together!
If you would like to contribute, please follow these steps:
- Fork the repository on GitHub.
- Create a new branch with a descriptive name for your feature or improvement.
- Make your changes to the codebase.
- Write tests, if applicable, to ensure the correctness of your changes.
- Commit your changes and push them to your forked repository.
- Submit a pull request, providing a detailed description of your changes and the rationale behind them.

[NB: Please note that all contributions are subject to review and may require some modifications before being merged into the main project.]

## License
This project is licensed under the [MIT License](LICENSE). See the LICENSE file for more information.