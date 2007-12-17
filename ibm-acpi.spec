Summary: IBM ThinkPad ACPI Extras configuration scripts
Name: ibm-acpi
Version: 0.11
Release:  %mkrel 1
Source0: http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://ibm-acpi.sourceforge.net/
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
