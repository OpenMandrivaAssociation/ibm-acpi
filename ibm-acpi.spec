Summary: IBM ThinkPad ACPI Extras configuration scripts
Name: ibm-acpi
Version: 0.11
Release:  6
Source0: http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://ibm-acpi.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
# laptop_mode
Requires: laptop-mode-tools
# idectl
Requires: tpctl

%description
This package contains configuration scripts to support ACPI Extras for
the IBM ThinkPad laptops.
It aims to support various features of these laptops which are
accessible through the ACPI framework but not otherwise supported by
the generic Linux ACPI drivers.

%prep
%setup -q
find config/etc/acpi/actions/ -type f -exec sed -i -e 's,/usr/local/sbin/idectl,/usr/sbin/idectl,' {} \;
sed -i -e 's,action=.*,action=/usr/sbin/pmsuspend2,' config/etc/acpi/events/hibernate
chmod a+r README CHANGES

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_sysconfdir}
cp -a config/%{_sysconfdir}/acpi $RPM_BUILD_ROOT/%{_sysconfdir}

# handled by laptop-mode-tools
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/acpi/events/ac
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/acpi/actions/battery.sh
# handled by suspend-scripts
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/acpi/events/sleep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES
%{_sysconfdir}/acpi/actions/*
%{_sysconfdir}/acpi/events/*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.11-5mdv2011.0
+ Revision: 619557
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.11-4mdv2010.0
+ Revision: 429488
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.11-3mdv2009.0
+ Revision: 247146
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.11-1mdv2008.1
+ Revision: 126931
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel

  + Emmanuel Andry <eandry@mandriva.org>
    - Import ibm-acpi



* Tue Oct  4 2005 Olivier Blin <oblin@mandriva.com> 0.11-1mdk
- initial release
