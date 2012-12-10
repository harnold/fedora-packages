Name:           fdm
Version:        1.6
Release:	1%{?dist}
Summary:        Program for fetching, filtering, and delivering mail

Group:          Applications/Internet
License:        ISC, BSD-2-Clause, BSD-3-Clause
URL:            http://fdm.sourceforge.net/
Source0:        http://downloads.sourceforge.net/fdm/fdm-%{version}.tar.gz

# All patches sent upstream via email 2012-12-10
Patch0:         fdm-00-make-install-dirs-configurable.patch
Patch1:         fdm-01-use-iquote-in-cppflags.patch
Patch2:         fdm-02-link-against-libcrypto.patch

BuildRequires:  libtdb-devel
BuildRequires:  openssl-devel
BuildRequires:	pcre-devel

%description
Fdm is a program to fetch mail and deliver it in various ways depending
on a user-supplied ruleset.  Mail may be fetched from stdin, IMAP or
POP3 servers, or from local maildirs, and filtered based on whether it
matches a regexp, its size or age, or the output of a shell command.  It
can be rewritten by an external process, dropped, left on the server or
delivered into maildirs, mboxes, to a file or pipe, or any combination.

Fdm is designed to be lightweight but powerful, with a compact but clear
configuration syntax.  It is primarily designed for single-user uses but
may also be configured to deliver mail in a multi-user setup.  In this
case, it uses privilege separation to minimise the amount of code
running as the root user.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1

%build
make %{?_smp_mflags} \
    PREFIX=%{_prefix} \
    CFLAGS="%{optflags}" \
    PCRE=1

%install
make install \
    PREFIX=%{_prefix} \
    BINDIR=%{_bindir} \
    MANDIR=%{_mandir} \
    DESTDIR=%{buildroot}
gzip -9 %{buildroot}%{_mandir}/*/*

%files
%{_bindir}/*
%{_mandir}/*/*
%doc CHANGES MANUAL README
%doc examples
%doc fdm-sanitize

%changelog
* Mon Dec 10 2012 Holger Arnold <holgerar@gmail.com> - 1.6-1
- Initial packaging.
