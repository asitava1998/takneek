import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()
        
        self.set_title("Motor")
        self.set_default_size(400, 300)
        self.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color(0,40535,40000))
        self.set_position(gtk.WIN_POS_CENTER)

        self.image=gtk.gdk.pixbuf_new_from_file_at_size("download.jpg",150,100)
        image1=gtk.Image();
        image1.set_from_pixbuf(self.image)

        self.label = gtk.Label("Set the rpm:")
        self.entry = gtk.Entry()

        self.btn1=gtk.Button("  Start  ")
        self.btn2=gtk.Button("  Stop  ")
        self.btn3=gtk.Button("  Quit  ")
        self.btn3.connect("clicked",gtk.main_quit)

        buttons=gtk.Fixed()
        buttons.put(image1,125,10)
        buttons.put(self.label,150,130)
        buttons.put(self.entry,120,160)
        buttons.put(self.btn1,140,200)
        buttons.put(self.btn2,210,200)
        buttons.put(self.btn3,20,260)


        self.add(buttons)
        self.show_all()

PyApp()
gtk.main()