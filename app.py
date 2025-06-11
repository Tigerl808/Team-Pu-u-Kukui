import streamlit as st
import streamlit.components.v1 as components
import leafmap.foliumap as leafmap
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit_shadcn_ui as ui
import seaborn as sns

from st_circular_progress import CircularProgress
from style_helper import apply_custom_style
import pandas as pd

@st.cache_data
def fetch_broadband_data():
    conn = st.connection('mysql', type='sql')
    df = conn.query('SELECT BroadbandCoverage, Latitude, Longitude FROM broadbcover_by_city', ttl=6)
    return df

@st.cache_data
def fetch_readiness_data():
    conn = st.connection('mysql', type='sql')
    df = conn.query('SELECT Dimension, Details, Unprepared, Old_Guard, Social_Users, Technical, Digital FROM readiness_by_dimensions', ttl=6)
    return df

@st.cache_data
def fetch_campaign_fund_data():
    conn = st.connection('mysql', type='sql')
    df = conn.query('SELECT CandidateName, CampaignTotal FROM Campaign_Fund ORDER BY CampaignTotal DESC LIMIT 5', ttl=6)
    return df

@st.cache_data
def fetch_usage_data():
    conn = st.connection('mysql', type='sql')
    df = conn.query("""SELECT Use_pc_internet, County, Estimate_Perccent AS Estimate_Percent 
        FROM use_pc_internet_by_county
        WHERE County = 'HawaiiState' AND Use_pc_internet != 'Total households'""", ttl=6)
    return df

def fetch_feedback_data():
    conn = st.connection('mysql', type='sql')
    df = conn.query("""
        SELECT
            SUM(Satisfied) AS Satisfied,
            SUM(Unsatisfied) AS Unsatisfied
        FROM user_feedback;
        """, ttl=6)
    return df

def fetch_budget_data():
    data = pd.read_csv("data/budget.csv")

    # Clean column names
    data.columns = data.columns.str.strip().str.replace('/', '_')
    
    # Filter out Total rows for per-category breakdown
    category_data = data[data['Category'] != 'Total']
    total_data = data[data['Category'] == 'Total']
    return category_data, total_data

def fetch_attendance_data():
  df = pd.read_csv("data/Tbl_RegAttend.csv")

  # Remove completely empty columns (extra commas at the end of CSV)
  df = df.dropna(axis=1, how='all')

  # Filter to rows where Island == "Total"
  df = df[df["Island"] == "Total"].copy()

  # Clean column names
  df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('/', '_')
  
  # Convert all columns that can be numeric
  for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='ignore')  # keep strings like 'Island', 'textDate'
  return df

def get_header_style():
    # Define the style for the card and header
    header_style = """
        <style>
            .card-header {
                background-image: linear-gradient(0deg, rgba(5, 96.7, 181, 1) 0%, rgba(2.2, 42.2, 1) 100%);
                color: white;
                padding: 10px 20px;
                font-size: 1.2rem;
                font-weight: bold;
                border-radius: 0.5rem 0.5rem 0 0;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .card-header .card-header-image img {
                height: 25px;
                width: auto;
            }
            .card {
                border: 1px solid #d3d3d3;
                border-radius: 0.5rem;
                box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
            }
            .card-footer {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 10px 20px;
                border-top: 1px solid #ddd;
            }
            .card-footer-text {
                font-size: 16px;
                color: #333;
            }
            .card-footer-button {
                display: flex;
                align-items: center;
                justify-content: center;
                width: 50px;
                height: 50px;
                font-size: 16px;
                color: #fff;
                background-color: #007BFF;
                border: none;
                border-radius: 50%;
                cursor: pointer;
                text-decoration: none;
            }
            .card-footer-button:hover {
                background-color: #0056b3;
            }
        </style>
    """
    return header_style

def create_card_header(title, image_link):
    st.markdown(f"""
        <div class="card">
            <div class="card-header">
                <div>{title}</div>
                <div class="card-header-image">
                    <img src="{image_link}" alt="Card Header Image">
                </div>
            </div>
            <div>
    """, unsafe_allow_html=True)

def show_budget_card(col):
    # Set up a blue header style for the card
    header_style = get_header_style()

    with col:
        # Display the custom styles in Streamlit
        st.markdown(header_style, unsafe_allow_html=True)
        # Create a card layout with a blue header
        create_card_header("Budget", "https://raw.githubusercontent.com/datjandra/Team-Pu-u-Kukui/refs/heads/main/images/money-dollar-circle-line.png")

        _, total_data = fetch_budget_data()

        fig, ax = plt.subplots()
        ax.bar(total_data['Date'], total_data['Budgeted'], label='Budgeted', alpha=0.6)
        ax.bar(total_data['Date'], total_data['Used'], label='Used')
        ax.set_ylabel("Amount ($)")
        ax.set_title("Total Budget vs Used")
        ax.legend()
        st.pyplot(fig)

        # Add the footer with "Read more about it" and a button
        st.markdown("""
                </div>
                <div class="card-footer">
                    <span class="card-footer-text">Read more about it</span>
                    <a href="/budget" target="_self" class="card-footer-button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                            <path d="M24 12l-12-9v5h-12v8h12v5l12-9z" fill="white"/>
                        </svg>
                    </a>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
        # Close the card footer and card div
        st.markdown("""
                </div>
            </div>
        """, unsafe_allow_html=True)
def show_digital_equity_card():
    # Set up a blue header style for the card
    header_style = get_header_style()

    # Display the custom styles in Streamlit
    st.markdown(header_style, unsafe_allow_html=True)

    create_card_header("Geographical Breakdown", "https://raw.githubusercontent.com/datjandra/Team-Pu-u-Kukui/refs/heads/main/images/earth-line.png")

    components.iframe("https://app.powerbi.com/view?r=eyJrIjoiM2JmM2QxZjEtYWEzZi00MDI5LThlZDMtODMzMjhkZTY2Y2Q2IiwidCI6ImMxMzZlZWMwLWZlOTItNDVlMC1iZWFlLTQ2OTg0OTczZTIzMiIsImMiOjF9", 
                      height=500)
    
    # Close the card div
    # Add the footer with "Read more about it" and a button
    st.markdown("""
            </div>
            <div class="card-footer">
                <span class="card-footer-text">Read more about it</span>
                <a href="https://app.powerbi.com/view?r=eyJrIjoiM2JmM2QxZjEtYWEzZi00MDI5LThlZDMtODMzMjhkZTY2Y2Q2IiwidCI6ImMxMzZlZWMwLWZlOTItNDVlMC1iZWFlLTQ2OTg0OTczZTIzMiIsImMiOjF9" target="_blank" class="card-footer-button">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                        <path d="M24 12l-12-9v5h-12v8h12v5l12-9z" fill="white"/>
                    </svg>
                </a>
    """, unsafe_allow_html=True)
    
    # Close the card footer and card div
    st.markdown("""
            </div>
        </div>
    """, unsafe_allow_html=True)

def show_device_access_card(col):
    # Set up a blue header style for the card
    header_style = get_header_style()
    
    with col:
        # Display the custom styles in Streamlit
        st.markdown(header_style, unsafe_allow_html=True)
        
        create_card_header("Device Access", "https://raw.githubusercontent.com/datjandra/Team-Pu-u-Kukui/refs/heads/main/images/monitor-mobbile.png")

        df = fetch_usage_data()
            
        # Group by county and display each type in two columns for each county
        for county, group in df.groupby("County", sort=False):
            st.write(f"### {county}")  # Display the county name as a section header
        
            # Create two columns for displaying progress bars side by side
            col1, col2 = st.columns(2)
            
            for i, (_, row) in enumerate(group.iterrows()):
                # Alternate between columns for each type of internet usage
                if i % 2 == 0:
                    col = col1
                    color = "#0778DF"
                else:
                    col = col2
                    color = "#FF3583"
    
                percentage = int(row['Estimate_Percent'] * 100)
    
                # Display the type of internet usage and the progress bar
                with col:
                    cp = CircularProgress(
                            label=row['Use_pc_internet'],
                            value=percentage,
                            color=color,
                            key=f"cell_{i}_{col}")
                    cp.st_circular_progress()  
        
        # Close the card div
        # Add the footer with "Read more about it" and a button
        st.markdown("""
                </div>
                <div class="card-footer">
                    <span class="card-footer-text">Read more about it</span>
                    <a href="/device_access" target="_self" class="card-footer-button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                            <path d="M24 12l-12-9v5h-12v8h12v5l12-9z" fill="white"/>
                        </svg>
                    </a>
        """, unsafe_allow_html=True)
        
        # Close the card footer and card div
        st.markdown("""
                </div>
            </div>
        """, unsafe_allow_html=True)

def show_broadband_card(col):
    # Set up a blue header style for the card
    header_style = get_header_style()

    with col:
        # Display the custom styles in Streamlit
        st.markdown(header_style, unsafe_allow_html=True)
        
        # Create a card layout with a blue header
        create_card_header("Broadband Connectivity", "https://raw.githubusercontent.com/datjandra/Team-Pu-u-Kukui/refs/heads/main/images/cloud-connection.png")
        
        st.subheader("Broadband Connectivity Map")
        
        # Create a Leaflet map centered at an example location
        # Drop rows where coordinates couldn't be found
        data = fetch_broadband_data()
        data.dropna(subset=['Latitude', 'Longitude'], inplace=True)
    
        # Create Leafmap map
        m = leafmap.Map(center=[20.5, -157.5], zoom=7)  # Center on Hawaii
    
        # Prepare data for heatmap
        # data['BroadbandCoverage'] = data['BroadbandCoverage'].str.replace('%', '').astype(float)
    
        # Add heatmap layer
        m.add_heatmap(data=data,
                      latitude="Latitude",
                      longitude="Longitude",
                      value="BroadbandCoverage",
                      name="Heat map",
                      radius=15,
                      blur=10, 
                      max_val=100)
            
        # Display the map in Streamlit
        m.to_streamlit(height=500)
        
        # Close the card div
        # Add the footer with "Read more about it" and a button
        st.markdown("""
                </div>
                <div class="card-footer">
                    <span class="card-footer-text">Read more about it</span>
                    <a href="/broadband" target="_self" class="card-footer-button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                            <path d="M24 12l-12-9v5h-12v8h12v5l12-9z" fill="white"/>
                        </svg>
                    </a>
        """, unsafe_allow_html=True)
        
        # Close the card footer and card div
        st.markdown("""
                </div>
            </div>
        """, unsafe_allow_html=True)

def show_digital_literacy_card(col):
    # Set up a blue header style for the card
    header_style = get_header_style()

    with col:
        # Display the custom styles in Streamlit
        st.markdown(header_style, unsafe_allow_html=True)
        
        # Create a card layout with a blue header
        create_card_header("Digital Literacy", "https://raw.githubusercontent.com/datjandra/Team-Pu-u-Kukui/refs/heads/main/images/book.png")

        df = fetch_readiness_data()
        # Select the first row where Dimension is 'Overall' and specific columns
        overall_row = df.loc[df['Dimension'] == 'Overall', ['Unprepared', 'Old_Guard', 'Social_Users', 'Technical', 'Digital']]

        # Prepare data for the pie chart
        categories = overall_row.columns
        values = overall_row.values[0]
        
        # Create a DataFrame for the pie chart
        pie_data = pd.DataFrame({
            "Category": categories,
            "Percentage": values
        })
        
        # Plot pie chart with custom colors
        fig = px.pie(
            pie_data,
            names="Category",
            values="Percentage",
            color="Category",
            color_discrete_sequence=["#0778DF", "#FF3583", "#32CD32", "#FFD700", "#FF7F50"]  # Custom color palette
        )
        fig.update_traces(textinfo='percent+label')
        
        # Display the pie chart
        st.plotly_chart(fig)

        # Close the card div
        # Add the footer with "Read more about it" and a button
        st.markdown("""
                </div>
                <div class="card-footer">
                    <span class="card-footer-text">Read more about it</span>
                    <a href="/digital_literacy" target="_self" class="card-footer-button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                            <path d="M24 12l-12-9v5h-12v8h12v5l12-9z" fill="white"/>
                        </svg>
                    </a>
        """, unsafe_allow_html=True)
        
        # Close the card footer and card div
        st.markdown("""
                </div>
            </div>
        """, unsafe_allow_html=True)

def show_open_data_card(col):
    # Set up a blue header style for the card
    header_style = get_header_style()

    with col:
        # Display the custom styles in Streamlit
        st.markdown(header_style, unsafe_allow_html=True)
        
        create_card_header("Open Data", "https://raw.githubusercontent.com/datjandra/Team-Pu-u-Kukui/refs/heads/main/images/stack-line.png")

        # Get data from the MySQL table
        df = fetch_campaign_fund_data()
        
        # Create a horizontal bar chart
        fig = px.bar(df, x="CampaignTotal", y="CandidateName", orientation='h',
                     title="Top 5 Campaign Fundraiser 2020",
                     labels={"CampaignTotal": "Total ($)", "CandidateName": "Candidate"})

        # Customize layout for better readability with long names
        fig.update_layout(yaxis_tickangle=0, margin=dict(l=200, r=20, t=50, b=20))

        fig.update_traces(marker_color="#0778DF")
        
        # Display the chart in Streamlit
        st.plotly_chart(fig)
        
        # Close the card div
        # Add the footer with "Read more about it" and a button
        st.markdown("""
                </div>
                <div class="card-footer">
                    <span class="card-footer-text">Read more about it</span>
                    <a href="https://opendata.hawaii.gov/organization/hbdeo" target="_blank" class="card-footer-button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                            <path d="M24 12l-12-9v5h-12v8h12v5l12-9z" fill="white"/>
                        </svg>
                    </a>
        """, unsafe_allow_html=True)
        
        # Close the card footer and card div
        st.markdown("""
                </div>
            </div>
        """, unsafe_allow_html=True)

def show_user_feedback_card(col):
    # Set up a blue header style for the card
    header_style = get_header_style()

    with col:
        # Display the custom styles in Streamlit
        st.markdown(header_style, unsafe_allow_html=True)

        create_card_header("User Feedback", "https://raw.githubusercontent.com/datjandra/Team-Pu-u-Kukui/refs/heads/main/images/user-line.png")

        df = fetch_feedback_data()
        satisfied_count = df['Satisfied'][0]
        unsatisfied_count = df['Unsatisfied'][0]
        
        # Prepare data for pie chart
        feedback_data = pd.DataFrame({
            "Feedback": ["Satisfied", "Unsatisfied"],
            "Count": [satisfied_count, unsatisfied_count]
        })
    
        # Plot pie chart
        fig = px.pie(
            feedback_data,
            names="Feedback",
            values="Count",
            color="Feedback",
            color_discrete_map={"Satisfied": "#0778DF", "Unsatisfied": "#FF3583"}
        )
        fig.update_traces(textinfo='percent+label')
        
        st.plotly_chart(fig)
        
        # Close the card div
        # Add the footer with "Read more about it" and a button
        st.markdown("""
                </div>
                <div class="card-footer">
                    <span class="card-footer-text">Read more about it</span>
                    <a href="feedback" target="_self" class="card-footer-button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                            <path d="M24 12l-12-9v5h-12v8h12v5l12-9z" fill="white"/>
                        </svg>
                    </a>
                </div>
            </div>
        """, unsafe_allow_html=True)

def show_income_distribution_card():
    # Set up a blue header style for the card
    header_style = get_header_style()

    # Display the custom styles in Streamlit
    st.markdown(header_style, unsafe_allow_html=True)

    create_card_header("Income Distribution Impact", "https://raw.githubusercontent.com/datjandra/Team-Pu-u-Kukui/refs/heads/main/images/money-dollar-circle-line.png")

    components.iframe("https://uhero.hawaii.edu/analytics-dashboards/hawaii-income-distribution-map/", 
                      height=1000)
    
    # Close the card div
    # Add the footer with "Read more about it" and a button
    st.markdown("""
            </div>
            <div class="card-footer">
                <span class="card-footer-text">Read more about it</span>
                <a href="https://uhero.hawaii.edu/analytics-dashboards/hawaii-income-distribution-map/" target="_blank" class="card-footer-button">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                        <path d="M24 12l-12-9v5h-12v8h12v5l12-9z" fill="white"/>
                    </svg>
                </a>
    """, unsafe_allow_html=True)
    
    # Close the card footer and card div
    st.markdown("""
            </div>
        </div>
    """, unsafe_allow_html=True)

def show_sample_data_table():
    # Set up a blue header style for the card
    header_style = get_header_style()
    
    # Display the custom styles in Streamlit
    st.markdown(header_style, unsafe_allow_html=True)
    # Create a card layout with a blue header
    create_card_header("Business Intelligence:", "https://raw.githubusercontent.com/datjandra/Team-Pu-u-Kukui/refs/heads/main/images/money-dollar-circle-line.png")

    # Load the JSON data
    df = pd.read_json('data/sample.json')

    # Displaying the DataFrame with 'Filed Date' included
    st.write("Sample Data table")
    st.dataframe(df)
    st.markdown("""</div>""", unsafe_allow_html=True)

    # Close the card div
    # Add the footer with "Read more about it" and a button
    st.markdown("""
            </div>
            <div class="card-footer">
                <span class="card-footer-text">Explore Dataset</span>
                <a href="/sample_data_table" target="_self" class="card-footer-button">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                        <path d="M24 12l-12-9v5h-12v8h12v5l12-9z" fill="white"/>
                    </svg>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Close the card footer and card div
    st.markdown("""
            </div>
        </div>
    """, unsafe_allow_html=True)



def show_attendance_card(col):
    # Set up a blue header style for the card
    header_style = get_header_style()

    with col:
        # Display the custom styles in Streamlit
        st.markdown(header_style, unsafe_allow_html=True)
        # Create a card layout with a blue header
        create_card_header("Attendance", "https://raw.githubusercontent.com/datjandra/Team-Pu-u-Kukui/refs/heads/main/images/user-line.png")

        df_total = fetch_attendance_data()

        # Drop rows with missing data in required columns
        df_total = df_total.dropna(subset=["Marketing_and_Outreach", "Attend_Rate"])

        fig, ax = plt.subplots()
        sns.regplot(
            x=df_total["Marketing_and_Outreach"],
            y=df_total["Attend_Rate"],
            ax=ax,
            scatter_kws={"s": 40}
        )
        ax.set_title("Attend Rate vs Marketing and Outreach")
        ax.set_xlabel("Marketing and Outreach")
        ax.set_ylabel("Attend Rate")
        st.pyplot(fig)

        # Add the footer with "Read more about it" and a button
        st.markdown("""
                </div>
                <div class="card-footer">
                    <span class="card-footer-text">Read more about it</span>
                    <a href="/attendance" target="_self" class="card-footer-button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                            <path d="M24 12l-12-9v5h-12v8h12v5l12-9z" fill="white"/>
                        </svg>
                    </a>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
        # Close the card footer and card div
        st.markdown("""
                </div>
            </div>
        """, unsafe_allow_html=True)

def main():
    apply_custom_style(suppress_anchor=True)
    
    st.header("Bridging Hawaii's Digital Divide")
    
    st.markdown(
        """
        Welcome to Hawaii's Digital Equity Dashboard, where we track technology and internet access across our islands. 
        This tool maps the digital divide in our communities, showing where support is needed most.
        """
    )

    col1, col2 = st.columns(2)
    show_budget_card(col1)
    show_device_access_card(col1)
    show_digital_literacy_card(col1)
    show_open_data_card(col2)
    show_broadband_card(col2)
    show_attendance_card(col1)
  
    show_user_feedback_card(col2)
    show_sample_data_table()
    show_digital_equity_card()
    show_income_distribution_card()

if __name__ == "__main__":
    main()
