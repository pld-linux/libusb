Summary:	Application access to USB devices
Summary(pl):	DostÍp z poziomu aplikacji do urz±dzeÒ USB
Name:		libusb
Version:	0.1.3b
Release:	3
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://prdownloads.sourceforge.net/libusb/%{name}-%{version}.tar.gz
URL:		http://libusb.sourceforge.net/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a library for application access to USB devices.

%description -l pl
Biblioteka umoøliwiaj±ca dostÍp do urz±dzeÒ USB z poziomu aplikacji.

%package devel
Summary:	%{name} library headers
Summary(pl):	Pliki nag≥Ûwkowe biblioteki %{name}
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
This package contains include files and other resources you can use to
incorporate %{name} into applications.

%description devel -l pl
Pliki nag≥Ûwkowe oraz dokumentacja pozwalaj±ca na dodawanie obs≥ugi
USB w swoich programach.

%package static
Summary:	libusb static libraries
Summary(pl):	Statyczne biblioteki do obs≥ugi USB
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
This is package with static libusb libraries.

%description static -l pl
Statyczne biblioteki libusb.

%prep
%setup  -q

%build
rm -f missing
libtoolize --copy --force
aclocal
autoupdate
autoconf
automake -a -c
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libusb-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
