import argparse
import viewerUtilities
import liteViewer
 
parser = argparse.ArgumentParser( description="Fast 2D viewer for single 3D+t MRs (fg,bg,labelmap)" )
parser.add_argument( "-f", "--foreground", nargs="+", required=True, help="MR file shown in foreground.", action="append")
parser.add_argument( "-b", "--background", nargs='*', required=False, help="MR file shown in background.", action="append")
parser.add_argument( "-l", "--labelmap", nargs='*', required=False, help="MR File of Label map", action="append")
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

if len(bgNodeList) :
     bgNode= bgNodeList[0]
else: 
     bgNode= None

if len(lmNodeList) :
     lmNode= lmNodeList[0]
else: 
     lmNode= None

sliceWidget=liteViewer.createViewer("TEST",fgNodeList[0], bgNode, lmNode)
cpWidget=viewerUtilities.CtrlPanelWidget("",sliceWidget,fgNodeList,fgImageList,bgNodeList,bgImageList,lmNodeList,lmImageList,args.orientation)
cpWidget.setup(args.window_name,sliceWidget)
## window does not come up for some reason if we do not do it that way 
sliceWidget.show()

# Debug stuff 
# slicer.util.saveScene('/tmp/scene.mrml')
# dir(foregroundNode) returns all functions 
# [s for s in dir(blub) if "Get" in s]

# class MarkupsInViewsSelfTestWidget:
