# encoding: utf-8

from gevent import pool
import requests
import npyscreen
import pickle
import os.path
import time


class RebMaControl:
	def __init__(self, repoListUrl):
		self.dumpFileName_repo = "./.repoList.bin"
		self.repoListUrl = repoListUrl
		try:
			if (os.path.isfile(self.dumpFileName_repo) and time.time() - os.path.getmtime(self.dumpFileName_repo) < 3600):
				self.repoList = self.readRepoListDump(self.dumpFileName_repo)
			else:
				self.repoList = self.readRepoListSource(self.repoListUrl)
				self.writeRepoListDump(self.repoList, self.dumpFileName_repo)
		except:
			self.repoList = []
		
	def readRepoListDump(self, dumpFileName_repo):
		dumpFile_repo = open(dumpFileName_repo, 'rb')
		return pickle.load(dumpFile_repo)

	def readRepoListSource(self, repoListUrl):
		repoPathList = [item
				for item in requests.get(repoListUrl, timeout=20).content.split("\n")
				if item.startswith("github.com")]
			#get list of repo urls'
		
		repoUrlList = ['https://api.github.com/repos/{0}'.format(item[11:]) for item in repoPathList]	
			#build valid github api url
		
		p = pool.Pool(20)
		repoResponseList = p.map(requests.get, repoUrlList)
		
		repoList = [ (
			str(request.json()["name"]),
			str(version),
			str(request.json()["description"]),
			str(request.json()["html_url"])
			)
			for request in repoResponseList
			for version in 
				[ item["name"]
					for item in requests.get('{0}/branches'.format(request.url)).json()
				] +
				[ item["name"]
					for item in requests.get('{0}/tags'.format(request.url)).json()
				]
			]
		return repoList

	def writeRepoListDump(self, repoList, dumpFileName_repo):
		dumpFile_repo = open(dumpFileName_repo, 'wb')
		pickle.dump(repoList, dumpFile_repo)

	def get_repoList(self):
		return self.repoList

