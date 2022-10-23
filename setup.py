from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="pong-atari",
    version="1.0.0",
    description="Pong written using pygame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jacob-thompson/pong-atari",
    author="Jacob A. Thompson",
    author_email="jacobalthompson@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Other Audience",
        "Topic :: Games/Entertainment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="pong, atari, game, retro, executable, application",
    packages=find_packages(where="pong-atari"),
    python_requires=">=3.10, <4",
    install_requires=["pygame"],
    entry_points={
        "console_scripts": [
            "pong=main.py:main",
        ],
    },
    project_urls={
        "Home": "https://github.com/jacob-thompson/pong-atari",
        "Bug Reports": "https://github.com/jacob-thompson/pong-atari/issues",
    },
)