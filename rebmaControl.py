# encoding: utf-8

from gevent import pool
import requests
import npyscreen


class RebMaControl:
	def __init__(self, repoListUrl):
		self.repoList = [("Cowboy", "1.0.0", "github.com/bla/cowboy")]

		repoPathList = [item
				for item in requests.get(repoListUrl, timeout=20).content.split("\n")
				if item.startswith("github.com")]
			#get list of repo urls'

		repoUrlList = ['https://api.github.com/repos/{0}'.format(item[11:]) for item in repoPathList]	
			#build valid github api url

		p = pool.Pool(20)
		repoResponseList = p.map(requests.get, repoUrlList)

		self.repoList = [ (str(request.json()["name"]), str(version), str(request.json()["description"]))
				for request in repoResponseList
				for version in 
					[ item["name"]
						for item in requests.get('{0}/branches'.format(request.url)).json()
					] +
					[ item["name"]
						for item in requests.get('{0}/tags'.format(request.url)).json()
					]
				]
		
	def get_repoList(self):
		return self.repoList

