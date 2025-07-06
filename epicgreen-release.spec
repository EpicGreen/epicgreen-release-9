Name:      epicgreen-release
Version:   9
Release:   2
BuildArch: noarch
Summary:   EpicGreen repository configuration
License:   GPLv2

Source:    epicgreen-release-9.tar.gz

%prep
%setup -q

%build
#Nothing to build

%install
# Create dirs
install -d -m755 \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# GPG Key
%{__install} -Dp -m644 \
    %{_builddir}/%{name}-%{version}/RPM-GPG-KEY-epicgreen \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg

# Copy files
%{__install} -p -m644 %{_builddir}/%{name}-%{version}/epicgreen.repo \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%files
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-epicgreen
%config %{_sysconfdir}/yum.repos.d/epicgreen.repo

%description
EpicGreen repository configuration

%changelog
* Sun Jul 06 2025 Ante de Baas <antedebaas@users.github.com> 9-2
- updated GPG Key
* Wed Aug 28 2024 Ante de Baas <antedebaas@users.github.com> 9-1
- Initial package
