%define		zope_subname	PortalContentFolder
Summary:	Product allow a mix of both PortalContent and SkinnedFolder
Summary(pl.UTF-8):   Produkt umożliwiający łączenie zawartości PortalContent i SkinnedFolder
Name:		Zope-CMF%{zope_subname}
Version:	0.2
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://zope.org/Members/efge/%{zope_subname}/%{version}/%{zope_subname}-%{version}.tgz
# Source0-md5:	5d0e180802af83c9c5334db93cd76325
URL:		http://zope.org/Members/efge/PortalContentFolder/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CMF
Conflicts:	CMF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PortalContentFolder (for CMF) is a mix of both PortalContent and
SkinnedFolder.

%description -l pl.UTF-8
PortalContentFolder (dla CMF) pozwala łączyć zawartość PortalContent i
SkinnedFolder.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {*.py,version.txt,refresh.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc README.txt
%{_datadir}/%{name}
