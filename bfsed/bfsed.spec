%global commit 0193dd08801dd285fd25cb20c2aa034e91889490
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           bfsed
Version:        0
Release:        1.20210918git%{shortcommit}%{?dist}
Summary:        A brainfuck compiler, written in sed

License:        NONE
URL:            https://github.com/stedolan/bf.sed
Source0:        %{url}/archive/%{commit}.tar.gz

BuildArch:      noarch

%description
An optimising compiler for brainfuck produces x86 Linux ELF binaries written
entirely in sed.

%prep
%autosetup -n bf.sed-%{commit}

%build

%install
install -Dpm 0755 bf.sed %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc README 99bottles.b factor.b helloworld.b

%changelog
* Sat Sep 18 2021 Oğuz Ersen <oguz@ersen.moe> - 0-1.20210918git0193dd0
- Initial version of the package
