import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fightchurn",
    version="1.2.0",
    author="Carl Gold",
    author_email="carl@fightchurnwithdata.com",
    description="Code from the book Fighting Churn With Data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carl24k/fight-churn",
    project_urls={
        "Bug Tracker": "https://github.com/carl24k/fight-churn/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={'fightchurn' : ['fightchurn/churnsim/*/*.csv',
                                  'fightchurn/churnsim/*/*.sql',
                                  'fightchurn/churnsim/*/*.yaml',
                                  'fightchurn/listings/conf/*.json',
                                  'fightchurn/listings/*/*.sql']},
    include_package_data=True,
    packages=['fightchurn',
              'fightchurn.churnsim',
              'fightchurn.churnsim.conf',
              'fightchurn.churnsim.schema',
              'fightchurn.listings',
              'fightchurn.listings.conf',
              'fightchurn.listings.chap3',
              'fightchurn.listings.chap5',
              'fightchurn.listings.chap6',
              'fightchurn.listings.chap7',
              'fightchurn.listings.chap8',
              'fightchurn.listings.chap9',
              'fightchurn.listings.chap10'],
    scripts=['fightchurn/run_churn_listing.py',
             'fightchurn/churnsim/churndb.py',
             'fightchurn/churnsim/churnsim.py'],
    python_requires=">=3.9,<3.13",
    install_requires=["antlr4-python3-runtime~=4.9",
                        "bleach~=6.0",
                        "build~=0.10",
                        "certifi",
                        "chardet~=5.2",
                        "cloudpickle~=2.2",
                        "colorama~=0.4",
                        "cycler~=0.11",
                        "docutils~=0.20",
                        "greenlet~=3.0",
                        "hydra-core~=1.3",
                        "importlib-metadata~=6.8",
                        "joblib~=1.3",
                        "keyring~=24.2",
                        "kiwisolver~=1.4",
                        "llvmlite~=0.40",
                        "matplotlib~=3.7",
                        "numba~=0.57",
                        "numpy~=2.0",
                        "packaging~=23.1",
                        "pandas~=2.0",
                        "patsy~=0.5",
                        "Pillow~=10.3",
                        "filelock~=3.12",
                        "omegaconf~=2.3",
                        "pkginfo~=1.9",
                        "postgres~=4.0",
                        "psycopg2-binary~=2.9",
                        "psycopg2-pool~=1.1",
                        "Pygments~=2.16",
                        "pyparsing~=2.4",
                        "python-dateutil~=2.8",
                        "pytz~=2023.3",
                        "pytest",
                        "readme-renderer~=41.0",
                        "requests~=2.31",
                        "requests-toolbelt~=1.0",
                        "rfc3986~=1.5",
                        "scikit-learn~=1.6",
                        "scipy~=1.11",
                        "shap~=0.42",
                        "six~=1.16",
                        "slicer~=0.0",
                        "SQLAlchemy~=1.4",
                        "statsmodels~=0.14",
                        "toml~=0.10",
                        "tqdm~=4.66",
                        "twine~=4.0",
                        "urllib3~=2.0",
                        "webencodings~=0.5",
                        "xgboost~=2.1",
                        "zipp~=3.16"]
)
