%global commit 6b821ac913b07f23b61b4b8bece6c07bd6d2098a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           pash
Version:        2.3.0
Release:        1.20210811git%{shortcommit}%{?dist}
Summary:        A simple password manager using GPG written in POSIX sh

License:        MIT
URL:            https://github.com/dylanaraps/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz

BuildArch:      noarch

Requires:       gnupg2
Requires:       tree
Recommends:     xclip

%description
Features:
- Written in safe and shellcheck compliant POSIX sh
- Only 120~ LOC (minus blank lines and comments)
- Compatible with pass's password store
- Clears the clipboard after a timeout
- Configurable password generation using /dev/urandom
- Guards against set -x, ps and /proc leakage
- Easily extendible through the shell

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
* Wed Aug 11 2021 Oğuz Ersen <oguz@ersen.moe> - 2.3.0-1.20210811git6b821ac
- Rebuild for the latest git commit

* Thu Feb 25 2021 Oğuz Ersen <oguz@ersen.moe> - 2.3.0-1
- Initial version of the package
