%global commit 788d63784ceecd4daa87d3546a5f1b2ffb621b34
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           bruteforce-luks
Version:        1.4.1
Release:        1.20251004git%{shortcommit}%{?dist}
Summary:        Try to find the password of a LUKS encrypted volume

License:        GPLv3
URL:            https://github.com/glv2/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  dh-autoreconf
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libcryptsetup)

%description
The purpose of this program is to try to find the password of a LUKS encrypted
volume.

%prep
%autosetup -n %{name}-%{commit}

%build
./autogen.sh
%configure
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license COPYING
%doc README

%changelog
* Sat Oct 04 2025 Oğuz Ersen <oguz@ersen.moe> - 1.4.1-1.20251004git788d637
- Initial version of the package
