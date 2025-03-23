# Language Cards

A Django application for memorizing foreign language vocabulary.

## Features

- **Create Cards**: Add words and their translations to create a personal collection of vocabulary cards.
- **Tour Mode**: Test your memory with a random sequence of cards. Recall the translation before flipping.
- **Canvas Mode**: Organize cards spatially on an infinite canvas for better memory association.

## Getting Started

### Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/dr-who-knows/cards.git
   cd cards
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```
   cd cards
   python manage.py migrate
   ```

4. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Visit http://127.0.0.1:8000/ in your browser.

### Docker Deployment

1. Build and run with Docker Compose:
   ```
   docker-compose build
   docker-compose up -d
   ```

2. Visit http://localhost:8000/ in your browser.

## Usage

1. Start by adding vocabulary cards through the "Add Card" page.
2. View all your cards in the "My Cards" section.
3. Practice with your cards using:
   - Tour Mode: For sequential practice with random ordering
   - Canvas Mode: For spatial organization and grouping related words

## License

This project is licensed under the MIT License. 