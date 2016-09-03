import gtk
string=""
class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()
        
        self.set_title("Device Centre")
        self.set_default_size(400, 300)
        self.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color(0,40535,40000))
        self.set_position(gtk.WIN_POS_CENTER)

        self.image=gtk.gdk.pixbuf_new_from_file_at_size("images.jpg",150,100)
        image1=gtk.Image();
        image1.set_from_pixbuf(self.image)

        self.label = gtk.Label("Select the device to configure")


        self.combo_box=gtk.combo_box_new_text()
        self.combo_box.connect("changed",self.on_changed)
        self.combo_box.append_text("Motor")
        self.combo_box.append_text("LED")

        self.btn1=gtk.Button("Go")
        self.btn1.connect("clicked",self.go)

        self.btn2=gtk.Button("Exit")
        self.btn2.connect("clicked",gtk.main_quit)

        buttons=gtk.Fixed()
        buttons.put(image1,125,10)
        buttons.put(self.label,100,100)
        buttons.put(self.combo_box,160,140)
        buttons.put(self.btn1,185,190)
        buttons.put(self.btn2,340,260)

        self.add(buttons)
        self.show_all()

    def on_changed(self, widget):
        global string
        string = widget.get_active_text()
        
    def go(self,widget):
        print string
        if string == "Motor":
            import motor.py 
        elif string == "LED":
            import led.py     

PyApp()
gtk.main()
