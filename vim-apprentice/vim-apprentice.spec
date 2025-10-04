%global commit 2a4557410fe6b5e3906c5290d42c4e4d8813b0d8
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           vim-apprentice
Version:        2.0
Release:        1.20251004git%{shortcommit}%{?dist}
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
* Sat Oct 04 2025 Oğuz Ersen <oguz@ersen.moe> - 2.0-1.20251004git2a45574
- Rebuild for the latest git commit

* Mon May 03 2021 Oğuz Ersen <oguz@ersen.moe> - 0-1.20210503git3491eda
- Initial version of the package
