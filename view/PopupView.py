import TKinterModernThemes as TKMT
class PopupView(TKMT.ThemedTKinterFrame):
    def __init__(self, message: str, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
        super().__init__("TITLE", theme, mode, usecommandlineargs, usethemeconfigfile)

        self.Text(message)

        # self.newVideoTitle = tk.StringVar(value="")
        # self.newVideoURL = tk.StringVar(value="")
        # self.newVideoAnnotationPath = tk.StringVar(value="")
        
        # self.setActiveCol(0)
        # # self.startFrame = self.parent.addLabelFrame("Start", padx=(0,1), pady=(0,1))
        # self.urlFrame = self.addLabelFrame("Video URL")
        # self.urlFrame.Entry(self.newVideoURL, widgetkwargs={"width": 80})
        # self.titleFrame = self.addLabelFrame("Title")
        # self.titleFrame.Entry(self.newVideoTitle, widgetkwargs={"width": 80})
        # self.annotationPathFrame = self.addLabelFrame("Annotation Path")
        # self.annotationPathFrame.Entry(self.newVideoAnnotationPath, widgetkwargs={"width": 80})
        # self.Button("Save", self.save)
        self.Button("Ok", self.cancel)
        self.run()

    
    # def save(self):
    #     # print("newVideoAnnotationPath", self.newVideoAnnotationPath.get())
    #     # print("newVideoTitle", self.newVideoTitle.get())
    #     self.titleView.initiateNewProject(videoURL=self.newVideoURL.get(), videoTitle=self.newVideoTitle.get(), annotationPath=self.newVideoAnnotationPath.get())
    #     self.root.destroy()
    
    def cancel(self):
        self.root.destroy()