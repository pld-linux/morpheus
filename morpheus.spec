Summary:	Morpheus is a mesh (3D model) viewer for GNOME desktop
Summary(pl):	Morpheus jest przegl±dark± dla projektów 3D
Name:		morpheus
Version:	0.3
Release:	5
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://wine.sexcity.pl/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	23f9af3e8b1ed538fb98a6f686c84dc7
Patch0:		%{name}-gtkgl.patch
URL:		http://wine.sexcity.pl/morpheus/
BuildRequires:	ORBit-devel >= 0.5.0
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	gtkglarea-devel >= 1.2.0
BuildRequires:	libmorph-devel >= 0.1.2
BuildRequires:	libtool
BuildRequires:	zlib-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Morpheus is a mesh (3D model) viewer for GNOME desktop. It uses OpenGL
as rendering API.

%description -l pl
Morpheus jest przegl±dark± dla projektów 3D. Posiada support dla 3D
Studio i LighWave.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--without-included-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps/morpheus/

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	utildir=%{_applnkdir}/Graphics

install pixmaps/* $RPM_BUILD_ROOT%{_pixmapsdir}/morpheus/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/morpheus
%{_applnkdir}/Graphics/morpheus.desktop
%{_pixmapsdir}/morpheus/*
