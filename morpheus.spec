Summary:	morpheus
Summary(pl):	morpheus
Name:		morpheus
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Application/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source0:	http://wine.sexcity.pl/%name/%{name}-%{version}.tar.gz
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	OpenGL-devel
BuildRequires:	libmorph-devel >= 0.1.2
BuildRequires:	gtkglarea-devel >= 1.2.0
BuildRequires:	ORBit-devel >= 0.5.0
BuildRequires:	zlib-devel
BuildRequires:	gettext-devel
URL:		http://wine.sexcity.pl/morpheus/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Morpheus is a mesh (3D model) viewer for GNOME desktop. It uses OpenGL as
rendering API.

%description -l pl
Morpheus jest przeglądarką dla projektów 3D. Posiada support dla 3D Studio
i LighWave.

%prep
%setup -q

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure \
	--without-included-gettext 
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps/morpheus/

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	utildir=%{_applnkdir}/Graphics

install pixmaps/* $RPM_BUILD_ROOT%{_datadir}/pixmaps/morpheus/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(755,root,root) %{_bindir}/morpheus
%{_applnkdir}/Graphics/morpheus.desktop
%{_datadir}/pixmaps/morpheus/*
