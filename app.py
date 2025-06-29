import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Thai Food Order App", layout="centered")


ORDERS_FILE = "orders.csv"
MENU_FILE = "menu.csv"

# Load menu from CSV
@st.cache_data
def load_menu():
    if os.path.exists(MENU_FILE):
        df = pd.read_csv(MENU_FILE)
        return dict(zip(df["Dish"], df["Price"]))
    else:
        return {}

menu = load_menu()

# Create orders file if it doesn't exist
if not os.path.exists(ORDERS_FILE):
    pd.DataFrame(columns=["Name", "Dish", "Price", "Quantity", "Spice Level", "Payment Method", "Total"]).to_csv(ORDERS_FILE, index=False)

st.set_page_config(page_title="Thai Food Order App", layout="centered")
st.title("🍜 Thai Express Ordering System")

tab1, tab2 = st.tabs(["🛒 Place Order", "📋 Order Summary"])

with tab1:
    st.subheader("Place a New Order")

    name = st.text_input("Your Name")

    if not menu:
        st.error("Menu is empty or missing. Please provide a valid menu.csv file.")
    else:
        food_choice = st.selectbox("Select a dish", list(menu.keys()))
        price = menu[food_choice]
        st.write(f"💰 Price: ${price:.2f}")

        quantity = st.number_input("Quantity", min_value=1, max_value=20, value=1, step=1)
        spice_level = st.slider("Select Spice Level", 0, 10, 0, help="0 = no spice, 10 = extremely spicy")
        payment_method = st.radio("Payment Method", options=["Cash", "Venmo (@danbern72)"], index=0)

        total = price * quantity
        st.write(f"🧾 Total: ${total:.2f}")

        if st.button("✅ Submit Order"):
            if name.strip() == "":
                st.warning("Please enter your name before placing the order.")
            else:
                new_order = pd.DataFrame([{
                    "Name": name.strip(),
                    "Dish": food_choice,
                    "Price": price,
                    "Quantity": quantity,
                    "Spice Level": spice_level,
                    "Payment Method": payment_method,
                    "Total": total
                }])
                new_order.to_csv(ORDERS_FILE, mode='a', header=False, index=False)
                st.success(f"Order placed for {quantity} x {food_choice} (Spice Level: {spice_level}) by {name} paying by {payment_method}!")
                st.balloons()

with tab2:
    st.subheader("Order Summary")

    try:
        df = pd.read_csv(ORDERS_FILE)
        if df.empty:
            st.info("No orders placed yet.")
        else:
            st.dataframe(df)
            grand_total = df["Total"].sum()
            st.write(f"🧾 **Grand Total of All Orders:** ${grand_total:.2f}")
    except pd.errors.ParserError:
        st.error("Order file is corrupted. Clearing orders and starting fresh.")
        if os.path.exists(ORDERS_FILE):
            os.remove(ORDERS_FILE)
        pd.DataFrame(columns=["Name", "Dish", "Price", "Quantity", "Spice Level", "Payment Method", "Total"]).to_csv(ORDERS_FILE, index=False)
    except Exception as e:
        st.error(f"Failed to load orders: {e}")

    # Confirm before clearing orders
    with st.expander("🗑️ Clear All Orders", expanded=False):
        if st.button("⚠️ Confirm Clear Orders"):
            os.remove(ORDERS_FILE)
            pd.DataFrame(columns=["Name", "Dish", "Price", "Quantity", "Spice Level", "Payment Method", "Total"]).to_csv(ORDERS_FILE, index=False)
            st.success("All orders cleared!")

