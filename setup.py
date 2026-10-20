# setup.py
"""Universal installer fallback for UASF."""

from setuptools import setup, find_packages

setup(
    name="uasf",
    version="1.0.0",
    description="Universal AI Skill Framework (UASF) — Multi-Host AI Run-time Layer",
    author="VannXD0",
    author_email="revan.23@outlook.com",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "uasf": ["*.json", "*.md"]
    },
    entry_points={
        "console_scripts": [
            "uasf = uasf.cli:main"
        ]
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
