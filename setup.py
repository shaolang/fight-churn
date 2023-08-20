import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fightchurn",
    version="1.1.1",
    author="Carl Gold",
    author_email="carl24k@fightchurnwithdata.com",
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
    python_requires=">=3.9,<3.10",
    install_requires=["antlr4-python3-runtime==4.9.3.0",
                        "bleach==6.0.0",
                        "build==0.10.0",
                        "certifi==2023.7.22",
                        "chardet==5.2.0",
                        "cloudpickle==2.2.1",
                        "colorama==0.4.6",
                        "cycler==0.11.0",
                        "docutils==0.20.1",
                        "greenlet==2.0.2",
                        "hydra-core==1.3.2",
                        "importlib-metadata==6.8.0",
                        "joblib==1.3.2",
                        "keyring==24.2.0",
                        "kiwisolver==1.4.4",
                        "llvmlite==0.40.1",
                        "matplotlib==3.7.2",
                        "numba==0.57.1",
                        "numpy==1.24.4",
                        "packaging==23.1",
                        "pandas==1.5.3",
                        "patsy==0.5.3",
                        "Pillow==10.0.0",
                        "filelock==3.12.2",
                        "omegaconf==2.3.0",
                        "pkginfo==1.9.6",
                        "postgres==4.0",
                        "psycopg2-binary==2.9.7",
                        "psycopg2-pool==1.1",
                        "Pygments==2.16.1",
                        "pyparsing==2.4.7",
                        "python-dateutil==2.8.2",
                        "pytz==2023.3",
                        "pytest",
                        "readme-renderer==41.0",
                        "requests==2.31.0",
                        "requests-toolbelt==1.0.0",
                        "rfc3986==1.5.0",
                        "scikit-learn==1.3.0",
                        "scipy==1.11.2",
                        "shap==0.42.1",
                        "six==1.16.0",
                        "slicer==0.0.7",
                        "SQLAlchemy==1.4.9",
                        "statsmodels==0.14.0",
                        "toml==0.10.2",
                        "tqdm==4.66.1",
                        "twine==4.0.2",
                        "urllib3==2.0.4",
                        "webencodings==0.5.1",
                        "xgboost==1.7.6",
                        "zipp==3.16.2"]
)
