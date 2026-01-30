import streamlit as st
import pandas as pd

# Απλό σύστημα κωδικού
PASSWORD = "mysecretpassword123"

st.title("📋 Σύστημα Παραγγελιών & Ελλείψεων")

# Session state για να αποθηκεύονται οι ανάγκες προσωρινά
if 'needs' not in st.session_state:
    st.session_state.needs = []

# --- ΠΛΕΥΡΙΚΟ ΜΕΝΟΥ (Login) ---
auth = st.sidebar.text_input("Εισάγετε Κωδικό", type="password")

if auth == PASSWORD:
    st.sidebar.success("Είστε συνδεδεμένος ως Διαχειριστής")
    
    st.header("📦 Τρέχουσες Ελλείψεις")
    if st.session_state.needs:
        df = pd.DataFrame(st.session_state.needs)
        st.table(df)
        if st.button("Καθαρισμός Λίστας"):
            st.session_state.needs = []
            st.rerun()
    else:
        st.info("Δεν υπάρχουν ελλείψεις αυτή τη στιγμή.")

else:
    st.warning("Παρακαλώ βάλτε τον κωδικό για να δείτε τις παραγγελίες.")

# --- ΦΟΡΜΑ ΔΗΛΩΣΗΣ ΑΝΑΓΚΩΝ (Για όλους) ---
st.divider()
st.header("➕ Δήλωση Νέας Ανάγκης")
item = st.text_input("Προϊόν / Είδος")
quantity = st.number_input("Ποσότητα", min_value=1, step=1)

if st.button("Αποστολή"):
    if item:
        st.session_state.needs.append({"Προϊόν": item, "Ποσότητα": quantity})
        st.success(f"Η ανάγκη για {item} καταχωρήθηκε!")
    else:
        st.error("Παρακαλώ συμπληρώστε το όνομα του προϊόντος.")