# EatDudeWeb

## Overview
EatDudeWeb is a web-based application designed to help users discover and manage restaurant menus and dishes with ease. This project offers a comprehensive platform for managing restaurant information, including the ability to add, edit, and delete menus and restaurant details.

## Features
- **Restaurant Management**: Add, edit, and delete restaurant details.
- **Menu Management**: Create, modify, and remove menus and individual menu items.
- **User Management**: Admin capabilities to manage users and their roles.
- **Categorization**: Organize menu items into categories for better navigation.
- **Example and Utility Functions**: Provided samples for XML handling and utility operations.

## Installation Instructions
### Prerequisites
- Python installed (version >= 3.6)
- Virtual environment tool (e.g., `virtualenv` or `conda`)

### Steps
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Yuriy/EatDudeWeb.git
    cd EatDudeWeb
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set Up the Database**:
    Follow instructions in `dbModel.py` to configure the database properly.

6. **Run the Application**:
    ```bash
    python main.py
    ```

## Usage Examples
### Example 1: Adding a New Restaurant
```python
# In admin/addrestaurant.py
def add_restaurant():
    name = "New Restaurant"
    address = "123 Main St"
    phone = "555-1234"
    # Logic to add restaurant to database
```

### Example 2: Adding a New Menu Item
```python
# In admin/addmenu.py
def add_menu_item():
    restaurant_id = 1
    item_name = "Pizza"
    item_description = "Delicious cheese pizza"
    item_price = 9.99
    # Logic to add menu item to database
```

### Example 3: User Authentication
```python
# In controller/main/user/admin.py
from google.appengine.api import users

def check_admin():
    user = users.get_current_user()
    if users.is_current_user_admin():
        return True
    return False
```

## Code Summary
### Code Structure
- **main.py**: The main entry point of the application.
- **admin.py**: Contains admin-specific functions and logic.
- **config.py**: Configuration settings for the application.
- **dbModel.py**: Defines the database models and setup.
- **app/ directory**: Contains subdirectories for different controllers and views:
  - **app/controller/admin/**: Admin-related functionalities.
  - **app/controller/main/**: Main application functionalities.
  - **app/controller/main/manager/**: Manager-specific functionalities.
  - **app/controller/main/user/**: User-specific functionalities.

### Key Files
- **admin.py**: Admin functions.
- **appcfg.py**: Application configuration.
- **config.py**: General configuration settings.
- **dbModel.py**: Database models.
- **main.py**: Main application executable.
  
## Contributing Guidelines
We welcome contributions to EatDudeWeb! To contribute, please follow these steps:

1. **Fork the repository** to your GitHub account.
2. **Clone your fork** to your local machine:
    ```bash
    git clone https://github.com/YOUR-USERNAME/EatDudeWeb.git
    ```
3. **Create a branch** for your feature or bugfix:
    ```bash
    git checkout -b feature-name
    ```
4. **Commit your changes**:
    ```bash
    git commit -am 'Add new feature'
    ```
5. **Push to the branch**:
    ```bash
    git push origin feature-name
    ```
6. **Create a pull request** on GitHub.

Please ensure your code follows the existing style and includes appropriate tests.

## License
This project is licensed under the GNU General Public License v3.0. You may obtain a copy of the License at:
```
http://www.gnu.org/licenses/gpl-3.0.html
```

---
Developed by Wiley Snyder.
# EatDudeWeb

## Overview
EatDudeWeb is a web application designed to manage and display information about restaurants, menus, and user profiles. It includes administrative functions for managing categories, items, and menus, as well as XML-based functionalities for handling data about cities, countries, states, and restaurants.

## Features
- User profile management
- Menu and item organization
- Restaurant information management
- Administrative tools for categories, items, and restaurants
- XML data management for various geographical entities 
- Open-source and GPL-licensed

## Installation Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Yuriy/EatDudeWeb.git
   cd EatDudeWeb
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app/main.py
   ```

## Usage Examples
Here are some examples of how you might interact with the application.

### Example 1: Retrieve a User Profile
```python
from app.controller.main.user import profile

user_profile = profile.get_user_profile(user_id)
print(user_profile)
```

### Example 2: Add a Menu Item
```python
from app.controller.main.user import menu

new_item = {
    "name": "Burger",
    "description": "Delicious beef burger",
    "price": 9.99
}

menu.add_menu_item(menu_id, new_item)
```

## Code Summary
The project structure is divided into several modules:

### Controllers
- **main/user/item.py**: Manages user items.
- **main/user/menu.py**: Manages user menus.
- **main/user/profile.py**: Handles user profiles.
- **main/user/restaurant.py**: Manages user restaurant data.
- **main/xml1/**: XML handling for app messages, city, country, restaurant, and state.

### Models
- **model/admin/**: Contains admin-related data models for categories, items, menus, restaurants.
- **model/main/manager/**: Handles main management logic for categories, cities, countries, items, menus, restaurants.

### Views
- **view/admin/**: Contains templates for admin views.
- **view/main/**: Contains templates for user and xml views.

## Contributing Guidelines
We welcome contributions from the community to make EatDudeWeb even better!

1. **Fork the repository and clone it locally.**
2. **Create a new branch for your feature or bugfix:**
   ```bash
   git checkout -b feature-name
   ```
3. **Commit your changes:**
   ```bash
   git commit -m "Description of the new feature or fix"
   ```
4. **Push to your branch:**
   ```bash
   git push origin feature-name
   ```
5. **Create a pull request explaining your changes.**

## License
This project is licensed under the GNU General Public License v3.0. Please see the [LICENSE](LICENSE) file for details. 

```text
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or 
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
``` 

Feel free to reach out if you have any questions or need further assistance!
```markdown
# EatDude Web

## Overview
EatDude Web is a web application framework designed to simplify the creation and management of web applications. The project leverages components from the [web.py](http://webpy.org) library to provide a streamlined experience for developers to build web applications with a minimalistic and modular approach.

## Features
- **Modular Design:** Easily extend functionality with organized file and directory structures.
- **Template Engine:** Use templates for rendering HTML with dynamic data.
- **Form Handling:** Simplify form creation and validation.
- **Session Management:** Maintain user sessions seamlessly.
- **Database Integration:** Connect and interact with databases effortlessly.
- **Error Handling:** Provide detailed and user-friendly error messages.
- **HTTP Utilities:** Easy handling and manipulation of HTTP requests and responses.

## Installation Instructions
1. **Clone the Repository:**
   ```shell
   git clone https://github.com/yourusername/EatDudeWeb.git
   cd EatDudeWeb
   ```

2. **Install Dependencies:**
   Ensure you have Python installed. Then, install required libraries:
   ```shell
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   Start the server:
   ```shell
   python web/application.py
   ```

4. **Open in Browser:**
   Visit `http://localhost:8080` to view the application running locally.

## Usage Examples
### Render a Template
Example of rendering a template from Python code:
```python
from web.template import render

def render_page():
    render = render('templates/')
    return render.hello(name='World')
```

### Handle Form Submission
Example of handling form data in the application:
```python
import web

class MyForm:
    def POST(self):
        form = web.input()
        # Process form data
        return "Form data processed!"

urls = ('/submit', 'MyForm')
app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
```

## Code Summary

### Structure
- `app/view/main/manager/`
    - `__init__.py`: Main manager initialization, imports submodules.
    - `add/__init__.py`: Handles item addition functionalities.
    - `delete/__init__.py`: Manages category deletion.
    - `edit/__init__.py`: Edits categories and items.
    - `main/__init__.py`: Main view rendering for menus.
    - `menu/__init__.py`: Handles menu-related views.
    - `menu_form/__init__.py`: Deals with forms related to menu categories.
    - `view/__init__.py`: Contains templates for viewing categories and items.
    - `user/__init__.py`: Manages user-specific views.
    - `xml/__init__.py`: XML-related handling (currently placeholder).

- `web/`
    - `application.py`: Main entry point for the web application.
    - Various modules like `browser.py`, `db.py`, `http.py` handle specific aspects like database, HTTP requests, and more.

## Contributing Guidelines
We welcome contributions to enhance EatDude Web. Please follow these steps:
1. **Fork the Repository** on GitHub.
2. **Clone Your Fork**:
   ```shell
   git clone https://github.com/yourusername/EatDudeWeb.git
   ```
3. **Create a Feature Branch**:
   ```shell
   git checkout -b feature/YourFeature
   ```
4. **Commit Your Changes**:
   ```shell
   git commit -m "Add your message"
   ```
5. **Push to Your Fork**:
   ```shell
   git push origin feature/YourFeature
   ```
6. **Open a Pull Request** on the original repository.

## License
This project is licensed under the [Public Domain License](LICENSE).
```
