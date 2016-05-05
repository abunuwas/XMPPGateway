#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import getpass
from optparse import OptionParser

import sleekxmpp

if sys.version_info < (3, 0):
	reload(sys)
	sys.setdefaultencoding('utf8')
else:
	raw_input = input
	

class SendMsgBot(sleekxmpp.ClientXMPP):

	def __init__(self, jid, password, recipient, msg):
		super(SendMsgBot, self).__init__(jid, password)

		self.recipient = recipient
		self.msg = msg

		self.add_event_handler('session_start', self.start)

	def start(self, event):
		self.send_presence()
		self.get_roster()

		self.send_message(mto=self.recipient, mbody=self.msg)

		self.disconnect(wait=True)

# To run this script do:
# python send_client.py -d -j oneshot@example.com -t someone@example.net -m "This is a message"