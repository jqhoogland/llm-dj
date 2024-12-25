# LLM DJ

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
<!-- [![Tests](https://img.shields.io/badge/tests-pytest-green.svg)](https://docs.pytest.org/en/stable/) --> 

An intelligent music curation system that leverages Large Language Models and Spotify's API to generate contextual playlists.

## Overview

LLM DJ combines natural language processing with Spotify's extensive music library to create personalized playlists. Simply describe the type of music you want, and the system will curate a playlist matching your preferences.

## Features

- Natural language playlist generation
- Intelligent music recommendations
- Spotify integration
- Playlist analysis and optimization
- Advanced genre exploration

## Prerequisites

- Python 3.8 or higher
- Spotify Developer Account
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jqhoogland/llm-dj.git
cd llm-dj
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env-template .env
```

Add the following credentials to your `.env` file:
```
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
LLM_API_KEY=your_llm_api_key
```

## Usage

Basic usage:
```bash
python src/main.py "Create an energetic workout mix with 90s hip-hop"
```

## Project Structure

```
llm-dj/
├── src/
│   └── llm_dj/
│       ├── spotify/      # Spotify API integration
│       ├── llm/          # LLM integration
│       ├── utils/        # Helper functions
│       ├── config.py     # Configuration
│       └── main.py       # Entry point
├── requirements.txt  # Dependencies
├── README.md         # This file
└── LICENSE           # License file
```

## API Configuration

### Spotify Setup
1. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new application
3. Configure the redirect URI
4. Copy credentials to `.env`

### LLM Setup
1. Obtain an API key from your OpenAI (other LLMs not supported yet)
2. Add to `.env` file

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [Spotipy](https://spotipy.readthedocs.io/)
- [OpenAI API](https://openai.com/api/)