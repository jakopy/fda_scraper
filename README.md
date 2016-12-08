==============
THE PURPOSE
==============
	-Add drug data to an existing application (NCLEX study aid)
	-Experiment with python queues and asynchronous code
	-Quickly gather large amounts of data
==============
THE SCRAPE
==============
		       Num of Pages  Time to Scrape
	Scrape 1 |     905     |  ~145 seconds  
	Scrape 2 |    75921    |  ~50 minutes

FDA Scrape Project was completed over a series of 2 scrape steps and 2 parsing sessions a brief description of the process is provided below

	Scrape 1
		initiated to gather all drug names with their corresponding set ids
		Asyncio and aiohttp were used to scrape this information
		aiohttp is non-blocking
		asyncio is the newest form of asynchronous python
	Scrape 1 Parse Session
		Extract all setids for 2nd scrape session
	Scrape 2
		initiated to gather detailed information corresponding with the drug names
		requests was used which is blocking
		requests blocks the main event loop in asyncio, however if requests is used in conjunction
		with Python Queue and Thread library it becomes non-blocking.
		It is documented that if the request library is used and it is run on seperate threads the overall job becomes
		asynchronous. See here: http://stackoverflow.com/questions/14245989/python-requests-non-blocking
		Also note here that requests is blocking: https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html
		Without the use of queues and doing requests in a for loop we can gather approximately 4.6 pages in a second
		With the use of queues and threading using the requests library we can gather approximately 30 pages in a second
		Python threading and queues were used to provide a continuous scrape
	Scrape 2 Parse Session
		Extract various sections of drug information from xml such as drugname, drug purpose etc.
==============
THE DATA
==============
	SOME data is provided from scrape 1 and 2, since there is a limit to how many files that can be posted only a portion of both scrapes are displayed.
==============
REFERENCE
==============
https://dailymed.nlm.nih.gov/dailymed/app-support-web-services.cfm

