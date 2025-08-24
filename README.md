# Store Navigation System

A smart store navigation system that helps users find products and navigate through stores efficiently using pathfinding algorithms and machine learning recommendations.

## Features

- **A* Pathfinding Algorithm**: Efficient navigation through store layouts
- **Product Recommendations**: ML-powered product suggestions using sentence transformers
- **Interactive Web Interface**: User-friendly frontend for navigation
- **Voice Navigation**: Voice-controlled navigation features
- **Store Layout Visualization**: Visual representation of store maps

## Project Structure

```
store_nav/
├── app/                    # Backend application
│   ├── main.py           # FastAPI main application
│   ├── pathfinding.py    # A* pathfinding implementation
│   ├── crud.py          # Database operations
│   ├── models.py        # Data models
│   ├── database.py      # Database configuration
│   └── grid.csv         # Store layout grid
├── frontend/             # Frontend files
│   ├── index.html       # Main navigation interface
│   ├── navigation.html  # Navigation page
│   ├── voice.html       # Voice navigation interface
│   └── store_map.png    # Store layout image
├── env/                  # Virtual environment (not in repo)
├── seed_data.py         # Database seeding script
└── requirements.txt      # Python dependencies
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/store-navigation.git
   cd store-navigation
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   # On Windows
   env\Scripts\activate
   # On macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python seed_data.py
   ```

5. **Run the application**
   ```bash
   cd app
   uvicorn main:app --reload
   ```

6. **Open your browser**
   Navigate to `http://localhost:8000`

## Usage

### Web Interface
- Open `index.html` in your browser
- Select your starting location and destination
- Get optimal navigation path through the store

### Voice Navigation
- Use the voice interface for hands-free navigation
- Speak your destination to get voice-guided directions

### API Endpoints
- `GET /`: Main application info
- `POST /find-path`: Calculate optimal path between two points
- `GET /products`: Get available products
- `POST /recommend`: Get product recommendations

## Technologies Used

- **Backend**: FastAPI, Python
- **Pathfinding**: A* Algorithm
- **Machine Learning**: Scikit-learn, Sentence Transformers
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Voice**: Web Speech API

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- A* pathfinding algorithm implementation
- FastAPI framework for the backend
- Scikit-learn for machine learning capabilities 