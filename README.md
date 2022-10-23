[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<br />
<div align="center">
  <a href="https://github.com/jacob-thompson/pong-atari">
    <img src="pong-atari/data/gfx/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">pong-atari</h3>

  <p align="center">
    Pong written using pygame
    <br />
  </p>
</div>


<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#download">Download</a></li>
        <li><a href="#run">Run</a></li>
      </ul>
    </li>
    <li><a href="#controls">Controls</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


## About The Project

[![Pong Screenshot][product-screenshot]](https://github.com/jacob-thompson/pong-atari/blob/main/pong-atari/data/gfx/screenshot.png)

This executable program is an implementation of [Pong](https://en.wikipedia.org/wiki/Pong), originally developed and released by [Atari](https://en.wikipedia.org/wiki/Atari,_Inc._(1972%E2%80%931992)) in 1972. This implementation was created using [Pygame](https://www.pygame.org/wiki/about) and hand-made [resources](https://github.com/jacob-thompson/pong-atari/tree/main/data).


## Getting Started

Follow the below steps to get the program running.

### Prerequisites

* Python >= 3.10
* pygame
```sh
pip install -r requirements.txt
```

### Download

To download the source code, clone the repository:
```sh
git clone https://github.com/jacob-thompson/pong-atari.git
```

### Run

To execute the program from source, run the script:
```sh
python3 pong.py
```

## Controls

The game may be quit by pressing `Esc` at any time.
Controls can be brought up in-game by pressing `C` on the menu screen.

### Menu

* `C` Show controls
* `1` Select first option (One player)
* `2` Select second option (Two players)
* `3` Toggle third option (Sound)

### In-Game

[![Controls Screenshot][controls-screenshot]](https://github.com/jacob-thompson/pong-atari/blob/main/pong-atari/data/gfx/controls.png)

##### Movement

* `W` Move Player1 up
* `S` Move Player1 down
* `I` Move Player2 (or Player1 in single-player) up
* `K` Move Player2 (or Player1 in single-player) down

##### Pause/Quit

* `P` or `Q` Pause the game
* `M` or `Z` Bring up the menu (Exits current game)


## License

Distributed under the MIT License. See `LICENSE` or click [here](https://github.com/jacob-thompson/pong-atari/blob/main/LICENSE) for more information.


## Contact

Jacob Alexander Thompson - jacobalthompson@gmail.com

Project Link - [jacob-thompson/pong-atari](https://github.com/jacob-thompson/pong-atari)


[contributors-shield]: https://img.shields.io/github/contributors/jacob-thompson/pong-atari.svg?style=flat
[contributors-url]: https://github.com/jacob-thompson/pong-atari/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jacob-thompson/pong-atari.svg?style=flat
[forks-url]: https://github.com/jacob-thompson/pong-atari/network/members
[stars-shield]: https://img.shields.io/github/stars/jacob-thompson/pong-atari.svg?style=flat
[stars-url]: https://github.com/jacob-thompson/pong-atari/stargazers
[issues-shield]: https://img.shields.io/github/issues/jacob-thompson/Pong.svg?style=flat
[issues-url]: https://github.com/jacob-thompson/pong-atari/issues
[license-shield]: https://img.shields.io/github/license/jacob-thompson/Pong.svg?style=flat
[license-url]: https://github.com/jacob-thompson/pong-atari/blob/main/LICENSE
[product-screenshot]: pong-atari/data/gfx/screenshot.png
[controls-screenshot]: pong-atari/data/gfx/controls.png
