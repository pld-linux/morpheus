Summary:	morpheus
Summary(pl):	morpheus
Name:		morpheus
Version:	0.3
Release:	1
Copyright:	GPL
Group:		X11/Application/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source0:	http://wine.sexcity.pl/%name/%name-%version.tar.gz
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	Mesa-devel >= 3.0
BuildRequires:	libmorph-devel >= 0.1.2
BuildRequires:	gtkglarea-devel >= 1.2.0
BuildRequires:	ORBit-devel >= 0.5.0
BuildRequires:	XFree86-devel >= 3.3.5
BuildRequires:	zlib-devel
URL:		http://wine.sexcity.pl/morpheus/
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
Morpheus is a mesh ( 3D model ) viewer for GNOME desktop.
It uses OpenGL as rendering API.

%description -l pl
Morpheus jest przegl±dark± dla projektów 3D .
Posiada support dla 3D Studio i LighWave.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps/morpheus/
make prefix=$RPM_BUILD_ROOT%{_prefix} install

install pixmaps/* $RPM_BUILD_ROOT%{_datadir}/pixmaps/morpheus/
%clean
rm -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps/morpheus/

%files
%defattr(644,root,root,755)
%doc
%attr(755,root,root) %{_bindir}/morpheus
%attr(644,root,root) %{_datadir}/gnome/apps/Graphics/morpheus.desktop
%attr(644,root,root) %{_datadir}/pixmaps/morpheus/*
