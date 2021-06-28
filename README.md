## Space Shooter

The classic retro game recreated using `Pygame` and `python`.

<p align="center">
<a href="https://www.paypal.me/tasdikrahman" target="_blank"><img src="https://tuxtricks.files.wordpress.com/2016/12/donate.png" alt="Donate via PayPal!" title="Donate via PayPal!" /></a>
</p>

If you are from the Indian subcontinent, 

<p align="center">
<a href="https://www.instamojo.com/@tasdikrahman" target="_blank"><img src="https://www.instamojo.com/blog/wp-content/uploads/2017/01/instamojo-91.png" alt="Donate via instamojo" title="Donate via instamojo" /></a>
</p>

Some of my projects are also on [gratipay](https://gratipay.com/~prodicus/)

<a href="https://news.ycombinator.com/item?id=10925168"><img src="https://raw.githubusercontent.com/wingify/across-tabs/master/images/hn.png" width="150" height="20"/></a>
<a href="https://www.producthunt.com/posts/space-shooter"><img src="https://raw.githubusercontent.com/wingify/across-tabs/master/images/product_hunt.png" width="100" height="20"/></a>


## Index

- [Demo](https://github.com/prodicus/spaceShooter#demo)
  - [Screenshots](https://github.com/prodicus/spaceShooter#screenshots)
- [Game Features](https://github.com/prodicus/spaceShooter#game-features)
  - [Controls](https://github.com/prodicus/spaceShooter#controls)
- [Installation](https://github.com/prodicus/spaceShooter#installation)
  - [For Windows](https://github.com/prodicus/spaceShooter#for-windows)
  - [Linux/Debian based systems](https://github.com/prodicus/spaceShooter#linuxdebian-based-systems)
    - [Option 1: Download the zipped executable file](https://github.com/prodicus/spaceShooter#option-1-download-the-zipped-executable-file)
    - [Option 2: Build from source](https://github.com/prodicus/spaceShooter#option-2-build-from-source)
  - [For MAC OS X](https://github.com/prodicus/spaceShooter#for-mac-os-x)
- [Contributing](https://github.com/prodicus/spaceShooter#contributing)
  - [Contributers](https://github.com/prodicus/spaceShooter#contributers)
  - [To-do](https://github.com/prodicus/spaceShooter#to-do)
- [Issues](https://github.com/prodicus/spaceShooter#issues)
- [Similar](https://github.com/prodicus/spaceShooter#similar)
- [License](https://github.com/prodicus/spaceShooter#license)

## Demo

[[Back to top]](https://github.com/prodicus/spaceShooter#index)

Follow the youtube video to see how I fared on ``spaceShooter``

[![Space Shooter Demo - Youtube](http://i.imgur.com/bHjlJfG.jpg)](https://www.youtube.com/watch?v=o99zpLsM-ZI)

## Screenshots

[[Back to top]](https://github.com/prodicus/spaceShooter#index)

| ![Screen 1](http://i.imgur.com/3MzfmbT.jpg) | ![Screen 2](http://i.imgur.com/4OgIByR.png) |
|---------------------------------------------|---------------------------------------------|
| ![Screen 3](http://i.imgur.com/PFQJjE8.png) | ![Screen 4](http://i.imgur.com/lV4aIur.png) |

## Game Features

[[Back to top]](https://github.com/prodicus/spaceShooter#index)

- Health bar for the space ship
- Score board to show how you are faring so far
- Power ups like
  - shield: increases the space ships life
  - bolt: increases the shooting capability of the ship by firing 2 to 3 bullets instead of one at time.
- Custom sounds and sprite animation for things like
  - meteorite explosion
  - bullet shoots
  - player explosion
- 3 lives per game
- Fun to play :)

## Controls

[[Back to top]](https://github.com/prodicus/spaceShooter#index)

|              | Button              |
|--------------|---------------------|
| Move Left    | <kbd>left</kbd>     |
| Move right   | <kbd>right</kbd>    |
| Fire bullets | <kbd>spacebar</kbd> |
| Quit game    | <kbd>Esc</kbd>      |

## Installation

[[Back to top]](https://github.com/prodicus/spaceShooter#index)

### For `Windows`

- :arrow_down: [Download the prebuilt zip file and unzip it.](https://github.com/prodicus/spaceShooter/releases/latest)
- Run the executable named `spaceShooter` inside the extracted file.

### `Linux/Debian` based systems

#### Option 1: Download the zipped executable file

- :arrow_down: [Download the latest zip file for linux](https://github.com/prodicus/spaceShooter/releases/latest)
- Unzip the file

If your download was saved on the `~/Downloads` folder

Press <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd> to open the shell if you are on `GNU/Linux` based systems and type

```bash
$ unzip ~/Downloads/SpaceShooter-0.0.3.Linux.zip -d ~/Desktop
$ cd ~/Desktop
$ ## navigate to the unzipped file and change the file permissions for the executable
~/Desktop $ chmod +x spaceShooter
~/Desktop $ ./spaceShooter
```

This will unzip the file on your `Desktop`, you can replace it with the directory of your choice

**NOTE** : If it gives you an error, you probably don't have `unzip` installed in your system.

```bash
$ sudo apt-get install unzip
```
That should fix the error.

- Run the executable named `spaceShooter`

A Similar process would be followed for `OS X`

#### Option 2: Build from source

You need to have `pygame` installed for this option. 

##### Ubuntu/Debian

```bash
$ sudo apt-get install python-pygame
```

##### Clone the repo

```bash
$ git clone https://github.com/prodicus/spaceShooter.git
$ cd spaceShooter/ 
$ python spaceShooter.py
```

### For `MAC OS X` 

You have to build from source to get it up and running on `OS X`. Reason?
I don't have an `OS X` system to build the executable! So I would love for a Pull request on that one.

Building from source will do the trick though


```bash
$ pip3 install hg+http://bitbucket.org/pygame/pygame
```

Install Pygame specific dependencies

```bash
$ brew install sdl sdl_image sdl_ttf portmidi libogg libvorbis
$ brew install sdl_mixer --with-libvorbis
```

##### Clone the repo

```bash
$ git clone https://github.com/prodicus/spaceShooter.git
$ cd spaceShooter/ 
$ python spaceShooter.py
```

## Contributing

[[Back to top]](https://github.com/prodicus/spaceShooter#index)

This game was written in one day, so the coding standards might not be up the mark. Don't be shy to make a Pull request :)

For details, please refer [the Contributing page](https://github.com/prodicus/spaceShooter/blob/master/CONTRIBUTING.rst)

### Contributers

[[Back to top]](https://github.com/prodicus/spaceShooter#index)

- [@bardlean86](https://github.com/bardlean86/) for adding the third missile powerup and the main menu

### To-do

[[Back to top]](https://github.com/prodicus/spaceShooter#index)

- [x] Add the `windows` executable file
- [x] Add main menu for the game
- [x] Fix [bug](https://github.com/prodicus/spaceShooter/blob/master/spaceShooter.py#L372) which stops the background music from looping 
- [x] Add support for `WAV` game music file as `ogg` format is not playable as described in [#1](https://github.com/prodicus/spaceShooter/issues/1)
- [ ] Add feature to pause to the game.
- [ ] add feature to replay the game after all players die
- [ ] Add `OS X` executable file as the `Debian` based one fails to execute on it


## Issues

[[Back to top]](https://github.com/prodicus/spaceShooter#index)

You can report the bugs at the [issue tracker](https://github.com/prodicus/spaceShooter/issues)

**OR**

You can [tweet me](https://twitter.com/tasdikrahman) if you can't get it to work. In fact, you should tweet me anyway.

## Similar

[[Back to top]](https://github.com/prodicus/spaceShooter#index)

- [Bullethell.py ](https://github.com/Frederikxyz/bullethell.py) : A fork of [prodicus/spaceShooter](https://github.com/prodicus/spaceShooter) which adds fancy shooting capabilities

## License

[[Back to top]](https://github.com/prodicus/spaceShooter#index)

Built with ♥ by [Tasdik Rahman](http://tasdikrahman.me)[(@tasdikrahman)](https://twitter.com/tasdikrahman) under [MIT License](http://prodicus.mit-license.org)

You can find a copy of the License at http://prodicus.mit-license.org/

- The images used in the game are taken from [http://opengameart.org/](http://opengameart.org/), more particulary from the [Space shooter content pack](http://opengameart.org/content/space-shooter-redux) from [@kenney](http://opengameart.org/users/kenney).

License for them is in `Public Domain`

- The game sounds were again taken from [http://opengameart.org/](http://opengameart.org/). The game music, [Frozen Jam](http://opengameart.org/content/frozen-jam-seamless-loop) by [tgfcoder](https://twitter.com/tgfcoder) licensed under [CC-BY-3](http://creativecommons.org/licenses/by/3.0/)
