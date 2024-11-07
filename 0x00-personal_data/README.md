This is the readme file for:
	0x00. Personal data

-----------------------------------------------
Personally identifiable information (PII) and personal data are two classifications of data that often confuse organizations that collect, store and analyze such data. Both terms cover common ground, classifying information that could reveal an individual’s identity directly or indirectly. 

PII is used in the US, but no specific legal document defines it. The legal system in the United States is a blend of numerous federal and state laws and sector-specific regulations, all of which describe and classify different pieces of information under the PII umbrella. 

On the other hand, personal data has one legal definition established by the General Data Protection Regulation (GDPR), which is accepted as law across the European Union (EU).

But why is all that so important? As a website admin, app creator or product owner, you need to be aware that visitors and users could share sensitive information with you. These traces might enable you to identify individuals, so you must handle such data carefully. From a legal standpoint, it could be a matter of breaches and violations with serious consequences. Grasping the bigger picture is crucial for your organization’s security and legal compliance.

-----------------------------------------------------
logging — Logging facility for Python
Source code: Lib/logging/__init__.py
This module defines functions and classes which implement a flexible event logging system for applications and libraries.

The key benefit of having the logging API provided by a standard library module is that all Python modules can participate in logging, so your application log can include your own messages integrated with messages from third-party modules.

- Here’s a simple example of idiomatic usage:
	# myapp.py
	import logging
	import mylib
	logger = logging.getLogger(__name__)

	def main():
    	logging.basicConfig(filename='myapp.log', level=logging.INFO)
    	logger.info('Started')
    	mylib.do_something()
    	logger.info('Finished')

	if __name__ == '__main__':
    	main()
