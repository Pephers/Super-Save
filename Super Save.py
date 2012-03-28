import sublime, sublime_plugin
import os, stat

class SuperSave(sublime_plugin.EventListener):
    def on_post_save(self, view):
        filename = view.file_name()
        os.chmod(filename, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH)