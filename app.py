import os
import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="KEGG Path View", page_icon=":dna:", layout="wide", menu_items={
        'About': "About"
    })

"""Shows a sticky navigation bar with links to other apps at the top of the page."""
st.write(
"""
<style>
    /* Add a black background color to the top navigation */
    .topnav-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 3.5rem;
        border-bottom: 1px solid rgba(38, 39, 48, 0.2);
        /* padding-left: 60px; */
        /* padding-top: 0.5rem;
        padding-bottom: 0.5rem; */
        /* padding-right: 100px; */
        background-color: white;
        z-index: 98;
        
        line-height: 3.5rem;
        
        flex: 1 1 0%;
        
    }
    
    .topnav {
        overflow: hidden;
        /* position: relative;
        top: -50px; */
        padding-left: 1rem;
        padding-right: 1rem;
    
        max-width: 730px;
        margin: 0 auto;
        
        display: flex;
        /*justify-content: space-between;*/
        justify-content: center;
        align-items: center;
        
        vertical-align: middle;
    }
    
    /* Style the links inside the navigation bar */
    .topnav a {
        color: rgb(38, 39, 48);
        text-align: center;
        text-decoration: none;
        /* font-size: 17px; */
    }
    
    /* Change the color of links on hover */
    .topnav a:hover {
        color: #e24768;
    }
    
    /* Add a color to the active/current link */
    .topnav a.active {
        color: #e24768;
    }
    
    /*.topnav-right a {
        margin-left: 3rem;
    }*/
    
    .topnav-right {
        display: none;
    }
    
    @media screen and (max-width: 800px) {
        .topnav-right {
            display: none;
        }
        
        .topnav {
            justify-content: center;
        }
    }
    
    .topnav-title {
        margin-left: 1rem;
        font-weight: 500;
    }
</style>

<div class="topnav-container">
    <nav class="topnav">
        <div class="topnav-left">
            <a href="https://share.streamlit.io/jrieke/st-frontpage/main">
                <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" width=35>
                <span class="topnav-title">View all apps</span>
            </a>
        </div>
        <div class="topnav-right">
            <a href="https://share.streamlit.io/jrieke/st-frontpage/main">View all apps</a>
            <a href="https://share.streamlit.io/" target="_blank"><img src="https://screenshots.imgix.net/mui-org/material-ui-icons/account-circle-outlined/~v=3.9.2/e6ffca0e-87fa-4e5b-92ca-05c6079b5f9e.png?ixlib=js-1.2.0&s=c0f87e872aac058178a34a41422a425d" width=35 style="border-radius: 100%; margin-left: 1rem;"></a>
        </div>
    </nav>
</div>
""",
unsafe_allow_html=True,
)


st.markdown(
    f"""
        <style>
            .main .block-container {{
                max-width: 100%;
            }}
            iframe {{
                left: 0;
            }}
            .block-container {{
                padding-top: 1.2rem;
                padding-bottom: 0rem;
                padding-left: 5rem;
                padding-right: 5rem;
            }}
        </style>
    """,
    unsafe_allow_html=True,
)

select_dataset = ''
select_compare = ''
select_pathway = ''
data_set = os.listdir('./7-Enrichment_pathway_image')
compare_group = ["T2vsS", "T4vsS", "T8vsS"]
pathway = []

with st.sidebar:
    st.info("**KEGG Path View**", icon="🍒")

    select_dataset = st.selectbox(
        label="Choose the dataset:",
        options=data_set,
    )

    select_compare = st.selectbox(
        label="Choose the compare group:",
        options=compare_group,
    )

    if select_compare:
        pathway = [p.replace('.html','') for p in os.listdir(os.path.join('7-Enrichment_pathway_image', select_dataset, select_compare)) if p.endswith('.html')]

    select_pathway = st.selectbox(
        label="Choose the KEGG pathway:",
        options=pathway,
    )

    st.markdown("---")
    st.markdown(
        '<h5 style="color:blue">@Author: ZengChui</h5>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<h5 style="color:blue">@Email: zengchui@126.com</h5>',
        unsafe_allow_html=True,
    )

st.title(":rainbow[Multiomics KEGG Pathway view:]")
st.markdown(
    f'<h3>Dataset: {select_dataset} --- Compare group: {select_compare} --- Pathway: {select_pathway}</h3>',
    unsafe_allow_html=True,
)

cols = st.columns([4, 3])
with cols[0]:
    kegg_map = open(os.path.join('7-Enrichment_pathway_image', select_dataset, select_compare, select_pathway+'.html'))
    components.html(kegg_map.read(), height=700, scrolling=True)   
with cols[1]:
    heatmap = os.path.join('7-Enrichment_pathway_image', select_dataset, select_compare, 'heatmap2', select_pathway.split(' ')[0].replace('map', 'mmu') + "_heatmap.png")
    st.image(heatmap, caption="heatmap")
