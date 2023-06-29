Title: ipfs setup for pelican
Date: 02.24.2017 14:37
Category: Articles
Tags: ipfs, general,pelican

To enable pelican's makefile to output ipfs add the following to your makefile

#!makefile
	ipfs: html
		ipfs swarm peers >/dev/null || (echo "ipfs daemon must be online to publish" && exit 1)
		ipfs add -r -q $(OUTPUTDIR) | tail -n1 >versions/current
		cat versions/current >>versions/history
		@export hash=`cat versions/current`; \
			echo ""; \
			echo "published website:"; \
			echo "- http://localhost:8080/ipfs/$$hash"; \
			echo "- https://ipfs.io/ipfs/$$hash"; \
			echo ""; \
			echo "next steps:"; \
			echo "- ipfs pin add -r /ipfs/$$hash"; \
			echo "- make ipfsio"; \
	ipfs name publish `cat versions/current`

Then be sure to add ipfs to your .PHONY section.

Make sure a directory called versions exists

You should be able to call `make ipfs` if ipfs daemon is running locally

To have traditional dns resolve your site you then need to set your domains A record to an ipfs gateway and your dns txt record to `dnslink=/ipns/ipnshash`

Also pin your site to multiple ipfs daemons and use something like cachewarmer to decrease initial load on your servers

To pin use `ipfs pin add -r /ipns/QmeMsvVh1yxrMXFyBvoU3QcTdJF2wjkMnteDRk1zkbYRt7` (thats my ipns entry if you'd like to help spread the load)