# Food Delivery Chatbot 🍔🤖

A fully terminal-based food delivery chatbot powered by Google's **Gemini AI**. This project provides an interactive command-line interface for users to browse a diverse food menu, manage their cart, get intelligent AI-powered food recommendations, place orders, and receive automated customer support. 

## ✨ Features

### 🍽️ Food Ordering & Menu
- **Extensive Menu:** Browse a rich, categorized menu featuring Fast Food, Italian, Japanese, Mexican, Healthy options, Indian, Chinese, Nepalese cuisines, and Beverages.
- **Cart Management:** Easily add items, remove specific quantities, and view your current cart along with a calculated subtotal.
- **Order Placement:** Seamlessly mock checkout with options for **UPI** or **Pay on Delivery**. 

### 🧠 AI-Powered Recommendations (Gemini 1.5 Flash)
- **"Chat with Chatori" Feature:** Tell the chatbot what you're in the mood for in natural language (e.g., *"I want something spicy"*, *"I'm looking for healthy Italian options"*), and the AI will analyze the menu and intelligently build a cart for you or provide tailored suggestions.
- **Smart Pairing:** Whenever you add an item to your cart, the AI dynamically suggests 2-3 complementary items (sides, drinks, or desserts) that pair perfectly with your choice.

### 🎧 Automated Customer Support
- **Issue Resolution:** Pre-defined, immediate solutions for common customer support queries such as order tracking, delivery delays, missing/wrong items, payment and refund statuses.
- **Intelligent Fallback:** If a user's query doesn't match predefined scenarios, the Gemini AI steps in to provide empathetic, contextual assistance based on standard food delivery support protocols.
- **Contextual Follow-ups:** The system handles conversational flow, such as asking for an Order ID when a missing item is reported.

## 📂 Project Structure

```text
food_delivery_chatbot/
├── main.py                     # The main entry point for the terminal application
├── config.py                   # Configuration settings, API keys, Food Menu, and Support data
├── gemini_service.py           # Integration wrapper for Google Generative AI (Gemini)
├── food_ordering/              # Core logic for handling food orders
│   ├── cart_manager.py         # Manages adding, removing, and viewing cart items
│   ├── order_processor.py      # Handles displaying the menu and processing mock payments
│   └── recommendations.py      # AI logic for analyzing preferences and suggesting pairings
├── customer_support/           # Logic for handling user queries and complaints
│   └── support_handler.py      # Routes customer queries to predefined answers or the AI
└── utils/
    └── helpers.py              # Utility functions for validating user inputs
```

## 🚀 Installation & Setup

### Prerequisites
- **Python 3.8+** installed on your system.
- A **Google Gemini API Key** (Get one from [Google AI Studio](https://aistudio.google.com/)).

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aarushbahuguna/food_delivery_chatbot.git
   cd food_delivery_chatbot
   ```

2. **Install the required dependencies:**
   This project relies on the official Google Generative AI SDK and `python-dotenv` for environment variable management.
   ```bash
   pip install google-generativeai python-dotenv
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory of the project and add your Gemini API Key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

## 🎮 Usage

To start the chatbot, run the main Python script from your terminal:

```bash
python main.py
```

### Main Menu Navigation
Upon starting, you will be greeted with the Main Menu:
1. **Food Order:** Takes you to the menu, cart, and checkout options.
2. **Customer Support:** Connects you to the automated help desk.
3. **Exit:** Closes the application.

### Ordering Workflow Example
1. Select `1` for Food Order.
2. Select `1` to View Menu.
3. Select `2` to Add an Item to Cart (e.g., enter `1` for a Burger). The AI will suggest a Cold Drink!
4. Select `5` to Chat with Chatori and ask *"I want a large meal for two people"*. Watch the AI populate your cart.
5. Select `6` to Place Order and select your preferred payment method.

## 🛠️ Technologies Used

- **Language:** Python
- **AI Model:** Google Gemini 1.5 Flash (`google-generativeai`)
- **Environment Management:** `python-dotenv`
