#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : expect
Version  : 5.45
Release  : 15
URL      : http://downloads.sourceforge.net/expect/expect5.45.tar.gz
Source0  : http://downloads.sourceforge.net/expect/expect5.45.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Public-Domain
Requires: expect-bin
Requires: expect-lib
Requires: expect-doc
BuildRequires : tcl
BuildRequires : tcl-dev

%description
NOTE: ALPHA AND BETA RELEASES OF TCL/TK ARE NOT SUPPORTED!
--------------------
Introduction
--------------------

%package bin
Summary: bin components for the expect package.
Group: Binaries

%description bin
bin components for the expect package.


%package dev
Summary: dev components for the expect package.
Group: Development
Requires: expect-lib
Requires: expect-bin
Provides: expect-devel

%description dev
dev components for the expect package.


%package doc
Summary: doc components for the expect package.
Group: Documentation

%description doc
doc components for the expect package.


%package lib
Summary: lib components for the expect package.
Group: Libraries

%description lib
lib components for the expect package.


%prep
%setup -q -n expect5.45

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484415984
%configure --disable-static --with-tcl=/usr/lib64
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
export SOURCE_DATE_EPOCH=1484415984
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/expect5.45/pkgIndex.tcl

%files bin
%defattr(-,root,root,-)
/usr/bin/autoexpect
/usr/bin/autopasswd
/usr/bin/cryptdir
/usr/bin/decryptdir
/usr/bin/dislocate
/usr/bin/expect
/usr/bin/ftp-rfc
/usr/bin/kibitz
/usr/bin/lpunlock
/usr/bin/mkpasswd
/usr/bin/multixterm
/usr/bin/passmass
/usr/bin/rftp
/usr/bin/rlogin-cwd
/usr/bin/timed-read
/usr/bin/timed-run
/usr/bin/tknewsbiff
/usr/bin/tkpasswd
/usr/bin/unbuffer
/usr/bin/weather
/usr/bin/xkibitz
/usr/bin/xpstat

%files dev
%defattr(-,root,root,-)
/usr/include/*.h

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/expect5.45/libexpect5.45.so
