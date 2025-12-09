# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sala 115 (test2)'
copyright = '2025, Camilo Fonseca'
author = 'Camilo Fonseca'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser","sphinx_design","sphinxcontrib.mermaid"]

myst_enable_extensions = [
    #"amsmath",
    "dollarmath", #ecuaciones matematicas con $
    "tasklist", # listas con casillas de verificacion pero como hacer para que sea editable?
    "colon_fence", #bloques con ::: en vez de ```
    "attrs_inline", # para agregar atributos en linea ejemplo: IMAGENES
    "smartquotes", #comillas inteligentes
    #"linkify", # convierte URLs en enlaces automaticamente
    "fieldlist" # listas de campos
]

myst_number_code_blocks = ["python", "c++"] # Numera bloques de código en los lenguajes especificados
myst_links_external_new_tab = True # Abre enlaces externos en una nueva pestaña
myst_links_internal_new_tab = True
myst_enable_checkboxes = True # Habilita casillas de verificación en las listas de tareas
myst_heading_anchors = 3 # Genera enlaces ancla para los encabezados (niveles 1 a 3)


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'style_external_links': True,
}