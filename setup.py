from setuptools import setup, find_packages

setup(
    name="openecho",
    version="0.1",
    description="A tool to check usernames and emails on Bulgarian websites.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "openecho=openecho.main:check_all_sites",  # Command-line entry point
        ]
    },
)
