# Import libraries
import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="HorshecrabDB", page_icon="🦀", layout="wide")
st.title("HorseshoecrabDB 🦀")

# Connect to the Google Sheet
url = r"Literature_Horseshoe crab repository.xlsx"
df = pd.read_excel(url, dtype=str).fillna("")

# Use a text_input to get the keywords to filter the dataframe
text_search = st.text_input("Search Reseach Articles", value="")

# Filter the dataframe using masks
m1 = df["Title"].str.contains(text_search)
m2 = df["Snippets"].str.contains(text_search)
m3 = df["Authors"].str.contains(text_search)
m3 = df["DOI"].str.contains(text_search)
m3 = df["ArticleURL"].str.contains(text_search)
df_search = df[m1 | m2 | m3]


# Another way to show the filtered results
# Show the cards
N_cards_per_row = 3
if text_search:
    for n_row, row in df_search.reset_index().iterrows():
        i = n_row%N_cards_per_row
        if i==0:
            st.write("---")
            cols = st.columns(N_cards_per_row, gap="large")
        # draw the card
        with cols[n_row%N_cards_per_row]:
            st.markdown(f"{row['Title'].strip()}")
            st.divider()
            st.markdown(f"**{row['Authors'].strip()}**")
            st.markdown(f"*{row['ArticleURL'].strip()}*")
            st.markdown(f"{row['DOI'].strip()}")
            st.markdown(f"**{row['Year']}**")

