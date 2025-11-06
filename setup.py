from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="eco-storm",
    version="0.1.0",
    author="Dr-Ai",
    author_email="",
    description="Economic Storm Analysis Platform for predicting and analyzing economic crises",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ELMOURABEA/ECO-STORM",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Office/Business :: Financial",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scipy>=1.7.0",
        "scikit-learn>=1.0.0",
        "statsmodels>=0.13.0",
        "matplotlib>=3.4.0",
        "flask>=2.0.0",
        "requests>=2.26.0",
        "python-dotenv>=0.19.0",
        "pyyaml>=5.4.0",
        "click>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "eco-storm=src.main:main",
        ],
    },
)
