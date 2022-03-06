%global commit 1925bc3e7a131dfcb1c6152c80675deb2a067020
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global _hardened_build 1

Name:           gmnisrv
Version:        1.0
Release:        1.20211116git%{shortcommit}%{?dist}
Summary:        Gemini server

License:        GPLv3
URL:            https://sr.ht/~sircmpwn/%{name}/
Source0:        https://git.sr.ht/~sircmpwn/%{name}/archive/%{commit}.tar.gz
Source1:        %{name}.service

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(scdoc)

Requires:       mailcap

%description
%{name} is a simple Gemini protocol server.

Gemini is a new, collaboratively designed internet protocol, which explores the
space inbetween gopher and the web, striving to address (perceived) limitations
of one while avoiding the (undeniable) pitfalls of the other.

%prep
%autosetup -n %{name}-%{commit}

%build
%configure
%make_build

%install
%make_install
install -dm 0755 %{buildroot}%{_sysconfdir}
mv %{buildroot}%{_datadir}/%{name}/%{name}.ini %{buildroot}%{_sysconfdir}
rmdir %{buildroot}%{_datadir}/%{name}
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.ini.5*
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}.ini
%license COPYING
%doc README.md

%changelog
* Tue Nov 16 2021 Oğuz Ersen <oguz@ersen.moe> - 1.0-1.20211116git1925bc3
- Rebuild for the latest git commit

* Thu Feb 04 2021 Oğuz Ersen <oguz@ersen.moe> - 0-1.20210204git32913c3
- Initial version of the package
