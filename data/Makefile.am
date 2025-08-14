# systemd control helper는 common/에서 빌드됨

kr.hamonikr.security.tool.policy.in: kr.hamonikr.security.tool.policy.in.in Makefile
	$(AM_V_GEN) sed -e "s|\@pkglibexecdir\@|$(pkglibexecdir)|" $< >$@

@INTLTOOL_POLICY_RULE@
polkitdir       = $(datadir)/polkit-1/actions
polkit_in_files = kr.hamonikr.security.tool.policy.in
polkit_DATA     = $(polkit_in_files:.policy.in=.policy)

CLEANFILES = \
	kr.hamonikr.security.tool.policy \
	kr.hamonikr.security.tool.policy.in

DISTCLEANFILES = Makefile.in
