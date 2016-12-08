==============
THE PURPOSE
==============
-Add drug data to an existing application (NCLEX study aid)
-Experiment with python queues and asynchronous code
-Quickly gather large amounts of data

==============
THE SCRAPE
==============

         | # of pages | Time to Scrape
Scrape 1 |    905     |  ~145 seconds  
Scrape 2 |   75921    |  ~50 minutes

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
		Python threading and queues were used to provide a continuous scrape
	Scrape 2 Parse Session
		Extract various sections of drug information from xml such as drugname, drug purpose etc.

==============
REFERENCE
==============
https://dailymed.nlm.nih.gov/dailymed/app-support-web-services.cfm

