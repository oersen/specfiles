%global commit a906ff89680c78cec9785f3ff49ca8b272a0f96b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           pfetch
Version:        0.6.0
Release:        1.20211210git%{shortcommit}%{?dist}
Summary:        A pretty system information tool written in POSIX sh

License:        MIT
URL:            https://github.com/dylanaraps/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz

BuildArch:      noarch
BuildRequires:  make

%description
The goal of this project is to implement a simple system information tool in
POSIX sh using features built into the language itself (where possible).

%prep
%autosetup -n %{name}-%{commit}

%build

%install
%make_install

%files
%{_bindir}/%{name}
%license LICENSE.md
%doc README.md

%changelog
* Fri Dec 10 2021 Oğuz Ersen <oguz@ersen.moe> - 0.6.0-1.20211210gita906ff8
- Rebuild for the latest git commit

* Wed Feb 24 2021 Oğuz Ersen <oguz@ersen.moe> - 0.6.0-1
- Initial version of the package
