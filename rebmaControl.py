# encoding: utf-8


class RebMaControl:
	@staticmethod
	def createErlAppAndRel():
		das  = "test1\n"
		das += "test2\n"
		das += "test3\n"
		return das

class RebMaDep:
	@staticmethod
	def getList():
		return [("Cowboy", "2.0.0"), ("Lager", "1.0.0"), ("mimetypes", "1.1.2")]


