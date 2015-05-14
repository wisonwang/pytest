import wx
import os
import sys

class TreeItemData(wx.TreeItemData):
    strValue = ''
    def __init__(self, strValue):
        wx.TreeItemData.__init__(self)
        self.strValue = strValue

    def getStringValue(self):
        return self.strValue

    def setStringValue(self, strValue):
        self.strValue = strValue

class MyTreeViewer(wx.TreeCtrl):
    projects = []#filepath list
    imglist = []
    
    
    '''
    @params parent, point, size, style wx.Point(0, 0), wx.Size(160, 250),
                           wx.TR_DEFAULT_STYLE | wx.NO_BORDER
    '''
    def __init__(self, parent, identity, point, size, style):
        wx.TreeCtrl.__init__(self, parent, identity, point, size, style)
        self.imglist = wx.ImageList(16, 16, True, 2)
        self.imglist.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16,16)))
        self.imglist.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16,16)))
        

    def add_project(self, path):
        if not os.path.exists(path):
            return False
        if path not in self.projects:
            self.projects.append(path)
        self.root = self.AddRoot(os.path.basename(path))
        #self.root = self.AddRoot(text = "root")
        self.SetItemData(item = self.root, data = TreeItemData(path))
        
        self.addPathItem(self.root, path)
                
        self.Expand(self.root)
        self.AssignImageList(self.imglist)

        return True

    def addPathItem(self, rootItem, filePath):
        if not os.path.exists(filePath):
            return ;
        for f in os.listdir(filePath):
            f = os.path.join(filePath, f)
            if os.path.isdir(f):
                item = self.appendItem(rootItem, os.path.basename(f), 0)
                addPathItem(item, f)
                self.SetItemData(item = item, data = f)
            else:
                item = self.AppendItem(rootItem, os.path.basename(f), 1)
                self.SetItemData(item = item, data = TreeItemData(f))
        
    def refresh(self):
        #self.RemoveChild()
        return 