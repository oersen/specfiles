%global commit 4ae78249f39e1c9ce67a939d338aab2ad1e3d919
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           wvkbd
Version:        0.21
Release:        1.20261118git%{shortcommit}%{?dist}
Summary:        On-screen virtual keyboard for wlroots

License:        GPLv3 and MIT
URL:            https://git.sr.ht/~proycon/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

%description
This project aims to deliver a minimal but practically usable implementation of
a wlroots on-screen keyboard in legible C. This will only be a keyboard, not a
feedback buzzer, led blinker, or anything that requires more than what's needed
to input text quickly. The end product should be a static codebase that can be
patched to add new features.

%prep
%autosetup -n %{name}-%{commit}

%build
%set_build_flags
CFLAGS="${CFLAGS/" -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1"/}"
CXXFLAGS="${CXXFLAGS/" -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1"/}"
LDFLAGS="${LDFLAGS/" -specs=/usr/lib/rpm/redhat/redhat-hardened-ld"/}"
%make_build LAYOUT=deskintl

%install
%make_install PREFIX=%{_prefix} LAYOUT=deskintl

%files
%{_bindir}/%{name}-deskintl
%{_mandir}/man1/%{name}.1*
%license COPYING COPYING_WESTON LICENSE
%doc README.md

%changelog
* Web Nov 18 2026 Oğuz Ersen <oguz@ersen.moe> - 0.21-1.20261118git4ae7824
- Change build to deskintl

* Tue Nov 17 2026 Oğuz Ersen <oguz@ersen.moe> - 0.21-1.20261117git4ae7824
- Rebuild for the latest git commit

* Wed Oct 28 2026 Oğuz Ersen <oguz@ersen.moe> - 0.21-1.20261028gitf7e9ea3
- Rebuild for the new version

* Wed Mar 09 2022 Oğuz Ersen <oguz@ersen.moe> - 0.7-1.20220309gite5648bc
- Initial version of the package
