#!/usr/bin/env python
import pygtk
import gtk


class MyProgram:
 
    def __init__(self):
        # create a new window
        app_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        app_window.set_title("MyProgram title")

        app_window.show()
        return


def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    MyProgram()
    main()