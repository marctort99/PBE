import codigo_base
import sys 
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class EntryWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Puzzle 2")
        self.set_size_request(400, 200)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        self.add(vbox)
        
        fbox = Gtk.Label(label="Escriba un texto de hasta 4 líneas con 20 caracteres")
        vbox.pack_start(fbox, True, True, 0)
        
        self.entry = Gtk.TextView()
        vbox.pack_start(self.entry, True, True, 0)

        hbox = Gtk.Box(spacing=2)
        vbox.pack_start(hbox, True, True, 0)

        self.check_editable = Gtk.CheckButton(label="Editable")
        self.check_editable.connect("toggled", self.on_editable_toggled)
        self.check_editable.set_active(True)
        hbox.pack_start(self.check_editable, True, True, 0)
        
        self.button = Gtk.Button(label="Imprimir")
        self.button.connect("clicked", self.on_button_clicked)
        hbox.pack_start(self.button, True, True, 0)
        
    def on_button_clicked(self, widget):
            codigo_base.main(self.entry.get_buffer().get_text(self.entry.get_buffer().get_start_iter(), self.entry.get_buffer().get_end_iter(), True))
            print(self.entry.get_buffer().get_text(self.entry.get_buffer().get_start_iter(), self.entry.get_buffer().get_end_iter(), True))    

    def on_editable_toggled(self, button):
        value = button.get_active()
        self.entry.set_editable(value)



win = EntryWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()