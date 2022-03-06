Name:           cbonsai
Version:        1.3.1
Release:        1%{?dist}
Summary:        Grow bonsai trees in your terminal

License:        GPLv3
URL:            https://gitlab.com/jallbrit/%{name}
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(panel)
BuildRequires:  pkgconfig(scdoc)

%description
%{name} is a bonsai tree generator, written in C using ncurses. It intelligently
creates, colors, and positions a bonsai tree, and is entirely configurable via
CLI options. There are 2 modes of operation: static (see finished bonsai tree),
and live (see growth step-by-step).

%prep
%autosetup -n %{name}-v%{version}

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license LICENSE
%doc README.md

%changelog
* Sun Aug 15 2021 Oğuz Ersen <oguz@ersen.moe> - 1.3.1-1
- Rebuild for the new version

* Sat Aug 14 2021 Oğuz Ersen <oguz@ersen.moe> - 1.3.0-1
- Initial version of the package
