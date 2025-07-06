Name:           epicgreen-repository
Version:        9
Release:        1
Summary:        EpicGreen DNF Repository configuration
License:        AGPLv3
Group:          System Tools
URL:            https://github.com/epicgreen/epicgreen-repository/
Source0:        https://github.com/epicgreen/epicgreen-repository/releases/download/v%{version}/epicgreen-repository-%{version}.tar.gz
Requires:       dnf

%prep
%setup -q

%build
#Nothing to build

%install
mkdir -p %{buildroot}/%{_sysconfdir}
install -d 755 %{buildroot}/%{_sysconfdir}/pki/rpm-gpg
install -d 755 %{buildroot}/%{_sysconfdir}/yum.repos.d
install -m 644 RPM-GPG-KEY-epicgreen %{buildroot}/%{_sysconfdir}/pki/rpm-gpg
install -m 644 epicgreen.repo %{buildroot}/%{_sysconfdir}/yum.repos.d/epicgreen.repo

%files
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-epicgreen
%config %{_sysconfdir}/yum.repos.d/epicgreen.repo

%description
EpicGreen DNF Repository configuration

%changelog
* Sun Jul 06 2025 Ante de Baas <antedebaas@users.github.com> 9-1
- Initial package

%maintainer Ante de Baas <antedebaas@users.github.com>