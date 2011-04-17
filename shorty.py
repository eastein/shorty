#!/usr/bin/env

import sys
import irclib
import shortyhelpers

class Shorty(irclib.SimpleIRCClient) :
	def __init__(self, server, nick, chan) :
		irclib.SimpleIRCClient.__init__(self)
		self.connect(server, 6667, nick)
		self.connection.join(chan)
	
	def on_join(self, c, e) :
		pass

	def on_pubmsg(self, c, e) :
		nick = e.source().split("!")[0]
		chan = e.target()
		txt = e.arguments()[0]
		n = 0
		msg = "%s's link%s:" % (nick, '%s')
		for short in shortyhelpers.short(txt, 30) :
			msg += " " + short
			n += 1

		if n > 0 :
			plur = ' is'
			if n > 1 :
				plur = 's are'
			msg = msg % plur

			self.connection.privmsg(chan, msg)

if __name__ == '__main__' :
	s = Shorty(sys.argv[1], sys.argv[2], sys.argv[3])
	s.start();
