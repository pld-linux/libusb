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
Version:	0.1.12
Release:	4
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libusb/%{name}-%{version}.tar.gz
# Source0-md5:	caf182cbc7565dac0fd72155919672e6
URL:		http://libusb.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.7.6
%if %{with doc}
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-style-dsssl
BuildRequires:	doxygen
BuildRequires:	openjade
%endif
BuildRequires:	libstdc++-devel
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

%package -n libusbpp
Summary:	C++ bindings for libusb
Summary(pl.UTF-8):	Wiązania C++ dla libusb
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libusbpp
C++ bindings for libusb based on Qt.

%description -n libusbpp -l pl.UTF-8
Wiązania C++ dla libusb oparte na Qt.

%package -n libusbpp-devel
Summary:	Header files for libusbpp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libusbpp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libusbpp = %{version}-%{release}
Requires:	libstdc++-devel

%description -n libusbpp-devel
Header files for libusbpp library.

%description -n libusbpp-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libusbpp.

%package -n libusbpp-static
Summary:	Static libusbpp library
Summary(pl.UTF-8):	Statyczna biblioteka libusbpp
Group:		Development/Libraries
Requires:	libusbpp-devel = %{version}-%{release}

%description -n libusbpp-static
Static libusbpp library.

%description -n libusbpp-static -l pl.UTF-8
Statyczna biblioteka libusbpp.

%prep
%setup -q

# docbook 4.1 is sufficient (for 4.2 we have only DocBook XML packaged)
%{__perl} -pi -e 's/DocBook V4\.2/DocBook V4.1/' doc/manual.sgml

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}
%{?with_tests:%{__make} check}

%{?with_doc:doxygen}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   -n libusbpp -p /sbin/ldconfig
%postun -n libusbpp -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README
%attr(755,root,root) %{_libdir}/libusb-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{?with_doc:%doc doc/html/*}
%attr(755,root,root) %{_bindir}/libusb-config
%attr(755,root,root) %{_libdir}/libusb.so
%{_libdir}/libusb.la
%{_includedir}/usb.h
%{_pkgconfigdir}/libusb.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libusb.a

%files -n libusbpp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libusbpp-*.so.*.*.*

%files -n libusbpp-devel
%defattr(644,root,root,755)
%{?with_doc:%doc apidocs/html/*}
%attr(755,root,root) %{_libdir}/libusbpp.so
%{_libdir}/libusbpp.la
%{_includedir}/usbpp.h

%files -n libusbpp-static
%defattr(644,root,root,755)
%{_libdir}/libusbpp.a
