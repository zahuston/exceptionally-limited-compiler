from setuptools import setup

setup(
    name = 'extremely-limited-compiler',
    version = '1.0',
    url = 'https://github.com/zahuston/exceptionally-limited-compiler',
    python_requires='>=3.8',
    packages=[
        'parser'
    ],
    scripts=[
        'compile.py'
    ],
)

# Build steps
# lexify
# ASTify
# targetify
