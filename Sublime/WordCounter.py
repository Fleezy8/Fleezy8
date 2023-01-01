import sublime
import sublime_plugin

class WordCounter(sublime_plugin.TextCommand):
	def run(self, edit):
		""" Count all words/numbers in a file """
		words = self.view.find_all(r"\w+\.\w+|\w+")
		word_count = len(words)
		sublime.status_message("Words: " + str(word_count))

class LiveWordCounter(sublime_plugin.ViewEventListener):
	""" Show a live view of the word count """

	def _count_words(self):
		""" Count all words/numbers in a file """
		words = self.view.find_all(r"\w+\.\w+|\w+")
		word_count = len(words)
		return word_count

	def on_load_async(self):
		sublime.status_message("Words: " + str(self._count_words()))

	def on_modified_async(self):	
		sublime.status_message("Words: " + str(self._count_words()))

	def on_activated_async(self):	
		sublime.status_message("Words: " + str(self._count_words()))	

	def on_post_save(self):	
		sublime.status_message("Words: " + str(self._count_words()))

	def on_close(self):
		sublime.status_message("Words: " + str(self._count_words()))
    