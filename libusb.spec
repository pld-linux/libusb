Summary:	Application access to USB devices
Summary(pl):	Dostêp z poziomu aplikacji do urz±dzeñ USB
Name:		libusb
Version:	0.1.0
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://download.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-comment.patch
URL:		http://libusb.sourceforge.net/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a library for application access to USB devices.

%description -l pl
Biblioteka umo¿liwiaj±ca dostêp do urz±dzeñ USB z poziomu aplikacji.

%package devel
Summary:	%{name} library headers
Summary(pl):	Pliki nag³ówkowe biblioteki %{name}
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%description -l pl devel
Pliki nag³ówkowe oraz dokumentacja pozwalaj±ca na dodawanie obs³ugi
USB w swoich programach.

%package static
Summary:	libusb static libraries
Summary(pl):	Statyczne biblioteki do obs³ugi USB
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description static
This is package with static libusb libraries.

%description -l pl static
Statyczne biblioteki libusb.

%prep
%setup  -q
%patch0 -p1

%build
rm missing
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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libusb-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
