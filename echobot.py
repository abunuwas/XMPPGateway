#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import getpass
from optparse import OptionParser

import sleekxmpp

class EchoBot(sleekxmpp.ClientXMPP):

	def __init__(self, jid, password):
		super(EchoBot, self).__init__(jid, password)


if __name__ == '__main__':
	pass