# Pokedex-Using-RESTAPI-PokeAPI-

# Pokédex using Python & PokéAPI

A simple command-line Pokédex built using **Python**, the **PokéAPI**, and the **requests** module. This project fetches Pokémon information in real time and displays details such as name, ID, type, height, weight, and an optional shiny sprite image.

This project was built to understand how REST APIs work, how Python interacts with web services, and how to process JSON and image data.

---

## Features

- Search Pokémon by name.
- Fetch live Pokémon data using the PokéAPI.
- Display:
  - Pokémon Name
  - Pokédex ID
  - Height
  - Weight
  - Primary Type
- View the Pokémon's shiny sprite.
- Gracefully handles invalid Pokémon names.

---

## Technologies Used

- Python
- Requests
- NumPy
- OpenCV
- PokéAPI

---

## How It Works

### 1. User enters a Pokémon name

Example:

```
Enter pokemon name: pikachu
```

---

### 2. The program sends an HTTP GET request

```python
requests.get(url)
```

to

```
https://pokeapi.co/api/v2/pokemon/pikachu
```

The server returns a **Response object**.

---

### 3. Check the HTTP Status Code

If

```
status_code == 200
```

the request was successful.

Otherwise, an error message is displayed.

---

### 4. Parse JSON Data

The response body is converted into a Python dictionary using

```python
response.json()
```

The application then extracts useful information like:

- Name
- Height
- Weight
- ID
- Type

---

### 5. Fetch the Pokémon Sprite

The sprite URL is obtained from

```python
pokemon_info["sprites"]["front_shiny"]
```

The image is downloaded using another HTTP request.

---

### 6. Display the Image

The downloaded image bytes are converted into a NumPy array and decoded using OpenCV.

```python
np.asarray(...)
cv2.imdecode(...)
```

The image is enlarged while preserving its pixel-art quality using

```python
cv2.INTER_NEAREST
```

---

## Example

### Input

```
Enter pokemon name:
charizard
```

### Output

```
NAME    : Charizard
HEIGHT  : 17 m
WEIGHT  : 905 kg
ID      : 6
TYPE    : Fire
```

Then the program asks

```
Want an image? (Y/n)
```

If the user enters

```
Y
```

the shiny sprite is displayed.

---

## Project Structure

```
Pokedex/

│── pokedex.py
│── README.md
```

---

## What I Learned

This project helped me understand:

- REST APIs
- HTTP GET Requests
- Response Objects
- HTTP Status Codes
- JSON Parsing
- Working with External APIs
- Fetching Binary Image Data
- NumPy Arrays
- Image Decoding using OpenCV
- Error Handling
- Python Modules

---

## Future Improvements

- Display all Pokémon types
- Show abilities
- Display Pokémon stats (HP, Attack, Defense, Speed, etc.)
- Show Normal and Shiny sprites
- Add a GUI using Tkinter or PyQt
- Search Pokémon by Pokédex ID
- Add Evolution Chain information
- Display Pokémon moves

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/pokedex-python.git
```

Move into the project

```bash
cd pokedex-python
```

Install dependencies

```bash
pip install requests numpy opencv-python
```

Run

```bash
python pokedex.py
```

---

## API Used

This project uses the free **PokéAPI**.

https://pokeapi.co/

---

## Author

**Parimella Pardha Sai**

B.Tech CSE Student

## License

This project is open-source and intended for learning and educational purposes.
