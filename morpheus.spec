Summary:	Morpheus - a mesh (3D model) viewer for GNOME desktop
Summary(pl.UTF-8):	Morpheus - przeglądarka dla projektów 3D
Name:		morpheus
Version:	0.3
Release:	7
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://wine.sexcity.pl/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	23f9af3e8b1ed538fb98a6f686c84dc7
Patch0:		%{name}-gtkgl.patch
Patch1:		%{name}-desktop.patch
URL:		http://wine.sexcity.pl/morpheus/
BuildRequires:	ORBit-devel >= 0.5.0
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
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
as rendering API. It supports 3D Studio and LightWave formats (via
libmorph).

%description -l pl.UTF-8
Morpheus to przeglądarka siatek (modeli 3D) dla środowiska GNOME.
Używa OpenGL jako API do renderowania. Obsługuje (poprzez libmorph)
formaty 3D Studio i LightWave.

Morpheus jest przeglądarką dla projektów 3D. Posiada support dla 3D
Studio i LightWave.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
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
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/morpheus

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	utildir=%{_desktopdir}

install pixmaps/* $RPM_BUILD_ROOT%{_pixmapsdir}/morpheus

echo 'Categories=Graphics;Viewer;' >> $RPM_BUILD_ROOT%{_desktopdir}/morpheus.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/morpheus
%{_desktopdir}/morpheus.desktop
%{_pixmapsdir}/morpheus
