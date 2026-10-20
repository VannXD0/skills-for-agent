# setup.py
"""Universal installer fallback for UASF."""

from setuptools import setup, find_packages

setup(
    name="skills-for-agent",
    version="1.0.0",
    description="Skills For Agent (UASF) — Standardized Multi-Agent Protocols & Skills",
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
