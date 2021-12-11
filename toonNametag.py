from direct.showbase.ShowBase import ShowBase, WindowControls, exitfunc
from panda3d.core import TransparencyAttrib
from panda3d.core import PandaNode
from panda3d.core import TextNode
from panda3d.core import Loader
from pandac.PandaModules import NodePath
from panda3d.core import DepthWriteAttrib

def createNametag(name, bg=(1,1,1,.5), fg=(0,0,0,1), plateFile='panel.bam'):
    #settings
    nameBg = bg #nameplate, or panel, colour
    model = loader.loadModel(plateFile) #panel model
    nameFg = fg #text colour
    wordWrap = 7.5 #wordwrap, default for TTR/TTO is 7.5
    displayName = name #current displayed name
    font = loader.loadFont('ImpressBT.ttf') #font to be used on nameplate, can be changed for cogs.
    font.setLineHeight(1) #line spacing, default for toontown is 1
    WIDTH_PADDING = 0.2 #horizontal padding of nametag
    HEIGHT_PADDING = 0.2 #vertical padding of nametag


    icon = PandaNode('icon')
    innerNP = PandaNode('nametag')
    innerNP = NodePath.anyPath(innerNP).attachNewNode('nametag_contents')

    # Create text node:
    innerNP.attachNewNode(icon)
    t = innerNP.attachNewNode(TextNode('name'), 1)
    t.node().setFont(font)
    t.node().setAlign(TextNode.ACenter)
    t.node().setWordwrap(wordWrap)
    t.node().setText(displayName)
    t.setColor(nameFg)
    t.setTransparency(nameFg[3] < 1.0)
    width, height = t.node().getWidth(), t.node().getHeight()

    # Put the actual written name a little in front of the nametag and
    # disable depth write so the text appears nice and clear, free from
    # z-fighting and bizarre artifacts. The text renders *after* the tag
    # behind it, due to both being in the transparency bin,
    # so there's really no problem with doing this.
    t.setY(-0.05)
    t.setAttrib(DepthWriteAttrib.make(0))

    # Apply panel behind the text:
    panel = model.copyTo(innerNP, 0)
    panel.setPos((t.node().getLeft()+t.node().getRight())/2.0, 0,
                 (t.node().getTop()+t.node().getBottom())/2.0)
    panel.setScale(width + WIDTH_PADDING, 1, height + HEIGHT_PADDING)
    panel.setColor(nameBg)
    panel.setTransparency(nameBg[3] < 1.0)

    #combine the two pieces into one nodepath, for later use
    nametag = NodePath('nametag')
    panel.reparentTo(nametag)
    t.reparentTo(nametag)

    #return the nametag
    return nametag
        




