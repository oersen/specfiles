%global commit 863c41dba6f16b8b487d6fa5b689184d2c9ee011
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gmni
Version:        0
Release:        1.20210223git%{shortcommit}%{?dist}
Summary:        Gemini client

License:        GPLv3
URL:            https://sr.ht/~sircmpwn/%{name}/
Source0:        https://git.sr.ht/~sircmpwn/%{name}/archive/%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(scdoc)

%description
This is a Gemini client. Included are:
 - A CLI utility (like curl): %{name}
 - A line-mode browser: gmnlm

Gemini is a new, collaboratively designed internet protocol, which explores the
space inbetween gopher and the web, striving to address (perceived) limitations
of one while avoiding the (undeniable) pitfalls of the other.

%prep
%autosetup -n %{name}-%{commit}

%build
%configure
%make_build

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0755 gmnlm %{buildroot}%{_bindir}/gmnlm
install -Dpm 0644 doc/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dpm 0644 doc/gmnlm.1 %{buildroot}%{_mandir}/man1/gmnlm.1

%files
%{_bindir}/%{name}
%{_bindir}/gmnlm
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/gmnlm.1*
%license COPYING
%doc README.md

%changelog
* Tue Feb 23 2021 Oğuz Ersen <oguz@ersen.moe> - 0-1.20210223git863c41d
- Rebuild for the latest git commit

* Mon Jan 25 2021 Oğuz Ersen <oguz@ersen.moe> - 0-1.20210125git8796267
- Initial version of the package
