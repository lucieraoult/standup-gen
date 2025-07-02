from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="standup-gen",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python CLI tool that generates daily standup updates using Git commits and OpenAI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucieraoult/standup-gen",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Tools",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=[
        "click>=8.0.0",
        "openai>=1.0.0",
        "python-dotenv>=0.19.0",
        "pyperclip>=1.8.0",
    ],
    entry_points={
        "console_scripts": [
            "standup-gen=standup_gen.cli:cli",
        ],
    },
    keywords="standup git openai cli development productivity",
    project_urls={
        "Bug Reports": "https://github.com/lucieraoult/standup-gen/issues",
        "Source": "https://github.com/lucieraoult/standup-gen",
    },
    license="MIT",
)