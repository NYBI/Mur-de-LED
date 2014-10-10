README.html: README
	markdown $< > $@

clean:
	rm -f *~ README.html
