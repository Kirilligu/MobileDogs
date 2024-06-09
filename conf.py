# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

project = 'MobileDogs'
author = 'Kirill Degtyariov'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

if not os.path.exists('_static'):
    os.makedirs('_static')

latex_elements = {
    'preamble': '''
    \\usepackage[utf8]{inputenc}
    \\usepackage[T2A]{fontenc}
    \\usepackage[russian,english]{babel}
    \\usepackage{fontspec}
    \\setmainfont{DejaVu Sans}
    \\usepackage{geometry}
    \\geometry{a4paper, margin=1in}
    \\maxdeadcycles=1000
    ''',
    'babel': '\\usepackage[russian,english]{babel}',
    'inputenc': '\\usepackage[utf8]{inputenc}',
    'fontenc': '\\usepackage[T2A]{fontenc}',
    'extraclassoptions': 'openany,oneside',
    'releasename': 'Version',
    'maketitle': '\\sphinxmaketitle'
}

autodoc_member_order = 'bysource'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': True,
    'show-inheritance': True,
}

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
