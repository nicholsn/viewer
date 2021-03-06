import CompareVolumes
import viewerUtilities
import argparse

parser = argparse.ArgumentParser( description="A 3D viewer of a single or multiple MRs" )
parser.add_argument( "-f", "--foreground",  nargs='+', required=True, help="Images shown in foreground.", action="append")
parser.add_argument( "-b", "--background",  nargs='*', required=False, help="Images shown in background.", action="append")
parser.add_argument( "-l", "--labelmap",  nargs='*', required=False, help="File name of Label maps", action="append")
parser.add_argument( "-4", "--fourD", required=False, help="Load in 4D image sequence.", action="store_true", default = False )
parser.add_argument( "-n", "--window_name", required=False, help="Window name", action="store", default = "Viewer")
parser.add_argument( "-o", "--orientation", required=False, help="View orientation (Axial, Sagittal, Coronal)", action="store", default = "Axial")

args = parser.parse_args()
fourDFlag=args.fourD

#
# Load Volume 
#
(fgNodeList,fgImageList,missingList) = viewerUtilities.loadVolumes(args.foreground,0,fourDFlag)
(bgNodeList,bgImageList,missingList) = viewerUtilities.loadVolumes(args.background,0,fourDFlag)
(lmNodeList,lmImageList,missingList) = viewerUtilities.loadVolumes(args.labelmap,1,fourDFlag)

# https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py
cvLogic=CompareVolumes.CompareVolumesLogic()
sliceNodeList = cvLogic.viewerPerVolume(volumeNodes=fgNodeList,background=bgNodeList,label=lmNodeList,orientation=args.orientation)

cpWidget=viewerUtilities.CtrlPanelWidget(sliceNodeList,None,fgNodeList,fgImageList,bgNodeList,bgImageList,lmNodeList,lmImageList,args.orientation)
ctrlWin = cpWidget.setup(args.window_name,"")
ctrlWin.show()

#sWidget = slicer.qMRMLSliceWidget()
#sWidget.setMRMLScene(slicer.mrmlScene)

#layoutManager = slicer.app.layoutManager()
#viewName = fgNodeList[0].GetName() + '-Axial'
#sliceWidget = layoutManager.sliceWidget(viewName)
#sliceWidget.sliceController().setSliceLink(1)

#sliceNodes = slicer.util.getNodes('vtkMRMLSliceNode*')
#layoutManager = slicer.app.layoutManager()
#for sliceNode in sliceNodes.values():
#  sliceWidget = layoutManager.sliceWidget(sliceNode.GetLayoutName())
#  if sliceWidget:  
#      print sliceNode.GetName()
#      sliceWidget.sliceController().setSliceLink(1)

#sliceNode = sliceWidget.mrmlSliceNode()
#sliceNode.SetOrientation(orientation)

#orientations = ('Axial', 'Sagittal', 'Coronal')


# window does not come up for some reason if we do not do it that way 

#

 
# Debug stuff 
# slicer.util.saveScene('/tmp/scene.mrml')
# dir(foregroundNode) returns all functions 
# [s for s in dir(blub) if "Get" in s]

# class MarkupsInViewsSelfTestWidget:
