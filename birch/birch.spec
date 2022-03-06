%global commit 27691aa4fb2746f73c373e6653c1fb17795729f9
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           birch
Version:        0
Release:        1.20210225git%{shortcommit}%{?dist}
Summary:        An IRC client written in bash

License:        MIT
URL:            https://github.com/dylanaraps/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz

BuildArch:      noarch

%description
Features:
- Full power of readline for input and keybindings
- Tab completion of nicks and channels
- Unique (or semi-unique) nick colors

Caveats (or limitations):
- Nick column is fixed and truncated to 10 columns wide
- Lines are word-wrapped to a fixed 60 columns
- No automatic server reconnect
- No SSL (sadly)

%prep
%autosetup -n %{name}-%{commit}

%build

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE.md
%doc README.md

%changelog
* Thu Feb 25 2021 Oğuz Ersen <oguz@ersen.moe> - 0-1.20210225git27691aa
- Initial version of the package
