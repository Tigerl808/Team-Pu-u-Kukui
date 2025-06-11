import streamlit as st

def apply_custom_style(suppress_anchor=False):
  st.set_page_config(layout="wide")
  
  # Define the HTML and CSS
  html_content = """
  <style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
  
  /* Set Montserrat as the default font */
  body {
      font-family: 'Montserrat', sans-serif;
  }
  .e1_15 { 
      color: rgba(255, 255, 255, 1);
      font-family: Montserrat;
      font-size: 3vw; /* Use vw for responsive font size */
      letter-spacing: 0;
      line-height: 1.2em; /* Adjusted for consistent line height */
  }
  .e2_21 { 
      background-image:linear-gradient(0deg, rgba(4.999259691685438, 96.68749898672104, 180.9985300898552, 1) 0%, rgba(2.1819744911044836, 42.20017835497856, 78.99852856993675, 1) 100%);
      width: 100%;
      height: 200px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 20px;
  }
  .e2_22 { 
      color: #f0f8ff;
      font-family: Montserrat;
      text-align: left;
      font-size: 3.5vw; /* Responsive font size */
      letter-spacing: 0;
      line-height: 1.2em;
  }
  .e2_23 { 
      transform: rotate(-2.4848083448933725e-17deg);
      width: 100%;
      height: 0px;
      border: 2px solid rgba(255, 255, 255, 1);
  }
  .e1_8 { 
      width:281px;
      height:281px;
      position: absolute;
      right: 20px;
  }
  .e1_9 { 
      width:259.046875px;
      height:166.84375px;
      position:absolute;
      left:10.9765625px;
      top:57.078125px;
  }
  .header-text-container {
      display: flex;
      flex-direction: column;
  }
  .header-image {
      max-width: 150px;
      height: auto;
  }
  .bottom-left-image-container {
      display: block;
      margin-top: 10px;
      text-align: left;
  }
  .stButton > button {
      background-image: linear-gradient(0deg, rgba(4, 65, 121, 1) 0%, rgba(7, 119, 223, 1) 100%);
      color: rgba(255, 255, 255, 1);
      width: 200px;  /* Set a maximum width */
      height: 60px;  /* Set height */
      border-radius: 23px;  /* Rounded corners */
      font-family: 'Montserrat', sans-serif;
      font-size: 16px;  /* Font size */
      text-align: center;
      line-height: 60px;  /* Center text vertically */
      border: none;  /* No border */
      cursor: pointer;  /* Change cursor on hover */
      transition: opacity 0.3s ease;  /* Smooth transition for hover effect */
      overflow-wrap: break-word;  /* Allow text to wrap */
      word-wrap: break-word;  /* For compatibility */
      hyphens: auto;  /* Hyphenate words if needed */
  }
  
  /* Hover effect */
  .stButton > button:hover {
      opacity: 0.9;  /* Slightly transparent on hover */
  }

  /* Responsive adjustments for smaller screens */
  @media (max-width: 768px) {
    .e1_15, .e2_22 {
        font-size: 5vw;
    }
  
    .header-image {
        max-width: 80px;
    }
  }
  </style>
  
  <div class="e2_21">
      <div class="header-text-container">
          <div class="e1_15">DIGITAL EQUITY DASHBOARD</div>
          <div class="e2_23"></div>
          <div class="e2_22">Hawaii</div>
      </div>
      <div class="header-image">
          <a href="./" target="_self">
              <img src="https://raw.githubusercontent.com/datjandra/Team-Pu-u-Kukui/refs/heads/main/images/hawaii.png" alt="Header Image">
          </a>
      </div>
  </div>
  """
  
  # Insert the HTML and CSS into the Streamlit app
  st.markdown(html_content, unsafe_allow_html=True)

  if not suppress_anchor:
    image_anchor = """
    <!-- Left-aligned image anchor at the bottom -->
    <div class="bottom-left-image-container">
        <a href="./" target="_self">
            <img src="https://raw.githubusercontent.com/datjandra/Team-Pu-u-Kukui/refs/heads/main/images/arrow-left-s-line.png" alt="Bottom Left Image" width="50px">
        </a>
    </div>
    """
    st.markdown(image_anchor, unsafe_allow_html=True)
