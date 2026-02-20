# WhatShouldIWatch (Work-in-Progress)

A tool designed to help you pick a movie or series to watch based on filters and preferences.

## 🚧 Project Status

This project is currently a **work-in-progress**. Contributions, feedback, and collaboration are welcome to enhance its features and usability.

## 📚 Description

**WhatShouldIWatch** is a Flask-based project that enables users to streamline their content selection by using genre-based filters, user preferences, and ratings.

## 🔧 Features **Work in progress**

- Filter by genre, release year, or rating.
- Login system for personalized user experience.
- Create and manage your Watchlist.
- Favorite movies and series for quick access later.
- Utilizes SQLite for lightweight and efficient data storage.
- Integrates with **TMDb API** for fetching detailed information about movies and TV shows.

## 🛠️ Tech Stack

- **Python**: Core language for back-end logic.
- **Flask**: Web framework for building and handling the application.
- **HTML** & **CSS**: For the structure and styling of the front-end.
- **SQLite**: A lightweight relational database for storing user data.
- **TMDb API**: Provides the data for movies and TV shows.

## 📝 License

This project is licensed under the [MIT License](https://github.com/skopo97/WhatShouldIWatch/blob/main/LICENSE). You are free to use, distribute, and modify the software under the terms of this license.

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/skopo97/WhatShouldIWatch.git
   ```

2. Navigate to the project directory:
   ```bash
   cd WhatShouldIWatch
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your TMDb API key:
   - Visit [The Movie Database](https://www.themoviedb.org/) to sign up and obtain an API key.
   - Create a `.env` file in the root of the project:
     ```bash
     cp .env.example .env
     ```
   - Add your API key to the `.env` file:
     ```
     TMDB_API_KEY=your_api_key_here

5. Run the application:
   ```bash
   python main.py
   ```

## 📭 Contact

For support, questions, or suggestions, reach out to [skopo97](https://github.com/skopo97).