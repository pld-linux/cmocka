Summary:	Fork of Google's cmockery unit testing framework
Summary(pl.UTF-8):	Odgałęzienie szkieletu testów jednostkowych cmockery Google'a
Name:		cmocka
Version:	1.1.0
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://open.cryptomilk.org/projects/cmocka/files
Source0:	https://open.cryptomilk.org/attachments/download/60/%{name}-%{version}.tar.xz
# Source0-md5:	59c9aa5735d9387fb591925ec53523ec
URL:		http://cmocka.org/
BuildRequires:	cmake >= 2.6.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cmocka is a fork for Google's cmockery unit testing framework
(<https://code.google.com/p/cmockery/>) to fix bugs and support it in
future.

%description -l pl.UTF-8
cmocka to odgałęzienie szkieletu testów jednostkowych cmockery
Google'a (<https://code.google.com/p/cmockery/>) mające na celu
poprawienie błędów i wsparcie w przyszłości.

%package devel
Summary:	Development files for cmocka framework
Summary(pl.UTF-8):	Pliki programistyczne szkieletu cmocka
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for cmocka framework.

%description devel -l pl.UTF-8
Pliki programistyczne szkieletu cmocka.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libcmocka.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcmocka.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcmocka.so
%{_includedir}/cmocka.h
%{_includedir}/cmocka_pbc.h
%{_pkgconfigdir}/cmocka.pc
%{_libdir}/cmake/cmocka
