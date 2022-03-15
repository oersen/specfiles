%global commit 8b3ec96e7f57b7c9280ed23b3e589ec1c77ecef2
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           fmawk
Version:        1.3
Release:        1.20220315git%{shortcommit}%{?dist}
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
* Tue Mar 15 2022 Oğuz Ersen <oguz@ersen.moe> - 1.3-1.20220315git8b3ec96
- Rebuild for the latest git commit

* Wed Nov 03 2021 Oğuz Ersen <oguz@ersen.moe> - 1.3-1
- Rebuild for the new version

* Sat Sep 04 2021 Oğuz Ersen <oguz@ersen.moe> - 1.0-1.20210904git52e432b
- Initial version of the package
