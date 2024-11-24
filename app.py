import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="HorseshoecrabDB",
    page_icon="🦀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for the entire application
st.markdown("""
<style>
    /* Overall theme */
    .stApp {
        background-color: #1a1a1a;
        color: #e0e0e0;
    }
    
    /* Navigation */
    .navigation-bar {
        background-color: #1a1a1a;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        border: 1px solid #333;
    }
    
    /* Navigation buttons */
    .stButton > button {
        width: 100%;
        background-color: transparent !important;
        color: #e0e0e0 !important;
        border: 1px solid #333 !important;
        padding: 15px 10px;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #333 !important;
        color: #fff !important;
        border-color: #444 !important;
    }
    .stButton > button:active {
        background-color: #444 !important;
    }
    
    /* Cards and sections */
    .feature-card {
        background-color: #2a2a2a;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 1.5rem;
        height: 100%;
        transition: transform 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-5px);
    }
    
    /* Fact cards */
    .fact-card {
        background-color: #2a2a2a;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .fact-card:hover {
        background-color: #333;
    }
    
    /* Headers and text */
    h1, h2, h3 {
        color: #fff !important;
    }
    p {
        color: #e0e0e0 !important;
    }
    
    /* Search elements */
    .stTextInput input {
        background-color: #2a2a2a !important;
        border-color: #333 !important;
        color: #e0e0e0 !important;
        border-radius: 6px;
    }
    
    /* Checkbox styling */
    .stCheckbox label {
        color: #e0e0e0 !important;
    }
    
    /* Gallery grid */
    .gallery-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1rem;
        padding: 1rem;
    }
    
    /* Title section */
    .title-section {
        text-align: center;
        padding: 3rem 0;
        background: linear-gradient(to right, #1a1a1a, #2d3748, #1a1a1a);
        border-radius: 10px;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

def home_page():
    # Title Section
    st.markdown("""
        <div class="title-section">
            <h1 style="font-size: 2.5rem;">🦀 Welcome to HorseshoecrabDB</h1>
            <p style="color: #a0aec0; font-size: 1.2rem;">Your comprehensive resource for horseshoe crab research</p>
        </div>
    """, unsafe_allow_html=True)

    # Feature Cards
    col1, col2, col3 = st.columns(3)
    feature_cards = [
        {
            "icon": "📚",
            "title": "Research Database",
            "description": "Access comprehensive research papers and publications"
        },
        {
            "icon": "🔬",
            "title": "Latest Discoveries",
            "description": "Stay updated with recent findings and breakthroughs"
        },
        {
            "icon": "📊",
            "title": "Statistics",
            "description": "Explore data trends and analytical insights"
        }
    ]

    for col, card in zip([col1, col2, col3], feature_cards):
        with col:
            st.markdown(f"""
                <div class="feature-card">
                    <h2 style="font-size: 2rem; margin-bottom: 1rem;">{card['icon']}</h2>
                    <h3 style="color: white; margin-bottom: 0.5rem;">{card['title']}</h3>
                    <p style="color: #a0aec0;">{card['description']}</p>
                </div>
            """, unsafe_allow_html=True)

    # Fun Facts Section
    st.markdown("""
        <h2 style="margin: 3rem 0 1.5rem;">Fascinating Facts</h2>
    """, unsafe_allow_html=True)

    facts = [
        "They are living fossils that have existed for at least 445 million years, predating dinosaurs by over 200 million years.",
        "Despite their name, horseshoe crabs are not true crabs but are more closely related to spiders and scorpions.",
        "They possess blue blood due to copper-based hemocyanin, which is used in medical testing for bacterial contamination.",
        "Horseshoe crabs have nine eyes scattered throughout their body, plus several light receptors near their tail.",
        "A female horseshoe crab can lay about 88,000 eggs in total, with around 4,000 eggs per cluster.",
        "They reach sexual maturity at 9-12 years of age and can live to be around 20 years old.",
        "The body is divided into three main parts: the prosoma (head), opisthosoma (abdomen), and telson (tail).",
        "They possess six pairs of legs, but only five pairs are used for walking.",
        "Their tail (telson) is not used for defense but helps them flip over when they get stuck upside down.",
        "Female horseshoe crabs grow to about 2 feet long, while males are approximately 30% smaller.",
        "They spawn during full and new moons in spring and summer, particularly during high tides.",
        "Horseshoe crab eggs are crucial for migrating shorebirds, especially red knots making their 9,300-mile journey.",
        "They have no jaws and crush their food between their legs before eating.",
        "Young horseshoe crabs molt about 16-17 times during their development.",
        "They are found along the Atlantic coast from Maine to Mexico and in parts of Asia.",
        "Newly hatched horseshoe crabs have translucent shells that darken as they age.",
        "They feed primarily on marine worms, clams, mollusks, and dead fish.",
        "The Delaware Bay has the largest population of horseshoe crabs in the world.",
        "Baby horseshoe crabs hatch after 2-4 weeks of incubation in the sand.",
        "Their hard exoskeleton is highly sensitive to their environment, particularly to light."
    ]

    for i in range(0, len(facts), 4):
        cols = st.columns(4)
        for j, col in enumerate(cols):
            if i + j < len(facts):
                with col:
                    st.markdown(f"""
                        <div class="fact-card">
                            <p style="font-size: 0.9rem;">
                                <span style="color: #4f8bf9; font-weight: bold;">#{i+j+1}</span><br>
                                {facts[i+j]}
                            </p>
                        </div>
                    """, unsafe_allow_html=True)

    # Gallery Section
    # Replace the gallery section in home_page() with:

    # Gallery Section
    st.markdown("""
        <h2 style="margin: 3rem 0 1.5rem;">Image Gallery</h2>
    """, unsafe_allow_html=True)

    # Display gallery in groups of 4
    for i in range(0, 11, 4):
        cols = st.columns(4)
        for j, col in enumerate(cols):
            idx = i + j
            with col:
                st.markdown("""
                    <div class="fact-card" style="padding: 0.5rem;">
                """, unsafe_allow_html=True)
                try:
                    st.image(
                        f"gallery/{idx+1}.png",
                        use_column_width=True
                    )
                except:
                    st.markdown("""
                        <div style="background: #2a2a2a; 
                                  aspect-ratio: 1;
                                  display: flex;
                                  align-items: center;
                                  justify-content: center;
                                  border-radius: 5px;">
                            <span style="color: #666;">More Coming Soon...</span>
                        </div>
                    """, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

# Add these additional CSS rules to your existing styles:
st.markdown("""
<style>
    /* Gallery image cards */
    .fact-card img {
        border-radius: 5px;
        width: 100%;
        aspect-ratio: 1;
        object-fit: cover;
    }
    
    .fact-card:hover {
        transform: translateY(-5px);
    }
</style>
""", unsafe_allow_html=True)

def search_page():
    st.title("Research Database")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        text_search = st.text_input("Enter keywords to search", value="", key="search_input")
    with col2:
        st.write("")
        st.write("")
        search_button = st.button("Search", key="search_button")
    
    col1, col2 = st.columns([1, 5])

    
    if text_search and search_button:
        try:
            df = pd.read_csv("Literature_Horseshoe crab repository.csv", dtype=str).fillna("")
            masks = [
                df["Title"].str.contains(text_search, case=False),
                df["Authors"].str.contains(text_search, case=False),
                df["DOI"].str.contains(text_search, case=False),
                df["ArticleURL"].str.contains(text_search, case=False)
            ]
            df_search = df[pd.concat(masks, axis=1).any(axis=1)]
            
            if len(df_search) > 0:
                for _, row in df_search.iterrows():
                    st.markdown(f"""
                        <div class="feature-card">
                            <h3>{row['Title']}</h3>
                            <p><strong>Authors:</strong> {row['Authors']}</p>
                            <p><strong>Year:</strong> {row['Year']}</p>
                            <p><strong>DOI:</strong> {row['DOI']}</p>
                            <a href="{row['ArticleURL']}" target="_blank">Read Article</a>
                        </div>
                        <br>
                    """, unsafe_allow_html=True)
            else:
                st.info("No results found. Try different keywords.")
        except Exception as e:
            st.error("Error searching the database. Please try again.")

def about_page():
    st.title("About")
    st.markdown("""
        <div class="feature-card">
            <p>This database serves as a comprehensive resource for researchers, students, and enthusiasts 
            interested in horseshoe crab biology, ecology, and conservation.</p>
        </div>
    """, unsafe_allow_html=True)

def statistics_page():
    st.title("Statistics")
    stats = [
        {"label": "Total Research Papers", "value": "1,245"},
        {"label": "Active Research Groups", "value": "89"},
        {"label": "Conservation Projects", "value": "34"},
        {"label": "Research Locations", "value": "56"}
    ]
    
    cols = st.columns(4)
    for col, stat in zip(cols, stats):
        with col:
            st.markdown(f"""
                <div class="feature-card" style="text-align: center;">
                    <h3>{stat['label']}</h3>
                    <p style="font-size: 2rem; color: #4f8bf9;">{stat['value']}</p>
                </div>
            """, unsafe_allow_html=True)

def contact_page():
    st.title("Contact Us")
    
    # Introduction card
    st.markdown("""
        <div class="feature-card" style="margin-bottom: 2rem;">
            <h3 style="color: #fff; margin-bottom: 1rem;">Get in Touch</h3>
            <p style="color: #e0e0e0;">
                Have questions about the database? Want to contribute or suggest improvements? 
                We'd love to hear from you. Fill out the form below and we'll get back to you soon.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Embed Google Form with custom styling
    st.markdown("""
        <div class="feature-card" style="padding: 0; overflow: hidden; border-radius: 10px;">
            <iframe 
                src="https://docs.google.com/forms/d/e/1FAIpQLScoA6rLD_v3pWDK0wbFNBmxux7ZZ8eSxlVTodweNRPQph7fZw/viewform?embedded=true" 
                width="100%" 
                height="800px" 
                frameborder="0" 
                marginheight="0" 
                marginwidth="0"
                style="background: transparent;">
                Loading...
            </iframe>
        </div>
        
        
        <style>
            /* Make form background match site theme */
            iframe {
                background-color: #1a1a1a !important;
            }
            
            /* Ensure responsive layout */
            @media screen and (max-width: 600px) {
                iframe {
                    height: 1000px;
                }
            }
        </style>
    """, unsafe_allow_html=True)

def main():
    if 'page' not in st.session_state:
        st.session_state.page = 'home'

    # Navigation
    col1, col2, col3, col4, col5 = st.columns(5)
    nav_items = [
        ('Home', col1, 'nav_home'),
        ('Search', col2, 'nav_search'),
        ('About', col3, 'nav_about'),
        ('Statistics', col4, 'nav_stats'),
        ('Contact', col5, 'nav_contact')
    ]
    
    for page_name, col, key in nav_items:
        with col:
            if st.button(page_name, key=key):
                st.session_state.page = page_name.lower()

    st.markdown("<hr style='margin: 0 0 2rem 0; border-color: #333;'>", unsafe_allow_html=True)

    # Page content
    if st.session_state.page == 'home':
        home_page()
    elif st.session_state.page == 'search':
        search_page()
    elif st.session_state.page == 'about':
        about_page()
    elif st.session_state.page == 'statistics':
        statistics_page()
    elif st.session_state.page == 'contact':
        contact_page()

if __name__ == "__main__":
    main()
