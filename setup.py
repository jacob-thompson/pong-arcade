from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name = "pong-atari",
    version = "1.2.0",
    description = "Pong written using pygame",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/jacob-thompson/pong-atari",
    author = "Jacob A. Thompson",
    author_email = "jacobalthompson@gmail.com",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Topic :: Games/Entertainment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords = "pong, atari, game, retro, executable, application",
    package_dir = {"": "src"},
    packages = find_packages("src"),
    include_package_data = True,
    python_requires = ">=3.7, <4",
    install_requires = ["pygame"],
    entry_points = {
        "console_scripts": [
            "pong=pong_atari.main:main",
        ],
    },
    project_urls = {
        "Bug Reports": "https://github.com/jacob-thompson/pong-atari/issues",
    },
)