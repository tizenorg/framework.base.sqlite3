Name:       sqlite3
Summary:    Library that implements an embeddable SQL database engine
Version:    3.7.9
%define tar_ver 3070900
Release:    1
Group:      Applications/Databases
License:    Public Domain
URL:        http://www.sqlite.org/download.html
#Source:    http://www.sqlite.org/sqlite-autoconf-%{tar_ver}.tar.gz
Source:     %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host

%package devel
Summary:    Development tools for the sqlite3 embeddable SQL database engine
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the header files and development documentation
for %{name}. If you like to develop programs using %{name}, you will need
to install %{name}-devel.

%prep
%setup -q -n %{name}-%{version}

#%patch0 -p1

%build

%reconfigure --prefix=%{_prefix} \
	CFLAGS="$RPM_OPT_FLAGS -DSQLITE_ENABLE_COLUMN_METADATA -DSQLITE_ENABLE_MEMORY_MANAGEMENT" \
	--enable-shared=yes \
	--enable-static=no \
	--enable-threadsafe

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}

%make_install
rm -rf $RPM_BUILD_ROOT/usr/share/man

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
