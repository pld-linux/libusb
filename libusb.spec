Summary:	Application access to USB devices
Summary(es):	libusb - Biblioteca USB
Summary(pl):	Dostêp z poziomu aplikacji do urz±dzeñ USB
Summary(pt_BR):	libusb - Biblioteca para acesso a devices USB
Name:		libusb
Version:	0.1.10
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libusb/%{name}-%{version}.tar.gz
# Source0-md5:	439a25e119d60d3847bd07673c883737
URL:		http://libusb.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.7.6
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-style-dsssl
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	openjade
Obsoletes:	libusb0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a library for application access to USB devices.

%description -l es
Biblioteca de uso en devices USB.

%description -l pl
Biblioteka umo¿liwiaj±ca dostêp do urz±dzeñ USB z poziomu aplikacji.

%description -l pt_BR
Biblioteca para acesso em devices USB.

%package devel
Summary:	Header files for libusb library
Summary(es):	Archivos de desarrollo de libusb
Summary(pl):	Pliki nag³ówkowe biblioteki libusb
Summary(pt_BR):	Arquivos de desenvolvimento da libusb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libusb0.1-devel

%description devel
This package contains header files and other resources you can use to
incorporate libusb into applications.

%description devel -l es
Bibliotecas de desarrolo para linusb.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja pozwalaj±ca na dodawanie obs³ugi
USB w swoich programach.

%description devel -l pt_BR
Bibliotecas de desenvolvimento para libusb.

%package static
Summary:	libusb static libraries
Summary(es):	Archivos de desarrollo de libusb - estatico
Summary(pl):	Statyczne biblioteki do obs³ugi USB
Summary(pt_BR):	Arquivos de desenvolvimento da libusb - biblioteca estática
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This is package with static libusb libraries.

%description static -l es
Bibliotecas de desarrolo para linusb - estatico.

%description static -l pl
Statyczne biblioteki libusb.

%description static -l pt_BR
Bibliotecas de desenvolvimento para libusb - estático.

%package -n libusbpp
Summary:	C++ bindings for libusb
Summary(pl):	Wi±zania C++ dla libusb
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n libusbpp
C++ bindings for libusb based on Qt.

%description -n libusbpp -l pl
Wi±zania C++ dla libusb oparte na Qt.

%package -n libusbpp-devel
Summary:	Header files for libusbpp library
Summary(pl):	Pliki nag³ówkowe biblioteki libusbpp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libusbpp = %{version}-%{release}
Requires:	libstdc++-devel

%description -n libusbpp-devel
Header files for libusbpp library.

%description -n libusbpp-devel -l pl
Pliki nag³ówkowe biblioteki libusbpp.

%package -n libusbpp-static
Summary:	Static libusbpp library
Summary(pl):	Statyczna biblioteka libusbpp
Group:		Development/Libraries
Requires:	libusbpp-devel = %{version}-%{release}

%description -n libusbpp-static
Static libusbpp library.

%description -n libusbpp-static -l pl
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

doxygen

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# missing in include_HEADERS (0.1.9)
install usbpp.h $RPM_BUILD_ROOT%{_includedir}

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
%doc doc/html/*
%attr(755,root,root) %{_bindir}/libusb-config
%attr(755,root,root) %{_libdir}/libusb.so
%{_libdir}/libusb.la
%{_includedir}/usb.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libusb.a

%files -n libusbpp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libusbpp-*.so.*.*.*

%files -n libusbpp-devel
%defattr(644,root,root,755)
%doc apidocs/html/*
%attr(755,root,root) %{_libdir}/libusbpp.so
%{_libdir}/libusbpp.la
%{_includedir}/usbpp.h

%files -n libusbpp-static
%defattr(644,root,root,755)
%{_libdir}/libusbpp.a
