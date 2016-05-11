'''
Created on 14.09.2013
@author: Emre Tekinalp
@e-mail: e.tekinalp@gmx.de
@website: www.gravityofexplosion.com
@brief: Includes nodes of maya
'''

import os
from maya import cmds


class Node(object):
    """
    This class creates and contains any kind of existing nodes in maya
    """

    def __init__(self):
        pass
    #END def __init__():

    def addDoubleLinear(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('addDoubleLinear', name = name + "_" + suffix)
            else:
                cmds.createNode('addDoubleLinear', name = name + "_ADL")
        else:
            cmds.createNode('addDoubleLinear')
    #END def addDoubleLinear()

    def addMatrix(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('addMatrix', name = name + "_" + suffix)
            else:
                cmds.createNode('addMatrix', name = name + "_AMX")
        else:
            cmds.createNode('addMatrix')
    #END def addMatrix()

    def aimConstraint(self, 
                        target = None, 
                        source = None, 
                        name = None, 
                        suffix = None, 
                        aimVector = [1,0,0], 
                        upVector = [0,1,0],
                        worldUpObject = None, 
                        worldUpType = 'vector', 
                        skip = 'none'):
        if target and source:
            if name:
                if suffix:
                    aim = cmds.aimConstraint(target, 
                                             source, 
                                             name = name + '_' + suffix,
                                             aimVector = aimVector, 
                                             upVector = upVector,
                                             worldUpObject = worldUpObject, 
                                             worldUpType = worldUpType, 
                                             skip = skip)
                else:
                    aim = cmds.aimConstraint(target, 
                                             source, 
                                             name = name + '_AIM',
                                             aimVector = aimVector, 
                                             upVector = upVector,
                                             worldUpObject = worldUpObject, 
                                             worldUpType = worldUpType, 
                                             skip = skip)
            else:
                aim = cmds.aimConstraint(target, 
                                         source, 
                                         aimVector = aimVector, 
                                         upVector = upVector, 
                                         worldUpObject = worldUpObject, 
                                         worldUpType = worldUpType, 
                                         skip = skip)
                if suffix:
                    aim = cmds.rename(aim[0], 
                                      aim[0].split('aimConstraint1')[0] + suffix)
                else:
                    aim = cmds.rename(aim[0], 
                                      aim[0].split('aimConstraint1')[0] + 'AIM')
        else:
            raise Exception('Specified target: ' + str(target) + ' and source: '
                            + str(source) + 'is not valid!')
        return aim
    #END def aimConstraint()

    def angleBetween(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('angleBetween', name = name + '_' + suffix)
            else:
                cmds.createNode('angleBetween', name = name + '_ABW')
        else:
            cmds.createNode('angleBetween')
    #END def angleBetween()

    def arrayMapper(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('arrayMapper', name = name + '_' + suffix)
            else:
                cmds.createNode('arrayMapper', name = name + '_AMP')
        else:
            cmds.createNode('arrayMapper')
    #END def arrayMapper()

    def blendColors(self, 
                     name = None, 
                     suffix = None,
                     blender = 0.5,
                     color1R = 1,
                     color1G = 0,
                     color1B = 0,
                     color2R = 0,
                     color2G = 0,
                     color2B = 1,
                     lockAttr = None):
        #--- create a blendColors node
        if name:
            if suffix:
                blc = cmds.createNode('blendColors', name = name + '_' + suffix)
            else:
                blc = cmds.createNode('blendColors', name = name + '_BLC')
        else:
            blc = cmds.createNode('blendColors')
        #--- take care of the node's settings
        if blender:
            if not float(blender) > 1:
                #--- blender
                cmds.setAttr(blc + '.blender', float(blender))
        if color1R:
            #--- color1R
            cmds.setAttr(blc + '.color1R', float(color1R))
        if color1G:
            #--- color1G
            cmds.setAttr(blc + '.color1G', float(color1G))
        if color1B:
            #--- color1B
            cmds.setAttr(blc + '.color1B', float(color1B))
        if color2R:
            #--- color2R
            cmds.setAttr(blc + '.color2R', float(color2R))
        if color2G:
            #--- color2G
            cmds.setAttr(blc + '.color2G', float(color2G))
        if color2B:
            #--- color2B
            cmds.setAttr(blc + '.color2B', float(color2B))
        if lockAttr:
            if isinstance(lockAttr, list):
                for i in lockAttr:
                    cmds.setAttr(blc + '.' + i, lock = True)
            else:
                cmds.setAttr(blc + '.' + lockAttr, lock = True)
        return blc
    #END def blendColors()

    def blendTwoAttr(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('blendTwoAttr', name = name + '_' + suffix)
            else:
                cmds.createNode('blendTwoAttr', name = name + '_BTA')
        else:
            cmds.createNode('blendTwoAttr')
    #END def blendTwoAttr()

    def bump2d(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('bump2d', name = name + '_' + suffix)
            else:
                cmds.createNode('bump2d', name = name + '_B2D')
        else:
            cmds.createNode('bump2d')
    #END def bump2d()

    def bump3d(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('bump3d', name = name + '_' + suffix)
            else:
                cmds.createNode('bump3d', name = name + '_B3D')
        else:
            cmds.createNode('bump3d')
    #END def bump3d()

    def closestPointOnMesh(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('closestPointOnMesh', name = name + '_' + suffix)
            else:
                cmds.createNode('closestPointOnMesh', name = name + '_CPM')                
        else:
            cmds.createNode('closestPointOnMesh')
    #END def closestPointOnMesh()

    def closestPointOnSurface(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('closestPointOnSurface', name = name + '_' + suffix)
            else:
                cmds.createNode('closestPointOnSurface', name = name + '_CPS')
        else:
            cmds.createNode('closestPointOnSurface')
    #END def closestPointOnSurface()

    def choice(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('choice', name = name + '_' + suffix)
            else:
                cmds.createNode('choice', name = name + '_CHO')
        else:
            cmds.createNode('choice')
    #END def choice()

    def chooser(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('chooser', name = name + '_' + suffix)
            else:
                cmds.createNode('chooser', name = name + '_CHU')
        else:
            cmds.createNode('chooser')
    #END def chooser()

    def clamp(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('clamp', name = name + '_' + suffix)
            else:
                cmds.createNode('clamp', name = name + '_CMP')                
        else:
            cmds.createNode('clamp')
    #END def clamp()

    def colorProfile(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('colorProfile', name = name + '_' + suffix)
            else:
                cmds.createNode('colorProfile', name = name + '_CPR')
        else:
            cmds.createNode('colorProfile')
    #END def colorProfile()

    def composeMatrix(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('composeMatrix', name = name + '_' + suffix)
            else:
                cmds.createNode('composeMatrix', name = name + '_CMX')
        else:
            cmds.createNode('composeMatrix')
    #END def composeMatrix()

    def condition(self, 
                   name = None, 
                   suffix = None,
                   firstTerm = 0,
                   secondTerm = 0,
                   operation = 0,
                   colorIfTrueR = 0,
                   colorIfTrueG = 0,
                   colorIfTrueB = 0,
                   colorIfFalseR = 1,
                   colorIfFalseG = 1,
                   colorIfFalseB = 1,
                   lockAttr = None):
        #--- create a condition node
        if name:
            if suffix:
                cnd = cmds.createNode('condition', name = name + '_' + suffix)
            else:
                cnd = cmds.createNode('condition', name = name + '_CND')
        else:
            cnd = cmds.createNode('condition')
        #--- take care of the node's settings
        if firstTerm:
            #--- firstTerm
            cmds.setAttr(cnd + '.firstTerm', float(firstTerm))
        if secondTerm:
            #--- secondTerm
            cmds.setAttr(cnd + '.secondTerm', float(secondTerm))
        if operation:
            #--- operation
            cmds.setAttr(cnd + '.operation', int(operation))
        if colorIfTrueR:
            #--- colorIfTrueR
            cmds.setAttr(cnd + '.colorIfTrueR', float(colorIfTrueR))
        if colorIfTrueG:
            #--- colorIfTrueG
            cmds.setAttr(cnd + '.colorIfTrueG', float(colorIfTrueG))
        if colorIfTrueB:
            #--- colorIfTrueB
            cmds.setAttr(cnd + '.colorIfTrueB', float(colorIfTrueB))
        if colorIfFalseR:
            #--- colorIfFalseR
            cmds.setAttr(cnd + '.colorIfFalseR', float(colorIfFalseR))
        if colorIfFalseG:
            #--- colorIfFalseG
            cmds.setAttr(cnd + '.colorIfFalseG', float(colorIfFalseG))
        if colorIfFalseB:
            #--- colorIfFalseB
            cmds.setAttr(cnd + '.colorIfFalseB', float(colorIfFalseB))
        #--- lock specified attribute
        if lockAttr:
            if isinstance(lockAttr, list):
                for i in lockAttr:
                    cmds.setAttr(cnd + '.' + i, lock = True)
            else:
                cmds.setAttr(cnd + '.' + lockAttr, lock = True)         
        return cnd
    #END def condition()

    def contrast(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('contrast', name = name + '_' + suffix)
            else:
                cmds.createNode('contrast', name = name + '_CON')                
        else:
            cmds.createNode('contrast')
    #END def contrast()

    def curveInfo(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('curveInfo', name = name + '_' + suffix)
            else:
                cmds.createNode('curveInfo', name = name + '_CIN')
        else:
            cmds.createNode('curveInfo')
    #END def curveInfo()

    def decomposeMatrix(self, name = None, suffix = None):
        #--- this method creates a decomposeMatrix node
        if name:
            if suffix:
                dcm = cmds.createNode('decomposeMatrix', name = name + '_' + suffix)
            else:
                dcm = cmds.createNode('decomposeMatrix', name = name + '_DCM')
        else:
            dcm = cmds.createNode('decomposeMatrix')
        return dcm
    #END def decomposeMatrix()

    def distanceBetween(self, 
                          name = None, 
                          suffix = None,
                          point1 = None,
                          point2 = None,
                          inMatrix1 = None,
                          inMatrix2 = None,
                          lockAttr = None):
        #--- this method creates a distanceBetween node
        if name:
            if suffix:
                dib = cmds.createNode('distanceBetween', name = name + '_' + suffix)
            else:
                dib = cmds.createNode('distanceBetween', name = name + '_DIB')
        else:
            dib = cmds.createNode('distanceBetween')
        #--- take care of the node's settings
        #--- point1
        if point1:
            if cmds.nodeType(point1) == 'transform':
                cmds.connectAttr(point1 + '.rotatePivotTranslate', dib + '.point1')
            else:
                raise Exception('You have to specify a transform node: ' + str(point1))
        #--- point2
        if point2:
            if cmds.nodeType(point2) == 'transform':
                cmds.connectAttr(point2 + '.rotatePivotTranslate', dib + '.point2')
            else:
                raise Exception('You have to specify a transform node: ' + str(point2))
        #--- inMatrix1
        if inMatrix1:
            if cmds.nodeType(inMatrix1) == 'transform':
                cmds.connectAttr(inMatrix1 + '.worldMatrix[0]', dib + '.inMatrix1')
            else:
                raise Exception('You have to specify a transform node: ' + str(inMatrix1))
        #--- inMatrix2
        if inMatrix2:
            if cmds.nodeType(inMatrix2) == 'transform':
                cmds.connectAttr(inMatrix2 + '.worldMatrix[0]', dib + '.inMatrix2')
            else:
                raise Exception('You have to specify a transform node: ' + str(inMatrix2))
        #--- lock specified attribute
        if lockAttr:
            if isinstance(lockAttr, list):
                for i in lockAttr:
                    cmds.setAttr(dib + '.' + i, lock = True)
            else:
                cmds.setAttr(dib + '.' + lockAttr, lock = True)             
        return dib
    #END def distanceBetween()

    def doubleSwitch(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('doubleShadingSwitch', name = name + '_' + suffix)
            else:
                cmds.createNode('doubleShadingSwitch', name = name + '_DSW')
        else:
            cmds.createNode('doubleShadingSwitch')
    #END def doubleSwitch()

    def eLocator(self, 
                  name = None, 
                  suffix = None,
                  shape = 0,
                  size = 1,
                  orientation = 0,
                  color = 0,
                  width = 1,
                  offset = [0,0,0],
                  lockAttr = None):
        #--- this method creates a eLocator node (PLUGIN)
        #--- check if eLocator plugin is loaded
        root = os.path.dirname(os.path.dirname(__file__))
        plugin = os.path.join(root, 'tools', 'custom_locator.py')
        if not cmds.pluginInfo('custom_locator.py', query = True, loaded = True):
            cmds.loadPlugin(plugin)
        #--- check naming of the node
        if name:
            if suffix:
                loc = cmds.createNode('eLocator', name = (name + '_' + 
                                                          suffix + 'Shape'))
            else:
                loc = cmds.createNode('eLocator', name = name + 'Shape')
        else:
            loc = cmds.createNode('eLocator')
        #--- take care of the node's settings
        if shape:
            #--- shape
            cmds.setAttr(loc + '.shape', int(shape))
        if size:
            #--- size
            cmds.setAttr(loc + '.size', float(size))
        if orientation:
            #--- orientation
            cmds.setAttr(loc + '.orientation', float(orientation))
        if color:
            #--- color
            cmds.setAttr(loc + '.color', int(color - 1))
        if width:
            #--- width
            cmds.setAttr(loc + '.width', int(width))
        if offset:
            cmds.setAttr(loc + '.localPositionX', offset[0])
            cmds.setAttr(loc + '.localPositionY', offset[1])
            cmds.setAttr(loc + '.localPositionZ', offset[2])
        #--- lock specified attribute
        if lockAttr:
            if isinstance(lockAttr, list):
                for i in lockAttr:
                    cmds.setAttr(loc + '.' + i, lock = True)
            else:
                cmds.setAttr(loc + '.' + lockAttr, lock = True)
        #--- lock attributes
        for axis in 'XYZ':
            cmds.setAttr(loc + '.localPosition' + axis, 
                         lock = True, keyable = False, channelBox = False)            
            cmds.setAttr(loc + '.localScale' + axis, 
                         lock = True, keyable = False, channelBox = False)
        for i in ['shape', 'size', 'orientation', 'color', 'width', 'offset']:
            try:
                cmds.setAttr(loc + '.' + i, lock=True, keyable=False, channelBox=False)
            except:
                pass

        #--- enable the locator shapes ovverrideEnabled attribute
        cmds.setAttr(loc + '.overrideEnabled', 1)

        #--- create dictionary
        locator = dict()
        locator['transform'] = loc.split('Shape')[0]
        locator['shape'] = loc
        return locator
    #END def eLocator()

    def follicle(self, 
                  name = None, 
                  suffix = None,
                  parameterU = 0,
                  parameterV = 0, 
                  parent = None, 
                  show = True,
                  lockAttr = None):
        #--- this node creates a follicle with additional parent and show flags
        trn = None
        shp = None
        if name:
            if suffix:
                if parent:
                    trn = cmds.createNode('transform', 
                                          name = name + '_' + suffix,
                                          parent = parent)
                else:
                    trn = cmds.createNode('transform', 
                                          name = name + '_' + suffix)
                shp = cmds.createNode('follicle', 
                                      name = name + '_' + suffix + 'Shape',
                                      parent = trn)
            else:
                if parent:
                    trn = cmds.createNode('transform', 
                                          name = name,
                                          parent = parent)
                else:
                    trn = cmds.createNode('transform', 
                                          name = name)
                shp = cmds.createNode('follicle', 
                                      name = name + 'Shape',
                                      parent = trn)
        else:
            if parent:
                trn = cmds.createNode('transform', 
                                      parent = parent)
            else:
                trn = cmds.createNode('transform')
            shp = cmds.createNode('follicle', 
                                  parent = trn)
        #--- hide the follicle shape
        if not show:
            cmds.setAttr(shp +'.visibility', 0)
        #--- connect the transform with the follicle properly
        cmds.connectAttr(shp +'.outTranslate', trn +'.translate')
        cmds.connectAttr(shp +'.outRotate', trn +'.rotate')
        #--- take care of the node's settings
        if parameterU:
            #--- parameterU
            cmds.setAttr(shp + '.parameterU', float(parameterU))
        if parameterV:
            #--- parameterV
            cmds.setAttr(shp + '.parameterV', float(parameterV))
        #--- lock specified attribute
        if lockAttr:
            if isinstance(lockAttr, list):
                for i in lockAttr:
                    cmds.setAttr(shp + '.' + i, lock = True)
            else:
                cmds.setAttr(shp + '.' + lockAttr, lock = True)
        result = [trn, shp]                
        return result
    #END def follicle()

    def frameCache(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('frameCache', name = name + '_' + suffix)
            else:
                cmds.createNode('frameCache', name = name + '_FRC')                
        else:
            cmds.createNode('frameCache')
    #END def frameCache()

    def gammaCorrect(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('gammaCorrect', name = name + '_' + suffix)
            else:
                cmds.createNode('gammaCorrect', name = name + '_GMC')
        else:
            cmds.createNode('gammaCorrect')
    #END def gammaCorrect()

    def heightField(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('heightField', name = name + '_' + suffix)
            else:
                cmds.createNode('heightField', name = name + '_HFI')
        else:
            cmds.createNode('heightField')
    #END def heightField()

    def hsvToRgb(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('hsvToRgb', name = name + '_' + suffix)
            else:
                cmds.createNode('hsvToRgb', name = name + '_H2R')
        else:
            cmds.createNode('hsvToRgb')
    #END def hsvToRgb()

    def inverseMatrix(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('inverseMatrix', name = name + '_' + suffix)
            else:
                cmds.createNode('inverseMatrix', name = name + '_INM')
        else:
            cmds.createNode('inverseMatrix')
    #END def inverseMatrix()

    def lightInfo(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('lightInfo', name = name + '_' + suffix)
            else:
                cmds.createNode('lightInfo', name = name + '_LIN')
        else:
            cmds.createNode('lightInfo')
    #END def lightInfo()

    def locator(self, 
                 name = None, 
                 suffix = None,
                 position = [0,0,0],
                 rotation = [0,0,0],
                 worldSpace = False,
                 parent = None):
        #--- this method creates a locator
        if name:
            if suffix:
                loc = cmds.spaceLocator(name = name + '_' + suffix)
            else:
                loc = cmds.spaceLocator(name = name + '_LOC')
        else:
            loc = cmds.spaceLocator()
        #--- parent the locator
        if parent:
            cmds.parent(loc, parent)
        #--- define position and rotation values
        if position:
            cmds.xform(loc[0], translation = position, worldSpace = worldSpace)
        if rotation:
            cmds.xform(loc[0], rotation = rotation, worldSpace = worldSpace)
        return loc[0]
    #END def locator()

    def luminance(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('luminance', name = name + '_' + suffix)
            else:
                cmds.createNode('luminance', name = name + '_LUM')
        else:
            cmds.createNode('luminance')
    #END def luminance()

    def mirrorSwitch(self, 
                      name = None, 
                      suffix = None,
                      mirror = 1,
                      mirrorAxis = 0,
                      lockAttr = None):
        #--- this method creates a mirrorSwitch node (PLUGIN)
        #--- check if mirrorSwitch plugin is loaded
        root = os.path.dirname(os.path.dirname(__file__))
        plugin = os.path.join(root, 'tools', 'mirror_node.py')
        if not cmds.pluginInfo('mirror_node.py', query = True, loaded = True):
            cmds.loadPlugin(plugin)
        #--- check naming of the node
        if name:
            if suffix:
                msw = cmds.createNode('mirrorSwitch', name = name + '_' + suffix)
            else:
                msw = cmds.createNode('mirrorSwitch', name = name + '_MSW')
        else:
            msw = cmds.createNode('mirrorSwitch')
        #--- take care of the node's settings
        if mirror:
            #--- mirror
            cmds.setAttr(msw + '.mirror', float(mirror))
        if mirrorAxis:
            #--- mirroAxis
            cmds.setAttr(msw + '.mirrorAxis', int(mirrorAxis))
        #--- lock specified attribute
        if lockAttr:
            if isinstance(lockAttr, list):
                for i in lockAttr:
                    cmds.setAttr(msw + '.' + i, lock = True)
            else:
                cmds.setAttr(msw + '.' + lockAttr, lock = True)        
        return msw
    #END def mirrorSwitch()

    def multDoubleLinear(self, 
                           name = None, 
                           suffix = None,
                           input1 = 0,
                           input2 = 0,
                           lockAttr = None):
        #--- this method creates a multDoubleLinear node
        if name:
            if suffix:
                mdl = cmds.createNode('multDoubleLinear', name = name + '_' + suffix)
            else:
                mdl = cmds.createNode('multDoubleLinear', name = name + '_MDL')
        else:
            mdl = cmds.createNode('multDoubleLinear')
        #--- take care of the node's settings
        if input1:
            #--- input1
            cmds.setAttr(mdl + '.input1', float(input1))
        if input2:
            #--- input2
            cmds.setAttr(mdl + '.input2', float(input2))
        #--- lock specified attribute
        if lockAttr:
            if isinstance(lockAttr, list):
                for i in lockAttr:
                    cmds.setAttr(mdl + '.' + i, lock = True)
            else:
                cmds.setAttr(mdl + '.' + lockAttr, lock = True)        
        return mdl
    #END def multDoubleLinear()

    def multiplyDivide(self, 
                         name = None, 
                         suffix = None,
                         operation = 1,
                         input1X = 0,
                         input1Y = 0,
                         input1Z = 0,
                         input2X = 1,
                         input2Y = 1,
                         input2Z = 1,
                         lockAttr = None):
        #--- this method creates a multiplyDivide node
        if name:
            if suffix:
                mlt = cmds.createNode('multiplyDivide', name = name + '_' + suffix)
            else:
                mlt = cmds.createNode('multiplyDivide', name = name + '_MLT')
        else:
            mlt = cmds.createNode('multiplyDivide')
        #--- take care of the node's settings
        if operation:
            #--- operation
            cmds.setAttr(mlt + '.operation', int(operation))
        if input1X:
            #--- input1X
            cmds.setAttr(mlt + '.input1X', float(input1X))
        if input1Y:
            #--- input1Y
            cmds.setAttr(mlt + '.input1Y', float(input1Y))
        if input1Z:
            #--- input1Z
            cmds.setAttr(mlt + '.input1Z', float(input1Z))
        if input2X:
            #--- input2X
            cmds.setAttr(mlt + '.input2X', float(input2X))
        if input2Y:
            #--- input2Y
            cmds.setAttr(mlt + '.input2Y', float(input2Y))
        if input2Z:
            #--- input2Z
            cmds.setAttr(mlt + '.input2Z', float(input2Z))
        #--- lock specified attribute
        if lockAttr:
            if isinstance(lockAttr, list):
                for i in lockAttr:
                    cmds.setAttr(mlt + '.' + i, lock = True)
            else:
                cmds.setAttr(mlt + '.' + lockAttr, lock = True)        
        return mlt
    #END def multiplyDivide()

    def nearestPointOnCurve(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('nearestPointOnCurve', name = name + '_' + suffix)
            else:
                cmds.createNode('nearestPointOnCurve', name = name + '_NPC')
        else:
            cmds.createNode('nearestPointOnCurve')
    #END def nearestPointOnCurve()

    def orientConstraint(self, 
                           objA = None, 
                           objB = None, 
                           name = None, 
                           suffix = None, 
                           maintainOffset = False):
        #--- this method creates an orientConstraint
        if objA:
            if objB:
                #--- unlock rotate values
                if isinstance(objB, list):
                    for i in objB:
                        for axis in'xyz':
                            cmds.setAttr(i + '.r' + axis, lock = False)
                else:
                    for axis in'xyz':
                        cmds.setAttr(objB + '.r' + axis, lock = False)               
                if name:
                    if suffix:
                        if isinstance(objA, list):
                            for a, b in zip(objA, objB):
                                ocn = cmds.orientConstraint(a, b, name = name + '_' + suffix,
                                                      maintainOffset = maintainOffset)
                        else:
                            ocn = cmds.orientConstraint(objA, objB, name = name + '_' + suffix,
                                                  maintainOffset = maintainOffset)
                    else:
                        if isinstance(objA, list):
                            for a, b in zip(objA, objB):
                               ocn =  cmds.orientConstraint(a, b, name = name + '_OCN',
                                                      maintainOffset = maintainOffset)                        
                        ocn = cmds.orientConstraint(objA, objB, name = name + '_OCN',
                                              maintainOffset = maintainOffset)
                else:
                    if suffix:
                        if isinstance(objA, list):
                            ocn = cmds.orientConstraint(objA, objB, maintainOffset = maintainOffset)
                            ocn = cmds.rename(ocn[0], ocn[0].split('orientConstraint1')[0] 
                                              + suffix)
                        else:
                            ocn = cmds.orientConstraint(objA, objB,
                                                  maintainOffset = maintainOffset)
                            ocn = cmds.rename(ocn[0], ocn[0].split('orientConstraint1')[0] 
                                        + suffix)

                    else:
                        if isinstance(objA, list):
                            for a, b in zip(objA, objB):
                                ocn = cmds.orientConstraint(a, b, maintainOffset = maintainOffset)                    
                        else:
                            ocn = cmds.orientConstraint(objA, objB, maintainOffset = maintainOffset)
            else:
                raise Exception('Specified objB: ' + str(objB) + ' is not valid!')
        else:
            raise Exception('Specified objA: ' + str(objA) + ' is not valid!')
        return ocn
    #END def orientConstraint()

    def parentConstraint(self, 
                           objA = None, 
                           objB = None, 
                           name = None, 
                           suffix = None, 
                           maintainOffset = True,
                           lock = False):
        #--- this method creates a parentConstraint
        pac = []
        if objA:
            if objB:
                #--- unlock translate and rotate values
                if isinstance(objB, list):
                    for i in objB:
                        for axis in'xyz':
                            cmds.setAttr(i + '.t' + axis, lock = False)
                            cmds.setAttr(i + '.r' + axis, lock = False)
                else:
                    for axis in'xyz':
                        cmds.setAttr(objB + '.t' + axis, lock = False)                
                        cmds.setAttr(objB + '.r' + axis, lock = False)                
                if name:
                    if suffix:
                        if isinstance(objA, list):
                            if isinstance(objB, list):
                                for a, b in zip(objA, objB):
                                    pacs = cmds.parentConstraint(a, b, name = name + '_' + suffix,
                                                                 maintainOffset = maintainOffset)[0]
                                    pac.append(pacs)
                                    if lock:
                                        #--- lock constraint attributes
                                        for axis in 'xyz':
                                            cmds.setAttr(b + '.t' + axis, 
                                                         lock = True,
                                                         keyable = False)
                                            cmds.setAttr(b + '.r' + axis, 
                                                         lock = True,
                                                         keyable = False)                        
                            else:
                                pac = cmds.parentConstraint(objA, objB, maintainOffset = maintainOffset)
                                if lock:
                                    #--- lock constraint attributes
                                    for axis in 'xyz':
                                            cmds.setAttr(objB + '.t' + axis, 
                                                         lock = True,
                                                         keyable = False)
                                            cmds.setAttr(objB + '.r' + axis, 
                                                         lock = True,
                                                         keyable = False)
                        else:
                            pac = cmds.parentConstraint(objA, objB, name = name + '_' + suffix,
                                                  maintainOffset = maintainOffset)
                            if lock:
                                #--- lock constraint attributes
                                for axis in 'xyz':
                                        cmds.setAttr(objB + '.t' + axis, 
                                                     lock = True,
                                                     keyable = False)
                                        cmds.setAttr(objB + '.r' + axis, 
                                                     lock = True,
                                                     keyable = False) 
                    else:
                        if isinstance(objA, list):
                            if isinstance(objB, list):
                                for a, b in zip(objA, objB):
                                    pacs = cmds.parentConstraint(a, b, name = name + '_PAC',
                                                                 maintainOffset = maintainOffset)[0]
                                    pac.append(pacs)
                                    if lock:
                                        #--- lock constraint attributes
                                        for axis in 'xyz':
                                                cmds.setAttr(b + '.t' + axis, 
                                                             lock = True,
                                                             keyable = False)
                                                cmds.setAttr(b + '.r' + axis, 
                                                             lock = True,
                                                             keyable = False)
                        else:
                            pac = cmds.parentConstraint(objA, objB, name = name + '_PAC',
                                                        maintainOffset = maintainOffset)
                            if lock:
                                #--- lock constraint attributes
                                for axis in 'xyz':
                                        cmds.setAttr(objB + '.t' + axis, 
                                                     lock = True,
                                                     keyable = False)
                                        cmds.setAttr(objB + '.r' + axis, 
                                                     lock = True,
                                                     keyable = False) 
                else:
                    if suffix:
                        if isinstance(objA, list):
                            if isinstance(objB, list):
                                for a, b in zip(objA, objB):
                                    pacs = cmds.parentConstraint(a, b, maintainOffset = maintainOffset)
                                    pacs = cmds.rename(pac[0], 
                                                       pac[0].split('parentConstraint1')[0] 
                                                       + suffix)
                                    pac.append(pacs)                                
                                    if lock:
                                        #--- lock constraint attributes
                                        for axis in 'xyz':
                                                cmds.setAttr(b + '.t' + axis, 
                                                             lock = True,
                                                             keyable = False)
                                                cmds.setAttr(b + '.r' + axis, 
                                                             lock = True,
                                                             keyable = False) 
                            else:
                                pac = cmds.parentConstraint(objA, objB, maintainOffset = maintainOffset)
                                if lock:
                                    #--- lock constraint attributes
                                    for axis in 'xyz':
                                            cmds.setAttr(objB + '.t' + axis, 
                                                         lock = True,
                                                         keyable = False)
                                            cmds.setAttr(objB + '.r' + axis, 
                                                         lock = True,
                                                         keyable = False)                                
                        else:
                            pac = cmds.parentConstraint(objA, objB,
                                                        maintainOffset = maintainOffset)
                            pac = cmds.rename(pac[0], 
                                              pac[0].split('parentConstraint1')[0] 
                                              + suffix)
                            if lock:
                                #--- lock constraint attributes
                                for axis in 'xyz':
                                        cmds.setAttr(objB + '.t' + axis, 
                                                     lock = True,
                                                     keyable = False)
                                        cmds.setAttr(objB + '.r' + axis, 
                                                     lock = True,
                                                     keyable = False) 
                    else:
                        if isinstance(objA, list):
                            if isinstance(objB, list):
                                for a, b in zip(objA, objB):
                                    pacs = cmds.parentConstraint(a, b, maintainOffset = maintainOffset)[0]
                                    pac.append(pacs)
                                    if lock:
                                        #--- lock constraint attributes
                                        for axis in 'xyz':
                                                cmds.setAttr(b + '.t' + axis, 
                                                             lock = True,
                                                             keyable = False)
                                                cmds.setAttr(b + '.r' + axis, 
                                                             lock = True,
                                                             keyable = False) 
                            else:
                                pac = cmds.parentConstraint(objA, objB, maintainOffset = maintainOffset)
                                if lock:
                                    #--- lock constraint attributes
                                    for axis in 'xyz':
                                            cmds.setAttr(objB + '.t' + axis, 
                                                         lock = True,
                                                         keyable = False)
                                            cmds.setAttr(objB + '.r' + axis, 
                                                         lock = True,
                                                         keyable = False) 
                        else:
                            pac = cmds.parentConstraint(objA, objB, maintainOffset = maintainOffset)
                            if lock:
                                #--- lock constraint attributes
                                for axis in 'xyz':
                                        cmds.setAttr(objB + '.t' + axis, 
                                                     lock = True,
                                                     keyable = False)
                                        cmds.setAttr(objB + '.r' + axis, 
                                                     lock = True,
                                                     keyable = False) 
            else:
                raise Exception('Specified objB: ' + str(objB) + ' is not valid!')
        else:
            raise Exception('Specified objA: ' + str(objA) + ' is not valid!')
        return pac
    #END def parentConstraint()

    def particleSampler(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('particleSampler', name = name + '_' + suffix)
            else:
                cmds.createNode('particleSampler', name = name + '_PSA')
        else:
            cmds.createNode('particleSampler')
    #END def particleSampler()

    def place2dTexture(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('place2dTexture', name = name + '_' + suffix)
            else:
                cmds.createNode('place2dTexture', name = name + '_P2T')
        else:
            cmds.createNode('place2dTexture')
    #END def place2dTexture()

    def place3dTexture(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('place3dTexture', name = name + '_' + suffix)
            else:
                cmds.createNode('place3dTexture', name = name + '_P3T')
        else:
            cmds.createNode('place3dTexture')
    #END def place3dTexture()

    def plusMinusAverage(self, 
                           name = None, 
                           suffix = None,
                           operation = 1,
                           lockAttr = None):
        #--- this method creates a plusMinusAverage node
        if name:
            if suffix:
                pma = cmds.createNode('plusMinusAverage', name = name + '_' + suffix)
            else:
                pma = cmds.createNode('plusMinusAverage', name = name + '_PMA')
        else:
            pma = cmds.createNode('plusMinusAverage')
        #--- take care of the node's settings
        if operation:
            #--- operation
            cmds.setAttr(pma + '.operation', int(operation))
        #--- lock specified attribute
        if lockAttr:
            if isinstance(lockAttr, list):
                for i in lockAttr:
                    cmds.setAttr(pma + '.' + i, lock = True)
            else:
                cmds.setAttr(pma + '.' + lockAttr, lock = True)        
        return pma
    #END def plusMinusAverage()

    def pointConstraint(self, 
                          objA = None, 
                          objB = None, 
                          name = None, 
                          suffix = None, 
                          maintainOffset = True,
                          lock = False):
        #--- this method creates a pointConstraint
        if objA:
            if objB:
                #--- unlock translate values
                if isinstance(objB, list):
                    for i in objB:
                        for axis in'xyz':
                            cmds.setAttr(i + '.t' + axis, lock = False)
                else:
                    for axis in'xyz':
                        cmds.setAttr(objB + '.t' + axis, lock = False)
                if name:
                    if suffix:
                        if isinstance(objB, list):
                            for a, b in zip(objA, objB):
                                pcn = cmds.pointConstraint(a, b, 
                                                           name = name + '_' + suffix,
                                                           maintainOffset = maintainOffset)
                                if lock:
                                    #--- lock constraint attributes
                                    for axis in 'xyz':
                                        cmds.setAttr(b + '.t' + axis, 
                                                     lock = True,
                                                     keyable = False)
                        else:
                            pcn = cmds.pointConstraint(objA, 
                                                       objB, 
                                                       name = name + '_' + suffix,
                                                       maintainOffset = maintainOffset)
                            if lock:
                                #--- lock constraint attributes
                                for axis in 'xyz':
                                    cmds.setAttr(objB + '.t' + axis, 
                                                 lock = True,
                                                 keyable = False)
                    else:
                        if isinstance(objB, list):
                            for a, b in zip(objA, objB):
                                pcn = cmds.pointConstraint(a, b, 
                                                           name = name + '_PCN',
                                                           maintainOffset = maintainOffset)
                                if lock:
                                    #--- lock constraint attributes
                                    for axis in 'xyz':
                                        cmds.setAttr(b + '.t' + axis, 
                                                     lock = True,
                                                     keyable = False)
                        else:
                            pcn = cmds.pointConstraint(objA, 
                                                       objB, 
                                                       name = name + '_PCN',
                                                       maintainOffset = maintainOffset)
                            if lock:
                                #--- lock constraint attributes
                                for axis in 'xyz':
                                    cmds.setAttr(objB + '.t' + axis, 
                                                 lock = True,
                                                 keyable = False)
                else:
                    if suffix:
                        if isinstance(objB, list):
                            for a, b in zip(objA, objB):
                                pcn = cmds.pointConstraint(a, b, maintainOffset = maintainOffset)
                                pcn = cmds.rename(pcn[0], pcn[0].split('pointConstraint1')[0] 
                                            + suffix)
                                if lock:
                                    #--- lock constraint attributes
                                    for axis in 'xyz':
                                        cmds.setAttr(b + '.t' + axis, 
                                                     lock = True,
                                                     keyable = False)
                        else:
                            pcn = cmds.pointConstraint(objA, 
                                                       objB,
                                                       maintainOffset = maintainOffset)
                            pcn = cmds.rename(pcn[0], pcn[0].split('pointConstraint1')[0] 
                                              + suffix)
                            if lock:
                                #--- lock constraint attributes
                                for axis in 'xyz':
                                    cmds.setAttr(objB + '.t' + axis, 
                                                 lock = True,
                                                 keyable = False)                            
                    else:
                        if isinstance(objB, list):
                            for a, b in zip(objA, objB):
                                pcn = cmds.pointConstraint(a, b, maintainOffset = maintainOffset)                    
                                if lock:
                                    #--- lock constraint attributes
                                    for axis in 'xyz':
                                        cmds.setAttr(b + '.t' + axis, 
                                                     lock = True,
                                                     keyable = False)
                        else:
                            pcn = cmds.pointConstraint(objA, 
                                                       objB, 
                                                       maintainOffset = maintainOffset)
                            if lock:
                                #--- lock constraint attributes
                                for axis in 'xyz':
                                    cmds.setAttr(objB + '.t' + axis, 
                                                 lock = True,
                                                 keyable = False)
            else:
                raise Exception('Specified objB: ' + str(objB) + ' is not valid!')
        else:
            raise Exception('Specified objA: ' + str(objA) + ' is not valid!')
        return pcn
    #END def pointConstraint()

    def pointMatrixMult(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('pointMatrixMult', name = name + '_' + suffix)
            else:
                cmds.createNode('pointMatrixMult', name = name + '_PMM')
        else:
            cmds.createNode('pointMatrixMult')
    #END def pointMatrixMult()

    def pointOnCurveInfo(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('pointOnCurveInfo', name = name + '_' + suffix)
            else:
                cmds.createNode('pointOnCurveInfo', name = name + '_PCI')
        else:
            cmds.createNode('pointOnCurveInfo')
    #END def pointOnCurveInfo()

    def pointOnSurfaceInfo(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('pointOnSurfaceInfo', name = name + '_' + suffix)
            else:
                cmds.createNode('pointOnSurfaceInfo', name = name + '_PSI')
        else:
            cmds.createNode('pointOnSurfaceInfo')
    #END def pointOnSurfaceInfo()

    def pointOnPolyConstraint(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('pointOnPolyConstraint', name = name + '_' + suffix)
            else:
                cmds.createNode('pointOnPolyConstraint', name = name + '_PPC')
        else:
            cmds.createNode('pointOnPolyConstraint')
    #END def pointOnPolyConstraint()

    def poleVectorConstraint(self, 
                               objA = None,
                               objB = None, 
                               name = None, 
                               suffix = None):
        if objA:
            if objB:
                if name:
                    if suffix:
                        if isinstance(objB, list):
                            for a, b in zip(objA, objB):
                                pvc = cmds.poleVectorConstraint(a, b, name = name + '_' + suffix)
                        else:
                            pvc = cmds.poleVectorConstraint(objA, objB, name = name + '_' + suffix)
                    else:
                        if isinstance(objB, list):
                            for a, b in zip(objA, objB):
                                pvc = cmds.poleVectorConstraint(a, b, name = name + '_PVC')
                        else:
                            pvc = cmds.poleVectorConstraint(objA, objB, name = name + '_PVC')
                else:
                    if suffix:
                        if isinstance(objB, list):
                            for a, b in zip(objA, objB):
                                pvc = cmds.poleVectorConstraint(a, b)
                                pvc = cmds.rename(pvc[0], pvc[0].split('poleVectorConstraint1')[0] 
                                            + suffix)
                        else:
                            pvc = cmds.poleVectorConstraint(objA, objB)
                            pvc = cmds.rename(pvc[0], pvc[0].split('poleVectorConstraint1')[0] 
                                        + suffix)
                    else:
                        if isinstance(objB, list):
                            for a, b in zip(objA, objB):
                                pvc = cmds.poleVectorConstraint(a, b)                    
                        else:
                            pvc = cmds.poleVectorConstraint(objA, objB)
            else:
                raise Exception('Specified objB: ' + str(objB) + ' is not valid!')
        else:
            raise Exception('Specified objA: ' + str(objA) + ' is not valid!')
        return pvc
    #END def poleVectorConstraint()

    def projection(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('projection', name = name + '_' + suffix)
            else:
                cmds.createNode('projection', name = name + '_PRJ')
        else:
            cmds.createNode('projection')
    #END def projection()

    def quadSwitch(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('quadSwitch', name = name + '_' + suffix)
            else:
                cmds.createNode('quadSwitch', name = name + '_QSW')
        else:
            cmds.createNode('quadSwitch')
    #END def quadSwitch()

    def remapColor(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('remapColor', name = name + '_' + suffix)
            else:
                cmds.createNode('remapColor', name = name + '_RMC')
        else:
            cmds.createNode('remapColor')
    #END def remapColor()

    def remapHsv(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('remapHsv', name = name + '_' + suffix)
            else:
                cmds.createNode('remapHsv', name = name + '_RMH')
        else:
            cmds.createNode('remapHsv')
    #END def remapHsv()

    def remapValue(self, 
                    name = None, 
                    suffix = None,
                    inputValue = 0, 
                    inputMin = 0, 
                    inputMax = 1,
                    outputMin = 0,
                    outputMax = 1,
                    lockAttr = None):
        #--- this method creates a remapValue node
        if name:
            if suffix:
                rmv = cmds.createNode('remapValue', name = name + '_' + suffix)
            else:
                rmv = cmds.createNode('remapValue', name = name + '_RMV')
        else:
            rmv = cmds.createNode('remapValue')
        #--- take care of the node's settings
        if inputValue:
            #--- inputValue
            cmds.setAttr(rmv + '.inputValue', float(inputValue))
        if inputMin:
            #--- inputMin
            cmds.setAttr(rmv + '.inputMin', float(inputMin))
        if inputMax:
            #--- inputMax
            cmds.setAttr(rmv + '.inputMax', float(inputMax))
        if outputMin:
            #--- outputMin
            cmds.setAttr(rmv + '.outputMin', float(outputMin))
        if outputMax:
            #--- outputMax
            cmds.setAttr(rmv + '.outputMax', float(outputMax))
        #--- lock specified attribute
        if lockAttr:
            if isinstance(lockAttr, list):
                for i in lockAttr:
                    cmds.setAttr(rmv + '.' + i, lock = True)
            else:
                cmds.setAttr(rmv + '.' + lockAttr, lock = True) 
        return rmv
    #END def remapValue()

    def reverse(self, 
                 name = None, 
                 suffix = None,
                 inputX = 0,
                 inputY = 0,
                 inputZ = 0,
                 lockAttr = None):
        #--- this method creates a reverse node
        if name:
            if suffix:
                rev = cmds.createNode('reverse', name = name + '_' + suffix)
            else:
                rev = cmds.createNode('reverse', name = name + '_REV')
        else:
            rev = cmds.createNode('reverse')
        #--- take care of the node's settings
        if inputX:
            #--- inputX
            cmds.setAttr(rev + '.inputX', float(inputX))
        if inputY:
            #--- inputY
            cmds.setAttr(rev + '.inputY', float(inputY))
        if inputZ:
            #--- inputZ
            cmds.setAttr(rev + '.inputZ', float(inputZ))
        #--- lock specified attribute
        if lockAttr:
            if isinstance(lockAttr, list):
                for i in lockAttr:
                    cmds.setAttr(rev + '.' + i, lock = True)
            else:
                cmds.setAttr(rev + '.' + lockAttr, lock = True)        
        return rev
    #END def reverse()

    def rgbToHsv(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('rgbToHsv', name = name + '_' + suffix)
            else:
                cmds.createNode('rgbToHsv', name = name + '_R2H')
        else:
            cmds.createNode('rgbToHsv')
    #END def rgbToHsv()

    def samplerInfo(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('samplerInfo', name = name + '_' + suffix)
            else:
                cmds.createNode('samplerInfo', name = name + '_SMP')
        else:
            cmds.createNode('samplerInfo')
    #END def samplerInfo()

    def scaleConstraint(self, 
                          objA = None, 
                          objB = None, 
                          name = None, 
                          suffix = None, 
                          maintainOffset = True):
        #--- create a scaleConstraint
        if objA:
            if objB:
                if name:
                    if suffix:
                        if isinstance(objB, list):
                            for a, b in zip(objA, objB):
                                scn = cmds.scaleConstraint(a, b, 
                                                           name = name + '_' + suffix,
                                                           maintainOffset = maintainOffset)
                        else:
                            scn = cmds.scaleConstraint(objA, objB, 
                                                       name = name + '_' + suffix,
                                                       maintainOffset = maintainOffset)
                    else:
                        if isinstance(objB, list):
                            for a, b in zip(objA, objB):
                                scn = cmds.scaleConstraint(a, b, 
                                                           name = name + '_SCN',
                                                           maintainOffset = maintainOffset)
                        else:
                            scn = cmds.scaleConstraint(objA, objB, 
                                                       name = name + '_SCN',
                                                       maintainOffset = maintainOffset)
                else:
                    if suffix:
                        if isinstance(objB, list):
                            for a, b in zip(objA, objB):
                                scn = cmds.scaleConstraint(a, b, 
                                                           maintainOffset = maintainOffset)
                                scn = cmds.rename(scn[0], 
                                                  scn[0].split('scaleConstraint1')[0] 
                                                  + suffix)
                        else:
                            scn = cmds.scaleConstraint(objA, objB,
                                                       maintainOffset = maintainOffset)
                            scn = cmds.rename(scn[0], scn[0].split('scaleConstraint1')[0] 
                                        + suffix)
                    else:
                        if isinstance(objB, list):
                            for a, b in zip(objA, objB):
                                scn = cmds.scaleConstraint(a, b, 
                                                           maintainOffset = maintainOffset)                    
                        else:
                            scn = cmds.scaleConstraint(objA, objB, 
                                                       maintainOffset = maintainOffset)
            else:
                raise Exception('Specified objB: ' + str(objB) + ' is not valid!')
        else:
            raise Exception('Specified objA: ' + str(objA) + ' is not valid!')
        return scn
    #END def scaleConstraint()

    def setRange(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('setRange', name = name + '_' + suffix)
            else:
                cmds.createNode('setRange', name = name + '_SRA')
        else:
            cmds.createNode('setRange')
    #END def setRange()

    def singleSwitch(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('singleSwitch', name = name + '_' + suffix)
            else:
                cmds.createNode('singleSwitch', name = name + '_SSW')
        else:
            cmds.createNode('singleSwitch')
    #END def singleSwitch()

    def stencil(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('stencil', name = name + '_' + suffix)
            else:
                cmds.createNode('stencil', name = name + '_STE')
        else:
            cmds.createNode('stencil')
    #END def stencil()

    def surfaceInfo(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('surfaceInfo', name = name + '_' + suffix)
            else:
                cmds.createNode('surfaceInfo', name = name + '_SFI')
        else:
            cmds.createNode('surfaceInfo')
    #END def surfaceInfo()

    def surfaceLuminance(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('surfaceLuminance', name = name + '_' + suffix)
            else:
                cmds.createNode('surfaceLuminance', name = name + '_SLU')
        else:
            cmds.createNode('surfaceLuminance')
    #END def surfaceLuminance()

    def transform(self, name = None, suffix = None, position = None, parent = None):
        #--- this method creates a transform node
        if name:
            if suffix:
                if parent:
                    trn = cmds.createNode('transform', name = name + '_' + suffix,
                                    parent = parent)
                else:
                    trn = cmds.createNode('transform', name = name + '_' + suffix)
            else:
                if parent:
                    trn = cmds.createNode('transform', name = name, parent = parent)
                else:
                    trn = cmds.createNode('transform', name = name)
        else:
            if parent:
                trn = cmds.createNode('transform', parent = parent)
            else:
                trn = cmds.createNode('transform')
        if position:
            cmds.xform(trn, translation = position, worldSpace = True)  
        return trn
    #END def transform()

    def transposeMatrix(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('transposeMatrix', name = name + '_' + suffix)
            else:
                cmds.createNode('transposeMatrix', name = name + '_TMX')
        else:
            cmds.createNode('transposeMatrix')
    #END def transposeMatrix()

    def tripleSwitch(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('tripleSwitch', name = name + '_' + suffix)
            else:
                cmds.createNode('tripleSwitch', name = name + '_TRI')
        else:
            cmds.createNode('tripleSwitch')
    #END def tripleSwitch()

    def unitConversion(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('unitConversion', name = name + '_' + suffix)
            else:
                cmds.createNode('unitConversion', name = name + '_UNI')
        else:
            cmds.createNode('unitConversion')
    #END def unitConversion()

    def vectorProduct(self, name = None, suffix = None):
        if name:
            if suffix:
                cmds.createNode('vectorProduct', name = name + '_' + suffix)
            else:
                cmds.createNode('vectorProduct', name = name + '_VCP')
        else:
            cmds.createNode('vectorProduct')
    #END def vectorProduct()
#END class Node()