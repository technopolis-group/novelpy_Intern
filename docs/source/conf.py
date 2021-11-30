# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'novelpy'
copyright = '2021, Pelletier, Wirtz'
author = 'Pelletier, Wirtz'

release = '0.1'
version = '0.1.4'

# -- General configuration

autosectionlabel_prefix_document = True

bibtex_bibfiles = ['refs.bib']

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.bibtex',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
