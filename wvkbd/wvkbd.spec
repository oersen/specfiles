%global commit e14b53aff4fd1f471add6b21b3885c2cff945509
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           wvkbd
Version:        0.20
Release:        1.20260925git%{shortcommit}%{?dist}
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
unset LDFLAGS
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/%{name}-mobintl
%{_mandir}/man1/%{name}.1*
%license COPYING COPYING_WESTON LICENSE
%doc README.md

%changelog
* Fri Sep 25 2026 Oğuz Ersen <oguz@ersen.moe> - 0.19.4-1.20260723gite14b53a
- Rebuild for the latest git commit

* Sat Jul 25 2026 Oğuz Ersen <oguz@ersen.moe> - 0.20-1.20260725git6b41504
- Rebuild for the new version

* Thu Jul 23 2026 Oğuz Ersen <oguz@ersen.moe> - 0.19.4-1.20260723gite14b53a
- Rebuild for the latest git commit

* Wed Mar 09 2022 Oğuz Ersen <oguz@ersen.moe> - 0.7-1.20220309gite5648bc
- Initial version of the package
