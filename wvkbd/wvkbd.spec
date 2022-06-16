%global commit c1b95f270030218b82e77c5daa67d96007986631
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           wvkbd
Version:        0.8.3
Release:        1.20220705git%{shortcommit}%{?dist}
Summary:        On-screen keyboard for wlroots

License:        GPLv3 and MIT
URL:            https://git.sr.ht/~proycon/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
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
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/%{name}-mobintl
%{_mandir}/man1/%{name}.1*
%license COPYING COPYING_WESTON LICENSE
%doc README.md

%changelog
* Tue Jul 05 2022 Oğuz Ersen <oguz@ersen.moe> - 0.8.3-1.20220705gitc1b95f2
- Rebuild for the latest git commit

* Wed Mar 09 2022 Oğuz Ersen <oguz@ersen.moe> - 0.7-1.20220309gite5648bc
- Initial version of the package
