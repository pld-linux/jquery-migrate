%define		plugin	migrate
Summary:	Migrate older jQuery code to jQuery 1.9+
Name:		jquery-%{plugin}
Version:	1.1.1
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	http://code.jquery.com/%{name}-%{version}.js
# Source0-md5:	70c6ea4d6766802a5513e017a04f9754
Source1:	http://code.jquery.com/%{name}-%{version}.min.js
# Source1-md5:	b3abf477069c9b8aa3204d2a75c40e4f
URL:		https://github.com/jquery/jquery-migrate/#readme
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	jquery >= 1.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
This plugin can be used to detect and restore APIs or features that
have been deprecated in jQuery and removed as of version 1.9. See the
warnings page for more information regarding messages the plugin
generates.

%prep
%setup -qcT
cp -p %{SOURCE0} %{plugin}.src.js
cp -p %{SOURCE1} %{plugin}.min.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p %{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p %{plugin}.src.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.src.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js
ln -s %{plugin}-%{version}.src.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
