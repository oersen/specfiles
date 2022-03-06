%global commit a5a0f4c5c5308750d11edf32fe335c6aec595f83
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           promptless
Version:        0
Release:        1.20210212git%{shortcommit}%{?dist}
Summary:        A super fast and extremely minimal shell prompt

License:        MIT
URL:            https://github.com/dylanaraps/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz

BuildArch:      noarch

%description
A super fast and extremely minimal shell prompt.

Features:
- Fast
- Minimal
- Lightweight
- POSIX sh (no external commands)
- No dependencies
- Works in all shells (that use $PS1)

%prep
%autosetup -n %{name}-%{commit}

%build

%install
install -Dpm 0644 %{name}.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh

%files
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh
%license LICENSE.md
%doc README.md

%changelog
* Wed Aug 11 2021 Oğuz Ersen <oguz@ersen.moe> - 0-1.20210811gita5a0f4c
- Rebuild for the latest git commit

* Fri Feb 12 2021 Oğuz Ersen <oguz@ersen.moe> - 0-1.20210212git9f22e59
- Initial version of the package
