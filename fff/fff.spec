%global commit 6f2dc6f3a003d24e8b3fd48b046241b486022ad5
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           fff
Version:        2.2
Release:        2.20211118git%{shortcommit}%{?dist}
Summary:        A simple file manager written in bash

License:        MIT
URL:            https://github.com/dylanaraps/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz

BuildArch:      noarch
BuildRequires:  make

Requires:       coreutils
Requires:       xdg-utils
Recommends:     w3m-img

%description
fff (Fucking Fast File-Manager)
- It's Fucking Fast
- Minimal (only requires bash and coreutils)
- Smooth Scrolling (using vim keybindings)
- Works on Linux, BSD, macOS, Haiku etc
- Supports $LS_COLORS
- File Operations (copy, paste, cut, ranger style bulk rename, etc)
- Instant as you type search
- Tab completion for all commands
- Automatic CD on exit
- Display images with w3m-img
- Supports $CDPATH

%prep
%autosetup -n %{name}-%{commit}

%build

%install
%make_install

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license LICENSE.md
%doc README.md

%changelog
* Thu Nov 18 2021 Oğuz Ersen <oguz@ersen.moe> - 2.2-2.20211118git6f2dc6f
- Rebuild for the latest git commit

* Wed Jan 27 2021 Oğuz Ersen <oguz@ersen.moe> - 2.2-1
- Initial version of the package
