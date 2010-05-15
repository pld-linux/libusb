#
# Conditional build:
%bcond_without	doc	# don't build documentation
%bcond_with	tests	# perform "make check"
#
Summary:	Application access to USB devices
Summary(es.UTF-8):	libusb - Biblioteca USB
Summary(pl.UTF-8):	Dostęp z poziomu aplikacji do urządzeń USB
Summary(pt_BR.UTF-8):	libusb - Biblioteca para acesso a devices USB
Name:		libusb
Version:	1.0.8
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libusb/%{name}-%{version}.tar.bz2
# Source0-md5:	37d34e6eaa69a4b645a19ff4ca63ceef
URL:		http://libusb.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6
%if %{with doc}
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-style-dsssl
BuildRequires:	doxygen
BuildRequires:	openjade
%endif
BuildRequires:	libtool >= 2:1.5
Obsoletes:	libusb0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a library for application access to USB devices.

%description -l es.UTF-8
Biblioteca de uso en devices USB.

%description -l pl.UTF-8
Biblioteka umożliwiająca dostęp do urządzeń USB z poziomu aplikacji.

%description -l pt_BR.UTF-8
Biblioteca para acesso em devices USB.

%package devel
Summary:	Header files for libusb library
Summary(es.UTF-8):	Archivos de desarrollo de libusb
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libusb
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento da libusb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libusb0.1-devel

%description devel
This package contains header files and other resources you can use to
incorporate libusb into applications.

%description devel -l es.UTF-8
Bibliotecas de desarrolo para linusb.

%description devel -l pl.UTF-8
Pliki nagłówkowe oraz dokumentacja pozwalająca na dodawanie obsługi
USB w swoich programach.

%description devel -l pt_BR.UTF-8
Bibliotecas de desenvolvimento para libusb.

%package static
Summary:	libusb static libraries
Summary(es.UTF-8):	Archivos de desarrollo de libusb - estatico
Summary(pl.UTF-8):	Statyczne biblioteki do obsługi USB
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento da libusb - biblioteca estática
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This is package with static libusb libraries.

%description static -l es.UTF-8
Bibliotecas de desarrolo para linusb - estatico.

%description static -l pl.UTF-8
Statyczne biblioteki libusb.

%description static -l pt_BR.UTF-8
Bibliotecas de desenvolvimento para libusb - estático.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}
%{__make} -C doc docs

%{?with_tests:%{__make} check}

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
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libusb-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libusb-1.0.so.0

%files devel
%defattr(644,root,root,755)
%{?with_doc:%doc doc/html/*}
%attr(755,root,root) %{_libdir}/libusb-1.0.so
%{_libdir}/libusb-1.0.la
%{_includedir}/libusb-1.0
%{_pkgconfigdir}/libusb-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libusb-1.0.a
