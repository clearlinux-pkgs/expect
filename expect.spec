#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : expect
Version  : 5.45
Release  : 13
URL      : http://downloads.sourceforge.net/expect/expect5.45.tar.gz
Source0  : http://downloads.sourceforge.net/expect/expect5.45.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Public-Domain
Requires: expect-bin
Requires: expect-doc
BuildRequires : tcl

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
Requires: expect-bin

%description dev
dev components for the expect package.


%package doc
Summary: doc components for the expect package.
Group: Documentation

%description doc
doc components for the expect package.


%prep
%setup -q -n expect5.45

%build
%configure --disable-static --with-tcl=/usr/lib64
make V=1 %{?_smp_mflags}

%check
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/expect5.45/libexpect5.45.so
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
