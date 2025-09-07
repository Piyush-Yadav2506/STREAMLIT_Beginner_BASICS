import streamlit as st

st.title("Food Order App")
st.text("Welcome to the restaurant")
if st.button("Complimentary Drink"):
    st.success("Complimentary Drink added to your order")
choice_lst=[]
choice = st.radio("Select your Preference",['Indian','Continental',
                                                'Chinese','Italian'])
if choice =='Indian':
    item1 = st.selectbox("Indian Menu",['Maharaja Thali','Veg. Samosa','Chicken Biryani',
                                'Chole Bhature','paneer Tikka'])
    choice_lst.append(item1)
elif choice=='Continental':
    item2 = st.selectbox("Continental Menu",['Salade Oriental','Mini Eggplant Parmesan',
                                     'Risotto','Bagel Platter'])
    choice_lst.append(item2)
elif choice=='Chinese':
    item3 = st.selectbox("Chinese Menu",['Hakka Noodles','Dimsums','Spring Rolls',
                                 'Shark Fin','Almond Fried Chicken'])
    choice_lst.append(item3)
elif choice=='Italian':
    item4 = st.selectbox("Italian Menu",['Margherita Pizza','Bacon and Cheese','Phareta',
                                 'Pulvinar','Farmhouse Cheese Burst with Garlic Bread'])
    choice_lst.append(item4)
st.write(f"Your Order includes {choice_lst}")
water = st.slider("Water Bottles",0,1,5)
st.write('Selected Water Bottles:',water)

qty = st.number_input("Please select the number of person",min_value=1,
                      max_value=10, step=1)
st.write(f"You have selected food for {qty} people.")

name = st.text_input("Enter your name")
if name:
    st.write(f"ThankYou {name}! Your order will be served shortly")

dob = st.date_input("Select your date of birth")
st.write("Your DOB is",dob)
