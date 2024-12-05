[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<br />
<div align="center">
  <a href="https://github.com/jacob-thompson/pong-arcade">
    <img src="https://raw.githubusercontent.com/jacob-thompson/pong-arcade/main/src/pong_arcade/data/gfx/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">pong-arcade</h3>

  <p align="center">
    Pong written using pygame
    <br />
  </p>
</div>


## About The Project

![Screenshot](https://raw.githubusercontent.com/jacob-thompson/pong-arcade/main/src/pong_arcade/data/gfx/screenshot.png)

This application is an implementation of [Pong](https://en.wikipedia.org/wiki/Pong), originally developed and released by [Atari](https://en.wikipedia.org/wiki/Atari,_Inc._(1972%E2%80%931992)) in 1972. `pong-arcade` was created using [pygame](https://www.pygame.org/wiki/about) and [various resources](https://github.com/jacob-thompson/pong-arcade/tree/main/src/pong_arcade/data).


## Play

#### Install

As per [PEP 668](https://peps.python.org/pep-0668/), it is recommended to use `pipx` to install this application:

```bash
pipx install pong-arcade
```

Otherwise:

```bash
pip install pong-arcade
```

###### From Source

This application may also be built and installed from source. Requires the pip package `build`:

```bash
python3 -m build
pipx install dist/*.tar.gz
```

```bash
python3 -m build
pip install dist/*.tar.gz
```

#### Run

```bash
pong
```

## Controls

The controls may be examined in-game from the menu.

#### Menu

* `Esc` Quit
* `C` Controls
* `1` Select first menu option
* `2` Select second menu option
* `3` Toggle third menu option

#### In-Game

![Controls Screenshot](https://raw.githubusercontent.com/jacob-thompson/pong-arcade/main/src/pong_arcade/data/gfx/controls.png)

###### Movement

* `W` / `I` Move up
* `S` / `K` Move down

Player1 may use either control scheme in single-player games.

###### Pause/Quit

* `P` / `Q` Pause the game
* `M` / `Z` Exit to menu


## License

Distributed under the MIT License. See [LICENSE](https://github.com/jacob-thompson/pong-arcade/blob/main/LICENSE) for more information.


## Project Links

Github - [jacob-thompson/pong-arcade](https://github.com/jacob-thompson/pong-arcade)

PyPI - [pong-arcade](https://pypi.org/project/pong-arcade/)


## Contact

Jacob Alexander Thompson - jacobalthompson@gmail.com


[contributors-shield]: https://img.shields.io/github/contributors/jacob-thompson/pong-arcade.svg?style=flat
[contributors-url]: https://github.com/jacob-thompson/pong-arcade/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jacob-thompson/pong-arcade.svg?style=flat
[forks-url]: https://github.com/jacob-thompson/pong-arcade/network/members
[stars-shield]: https://img.shields.io/github/stars/jacob-thompson/pong-arcade.svg?style=flat
[stars-url]: https://github.com/jacob-thompson/pong-arcade/stargazers
[issues-shield]: https://img.shields.io/github/issues/jacob-thompson/Pong.svg?style=flat
[issues-url]: https://github.com/jacob-thompson/pong-arcade/issues
[license-shield]: https://img.shields.io/github/license/jacob-thompson/Pong.svg?style=flat
[license-url]: https://github.com/jacob-thompson/pong-arcade/blob/main/LICENSE
