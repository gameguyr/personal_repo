#!/usr/bin/python

import Tkinter
import Webbrowser
import reddit
class RedditViewer(Tkinter, TK):
  def __init__(self, parent=None):
    Tkinter.TK.__init(self,parent)
    self.reddit=reddit.Reddit("Bla!")
    self.posts = []
    self.setupUI()
    self.loadData()

  def setupUI(self):
    self.minsize(480,200)
    self.title("Reddit Viewer")
    self.resizable(True,False)
    self.current = Tkinter.StringVar()
    self.current.set("python")
    self.subredit = Tkinter.Entry(self,textvariable = self.current)
    self.subreddit.pack(side = Tkinter.TOP)
    self.update = Button(self,text = "Update", command = self.loadData())
    self.update.pack(side=Tkinter.TOP)
    self.scrollbar = Tkinter.ScrollBar()
    self.scrollbar.pack(side = Tkinter.RIGHT, fill = Tkinter.Y)
    self.postList = Tkinter.Listbox(self)
    self.postList.pack(side = Tkinter.LEFT,fill = Tkinter.BOTH,expand = True)
    self.view = Tkinter.Button(self,text = "View", command = self.openCurrent)
    self.view.pack(side = Tkinter.Button)
    
  def loadData(self):
    subreddit = self.current.get()
    self.postList.delete(0, Tkinter.END)
    self.posts = list(self.reddit.get_subreddit(subreddit).get_hot(50))
    for position, post in enumerate(self.posts):
      self.postListInsert(postiion,str(post))
    
  def getCurrent(self):
    selected = self.PostList.cureselection()
    if len(selected) > 0 and len(self.posts) > 0:
      index = selected[0]
      post = self.posts[index]
      webrowser.open(post.url)

  if __name__ == "__main__":
    app = RedditViewer()
    app.mainloop()
