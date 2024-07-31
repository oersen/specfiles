%global commit cb051ec95d12fa34169bb384142b8e50e328cd97
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           vim-apprentice
Version:        2.0
Release:        1.20240731git%{shortcommit}%{?dist}
Summary:        A dark, low-contrast, Vim colorscheme

License:        MIT
URL:            https://github.com/romainl/Apprentice
Source0:        %{url}/archive/%{commit}.tar.gz

BuildArch:      noarch
BuildRequires:  vim-filesystem

Requires:       vim-filesystem

%description
Apprentice is a dark, low-contrast colorscheme for Vim based on the awesome
Sorcerer by Jeet Sukumaran.

It is essentially a streamlined version of the original, with a reduced number
of colors entirely taken from the default xterm palette to ensure a similar
look in 256colors-ready terminal emulators and GUI Vim.

%prep
%autosetup -n Apprentice-%{commit}

%build

%install
install -Dpm 0644 colors/apprentice.vim %{buildroot}%{vimfiles_root}/colors/apprentice.vim

%files
%{vimfiles_root}/colors/apprentice.vim
%license LICENSE
%doc README.md

%changelog
* Wed Jul 31 2024 Oğuz Ersen <oguz@ersen.moe> - 2.0-1.20240731gitcb051ec
- Rebuild for the latest git commit

* Mon May 03 2021 Oğuz Ersen <oguz@ersen.moe> - 0-1.20210503git3491eda
- Initial version of the package
