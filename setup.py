from setuptools import setup

setup(
    name="pandoc-latex-writer",
    description="practical markdown to latex conversion using pandoc",
    author="Amine Aboufirass",
    author_email="amine.aboufirass@gmail.com",
    install_requires=[
        "panflute>=2.2.3",
        "beautifulsoup4>=4.11.1",
        "requests>=2.28.1",
        "urllib3>=1.26.12"
    ]
)
