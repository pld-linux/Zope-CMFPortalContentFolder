%define		zope_subname	PortalContentFolder
Summary:	Product allow a mix of both PortalContent and SkinnedFolder
Summary(pl):	Produkt umo¿liwiaj±cy ³±czenie zawarto¶ci PortalContent i SkinnedFolder
Name:		Zope-CMF%{zope_subname}
Version:	0.2
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://zope.org/Members/efge/%{zope_subname}/%{version}/%{zope_subname}-%{version}.tgz
# Source0-md5:	5d0e180802af83c9c5334db93cd76325
URL:		http://zope.org/Members/efge/PortalContentFolder/
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CMF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	CMF

%description
PortalContentFolder (for CMF) is a mix of both PortalContent and
SkinnedFolder.

%description -l pl
PortalContentFolder (dla CMF) pozwala ³±czyæ zawarto¶æ PortalContent i
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
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc README.txt
%{_datadir}/%{name}
