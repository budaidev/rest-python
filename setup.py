"""Setup configuration for the Flask REST API package."""

from setuptools import find_packages, setup

setup(
    name="my-flask-api",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask>=2.0.0",
        "flask-cors>=3.0.0",
        "gunicorn>=20.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "flake8-docstrings>=1.6.0",
            "isort>=5.0.0",
            "pre-commit>=3.0.0",
        ]
    },
    python_requires=">=3.8",
    description="A production-ready Flask REST API",
    author="Developer",
    author_email="developer@example.com",
    url="https://github.com/username/my-flask-api",
)
