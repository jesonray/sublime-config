import sublime, sublime_plugin
import datetime

class InsertDateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("insert_snippet", {"contents": datetime.datetime.now().strftime("%Y-%m-%d")})
