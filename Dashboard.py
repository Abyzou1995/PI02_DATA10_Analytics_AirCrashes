import streamlit as st


st.title("Hola aaaaa")
st.markdown("***")
st.markdown("Holus")

st.sidebar.markdown("Dashboard")


st.write("# This works:")


# init session value
if 'btn' not in st.session_state:
    st.session_state['btn'] = False


def callback1():
    st.session_state['btn'] = True


def callback2():
    st.session_state['btn'] = False


city = st.selectbox(" Select a city", ['a', 'b'], on_change=callback2)
b1 = st.button("See further options", on_click=callback1)
if st.session_state['btn']:  # session value judge
    suburbs = st.selectbox("Select Suburb", "sub")
    if suburbs:
        col1, col2 = st.columns(2)
        with col1:
            select_bus = st.selectbox("Available Bus", "bus_schedule")
            bus_timetable = st.download_button(
                "Download Bus timetable", data="df.to_csv()", )

        with col1:
            select_train = st.selectbox("Available Train", "Train_schedule")
            train_timetable = st.download_button("Download train timetable")
