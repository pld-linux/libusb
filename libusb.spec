Summary:	Application access to USB devices
Summary(pl):	Dostêp z poziomu aplikacji do urz±dzeñ USB
Summary(pt_BR):	libusb - Biblioteca para acesso a devices USB
Summary(es):	libusb - Biblioteca USB
Name:		libusb
Version:	0.1.6a
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.sourceforge.net/libusb/%{name}-%{version}.tar.gz
URL:		http://libusb.sourceforge.net/
Patch0:		%{name}-am15.patch
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libusb0.1

%description
Provides a library for application access to USB devices.

%description -l pl
Biblioteka umo¿liwiaj±ca dostêp do urz±dzeñ USB z poziomu aplikacji.

%description -l pt_BR
Biblioteca para acesso em devices USB.

%description -l es
Biblioteca de uso en devices USB.

%package devel
Summary:	%{name} library headers
Summary(pl):	Pliki nag³ówkowe biblioteki %{name}
Summary(pt_BR):	Arquivos de desenvolvimento da libusb
Summary(es):	Archivos de desarrollo de libusb
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libusb0.1-devel

%description devel
This package contains include files and other resources you can use to
incorporate %{name} into applications.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja pozwalaj±ca na dodawanie obs³ugi
USB w swoich programach.

%description devel -l pt_BR
Bibliotecas de desenvolvimento para libusb.

%description devel -l es
Bibliotecas de desarrolo para linusb.

%package static
Summary:	libusb static libraries
Summary(pl):	Statyczne biblioteki do obs³ugi USB
Summary(pt_BR):	Arquivos de desenvolvimento da libusb - biblioteca estática
Summary(es):	Archivos de desarrollo de libusb - estatico
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This is package with static libusb libraries.

%description static -l pl
Statyczne biblioteki libusb.

%description static -l pt_BR
Bibliotecas de desenvolvimento para libusb - estático.

%description static -l es
Bibliotecas de desarrolo para linusb - estatico.

%prep
%setup  -q
#%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_bindir}/libusb-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
