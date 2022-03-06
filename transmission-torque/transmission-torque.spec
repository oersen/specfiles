%global commit 567a94bc4f483fb96b514190768a9e6012b94f0b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           transmission-torque
Version:        0
Release:        1.20210225git%{shortcommit}%{?dist}
Summary:        A TUI client for transmission written in pure bash

License:        MIT
URL:            https://github.com/dylanaraps/torque
Source0:        %{url}/archive/%{commit}.tar.gz

BuildArch:      noarch

Requires:       transmission-common

%description
A simple TUI client for transmission-daemon.

- Fast (Written in pure bash)
- Minimal (Only 50~ LOC)
- Smooth Scrolling (Using vim keybindings)

%prep
%autosetup -n torque-%{commit}

%build

%install
install -Dpm 0755 torque %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE.md
%doc README.md

%changelog
* Thu Feb 25 2021 Oğuz Ersen <oguz@ersen.moe> - 0-1.20210225git567a94b
- Initial version of the package
