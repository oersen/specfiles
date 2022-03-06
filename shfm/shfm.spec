%global commit 696318e94792a2a81449e3b419689dfc017498f9
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           shfm
Version:        0.4.2
Release:        1.20210811git%{shortcommit}%{?dist}
Summary:        File manager written in posix shell

License:        MIT
URL:            https://github.com/dylanaraps/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz

BuildArch:      noarch

%description
Features:
- no dependencies other than a POSIX shell + POSIX [, printf, dd and stty
- tiny
- single file
- no compilation needed
- correctly handles files with funky names (newlines, etc)
- works with very small terminal sizes
- cd on exit
- works when run in subshell $(shfm)

%prep
%autosetup -n %{name}-%{commit}

%build

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README

%changelog
* Wed Aug 11 2021 Oğuz Ersen <oguz@ersen.moe> - 0.4.2-1.20210811git696318e
- Rebuild for the latest git commit

* Wed Feb 24 2021 Oğuz Ersen <oguz@ersen.moe> - 0.4.2-1
- Initial version of the package
