# ThaiFoodApp

A simple web app for ordering Thai food, built with Streamlit.

## Features

- 📋 **Place Orders:** Users can select a dish from a menu, set quantity, spice level, and payment method, then submit their order.
- 🧾 **Order Summary:** View all submitted orders in a table, see the grand total, and clear all orders if needed.
- 🗂️ **CSV-based Storage:** Orders and menu are managed using CSV files (`orders.csv`, `menu.csv`).

## Demo

The app uses a tabbed interface:

- **Place Order:** For submitting new orders.
- **Order Summary:** For viewing, totaling, and clearing orders.

## Installation

Clone the repository:

```bash
git clone https://github.com/ronaldmanganaro/ThaiFoodApp.git
cd ThaiFoodApp

Install dependencies:

pip install -r requirements.txt

Prepare the menu file:
Create a menu.csv file in the root directory with columns:
Dish,Price
Pad Thai,10.0
Green Curry,12.0

Run the app:
streamlit run app.py
