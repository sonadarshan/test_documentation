import os
import sys
import sphinx_rtd_theme
sys.path.insert(0, os.path.abspath('../'))

project = 'Test Documentation'
copyright = '2024, SD'
author = 'SD'
release = '1.0'

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinx.ext.viewcode',
              'sphinx.ext.autosummary',
              'sphinx.ext.autodoc.typehints',
              'sphinx.ext.coverage']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

autodoc_typehints = 'description'
autosummary_generate = True