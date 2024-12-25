# LLM DJ 🎵

An AI-powered music curator that combines Spotify's extensive music library with Large Language Models to create intelligent, personalized playlists.

## Features

- 🎵 Create playlists using natural language
- 🤖 AI-powered music recommendations
- 🎧 Spotify integration
- 📊 Playlist analysis and enhancement
- 🎸 Genre exploration and music discovery

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/llm-dj.git
cd llm-dj
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy the environment file and add your credentials:
```bash
cp .env.example .env
```

4. Set up your environment variables in `.env`:
- `SPOTIFY_CLIENT_ID`: Your Spotify Developer Client ID
- `SPOTIFY_CLIENT_SECRET`: Your Spotify Developer Client Secret
- `SPOTIFY_REDIRECT_URI`: Your callback URL (default: http://localhost:8888/callback)
- `LLM_API_KEY`: Your LLM API key

## Usage

Run the main application:
```bash
python src/main.py
```

Example prompt:
```python
await dj.create_playlist_from_prompt(
    "Create a workout playlist with upbeat rock songs from the 80s",
    "80s Workout Rock"
)
```

## Project Structure

```
llm-dj/
├── src/
│   ├── spotify/      # Spotify API integration
│   ├── llm/          # LLM integration
│   ├── utils/        # Helper functions
│   ├── config.py     # Configuration management
│   └── main.py       # Main application
├── tests/            # Test files
├── .env.example      # Example environment variables
└── requirements.txt  # Project dependencies
```

## Required API Access

1. Spotify Developer Account
   - Create an account at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new application to get Client ID and Secret
   - Add your redirect URI to the application settings

2. LLM API Access
   - Sign up for an API key from your chosen LLM provider
   - Add the API key to your `.env` file

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Spotify Web API
- Spotipy Python Library
- Anthropic Claude API

## Future Enhancements

- Web interface for playlist creation
- Voice command support
- Advanced music analysis
- Collaborative playlist features
- Music theory insights
- Mood-based recommendations