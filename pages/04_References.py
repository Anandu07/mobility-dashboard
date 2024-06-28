import streamlit as st
import bibtexparser

# Your BibTeX string
bibtex_str = """
@article{Liao2024Mar,
	author = {Liao, Yuan and Gil, Jorge and Yeh, Sonia and Pereira, Rafael H. M. and Alessandretti, Laura},
	title = {{Socio-spatial segregation and human mobility: A review of empirical evidence}},
	journal = {arXiv},
	year = {2024},
	month = mar,
	eprint = {2403.06641},
	doi = {10.48550/arXiv.2403.06641}
}
@incollection{Reed2016Jun,
	author = {Reed, Philip J. and Khan, Muhammad Raza and Blumenstock, Joshua},
	title = {{Observing gender dynamics and disparities with mobile phone metadata}},
	booktitle = {{ACM Other conferences}},
	pages = {1--4},
	year = {2016},
	month = jun,
	publisher = {Association for Computing Machinery},
	address = {New York, NY, USA},
	doi = {10.1145/2909609.2909632}
}
"""

# Parse the BibTeX string
bib_database = bibtexparser.loads(bibtex_str)

# Function to create markdown text with clickable DOI
def create_markdown(entry):
    title = entry.get('title', 'No title').strip('{}')
    authors = entry.get('author', 'Unknown author')
    year = entry.get('year', 'No year')
    doi = entry.get('doi', '')
    doi_link = f"https://doi.org/{doi}" if doi else 'No DOI'
    return f"* **{title}** by {authors} ({year}) [[DOI]({doi_link})]"


st.title("References")
for entry in bib_database.entries:
    reference_md = create_markdown(entry)
    st.markdown(reference_md, unsafe_allow_html=True)
