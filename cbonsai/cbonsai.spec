%global commit 50fe627c84036e3be4115b02be04d17f58480199
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           cbonsai
Version:        1.3.1
Release:        2.20230125git%{shortcommit}%{?dist}
Summary:        Grow bonsai trees in your terminal

License:        GPLv3
URL:            https://gitlab.com/jallbrit/%{name}
Source0:        %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.gz

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
%autosetup -n %{name}-%{commit}

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix} WITH_BASH=1

%files
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/bash-completion/completions/%{name}
%license LICENSE
%doc README.md

%changelog
* Wed Jan 25 2023 Oğuz Ersen <oguz@ersen.moe> - 1.3.1-2.20230125git50fe627
- Rebuild for the latest git commit

* Sun Aug 15 2021 Oğuz Ersen <oguz@ersen.moe> - 1.3.1-1
- Rebuild for the new version

* Sat Aug 14 2021 Oğuz Ersen <oguz@ersen.moe> - 1.3.0-1
- Initial version of the package
