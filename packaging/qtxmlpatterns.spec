# Package prefix
%define pkgname qt5-qtxmlpatterns

Name:       qtxmlpatterns
Summary:    Qt XML Patterns library
Version:    5.3.2
Release:    1
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.io
Source0:    %{name}-%{version}.tar.xz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtxml-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains the XMLPatterns library


%package -n qt5-qtxmlpatterns
Summary:    Qt XML Patterns library
Group:      Qt/Qt

%description -n qt5-qtxmlpatterns
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains the XMLPatterns library.


%package -n qt5-qtxmlpatterns-devel
Summary:    Qt XML Patterns - development files
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtxmlpatterns-devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains the XMLPatterns library development files.


%prep
%setup -q -n %{name}-%{version}


%build
export QTDIR=/usr/share/qt5
touch .git
%qmake5
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%qmake5_install

# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la

# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
    -exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;

# We don't need qt5/Qt/
rm -rf %{buildroot}/%{_includedir}/qt5/Qt

%fdupes %{buildroot}/%{_includedir}


%post -n qt5-qtxmlpatterns -p /sbin/ldconfig
%postun -n qt5-qtxmlpatterns -p /sbin/ldconfig


%files -n qt5-qtxmlpatterns
%defattr(-,root,root,-)
%{_libdir}/libQt5XmlPatterns.so.5
%{_libdir}/libQt5XmlPatterns.so.5.*
%{_qt5_bindir}/*

%files -n qt5-qtxmlpatterns-devel
%defattr(-,root,root,-)
%{_libdir}/libQt5XmlPatterns.so
%{_libdir}/libQt5XmlPatterns.prl
%{_libdir}/pkgconfig/*
%{_includedir}/qt5/
%{_datadir}/qt5/mkspecs/
%{_libdir}/cmake/
