# Toontown-Nametag
Toontown-Nametag is a tool for creating Toontown Online/Toontown Rewritten-style nametags in Panda3D. It contains a function, createNametag(), which will return a NodePath of a Toontown-styled nametag/nameplate, complete with text.

# Prerequisites
Panda3D

```pip install Panda3D```

More info: https://pypi.org/project/Panda3D/

# Usage

**Function** createNametag

**Parameters:**

name \*required*: The text to be displayed on the nametag. No default.

bg: Background colour, or colour of the panel. Default `(1,1,1,.5)`

fg: Foreground colour, or colour of the text. Default `(0,0,0,1)`

plateFile: Path for the .bam of your nameplate file. Default `panel.bam`

# Final Notes
I threw this together in a few minutes to throw onto github, and it's most likely missing a lot of important functionality. I'll probably be messing with it in the future, but feel free to make suggestions in Issues or simply make a pull request. Above all else, if you need help with anything, feel free to shoot me an email to the one on my profile, or DM me on Twitter. I'll try to respond ASAP.

Please also note that not all default values are perfect to toontown, such as transparency & colour. You can change these yourself through the paramaters. 
