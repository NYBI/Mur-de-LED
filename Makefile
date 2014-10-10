README.html: README.md
	markdown $< > $@

clean:
	rm -f *~ README.html
