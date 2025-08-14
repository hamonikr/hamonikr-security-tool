utilsdir = $(libdir)/hamonikr-security-tool

utils_SCRIPTS = \
	hamonikr-security-logparser.py \
	gsl_util.py \
	hamonikr-logparser-seektime-helper \
	hamonikr-security-logparser-wrapper \
	hamonikr-security-status-vulnerable-helper

utils_DATA = \
	default-log.conf \
	translation

EXTRA_DIST = \
	$(utils_SCRIPTS) \
	$(utils_DATA)

DISTCLEANFILES = Makefile.in