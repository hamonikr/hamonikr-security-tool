libcommon_la_CPPFLAGS = \
	-I$(top_srcdir)/common \
	-DHAMONIKR_LOGPARSER_SEEKTIME_HELPER=\"/usr/lib/hamonikr-security-tool/hamonikr-logparser-seektime-helper\" \
	-DHAMONIKR_SECURITY_LOGPARSER_WRAPPER=\"/usr/lib/hamonikr-security-tool/hamonikr-security-logparser-wrapper\" \
	$(AM_CPPFLAGS)

noinst_LTLIBRARIES = libcommon.la

libcommon_la_SOURCES =	\
	common.h \
	common.c

libcommon_la_CFLAGS = \
	$(GLIB_CFLAGS)	\
	$(POLKIT_CFLAGS)	\
	$(JSON_C_CFLAGS)

libcommon_la_LDFLAGS = \
	$(AM_LDFLAGS)


libcommon_la_LIBADD = \
	$(GLIB_LIBS)	\
	$(POLKIT_LIBS)	\
	$(JSON_C_LIBS)

pkglibexec_PROGRAMS = hamonikr-systemd-control-helper

hamonikr_systemd_control_helper_SOURCES = hamonikr-systemd-control-helper.c
hamonikr_systemd_control_helper_CFLAGS = $(GIO_CFLAGS)
hamonikr_systemd_control_helper_LDFLAGS = $(GIO_LIBS)

DISTCLEANFILES = Makefile.in
