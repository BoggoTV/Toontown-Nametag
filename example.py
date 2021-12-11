from direct.showbase.ShowBase import ShowBase, WindowControls, exitfunc
from panda3d.core import TransparencyAttrib
from panda3d.core import PandaNode
from panda3d.core import TextNode
from pandac.PandaModules import NodePath
from panda3d.core import DepthWriteAttrib

from toonNametag import createNametag

class Window(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

game = Window()
nametag = createNametag("John McTestToon")
nametag.setPos(0,20,0)
nametag.reparentTo(render)
game.run()