%define		plugin	check_temperature
Summary:	Nagios plugin to check temperatures
Name:		nagios-plugin-%{plugin}
Version:	1.2
Release:	1
License:	BSD
Group:		Networking
Source0:	http://www.hoppie.nl/tempsens/check_temperature
# Source0-md5:	52af8cf292537680f9a624e41d557edf
Patch0:		paths.patch
Patch1:		compatible-devs.patch
Source1:	%{plugin}.cfg
URL:		http://www.hoppie.nl/tempsens/
Requires:	nagios-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
Nagios plugin to check temperatures using Digitemp (or compatible
device).

%prep
%setup -qcT
cp -p %{SOURCE0} %{plugin}
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}/%{plugin}
sed -e 's,@plugindir@,%{plugindir},' %{SOURCE1} > $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
