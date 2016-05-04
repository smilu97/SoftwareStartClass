import wx

class TestFrame(wx.Frame) :
	def __init__(self, parent, id, title) :
		wx.Frame.__init__(self,parent,id,title,wx.DefaultPosition, wx.Size(300,400))
		panel = wx.Panel(self,-1,(0,0),(300,400),style=wx.SUNKEN_BORDER)
		self.picture = wx.StaticBitmap(panel)
		panel.SetBackgroundColour(wx.WHITE)
		self.picture.SetFocus()
		self.picture.SetBitmap(wx.Bitmap('images/apollo.bmp'))

class TestApp(wx.App) :
	def OnInit(self) :
		frame = TestFrame(None, -1, 'Apollo Image')
		frame.CenterOnScreen()

		StatusBar = frame.CreateStatusBar()
		StatusBar.SetStatusText('StatusBar')

		MenuBar = wx.MenuBar()
		menu = wx.Menu()
		menu.Append(wx.ID_EXIT, 'E&xit\tAlt-X', 'exit')
		MenuBar.Append(menu, 'file')

		menu1 = wx.Menu()
		menu1.Append(200, 'Test', 'testmenu')
		menu1.Append(201, 'Copy', 'copy')
		menu1.Append(202, 'Paste', 'paste')
		MenuBar.Append(menu1, 'edit')
		frame.SetMenuBar(MenuBar)

		frame.Show(True)
		return True

app = TestApp(0)
app.MainLoop()