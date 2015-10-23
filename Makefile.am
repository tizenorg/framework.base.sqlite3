
AM_CFLAGS = @THREADSAFE_FLAGS@ @DYNAMIC_EXTENSION_FLAGS@ \
				@ENABLE_ICU_FLAGS@ \
				-DSQLITE_ENABLE_FTS3 \
				-DSQLITE_ENABLE_RTREE \
				-DSQLITE_ENABLE_COLUMN_METADATA \
				-DSQLITE_ENABLE_MEMORY_MANAGEMENT \
				-DSQLITE_DEFAULT_AUTOVACUUM=1 \
				-DSQLITE_DEFAULT_PAGE_SIZE=4096 \
				-Dfdatasync=fdatasync \
				-DSQLITE_TIZEN_FEATURE \
				-DSQLITE_TEMP_STORE=2 \
				-DHAVE_USLEEP=1 \
				-DSQLITE_DEFAULT_JOURNAL_SIZE_LIMIT=1048576 \
				-DSQLITE_DEFAULT_FILE_FORMAT=4 \
				-DSQLITE_POWERSAFE_OVERWRITE=1 \
				-DSQLITE_ENABLE_ATOMIC_WRITE \
				-DSQLITE_ENABLE_FTS4

lib_LTLIBRARIES = libsqlite3.la
libsqlite3_la_SOURCES = sqlite3.c
libsqlite3_la_LDFLAGS = -no-undefined -version-info 8:6:8

bin_PROGRAMS = sqlite3
sqlite3_SOURCES = shell.c sqlite3.h
sqlite3_LDADD = sqlite3.$(OBJEXT) @READLINE_LIBS@

include_HEADERS = sqlite3.h sqlite3ext.h

EXTRA_DIST = sqlite3.1 tea
pkgconfigdir = ${libdir}/pkgconfig
pkgconfig_DATA = sqlite3.pc

man_MANS = sqlite3.1
