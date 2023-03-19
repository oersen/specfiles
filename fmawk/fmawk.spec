%global commit 82505635a22c89aeeab679031b8755ab22e04ac6
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           fmawk
Version:        1.3
Release:        1.20230319git%{shortcommit}%{?dist}
Summary:        File manager written in awk

License:        GPLv3
URL:            https://github.com/huijunchen9260/fm.awk
Source0:        %{url}/archive/%{commit}.tar.gz

BuildArch:      noarch
BuildRequires:  make

Requires:       coreutils
Requires:       xdg-utils
Recommends:     chafa
Recommends:     ffmpegthumbnailer
Recommends:     poppler-utils

%description
fm.awk - File manager written in awk.

%prep
%autosetup -n fm.awk-%{commit}

%build

%install
%make_install

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-opener
%{_bindir}/%{name}-previewer
%{_bindir}/fm.awk
%license LICENSE.md
%doc README.md

%changelog
* Sun Mar 19 2023 Oğuz Ersen <oguz@ersen.moe> - 1.3-1.20230319git8250563
- Rebuild for the latest git commit

* Wed Nov 03 2021 Oğuz Ersen <oguz@ersen.moe> - 1.3-1
- Rebuild for the new version

* Sat Sep 04 2021 Oğuz Ersen <oguz@ersen.moe> - 1.0-1.20210904git52e432b
- Initial version of the package
