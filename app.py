import os
import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="KEGG Path View", page_icon=":dna:", layout="wide", menu_items={
        'About': "About"
    })

hide_github_icon = """
        #MainMenu {
          visibility: hidden;
}
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)


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
compare_group = ["T4vsT2", "T8vsT2", "T8vsT4"]
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
kegg_map = open(os.path.join('7-Enrichment_pathway_image', select_dataset, select_compare, select_pathway+'.html'))
components.html(kegg_map.read(), height=1000, scrolling=True)   

